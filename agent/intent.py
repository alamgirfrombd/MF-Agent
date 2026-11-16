"""Lightweight input checks before invoking an LLM planner."""
from app.config import get_settings

def validate_question(question: str) -> str:
    if not isinstance(question, str):
        raise TypeError("Question must be text")
    question = question.strip()
    if not question:
        raise ValueError("Question cannot be empty")
    if len(question) > get_settings().max_question_chars:
        raise ValueError("Question exceeds configured length limit")
    return question
