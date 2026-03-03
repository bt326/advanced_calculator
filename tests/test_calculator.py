import pytest
from app.calculator import Calculator
from app.exceptions import OperationError, ValidationError


def test_perform_add():
    calc = Calculator()
    result = calc.perform_operation("add", 2, 3)
    assert result == 5


def test_invalid_operation_error():
    calc = Calculator()
    with pytest.raises(OperationError):
        calc.perform_operation("unknown", 2, 3)


def test_validation_error():
    calc = Calculator()
    with pytest.raises(ValidationError):
        calc.perform_operation("add", "abc", 3)


def test_max_input_validation():
    calc = Calculator()
    calc.config.max_input_value = 10

    with pytest.raises(ValidationError):
        calc.perform_operation("add", 100, 1)


def test_precision_applied():
    calc = Calculator()
    calc.config.precision = 2

    result = calc.perform_operation("divide", 10, 3)
    assert result == round(10 / 3, 2)


def test_undo_redo_integration():
    calc = Calculator()
    calc.perform_operation("add", 2, 3)
    calc.undo()
    assert len(calc.get_history()) == 0

    calc.redo()
    assert len(calc.get_history()) == 1


def test_clear_history():
    calc = Calculator()
    calc.perform_operation("add", 2, 3)
    calc.clear_history()
    assert len(calc.get_history()) == 0


def test_register_observer():
    calc = Calculator()

    class DummyObserver:
        def update(self, calculation):
            pass

    calc.register_observer(DummyObserver())
    assert len(calc._observers) > 0