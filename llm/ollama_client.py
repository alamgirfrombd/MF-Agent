"""Minimal Ollama chat client."""
import requests
from app.config import get_settings

def chat(prompt: str, system: str = "") -> str:
    s = get_settings()
    response = requests.post(
        f"{s.ollama_base_url.rstrip('/')}/api/chat",
        json={"model": s.ollama_model,
              "messages": ([{"role": "system", "content": system}] if system else []) +
                          [{"role": "user", "content": prompt}],
              "stream": False,
              "options": {"temperature": s.ollama_temperature}},
        timeout=s.ollama_timeout,
    )
    response.raise_for_status()
    return response.json()["message"]["content"]
