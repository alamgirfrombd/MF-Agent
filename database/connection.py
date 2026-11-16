"""SQL Server connection helpers. Connections are created on demand, not at import time."""
import pyodbc
from app.config import Settings, get_settings

def build_connection_string(settings: Settings | None = None) -> str:
    s = settings or get_settings()
    parts = [
        f"DRIVER={{{s.sql_driver}}}", f"SERVER={s.sql_server}", f"DATABASE={s.sql_database}",
        f"Encrypt={'yes' if s.sql_encrypt else 'no'}",
        f"TrustServerCertificate={'yes' if s.sql_trust_server_certificate else 'no'}",
        f"Connection Timeout={s.sql_connection_timeout}",
    ]
    if s.sql_trusted_connection:
        parts.append("Trusted_Connection=yes")
    else:
        parts.extend([f"UID={s.sql_username}", f"PWD={s.sql_password.get_secret_value()}"])
    return ";".join(parts) + ";"

def get_connection(settings: Settings | None = None):
    s = settings or get_settings()
    connection = pyodbc.connect(build_connection_string(s), timeout=s.sql_connection_timeout)
    connection.timeout = s.sql_query_timeout
    return connection

def health_check(settings: Settings | None = None) -> dict:
    s = settings or get_settings()
    with get_connection(s) as conn:
        row = conn.cursor().execute("SELECT DB_NAME(), SUSER_SNAME(), @@SERVERNAME").fetchone()
    return {"ok": True, "database": row[0], "login": row[1], "server": row[2]}
