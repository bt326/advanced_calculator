import pytest
from app.calculator_config import CalculatorConfig
from app.exceptions import ConfigurationError


def test_config_defaults():
    config = CalculatorConfig()

    assert config.max_history_size > 0
    assert isinstance(config.auto_save, bool)
    assert config.precision > 0
    assert config.max_input_value > 0
    assert config.default_encoding == "utf-8"


def test_config_env_override(monkeypatch):
    monkeypatch.setenv("CALCULATOR_MAX_HISTORY_SIZE", "50")
    monkeypatch.setenv("CALCULATOR_AUTO_SAVE", "false")
    monkeypatch.setenv("CALCULATOR_PRECISION", "3")
    monkeypatch.setenv("CALCULATOR_MAX_INPUT_VALUE", "500")
    monkeypatch.setenv("CALCULATOR_DEFAULT_ENCODING", "utf-16")

    config = CalculatorConfig()

    assert config.max_history_size == 50
    assert config.auto_save is False
    assert config.precision == 3
    assert config.max_input_value == 500.0
    assert config.default_encoding == "utf-16"


def test_invalid_config(monkeypatch):
    monkeypatch.setenv("CALCULATOR_PRECISION", "invalid")

    with pytest.raises(ConfigurationError):
        CalculatorConfig()