# src/scan_releases.py
import os, json, sys, time
from urllib.parse import urlencode
import requests
from pathlib import Path

GH_API = "https://api.github.com"

def gh_get(url, token, params=None):
    hdrs = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28"
    }
    if params:
        url = f"{url}?{urlencode(params)}"
    r = requests.get(url, headers=hdrs, timeout=30)
    return r

def list_user_repos(user, token):
    repos = []
    page = 1
    while True:
        r = gh_get(f"{GH_API}/users/{user}/repos", token, params={"per_page":100, "page":page, "type":"owner", "sort":"updated"})
        if r.status_code != 200: raise RuntimeError(f"user repos http {r.status_code}: {r.text}")
        batch = r.json()
        if not batch: break
        repos.extend(batch)
        page += 1
    return repos

def list_org_repos(org, token):
    repos = []
    page = 1
    while True:
        r = gh_get(f"{GH_API}/orgs/{org}/repos", token, params={"per_page":100, "page":page, "type":"all", "sort":"updated"})
        if r.status_code == 404:  # Org evtl. privat / nicht zugänglich
            break
        if r.status_code != 200: raise RuntimeError(f"org repos {org} http {r.status_code}: {r.text}")
        batch = r.json()
        if not batch: break
        repos.extend(batch)
        page += 1
    return repos

def get_latest_release(owner, repo, token):
    r = gh_get(f"{GH_API}/repos/{owner}/{repo}/releases/latest", token)
    if r.status_code == 404:
        return None  # keine Releases
    if r.status_code != 200:
        raise RuntimeError(f"latest release {owner}/{repo} http {r.status_code}: {r.text}")
    return r.json()

def load_json(p: Path, default):
    if p.exists():
        try:
            return json.loads(p.read_text(encoding="utf-8"))
        except Exception:
            return default
    return default

def save_json(p: Path, data):
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

def main():
    gh_user = os.environ.get("GH_USER", "").strip()
    gh_pat  = os.environ.get("GH_PAT", "").strip()
    orgs_csv = os.environ.get("ORGS_CSV", "").strip()

    if not gh_user or not gh_pat:
        print("❌ GH_USER oder GH_PAT fehlt.")
        sys.exit(1)

    state_dir = Path("state")
    known_path = state_dir / "known_releases.json"
    pending_path = state_dir / "pending.json"

    known_ids = set(load_json(known_path, default=[]))
    pending = []

    # Alle Repos einsammeln
    repos = list_user_repos(gh_user, gh_pat)

    if orgs_csv:
        for org in [o.strip() for o in orgs_csv.split(",") if o.strip()]:
            repos.extend(list_org_repos(org, gh_pat))

    # Deduplizieren nach full_name
    seen = set()
    unique_repos = []
    for r in repos:
        fn = r.get("full_name")
        if fn and fn not in seen:
            seen.add(fn)
            unique_repos.append(r)

    # Neueste Releases prüfen
    for r in unique_repos:
        full_name = r["full_name"]  # owner/repo
        owner, repo = full_name.split("/", 1)

        try:
            rel = get_latest_release(owner, repo, gh_pat)
        except RuntimeError as e:
            # z. B. 403 bei rate limit; einfach weiter
            print(f"⚠️  {e}")
            continue

        if not rel:
            continue

        rid = rel.get("id")
        tag = rel.get("tag_name") or ""
        name = (rel.get("name") or "").strip()
        html_url = rel.get("html_url") or f"https://github.com/{owner}/{repo}/releases"

        key = f"{full_name}#{rid}"
        if rid and key not in known_ids:
            # Kurzer, plattformfreundlicher Text
            title = name if name else tag
            if not title:
                title = "New release"
            body = f"{full_name} — {title}"
            # sehr kurz halten, damit auch deine ursprüngliche post_to_x.py nicht trimmen muss
            if len(body) > 230:
                body = body[:227] + "..."

            pending.append({
                "body": body,
                "url": html_url,
                "id": rid,
                "key": key
            })
            known_ids.add(key)

    # Outputs/State schreiben
    has_new = "1" if pending else "0"
    save_json(known_path, sorted(list(known_ids)))
    save_json(pending_path, pending)

    print(f"ℹ️  Pending: {len(pending)} neue Releases.")
    # GitHub Actions Output
    out = os.environ.get("GITHUB_OUTPUT")
    if out:
        with open(out, "a", encoding="utf-8") as f:
            f.write(f"has_new={has_new}\n")

if __name__ == "__main__":
    main()
