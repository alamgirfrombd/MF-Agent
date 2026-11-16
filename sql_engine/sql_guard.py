"""Conservative SELECT-only SQL validation using SQLGlot."""
import sqlglot
from sqlglot import exp

class SQLRejected(ValueError):
    pass

FORBIDDEN_NODES = (exp.Insert, exp.Update, exp.Delete, exp.Drop, exp.Create, exp.Alter,
                   exp.Command, exp.Merge, exp.Transaction, exp.TruncateTable)

def validate_read_only_sql(sql: str, max_chars: int = 12000) -> str:
    if not isinstance(sql, str) or not sql.strip():
        raise SQLRejected("SQL is empty")
    if len(sql) > max_chars:
        raise SQLRejected("SQL exceeds configured maximum length")
    try:
        statements = sqlglot.parse(sql, read="tsql")
    except Exception as exc:
        raise SQLRejected(f"SQL parse failed: {exc}") from exc
    statements = [s for s in statements if s is not None]
    if len(statements) != 1:
        raise SQLRejected("Exactly one SQL statement is allowed")
    tree = statements[0]
    if not isinstance(tree, (exp.Select, exp.Union, exp.Intersect, exp.Except)):
        raise SQLRejected("Only SELECT queries are allowed")
    for node in tree.walk():
        if isinstance(node, FORBIDDEN_NODES):
            raise SQLRejected(f"Forbidden SQL operation: {type(node).__name__}")
        if isinstance(node, exp.Into):
            raise SQLRejected("SELECT INTO is not allowed")
    return tree.sql(dialect="tsql")
