# Roadmap

## Completed

- [x] Multi-source RSS aggregation (TechCrunch AI, The Verge AI, VentureBeat AI, Artificial Intelligence News)
- [x] Smart deduplication based on title
- [x] Provider-agnostic LLM layer (OpenAI, OpenRouter, Ollama)
- [x] English-language briefing generation
- [x] Telegram message delivery with automatic splitting
- [x] Provider factory with config-based selection
- [x] Global config validation with clear error messages
- [x] Scheduled execution via GitHub Actions (06:00 UTC daily)
- [x] Manual workflow trigger via `workflow_dispatch`
- [x] Dockerfile for containerised deployment
- [x] CI pipeline with pytest on push / PR
- [x] Per-article intelligence analysis (impact score, category, companies, audience, opportunity)

## Planned

- [ ] Anthropic Claude provider
- [ ] Google Gemini provider
- [ ] Groq provider
- [ ] Configurable RSS feed list via `FEED_LIST` env var
- [ ] Per-article summarisation with inline source links
- [ ] CLI flags for one-off vs. continuous mode (`--once`, `--watch`)
- [ ] Opt-in English / Dutch language toggle
- [ ] Unit tests for all services (news_fetcher, summarizer, telegram_sender)
- [ ] Integration test suite with mock providers
- [ ] Historical database (SQLite) for trend tracking
