# AI News Intelligence Agent

A Python tool that fetches the latest AI news from multiple RSS feeds, generates a structured English briefing using an LLM of your choice, and sends it to a Telegram chat.

## Features

- **Multi-source RSS aggregation** – TechCrunch AI, The Verge AI, VentureBeat AI, Artificial Intelligence News
- **Smart deduplication** – removes duplicate articles by lowercase title
- **Provider-agnostic LLM layer** – swap between OpenAI, OpenRouter, and Ollama without changing code
- **English briefing** – structured summary with key developments, analysis, opportunities, risks, and sources
- **Telegram delivery** – sends the briefing directly to your Telegram chat with automatic message splitting
- **Scheduled or manual execution** – runs daily at 06:00 UTC via GitHub Actions, with manual trigger support
- **Production-ready** – clean architecture, dependency injection, custom exceptions, and type hints throughout

## Installation

```bash
git clone https://github.com/yourusername/ai-news-intelligence-agent.git
cd ai-news-intelligence-agent

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

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

OPENROUTER_API_KEY=your_openrouter_api_key
OPENAI_API_KEY=your_openai_api_key

TELEGRAM_BOT_TOKEN=your_telegram_bot_token
TELEGRAM_CHAT_ID=your_chat_id
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
3. Generate a briefing via your configured LLM provider.
4. Send the briefing to your Telegram chat.

## GitHub Actions

A workflow at `.github/workflows/daily-news.yml` runs the agent automatically every day.

### Schedule

The workflow runs daily at **06:00 UTC**. To change the schedule, edit the `cron` expression:

```yaml
schedule:
  - cron: "0 6 * * *"
```

GitHub Actions uses UTC for all scheduled events.

### Secrets Configuration

1. Go to your repository on GitHub.
2. Navigate to **Settings** → **Secrets and variables** → **Actions**.
3. Click **New repository secret** and add each of the following:

| Secret                 | Required               | Description                          |
|------------------------|------------------------|--------------------------------------|
| `LLM_PROVIDER`         | Yes                    | LLM backend                          |
| `MODEL`                | Yes                    | Model name                           |
| `OPENAI_API_KEY`       | If provider is `openai` | OpenAI API key                      |
| `OPENROUTER_API_KEY`   | If provider is `openrouter` | OpenRouter API key              |
| `OLLAMA_BASE_URL`      | No                     | Ollama server URL                    |
| `TELEGRAM_BOT_TOKEN`   | Yes                    | Telegram bot token                   |
| `TELEGRAM_CHAT_ID`     | Yes                    | Target chat ID                       |

### Manual Trigger

1. Go to your repository on GitHub.
2. Click the **Actions** tab.
3. Select **Daily AI News Briefing** in the left sidebar.
4. Click **Run workflow** → **Run workflow**.

## Security

**.env contains sensitive credentials. Never commit it to version control.**
The `.gitignore` is configured to exclude `.env` by default. Always verify before pushing.

See [`docs/security.md`](docs/security.md) for a detailed guide on secret management and what to do if you accidentally push a key.

## Architecture

```
app/
├── core/                  # Cross-cutting concerns (config, logging, exceptions)
├── llm/                   # LLM provider abstraction (abstract base + implementations)
├── models/                # Domain models (Article dataclass)
├── prompts/               # LLM prompt templates
├── services/              # Business logic (news_fetcher, summarizer, telegram_sender)
└── main.py                # Application entry point
```

The summarisation layer depends only on the `LLMProvider` abstraction. Adding a new provider (Anthropic, Gemini, Groq) requires only a new file in `app/llm/` and a new entry in the factory.

## Roadmap

See [`docs/roadmap.md`](docs/roadmap.md) for the full roadmap.

## Contributing

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/my-feature`).
3. Commit your changes (`git commit -m 'Add my feature'`).
4. Push to the branch (`git push origin feature/my-feature`).
5. Open a Pull Request.

## License

MIT
