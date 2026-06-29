from typing import List

from app.models.article import Article


def deduplicate_articles(articles: List[Article]) -> List[Article]:
    seen: set[str] = set()
    unique: List[Article] = []
    for article in articles:
        key = article.title.strip().lower()
        if key and key not in seen:
            seen.add(key)
            unique.append(article)
    return unique
