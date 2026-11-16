"""Append-only metadata audit log; never log credentials or result rows."""
import json
from datetime import datetime, timezone
from pathlib import Path
from app.config import get_settings

def write_audit(event: dict) -> None:
    settings = get_settings()
    path = settings.resolve_path(settings.audit_log_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    safe = {"timestamp": datetime.now(timezone.utc).isoformat(), **event}
    with path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(safe, ensure_ascii=False, default=str) + "\n")
