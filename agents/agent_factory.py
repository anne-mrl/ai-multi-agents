from strategies.faiss_strategy import FAISSResolution
from strategies.gpt_strategy import GPTResolution
from agents.faiss_manager import FAISSKnowledgeDatabaseManager
from agents.main_agent import MainAgent
from database.sqlite3_database import SQLite3Database


class AgentFactory:
    """Factory to instantiate agents dynamically."""

    @staticmethod
    def create_faiss_manager() -> FAISSKnowledgeDatabaseManager:
        return FAISSKnowledgeDatabaseManager("database/data_test_python.json")

    @staticmethod
    def create_database() -> SQLite3Database:
        return SQLite3Database()

    @staticmethod
    def create_main_agent() -> MainAgent:
        faiss_strategy = FAISSResolution(AgentFactory.create_faiss_manager())
        gpt_strategy = GPTResolution()
        faiss_strategy.fallback = gpt_strategy  # If FAISS fails, fallback to GPT4o
        return MainAgent(faiss_strategy)
