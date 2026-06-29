import json
from typing import List

from app.llm import create_provider
from app.models.analysis import ArticleAnalysis, Category
from app.models.article import Article
from app.prompts.analysis_prompt import build_analysis_prompt


def _parse_analysis(raw: str) -> List[ArticleAnalysis]:
    cleaned = raw.strip()
    if cleaned.startswith("```"):
        cleaned = cleaned.strip("`")
        if cleaned.startswith("json"):
            cleaned = cleaned[4:].strip()

    data = json.loads(cleaned)
    if not isinstance(data, list):
        raise ValueError("Expected JSON array")

    results: List[ArticleAnalysis] = []
    for item in data:
        category = Category(item.get("category", "Other"))
        results.append(
            ArticleAnalysis(
                title=item.get("title", ""),
                impact_score=int(item.get("impact_score", 1)),
                category=category,
                companies=item.get("companies", []),
                audience=item.get("audience", ""),
                opportunity=item.get("opportunity", ""),
            )
        )
    return results


def analyze_articles(articles: List[Article]) -> List[ArticleAnalysis]:
    if not articles:
        return []

    provider = create_provider()
    prompt = build_analysis_prompt(articles)

    try:
        raw = provider.summarize(prompt)
        return _parse_analysis(raw)
    except Exception:
        return []
