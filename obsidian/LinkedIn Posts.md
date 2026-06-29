# LinkedIn Posts

**Tags:** #linkedin #portfolio

## Post 1: Project Launch

> I built an AI News Intelligence Agent that fetches the latest AI news from multiple RSS feeds, generates a structured briefing with an LLM, and sends it to my Telegram every morning.
>
> Stack: Python, OpenAI / OpenRouter, GitHub Actions, Telegram API.
>
> Key design choices:
> - Provider-agnostic LLM layer (swap OpenAI ↔ OpenRouter ↔ Ollama with one env var)
> - Factory pattern for clean dependency injection
> - Deduplication before summarisation to save tokens and avoid repetition
> - Scheduled daily run via GitHub Actions with manual trigger fallback
>
> No hardcoded secrets. Clean architecture. Production-ready logging.
>
> Code: https://github.com/MKastibi/ai-news-intelligence-agent

## Post 2: Architecture Deep Dive

> Most "AI agents" you see are Jupyter notebooks with API calls. Here's what a production-ready version looks like:
>
> ```
> app/
> ├── core/          # Config, logging, exceptions
> ├── llm/           # Provider abstraction (abstract base + 3 providers)
> ├── models/        # Article dataclass
> ├── prompts/       # Prompt templates (separate from logic)
> ├── services/      # Business logic (fetcher, summariser, sender)
> └── main.py        # Entry point
> ```
>
> The summariser depends on `LLMProvider` (the abstraction), never on OpenAI or OpenRouter directly. Adding Claude or Gemini next week means writing exactly one new file and adding two lines to the factory.
>
> Dependency inversion is not just for enterprise Java. It makes small Python projects extensible too.

## Post 3: Security PSA

> Quick security win for anyone building Python tools with API keys:
>
> 1. Put ALL secrets in `.env` (not in your code)
> 2. Add `.env` to `.gitignore` BEFORE your first commit
> 3. Commit only `.env.example` with placeholder values
> 4. Use GitHub Secrets for CI/CD – never paste keys into YAML
>
> I documented the full process (including what to do if you accidentally push a key) in my repo's `docs/security.md`.
>
> One leaked API key can cost you thousands. Five minutes of setup prevents it entirely.
