# Architecture

## Project Structure

```
app/
├── core/                  # Cross-cutting concerns
│   ├── config.py          # Environment variable loading and validation
│   ├── exceptions.py      # Custom exception classes
│   └── logger.py          # Logging configuration
├── llm/                   # LLM provider abstraction layer
│   ├── base.py            # Abstract LLMProvider interface
│   ├── factory.py         # Provider factory (only class that instantiates providers)
│   ├── openai_provider.py
│   ├── openrouter_provider.py
│   └── ollama_provider.py
├── models/                # Domain models
│   └── article.py         # Article dataclass
├── prompts/               # LLM prompt templates
│   └── summarizer_prompt.py
├── services/              # Business logic
│   ├── news_fetcher.py    # RSS feed aggregation
│   ├── summarizer.py      # Orchestrates LLM summarisation
│   ├── telegram_sender.py # Telegram message delivery
│   └── deduplicator.py    # Article deduplication
└── main.py                # Application entry point
```

## Design Principles

- **Dependency Inversion** – The summarisation layer depends on the `LLMProvider` abstraction, not on concrete implementations. Adding a new provider requires only a new file in `app/llm/` and a new entry in the factory.
- **Separation of Concerns** – Each module has a single responsibility: fetching news, deduplicating, prompting, summarising, or sending messages.
- **Configuration over Hardcoding** – All secrets and environment-specific values are read from environment variables via `.env`.
