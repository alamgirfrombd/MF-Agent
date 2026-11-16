"""Validation façade for callers."""
from sql_engine.sql_guard import validate_read_only_sql

def validate(sql: str) -> str:
    return validate_read_only_sql(sql)
