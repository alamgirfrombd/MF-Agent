"""Command-friendly database health check."""
from database.connection import health_check

def check() -> dict:
    return health_check()
