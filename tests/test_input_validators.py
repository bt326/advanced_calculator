import pytest
from app.input_validators import validate_numeric, validate_max_value
from app.exceptions import ValidationError


def test_validate_numeric_success():
    assert validate_numeric("10") == 10.0


def test_validate_numeric_failure():
    with pytest.raises(ValidationError):
        validate_numeric("abc")


def test_validate_max_value_success():
    assert validate_max_value(5, 10) == 5


def test_validate_max_value_failure():
    with pytest.raises(ValidationError):
        validate_max_value(20, 10)