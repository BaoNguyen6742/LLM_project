import os
from pathlib import Path

import dotenv

root_path = Path(__file__).parents[3]

dotenv.load_dotenv(root_path / ".env/.env")

GROQ_API_KEY: str = os.getenv("GROQ_API_KEY")
GG_API_KEY: str = os.getenv("GG_API_KEY")
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
