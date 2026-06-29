from typing import List, Optional

from app.llm import create_provider
from app.models.analysis import ArticleAnalysis
from app.models.article import Article
from app.prompts.summarizer_prompt import build_summarizer_prompt


def summarize(
    articles: List[Article],
    analyses: Optional[List[ArticleAnalysis]] = None,
) -> str:
    if not articles:
        return "No news articles found to summarise."

    provider = create_provider()
    prompt = build_summarizer_prompt(articles, analyses)
    return provider.summarize(prompt)
