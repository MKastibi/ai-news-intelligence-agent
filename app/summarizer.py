from typing import List, Dict, Any

from app.llm import create_provider

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


def build_prompt(articles: List[Dict[str, Any]]) -> str:
    lines: List[str] = ["Here are the latest AI articles:\n"]
    for i, article in enumerate(articles, 1):
        lines.append(
            f"{i}. **{article['title']}**\n"
            f"   {article['summary'][:300]}\n"
            f"   Source: {article['source']} | {article['link']}\n"
        )
    return "\n".join(lines)


def summarize(articles: List[Dict[str, Any]]) -> str:
    if not articles:
        return "No news articles found to summarise."

    provider = create_provider()
    user_prompt = build_prompt(articles)
    full_prompt = f"{SYSTEM_PROMPT}\n\n{user_prompt}"
    return provider.summarize(full_prompt)
