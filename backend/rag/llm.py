import os
from functools import lru_cache

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

# Load environment variables so GOOGLE_API_KEY is available from .env.
load_dotenv()


@lru_cache(maxsize=1)
def get_llm() -> ChatGoogleGenerativeAI:
    """Create and reuse one Gemini model instance."""
    api_key = os.getenv("GOOGLE_API_KEY", "").strip()
    if not api_key:
        raise ValueError("GOOGLE_API_KEY is missing. Please set it in your .env file.")

    return ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0.2,
        google_api_key=api_key,
    )
