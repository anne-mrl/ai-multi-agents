import openai
import os
from dotenv import load_dotenv


def load_api_key():
    load_dotenv()
    openai.api_key = os.getenv("OPENAI_API_KEY")
    if not openai.api_key:
        raise EnvironmentError("'OPENAI_API_KEY' is not set in .env file")
