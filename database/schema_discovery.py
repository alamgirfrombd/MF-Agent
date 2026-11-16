"""Read-only SQL Server metadata discovery; exports metadata without row-level data."""
from pathlib import Path
import json
from database.connection import get_connection

TABLES_SQL = """SELECT s.name AS schema_name, t.name AS table_name,
       SUM(CASE WHEN p.index_id IN (0,1) THEN p.rows ELSE 0 END) AS approximate_rows
FROM sys.tables t JOIN sys.schemas s ON t.schema_id=s.schema_id
LEFT JOIN sys.partitions p ON p.object_id=t.object_id
GROUP BY s.name,t.name ORDER BY s.name,t.name"""
COLUMNS_SQL = """SELECT s.name AS schema_name,t.name AS table_name,c.column_id,c.name AS column_name,
       TYPE_NAME(c.user_type_id) AS data_type,c.max_length,c.precision,c.scale,c.is_nullable,
       c.is_identity
FROM sys.tables t JOIN sys.schemas s ON t.schema_id=s.schema_id
JOIN sys.columns c ON c.object_id=t.object_id
ORDER BY s.name,t.name,c.column_id"""
KEYS_SQL = """SELECT fk.name AS constraint_name,
       OBJECT_SCHEMA_NAME(fkc.parent_object_id) AS schema_name,
       OBJECT_NAME(fkc.parent_object_id) AS table_name, pc.name AS column_name,
       OBJECT_SCHEMA_NAME(fkc.referenced_object_id) AS referenced_schema,
       OBJECT_NAME(fkc.referenced_object_id) AS referenced_table, rc.name AS referenced_column
FROM sys.foreign_key_columns fkc JOIN sys.foreign_keys fk
 ON fk.object_id=fkc.constraint_object_id
JOIN sys.columns pc ON pc.object_id=fkc.parent_object_id AND pc.column_id=fkc.parent_column_id
JOIN sys.columns rc ON rc.object_id=fkc.referenced_object_id AND rc.column_id=fkc.referenced_column_id
ORDER BY table_name,constraint_name"""
PK_SQL = """SELECT s.name AS schema_name,t.name AS table_name,c.name AS column_name,
       kc.name AS constraint_name, ic.key_ordinal
FROM sys.key_constraints kc JOIN sys.tables t ON t.object_id=kc.parent_object_id
JOIN sys.schemas s ON s.schema_id=t.schema_id
JOIN sys.index_columns ic ON ic.object_id=t.object_id AND ic.index_id=kc.unique_index_id
JOIN sys.columns c ON c.object_id=t.object_id AND c.column_id=ic.column_id
WHERE kc.type='PK' ORDER BY s.name,t.name,ic.key_ordinal"""

def _rows(cursor):
    names = [d[0] for d in cursor.description]
    return [dict(zip(names, row)) for row in cursor.fetchall()]

def discover_schema(connection=None) -> dict:
    owns = connection is None
    if owns:
        connection = get_connection()
    try:
        cur = connection.cursor()
        result = {"tables": _rows(cur.execute(TABLES_SQL)),
                  "columns": _rows(cur.execute(COLUMNS_SQL)),
                  "foreign_keys": _rows(cur.execute(KEYS_SQL)),
                  "primary_keys": _rows(cur.execute(PK_SQL))}
        result["metadata_only"] = True
        return result
    finally:
        if owns:
            connection.close()

def export_schema(path: str | Path = "output/schema_metadata.json") -> Path:
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    data = discover_schema()
    target.write_text(json.dumps(data, ensure_ascii=False, indent=2, default=str), encoding="utf-8")
    return target
