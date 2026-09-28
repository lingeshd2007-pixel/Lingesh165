"""Central Gemini API client for EduGenie."""

import os
from functools import lru_cache

from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

MODEL_NAME = os.getenv("GEMINI_MODEL", "gemini-3.8-flash").strip()
API_KEY = os.getenv("GEMINI_API_KEY", "").strip()


@lru_cache(maxsize=1)
def get_client() -> genai.Client:
    """Create one reusable Gemini client."""
    if not API_KEY or API_KEY == "PASTE_YOUR_GEMINI_API_KEY_HERE":
        raise RuntimeError(
            "GEMINI_API_KEY is missing. Create a .env file and add your Gemini API key."
        )
    return genai.Client(api_key=API_KEY)


def generate_text(
    prompt: str,
    *,
    temperature: float = 0.3,
    max_output_tokens: int = 2048,
) -> str:
    """Generate text with Gemini and return a clean string."""
    client = get_client()

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt,
        config=types.GenerateContentConfig(
            temperature=temperature,
            max_output_tokens=max_output_tokens,
        ),
    )

    text = getattr(response, "text", None)
    if not text or not text.strip():
        raise RuntimeError("Gemini returned an empty response.")

    return text.strip()
