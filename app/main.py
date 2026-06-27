from typing import List, Dict, Any

from app.config import Config
from app.news_fetcher import fetch_news
from app.summarizer import summarize
from app.telegram_sender import send_telegram_message


def run() -> None:
    print("=" * 60)
    print("  AI News Intelligence Agent")
    print("=" * 60)

    print("\nValidating configuration...")
    Config.validate()
    print("  [OK] Configuration valid.\n")

    print("Fetching news from RSS feeds...")
    articles: List[Dict[str, Any]] = fetch_news()
    print(f"\n  Total unique articles: {len(articles)}\n")

    if not articles:
        print("No articles fetched. Nothing to send.")
        return

    print("Generating AI briefing...")
    briefing = summarize(articles)
    if not briefing:
        print("  [ERR] Summary generation returned empty content.")
        return
    print("  [OK] Briefing generated.\n")

    print("Sending briefing to Telegram...")
    send_telegram_message(briefing)
    print("  [OK] Briefing sent to Telegram.\n")

    print("Done.")
