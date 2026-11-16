"""OpenAI adapter placeholder. Add official SDK integration when cloud provider is selected."""
class OpenAIProviderNotReady(RuntimeError):
    pass

def chat(prompt: str, system: str = "") -> str:
    raise OpenAIProviderNotReady("OpenAI adapter is not configured in this starter release")
