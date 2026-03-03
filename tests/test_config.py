from app.calculator_config import CalculatorConfig


def test_config_defaults():
    config = CalculatorConfig()
    assert config.max_history_size > 0
    assert isinstance(config.auto_save, bool)
    assert config.precision > 0
    assert config.max_input_value > 0