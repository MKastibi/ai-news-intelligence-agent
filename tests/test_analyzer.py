import json

from app.models.analysis import ArticleAnalysis, Category, AnalysisResult
from app.services.analyzer import _parse_analysis


def build_valid_json() -> str:
    return json.dumps([
        {
            "title": "OpenAI Launches GPT-5",
            "impact_score": 9,
            "category": "LLMs",
            "companies": ["OpenAI"],
            "audience": "developers",
            "opportunity": "Build a custom chatbot",
        },
        {
            "title": "EU AI Act Passed",
            "impact_score": 7,
            "category": "Regulation",
            "companies": [],
            "audience": "founders and compliance teams",
            "opportunity": "Create an AI compliance checklist tool",
        },
    ])


def test_parse_valid_json() -> None:
    raw = build_valid_json()
    result = _parse_analysis(raw)
    assert len(result) == 2
    assert result[0].title == "OpenAI Launches GPT-5"
    assert result[0].impact_score == 9
    assert result[0].category == Category.LLMS
    assert result[0].companies == ["OpenAI"]
    assert result[1].category == Category.REGULATION
    assert result[1].companies == []


def test_parse_json_with_code_fence() -> None:
    raw = f"```json\n{build_valid_json()}\n```"
    result = _parse_analysis(raw)
    assert len(result) == 2


def test_parse_json_with_backticks_only() -> None:
    raw = f"```\n{build_valid_json()}\n```"
    result = _parse_analysis(raw)
    assert len(result) == 2


def test_parse_empty_array() -> None:
    result = _parse_analysis("[]")
    assert result == []


def test_analysis_result_dataclass() -> None:
    result = AnalysisResult()
    assert result.analyses == []

    item = ArticleAnalysis(
        title="Test",
        impact_score=5,
        category=Category.AGENTS,
        companies=[],
        audience="devs",
        opportunity="Build something",
    )
    result = AnalysisResult(analyses=[item])
    assert len(result.analyses) == 1
    assert result.analyses[0].title == "Test"
