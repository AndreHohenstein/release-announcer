
# 📋 # 🚀 Usage Guide – Announce GitHub Release on X

**Projekt:** *Announce GitHub Release on X (Debug/Production)*
**Stand:** 08. August 2025

---

## 1️⃣ Debug → Produktiv umstellen

Standardmäßig läuft das Projekt aktuell im **Debug-Modus** (`DEBUG_MODE=true`), damit keine echten Posts gesendet werden.

**Änderungsschritte:**

1. **GitHub → Repository → Settings → Secrets and variables → Actions**
2. Secret `DEBUG_MODE` suchen
3. Wert ändern von `true` auf `false`
4. Speichern ✅
5. Optional: In `README.md` und `CHANGELOG.md` vermerken, dass Debug deaktiviert wurde.

---

## 2️⃣ Secrets prüfen (Pflicht für Produktivmodus)

| Secret-Name             | Inhalt                                               | Quelle / Hinweis   |
| ----------------------- | ---------------------------------------------------- | ------------------ |
| `DEBUG_MODE`            | `false`                                              | Siehe oben         |
| `GH_USER`               | GitHub-Username                                      | GitHub             |
| `GH_PAT`                | Personal Access Token (Classic, nur *read* für Repo) | GitHub             |
| `X_API_KEY`             | API Key                                              | Developer Portal X |
| `X_API_SECRET`          | API Secret Key                                       | Developer Portal X |
| `X_ACCESS_TOKEN`        | Access Token                                         | Developer Portal X |
| `X_ACCESS_TOKEN_SECRET` | Access Token Secret                                  | Developer Portal X |

---

## 3️⃣ Workflow starten

1. In **Actions** im Repository wechseln
2. Workflow **"Announce GitHub Release on X"** auswählen
3. `Run workflow` klicken
4. Ziel-Repository angeben (z. B. `AndreHohenstein/vscode-extension-updater`)
5. Branch auswählen (`main` oder `master`)
6. **Run workflow** bestätigen
7. Logausgabe beobachten

---

## 4️⃣ Funktionsprüfung vor Live-Post

* **Debug aktiv** → `[TEST MODE]` erscheint im Log → kein echter Post
* **Debug deaktiviert** → keine `[TEST MODE]`-Kennzeichnung → echter Post auf X

---

## 5️⃣ Sicherheitshinweise

* API Keys **niemals** im Klartext im Repo hinterlegen – nur als **GitHub Secrets**
* Zugriff nur an berechtigte Personen vergeben (Least Privilege)
* Bei Missbrauchsverdacht: Keys sofort im Developer-Portal von X neu generieren

---

## 6️⃣ Einsatz im Training

* Debug-Modus ideal für Schulungen – reale Abläufe ohne Live-Posting zeigen
* Für beliebige Repositories nutzbar
* Beispiel-Link zu echtem Post einfügen, sobald erste Produktivveröffentlichung erfolgt

---
© 2025 André Hohenstein – Microsoft Certified Trainer