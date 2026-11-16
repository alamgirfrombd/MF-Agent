"""Executes validated read-only queries with a hard row cap."""
import pandas as pd
from app.config import get_settings
from database.connection import get_connection
from sql_engine.sql_guard import validate_read_only_sql

def execute_select(sql: str, params: tuple = ()) -> pd.DataFrame:
    settings = get_settings()
    safe_sql = validate_read_only_sql(sql, settings.max_sql_chars)
    with get_connection(settings) as conn:
        cursor = conn.cursor()
        cursor.timeout = settings.sql_query_timeout
        cursor.execute(safe_sql, params)
        if cursor.description is None:
            raise ValueError("Query did not return a result set")
        columns = [col[0] for col in cursor.description]
        rows = cursor.fetchmany(settings.sql_max_rows + 1)
        if len(rows) > settings.sql_max_rows:
            rows = rows[:settings.sql_max_rows]
        return pd.DataFrame.from_records(rows, columns=columns)
