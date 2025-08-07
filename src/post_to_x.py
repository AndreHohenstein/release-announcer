import os
import sys
import tweepy

def send_tweet(text: str):
    """Send a single tweet."""
    auth = tweepy.OAuth1UserHandler(
        os.environ["X_API_KEY"],
        os.environ["X_API_SECRET"],
        os.environ["X_ACCESS_TOKEN"],
        os.environ["X_ACCESS_TOKEN_SECRET"]
    )
    api = tweepy.API(auth)

    if len(text) > 280:
        print("⚠️ Tweet zu lang – wird gekürzt.")
        text = text[:277] + "..."

    api.update_status(text)
    print(f"✅ Tweet gesendet: {text}")

def main():
    # Unterstützt mehrere Tweets, getrennt durch | falls nötig
    release_bodies = os.environ.get("RELEASE_BODY", "").strip()
    release_urls = os.environ.get("RELEASE_URL", "").strip()

    if not release_bodies or not release_urls:
        print("❌ Fehler: RELEASE_BODY oder RELEASE_URL fehlt.")
        sys.exit(1)

    # Falls mehrere Releases in einer Runde gefunden wurden → splitten
    bodies = release_bodies.split("|")
    urls = release_urls.split("|")

    for body, url in zip(bodies, urls):
        tweet_text = f"{body}\n\n{url}"
        send_tweet(tweet_text)

if __name__ == "__main__":
    main()
