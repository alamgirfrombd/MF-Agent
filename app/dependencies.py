"""Shared application dependencies; extend with authenticated request context later."""
from app.config import get_settings

def get_app_settings():
    return get_settings()
