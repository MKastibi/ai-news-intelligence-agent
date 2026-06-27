import hashlib
from typing import List, Dict, Any

import feedparser

RSS_FEEDS: Dict[str, str] = {
    "TechCrunch AI": "https://techcrunch.com/category/artificial-intelligence/feed/",
    "The Verge AI": "https://www.theverge.com/ai-artificial-intelligence/rss/index.xml",
    "VentureBeat AI": "https://venturebeat.com/category/ai/feed/",
    "Artificial Intelligence News": "https://www.artificialintelligence-news.com/feed/",
}


def _deduplicate(articles: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    seen: set[str] = set()
    unique: List[Dict[str, Any]] = []
    for article in articles:
        key = hashlib.md5(article["title"].encode()).hexdigest()
        if key not in seen:
            seen.add(key)
            unique.append(article)
    return unique


def _parse_entry(entry: Any, source: str) -> Dict[str, Any]:
    title = getattr(entry, "title", "").strip()
    link = getattr(entry, "link", "").strip()
    summary = getattr(entry, "summary", getattr(entry, "description", "")).strip()
    return {
        "title": title,
        "link": link,
        "summary": summary,
        "source": source,
    }


def fetch_news() -> List[Dict[str, Any]]:
    articles: List[Dict[str, Any]] = []
    for source, url in RSS_FEEDS.items():
        try:
            feed = feedparser.parse(url)
            if feed.bozo and not feed.entries:
                print(f"  [WARN] Could not parse feed: {source} ({url})")
                continue
            for entry in feed.entries:
                parsed = _parse_entry(entry, source)
                if parsed["title"]:
                    articles.append(parsed)
            print(f"  [OK]   {source}: {len(feed.entries)} articles")
        except Exception as e:
            print(f"  [ERR]  {source}: {e}")

    return _deduplicate(articles)
