"""Approved query templates will be added after the live schema is verified."""
TEMPLATES: dict[str, str] = {}

def get_template(template_id: str) -> str:
    try:
        return TEMPLATES[template_id]
    except KeyError as exc:
        raise KeyError(f"No approved SQL template: {template_id}") from exc
