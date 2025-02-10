from strategies.base_strategy import ResolutionStrategy


class MainAgent:
    """MainAgent first asks FAISS Agent, then falls back to GPT-4o Agent."""

    def __init__(self, strategy: ResolutionStrategy):
        self.strategy = strategy

    def process_request(self, user_question: str) -> str:
        """Executes the resolution strategy, with fallback if necessary."""
        return self.strategy.execute(user_question)
