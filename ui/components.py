"""Reusable UI display helpers."""
def status_label(status: str) -> str:
    return {"draft": "Draft — not executable", "review": "Under review",
            "active": "Active", "disabled": "Disabled"}.get(status, "Unknown")
