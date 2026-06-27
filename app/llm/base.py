from abc import ABC, abstractmethod


class LLMProvider(ABC):
    @abstractmethod
    def summarize(self, prompt: str) -> str:
        ...
