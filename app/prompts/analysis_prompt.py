from typing import List

from app.models.article import Article

SYSTEM_PROMPT = (
    "You are an AI industry analyst. Your task is to analyse each news article and "
    "return a **valid JSON array** — no markdown, no code fences, no extra text.\n\n"
    "Each object in the array must have exactly these fields:\n"
    "- `title`: the exact article title\n"
    "- `impact_score`: integer 1–10 (1 = minor, 10 = groundbreaking)\n"
    "- `category`: one of \"LLMs\", \"Agents\", \"Regulation\", \"Robotics\", \"AI Tools\", \"Security\", \"Other\"\n"
    "- `companies`: list of company names mentioned (empty list if none)\n"
    "- `audience`: short phrase describing who should care (e.g. \"developers\", \"researchers\", \"founders\")\n"
    "- `opportunity`: concrete idea or application someone could build based on this news\n\n"
    "Example:\n"
    "[\n"
    "  {\n"
    "    \"title\": \"OpenAI Launches GPT-5\",\n"
    "    \"impact_score\": 9,\n"
    "    \"category\": \"LLMs\",\n"
    "    \"companies\": [\"OpenAI\"],\n"
    "    \"audience\": \"developers and product builders\",\n"
    "    \"opportunity\": \"Build a custom chatbot that leverages the new reasoning capabilities\"\n"
    "  }\n"
    "]"
)


def build_analysis_prompt(articles: List[Article]) -> str:
    lines: List[str] = ["Analyse the following news articles:\n"]
    for i, article in enumerate(articles, 1):
        lines.append(
            f"{i}. **{article.title}**\n"
            f"   {article.summary[:400]}\n"
            f"   Source: {article.source}\n"
        )
    return f"{SYSTEM_PROMPT}\n\n{''.join(lines)}"
