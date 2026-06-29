from typing import List, Optional

from app.models.analysis import ArticleAnalysis
from app.models.article import Article

SYSTEM_PROMPT = (
    "You are an AI news analyst. You receive a list of the latest AI articles "
    "along with per-article analysis. "
    "Write a concise English briefing with the following structure:\n\n"
    "📌 **Key Developments**\n"
    "- Briefly summarise the 3-5 most important news items.\n\n"
    "🔍 **Why This Matters**\n"
    "- Explain the impact of these developments.\n\n"
    "🛠 **Opportunities to Build On**\n"
    "- Suggest 2-3 concrete ideas or applications.\n\n"
    "⚠️ **Risks & Considerations**\n"
    "- What to watch out for?\n\n"
    "📚 **Sources**\n"
    "- Include links to the original articles.\n\n"
    "Keep the briefing short and readable for Telegram."
)


def _build_analysis_section(analyses: List[ArticleAnalysis]) -> str:
    lines: List[str] = ["\nPer-article analysis:\n"]
    for a in analyses:
        lines.append(
            f"- **{a.title}**\n"
            f"  Impact: {a.impact_score}/10 | Category: {a.category.value}\n"
            f"  Audience: {a.audience}\n"
            f"  Opportunity: {a.opportunity}\n"
        )
    return "".join(lines)


def build_summarizer_prompt(
    articles: List[Article],
    analyses: Optional[List[ArticleAnalysis]] = None,
) -> str:
    lines: List[str] = ["Here are the latest AI articles:\n"]
    for i, article in enumerate(articles, 1):
        lines.append(
            f"{i}. **{article.title}**\n"
            f"   {article.summary[:300]}\n"
            f"   Source: {article.source} | {article.link}\n"
        )
    user_prompt = "".join(lines)

    if analyses:
        user_prompt += _build_analysis_section(analyses)

    return f"{SYSTEM_PROMPT}\n\n{user_prompt}"
