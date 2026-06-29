from app.models.article import Article
from app.services.deduplicator import deduplicate_articles


def test_deduplicate_removes_duplicates_by_lowercase_title() -> None:
    articles = [
        Article(title="OpenAI Launches GPT-5", link="https://example.com/1", summary="...", source="TechCrunch"),
        Article(title="openai launches gpt-5", link="https://example.com/1", summary="...", source="TechCrunch"),
        Article(title="Google Announces Gemini", link="https://example.com/2", summary="...", source="The Verge"),
    ]
    result = deduplicate_articles(articles)
    assert len(result) == 2
    assert result[0].title == "OpenAI Launches GPT-5"
    assert result[1].title == "Google Announces Gemini"


def test_deduplicate_keeps_unique_articles() -> None:
    articles = [
        Article(title="Title A", link="https://example.com/a", summary="...", source="Source 1"),
        Article(title="Title B", link="https://example.com/b", summary="...", source="Source 2"),
    ]
    result = deduplicate_articles(articles)
    assert len(result) == 2


def test_deduplicate_empty_list() -> None:
    result = deduplicate_articles([])
    assert result == []


def test_deduplicate_removes_empty_titles() -> None:
    articles = [
        Article(title="", link="https://example.com/1", summary="...", source="Source"),
        Article(title="Valid Title", link="https://example.com/2", summary="...", source="Source"),
    ]
    result = deduplicate_articles(articles)
    assert len(result) == 1
    assert result[0].title == "Valid Title"
