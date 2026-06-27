import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    llm_provider: str = os.getenv("LLM_PROVIDER", "openai")
    model: str = os.getenv("MODEL") or os.getenv("OPENAI_MODEL", "gpt-4.1-mini")

    telegram_bot_token: str = os.getenv("TELEGRAM_BOT_TOKEN", "")
    telegram_chat_id: str = os.getenv("TELEGRAM_CHAT_ID", "")

    openai_api_key: str = os.getenv("OPENAI_API_KEY", "")
    openrouter_api_key: str = os.getenv("OPENROUTER_API_KEY", "")
    ollama_base_url: str = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")

    @classmethod
    def validate(cls) -> None:
        missing = []
        if not cls.telegram_bot_token:
            missing.append("TELEGRAM_BOT_TOKEN")
        if not cls.telegram_chat_id:
            missing.append("TELEGRAM_CHAT_ID")

        provider = cls.llm_provider.lower()
        if provider == "openai" and not cls.openai_api_key:
            missing.append("OPENAI_API_KEY (required for LLM_PROVIDER=openai)")
        elif provider == "openrouter" and not cls.openrouter_api_key:
            missing.append("OPENROUTER_API_KEY (required for LLM_PROVIDER=openrouter)")
        elif provider not in ("openai", "openrouter", "ollama"):
            raise ValueError(
                f"Unsupported LLM_PROVIDER: '{cls.llm_provider}'. "
                f"Supported values: openai, openrouter, ollama"
            )

        if missing:
            raise ValueError(
                f"Missing required environment variables: {', '.join(missing)}. "
                "Ensure they are set in your .env file."
            )
