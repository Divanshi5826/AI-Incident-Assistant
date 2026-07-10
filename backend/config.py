import os
from dataclasses import dataclass

from dotenv import load_dotenv

# Load environment variables from a local .env file when present.
load_dotenv()


@dataclass(frozen=True)
class Settings:
    project_name: str = os.getenv("PROJECT_NAME", "AI Incident Assistant")
    api_title: str = os.getenv("API_TITLE", "AI Incident Assistant API")
    api_version: str = os.getenv("API_VERSION", "0.1.0")
    cors_origins: tuple[str, ...] = tuple(
        origin.strip()
        for origin in os.getenv("CORS_ORIGINS", "http://localhost:5173").split(",")
        if origin.strip()
    )


settings = Settings()
