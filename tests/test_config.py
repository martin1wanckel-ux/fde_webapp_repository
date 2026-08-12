from src.config.config import Config
import os
import pytest 

def test_config_from_env_valid(monkeypatch):
    monkeypatch.setenv("PORT", "8080")
    monkeypatch.setenv("APP_ENV", "development")
    monkeypatch.setenv("LOG_LEVEL", "DEBUG")
    # Make the instance of our Config class using the from_env class method
    config = Config.from_env()
    # Check that the config object has the expected values
    assert config.port == 8080, f"Failed: Expected port to be 8080, but got {config.port}"
    assert config.app_env == "development", f"Failed: Expected app_env to be 'development', but got {config.app_env}"
    assert config.log_level == "DEBUG", f"Failed: Expected log_level to be 'DEBUG', but got {config.log_level}"


    # Explain assert: 
    # if not condition:
        # raise AssertionError()

def test_missing_env_vars(monkeypatch):
    clear_env_vars = ["PORT", "APP_ENV", "LOG_LEVEL"]
    for var in clear_env_vars:
        monkeypatch.delenv(var, raising=False)
    config = Config.from_env() 
    assert config.port == 8000, f"Failed: Expected default port to be 8000, but got {config.port}"
    assert config.app_env == "development", f"Failed: Expected default app_env to be 'development', but got {config.app_env}"
    assert config.log_level == "INFO", f"Failed: Expected default log_level to be 'INFO', but got {config.log_level}"


def test_invalid_port(monkeypatch):
    invalid_port = "invalid_port"
    monkeypatch.setenv("PORT", invalid_port)
    with pytest.raises(ValueError, match = f"Invalid PORT value"): # Match is a regex pattern or a text pattern. .dot is a character in regex and we should be careful here. I know the error will happen here
        test_config = Config.from_env()     # with -> context manager 

    