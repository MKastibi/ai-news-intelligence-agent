import os
from dotenv import load_dotenv

load_dotenv()

VALID_PROVIDERS = ("openai", "openrouter", "ollama")


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
        missing: list[str] = []

        if not cls.telegram_bot_token:
            missing.append("TELEGRAM_BOT_TOKEN")
        if not cls.telegram_chat_id:
            missing.append("TELEGRAM_CHAT_ID")

        provider = cls.llm_provider.lower()
        if provider not in VALID_PROVIDERS:
            raise ValueError(
                f"Unsupported LLM_PROVIDER: '{cls.llm_provider}'. "
                f"Supported values: {', '.join(VALID_PROVIDERS)}"
            )

        key_map = {
            "openai": ("OPENAI_API_KEY", cls.openai_api_key),
            "openrouter": ("OPENROUTER_API_KEY", cls.openrouter_api_key),
        }

        env_name, key_value = key_map.get(provider, ("", ""))
        if env_name and not key_value:
            missing.append(f"{env_name} (required for LLM_PROVIDER={provider})")

        if missing:
            raise ValueError(
                f"Missing required environment variables: {', '.join(missing)}. "
                "Ensure they are set in your .env file."
            )
