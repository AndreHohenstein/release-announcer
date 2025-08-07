# src/post_to_x.py
import os
import sys
import tweepy

def build_message(body: str, url: str) -> str:
    msg = f"{body}\n\n{url}".strip()
    if len(msg) > 280:
        msg = msg[:277] + "..."
    return msg

def main():
    # Debug-Flag aus Secrets/Env
    debug = os.getenv("DEBUG_MODE", "false").lower() == "true"

    body = os.getenv("RELEASE_BODY", "").strip()
    url  = os.getenv("RELEASE_URL", "").strip()

    if not body or not url:
        print("❌ RELEASE_BODY oder RELEASE_URL fehlt.")
        sys.exit(1)

    message = build_message(body, url)

    if debug:
        print(f"[TEST MODE] Would post to X:\n{message}")
        return

    # Nur im Live-Modus: echte API-Credentials nötig
    try:
        auth = tweepy.OAuth1UserHandler(
            os.environ["X_API_KEY"],
            os.environ["X_API_SECRET"],
            os.environ["X_ACCESS_TOKEN"],
            os.environ["X_ACCESS_TOKEN_SECRET"]
        )
        api = tweepy.API(auth)
        api.update_status(message)
        print("✅ Posted to X")
    except KeyError as e:
        print(f"❌ Missing credential env var: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Failed to post: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
