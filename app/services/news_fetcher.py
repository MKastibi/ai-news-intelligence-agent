from typing import List

import feedparser

from app.models.article import Article
from app.services.deduplicator import deduplicate_articles

RSS_FEEDS: dict[str, str] = {
    "TechCrunch AI": "https://techcrunch.com/category/artificial-intelligence/feed/",
    "The Verge AI": "https://www.theverge.com/ai-artificial-intelligence/rss/index.xml",
    "VentureBeat AI": "https://venturebeat.com/category/ai/feed/",
    "Artificial Intelligence News": "https://www.artificialintelligence-news.com/feed/",
}


def _parse_entry(entry: feedparser.FeedParserDict, source: str) -> Article:
    title = getattr(entry, "title", "").strip()
    link = getattr(entry, "link", "").strip()
    summary = getattr(entry, "summary", getattr(entry, "description", "")).strip()
    return Article(title=title, link=link, summary=summary, source=source)


def fetch_news() -> List[Article]:
    articles: List[Article] = []
    for source, url in RSS_FEEDS.items():
        try:
            feed = feedparser.parse(url)
            if feed.bozo and not feed.entries:
                print(f"  [WARN] Could not parse feed: {source} ({url})")
                continue
            for entry in feed.entries:
                article = _parse_entry(entry, source)
                if article.title:
                    articles.append(article)
            print(f"  [OK]   {source}: {len(feed.entries)} articles")
        except Exception as e:
            print(f"  [ERR]  {source}: {e}")

    return deduplicate_articles(articles)
