"""Safe planning boundary: the model proposes a plan, never executes SQL itself."""
import json
from llm.provider import chat

SYSTEM_PROMPT = """You are a microfinance data analysis planner. Use only supplied registry metadata.
Do not invent table names, columns, keys, joins, formulas, or metrics. If metadata is insufficient,
return status=needs_clarification. Return JSON only with keys status, dataset_id, intent, filters,
metrics, dimensions, clarification. Never return executable SQL."""

def create_plan(question: str, registry_summary: dict) -> dict:
    raw = chat(json.dumps({"question": question, "available_datasets": registry_summary}, ensure_ascii=False), SYSTEM_PROMPT)
    try:
        plan = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise ValueError("LLM did not return valid JSON plan") from exc
    if plan.get("status") not in {"ready", "needs_clarification"}:
        raise ValueError("Invalid plan status")
    return plan
