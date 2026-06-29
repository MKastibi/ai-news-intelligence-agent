# Development

## Prerequisites

- Python 3.12+
- pip

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/ai-news-intelligence-agent.git
cd ai-news-intelligence-agent
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate       # Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

```bash
cp .env.example .env
```

Edit `.env` with your API keys (see README for details).

### 5. Run the application

```bash
python run.py
```

## Running Tests

```bash
# Install pytest if not already installed
pip install pytest

# Run all tests
python -m pytest tests/ -v

# Run a specific test file
python -m pytest tests/test_deduplicator.py -v
```

## Docker

### Build

```bash
docker build -t ai-news-agent .
```

### Run

```bash
docker run --env-file .env ai-news-agent
```

## Code Quality

- All Python files use type hints.
- Custom exceptions are defined in `app/core/exceptions.py`.
- Logging is configured via `app/core/logger.py`.
- The LLM layer uses an abstract base class and factory pattern.

## Adding a New LLM Provider

1. Create a new file in `app/llm/` (e.g. `anthropic_provider.py`).
2. Implement the `LLMProvider` interface from `app/llm/base.py`.
3. Add the provider to the factory in `app/llm/factory.py`.
4. Add the required env vars to `app/core/config.py` and `.env.example`.

No other code needs to change.

## CI/CD

- **Daily schedule** — `.github/workflows/daily-news.yml` runs the agent at 06:00 UTC.
- **CI** — `.github/workflows/ci.yml` runs tests on every push / PR to `main`.
