from typing import List, Dict, Any

from app.llm import create_provider

SYSTEM_PROMPT = (
    "Je bent een AI-nieuwsanalist. Je krijgt een lijst met de laatste AI-artikelen. "
    "Maak een beknopte Nederlandse briefing met de volgende structuur:\n\n"
    "📌 **Belangrijkste ontwikkelingen**\n"
    "- Vat de 3-5 belangrijkste nieuwsitems kort samen.\n\n"
    "🔍 **Waarom dit belangrijk is**\n"
    "- Leg uit wat de impact is van deze ontwikkelingen.\n\n"
    "🛠 **Kansen om iets mee te bouwen**\n"
    "- Noem 2-3 concrete ideeën of toepassingen.\n\n"
    "⚠️ **Risico's of aandachtspunten**\n"
    "- Waar moet je op letten?\n\n"
    "📚 **Bronnen**\n"
    "- Voeg links toe naar de originele artikelen.\n\n"
    "Houd de briefing kort en leesbaar voor Telegram."
)


def build_prompt(articles: List[Dict[str, Any]]) -> str:
    lines: List[str] = ["Hier zijn de laatste AI-artikelen:\n"]
    for i, article in enumerate(articles, 1):
        lines.append(
            f"{i}. **{article['title']}**\n"
            f"   {article['summary'][:300]}\n"
            f"   Bron: {article['source']} | {article['link']}\n"
        )
    return "\n".join(lines)


def summarize(articles: List[Dict[str, Any]]) -> str:
    if not articles:
        return "Geen nieuwsartikelen gevonden om samen te vatten."

    provider = create_provider()
    user_prompt = build_prompt(articles)
    full_prompt = f"{SYSTEM_PROMPT}\n\n{user_prompt}"
    return provider.summarize(full_prompt)
