from typing import List

from app.core.config import Config
from app.models.article import Article
from app.services.news_fetcher import fetch_news
from app.services.summarizer import summarize
from app.services.telegram_sender import send_telegram_message


def run() -> None:
    print("=" * 60)
    print("  AI News Intelligence Agent")
    print("=" * 60)

    print("\nValidating configuration...")
    Config.validate()
    print("  [OK] Configuration valid.\n")

    print("Fetching news from RSS feeds...")
    articles: List[Article] = fetch_news()
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
