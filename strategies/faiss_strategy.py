from typing import Optional
from strategies.base_strategy import ResolutionStrategy
from agents.faiss_manager import FAISSKnowledgeDatabaseManager


class FAISSResolution(ResolutionStrategy):
    """Strategy to resolve question using FAISS."""

    def __init__(self, faiss_manager: FAISSKnowledgeDatabaseManager, fallback: Optional[ResolutionStrategy] = None):
        super().__init__(fallback)
        self.faiss_manager = faiss_manager

    def resolve(self, question: str) -> Optional[str]:
        """Try to resolve using FAISS. Returns None if no match found."""
        result = self.faiss_manager.search(question)
        if result:
            return f"AGENT FAISS RESPONSE:\n\n" \
                   f"{result[0]['issue']}\n\n" \
                   f"Resolution steps: {' '.join(result[0]['steps'])}"
        return None
