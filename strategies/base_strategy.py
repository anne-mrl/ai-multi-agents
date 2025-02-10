from abc import ABC, abstractmethod
from typing import Optional


class ResolutionStrategy(ABC):
    """Abstract class for query resolution with optional fallback mechanism."""

    def __init__(self, fallback: Optional["ResolutionStrategy"] = None):
        self.fallback = fallback

    @abstractmethod
    def resolve(self, question: str) -> Optional[str]:
        pass

    def execute(self, question: str) -> str:
        """Executes the strategy and falls back if necessary."""
        response = self.resolve(question)
        if response:
            return response
        elif self.fallback:
            return self.fallback.execute(question)
        else:
            return "Sorry, no answer could be found."
