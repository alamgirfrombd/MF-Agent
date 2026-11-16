"""CLI health entry point."""
from database.connection import health_check
from app.config import get_settings

def main() -> None:
    s = get_settings()
    print(f"{s.app_name} | environment={s.app_env}")
    print(health_check())

if __name__ == "__main__":
    main()
