# AI News Intelligence Agent

A Python tool that fetches the latest AI news from multiple RSS feeds, generates a structured Dutch-language briefing using an LLM of your choice, and sends it to a Telegram chat.

## Features

- **Multi-source RSS aggregation** – TechCrunch AI, The Verge AI, VentureBeat AI, and Artificial Intelligence News
- **Smart deduplication** – removes duplicate articles by title
- **Provider-agnostic LLM layer** – swap between OpenAI, OpenRouter, and Ollama without changing code
- **Dutch-language briefing** – structured summary with key developments, analysis, opportunities, risks, and sources
- **Telegram delivery** – sends the briefing directly to your Telegram chat with automatic message splitting
- **Production-ready** – clean config validation, error handling, type hints, and dependency injection

## Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/ai-news-intelligence-agent.git
cd ai-news-intelligence-agent

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## LLM Provider Setup

### OpenAI
1. Get an API key from [platform.openai.com](https://platform.openai.com/api-keys).
2. Set `LLM_PROVIDER=openai` and `OPENAI_API_KEY` in your `.env`.

### OpenRouter
1. Get an API key from [openrouter.ai](https://openrouter.ai/keys).
2. Set `LLM_PROVIDER=openrouter`, `OPENROUTER_API_KEY`, and `MODEL` (e.g. `qwen/qwen3-32b`) in your `.env`.

### Ollama (local)
1. Install Ollama from [ollama.ai](https://ollama.ai) and pull a model (e.g. `ollama pull llama3`).
2. Set `LLM_PROVIDER=ollama` and `MODEL` (e.g. `llama3`) in your `.env`.
3. Optionally change `OLLAMA_BASE_URL` if Ollama is not on `localhost:11434`.

## Telegram Bot Setup

1. Open Telegram and search for [@BotFather](https://t.me/BotFather).
2. Send `/newbot` and follow the prompts to create a new bot.
3. Copy the API token you receive.
4. Start a chat with your new bot and send any message.
5. Visit `https://api.telegram.org/bot<YOUR_TOKEN>/getUpdates` to find your `chat_id` (look for the `chat` object &rarr; `id` field).

## Environment Variables

Copy `.env.example` to `.env` and fill in your values:

```env
LLM_PROVIDER=openrouter
MODEL=qwen/qwen3-32b
OPENAI_API_KEY=
OPENROUTER_API_KEY=
OLLAMA_BASE_URL=http://localhost:11434
TELEGRAM_BOT_TOKEN=your_telegram_bot_token_here
TELEGRAM_CHAT_ID=your_telegram_chat_id_here
```

| Variable             | Required               | Default                  | Description                          |
|----------------------|------------------------|--------------------------|--------------------------------------|
| `LLM_PROVIDER`       | Yes                    | `openai`                 | LLM backend (`openai`, `openrouter`, `ollama`) |
| `MODEL`              | Yes                    | `gpt-4.1-mini`           | Model name to use                    |
| `OPENAI_API_KEY`     | If provider is `openai` | –                        | OpenAI API key                       |
| `OPENROUTER_API_KEY` | If provider is `openrouter` | –                    | OpenRouter API key                   |
| `OLLAMA_BASE_URL`    | No                     | `http://localhost:11434`  | Ollama server URL                    |
| `TELEGRAM_BOT_TOKEN` | Yes                    | –                        | Telegram bot token                   |
| `TELEGRAM_CHAT_ID`   | Yes                    | –                        | Target chat ID                       |

## Usage

```bash
python run.py
```

The script will:
1. Validate your configuration (including provider-specific API keys).
2. Fetch articles from all RSS feeds.
3. Generate a Dutch briefing via your configured LLM provider.
4. Send the briefing to your Telegram chat.

## Architecture

```
app/
├── llm/
│   ├── base.py              # Abstract LLMProvider interface
│   ├── factory.py           # Provider selection (only class that instantiates providers)
│   ├── openai_provider.py   # OpenAI implementation
│   ├── openrouter_provider.py
│   └── ollama_provider.py
├── config.py                # Environment variable loading and validation
├── news_fetcher.py          # RSS feed fetching and deduplication
├── summarizer.py            # Prompt building and orchestration
├── telegram_sender.py       # Telegram message delivery
└── main.py                  # Application entry point
```

The summarization layer depends only on the `LLMProvider` abstraction. Adding a new provider (Anthropic, Gemini, Groq) requires only a new file in `app/llm/` and a new entry in the factory.

## Security

**.env contains sensitive credentials. Never commit it to version control.**
The `.gitignore` is configured to exclude `.env` by default. Always verify before pushing.

## Roadmap

- [ ] Anthropic Claude provider
- [ ] Google Gemini provider
- [ ] Groq provider
- [ ] Customisable RSS feed list via config
- [ ] Scheduled execution (cron / GitHub Actions)
- [ ] CLI flags for one-off vs. continuous mode

## License

MIT
