from app.core.config import Config
from app.llm.base import LLMProvider
from app.llm.openai_provider import OpenAIProvider
from app.llm.openrouter_provider import OpenRouterProvider
from app.llm.ollama_provider import OllamaProvider


def create_provider() -> LLMProvider:
    provider_name = Config.llm_provider.lower()

    if provider_name == "openai":
        if not Config.openai_api_key:
            raise ValueError(
                "OPENAI_API_KEY is required when LLM_PROVIDER is 'openai'."
            )
        return OpenAIProvider(
            api_key=Config.openai_api_key,
            model=Config.model,
        )

    if provider_name == "openrouter":
        if not Config.openrouter_api_key:
            raise ValueError(
                "OPENROUTER_API_KEY is required when LLM_PROVIDER is 'openrouter'."
            )
        return OpenRouterProvider(
            api_key=Config.openrouter_api_key,
            model=Config.model,
        )

    if provider_name == "ollama":
        return OllamaProvider(
            base_url=Config.ollama_base_url,
            model=Config.model,
        )

    raise ValueError(
        f"Unsupported LLM_PROVIDER: '{provider_name}'. "
        f"Supported values: openai, openrouter, ollama"
    )
