from typing import List

from app.models.article import Article

SYSTEM_PROMPT = (
    "You are an AI news analyst. You receive a list of the latest AI articles. "
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


def build_summarizer_prompt(articles: List[Article]) -> str:
    lines: List[str] = ["Here are the latest AI articles:\n"]
    for i, article in enumerate(articles, 1):
        lines.append(
            f"{i}. **{article.title}**\n"
            f"   {article.summary[:300]}\n"
            f"   Source: {article.source} | {article.link}\n"
        )
    return f"{SYSTEM_PROMPT}\n\n{''.join(lines)}"
