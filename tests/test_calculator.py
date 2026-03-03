import pytest
from app.calculator import Calculator
from app.exceptions import OperationError, ValidationError


def test_perform_add():
    calc = Calculator()
    result = calc.perform_operation("add", 2, 3)
    assert result == 5


def test_invalid_operation():
    calc = Calculator()
    with pytest.raises(OperationError):
        calc.perform_operation("invalid", 2, 3)


def test_validation_error():
    calc = Calculator()
    with pytest.raises(ValidationError):
        calc.perform_operation("add", "abc", 3)


def test_history_integration():
    calc = Calculator()
    calc.perform_operation("add", 2, 3)
    assert len(calc.get_history()) == 1