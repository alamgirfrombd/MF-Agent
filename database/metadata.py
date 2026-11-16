"""Metadata utility functions."""
def index_columns(schema_export: dict) -> dict:
    result = {}
    for col in schema_export.get("columns", []):
        key = f"{col.get('schema_name')}.{col.get('table_name')}"
        result.setdefault(key, []).append(col)
    return result
