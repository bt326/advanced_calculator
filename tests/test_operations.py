import pytest
from app.operations import (
    AddOperation,
    SubtractOperation,
    MultiplyOperation,
    DivideOperation,
    PowerOperation,
    RootOperation,
    ModulusOperation,
    IntegerDivideOperation,
    PercentOperation,
    AbsoluteDifferenceOperation,
    OperationFactory,
)
from app.exceptions import OperationError


def test_add_operation():
    assert AddOperation().execute(2, 3) == 5


def test_subtract_operation():
    assert SubtractOperation().execute(5, 3) == 2


def test_multiply_operation():
    assert MultiplyOperation().execute(4, 5) == 20


def test_divide_operation():
    assert DivideOperation().execute(10, 2) == 5


def test_divide_by_zero():
    with pytest.raises(OperationError):
        DivideOperation().execute(10, 0)


def test_power_operation():
    assert PowerOperation().execute(2, 3) == 8


def test_root_operation():
    assert RootOperation().execute(9, 2) == 3


def test_root_zero_degree():
    with pytest.raises(OperationError):
        RootOperation().execute(10, 0)


def test_root_even_negative():
    with pytest.raises(OperationError):
        RootOperation().execute(-4, 2)


def test_modulus_operation():
    assert ModulusOperation().execute(10, 3) == 1


def test_modulus_zero():
    with pytest.raises(OperationError):
        ModulusOperation().execute(10, 0)


def test_integer_divide_operation():
    assert IntegerDivideOperation().execute(10, 3) == 3


def test_integer_divide_zero():
    with pytest.raises(OperationError):
        IntegerDivideOperation().execute(10, 0)


def test_percent_operation():
    assert PercentOperation().execute(50, 200) == 25


def test_percent_zero():
    with pytest.raises(OperationError):
        PercentOperation().execute(10, 0)


def test_absolute_difference_operation():
    assert AbsoluteDifferenceOperation().execute(10, 4) == 6


def test_absolute_difference_negative():
    assert AbsoluteDifferenceOperation().execute(4, 10) == 6


def test_operation_factory_valid():
    op = OperationFactory.create_operation("add")
    assert isinstance(op, AddOperation)


def test_operation_factory_invalid():
    with pytest.raises(OperationError):
        OperationFactory.create_operation("invalid_operation")