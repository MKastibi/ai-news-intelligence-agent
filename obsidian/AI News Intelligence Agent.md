# AI News Intelligence Agent

**Tags:** #project #ai #automation

## Goal

Automate the collection, summarisation, and delivery of AI news to a Telegram chat.

## Architecture

```
RSS Feeds → news_fetcher → deduplicator → summarizer (LLM) → telegram_sender → Telegram
```

The app runs daily at 06:00 UTC via GitHub Actions (`workflow_dispatch` also available).

## Key Design Decisions

| Decision                | Rationale                                      |
|-------------------------|------------------------------------------------|
| Provider-agnostic LLM   | Swap OpenAI / OpenRouter / Ollama without code changes |
| Article dataclass       | Type-safe, self-documenting data model         |
| Dedicated prompt module | Separates prompt engineering from orchestration|
| Factory pattern         | Only the factory knows which provider to use   |

## LLM Providers

- **OpenAI** – `openai` provider, requires `OPENAI_API_KEY`
- **OpenRouter** – `openrouter` provider, requires `OPENROUTER_API_KEY`
- **Ollama** – `ollama` provider, local inference, no API key needed

Set via `LLM_PROVIDER` in `.env`.

## Related Notes

- [[Lessons Learned]]
- [[LinkedIn Posts]]
