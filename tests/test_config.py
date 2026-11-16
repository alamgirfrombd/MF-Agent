from app.config import Settings

def test_default_settings_are_valid():
    settings = Settings(_env_file=None)
    assert settings.app_env == "development"
    assert settings.sql_max_rows > 0
