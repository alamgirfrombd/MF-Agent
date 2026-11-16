"""LLM provider dispatch. OpenAI support is intentionally explicit and optional."""
from app.config import get_settings
from llm.ollama_client import chat as ollama_chat

def chat(prompt: str, system: str = "") -> str:
    settings = get_settings()
    if settings.llm_provider == "ollama":
        return ollama_chat(prompt, system)
    raise NotImplementedError("OpenAI provider adapter is not implemented in this starter build")
