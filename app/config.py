"""Central, validated application configuration."""
from functools import lru_cache
from pathlib import Path
from pydantic import Field, SecretStr, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict

ROOT_DIR = Path(__file__).resolve().parents[1]

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=ROOT_DIR / ".env", env_file_encoding="utf-8", extra="ignore")
    app_env: str = "development"
    app_name: str = "MF Agent"
    log_level: str = "INFO"
    sql_server: str = "localhost"
    sql_database: str = "DataAnalysis"
    sql_driver: str = "ODBC Driver 18 for SQL Server"
    sql_trusted_connection: bool = True
    sql_username: str = ""
    sql_password: SecretStr = SecretStr("")
    sql_encrypt: bool = True
    sql_trust_server_certificate: bool = True
    sql_connection_timeout: int = Field(default=15, ge=1, le=120)
    sql_query_timeout: int = Field(default=30, ge=1, le=600)
    sql_max_rows: int = Field(default=200, ge=1, le=10000)
    llm_provider: str = "ollama"
    ollama_base_url: str = "http://localhost:11434"
    ollama_model: str = "qwen2.5-coder:3b"
    ollama_timeout: int = Field(default=180, ge=1)
    ollama_temperature: float = Field(default=0.0, ge=0, le=2)
    openai_api_key: SecretStr = SecretStr("")
    openai_model: str = "gpt-4.1-mini"
    max_question_chars: int = Field(default=1000, ge=1)
    max_sql_chars: int = Field(default=12000, ge=100)
    max_result_bytes: int = Field(default=5_000_000, ge=1024)
    max_concurrent_requests: int = Field(default=2, ge=1)
    audit_log_path: str = "logs/agent_audit.jsonl"
    registry_path: str = "registry/master_registry.json"

    @field_validator("app_env")
    @classmethod
    def valid_env(cls, value: str) -> str:
        value = value.lower().strip()
        if value not in {"development", "test", "production"}:
            raise ValueError("APP_ENV must be development, test, or production")
        return value

    @field_validator("llm_provider")
    @classmethod
    def valid_provider(cls, value: str) -> str:
        value = value.lower().strip()
        if value not in {"ollama", "openai"}:
            raise ValueError("LLM_PROVIDER must be ollama or openai")
        return value

    @property
    def root_dir(self) -> Path:
        return ROOT_DIR

    def resolve_path(self, value: str) -> Path:
        path = Path(value)
        return path if path.is_absolute() else ROOT_DIR / path

@lru_cache
def get_settings() -> Settings:
    return Settings()
