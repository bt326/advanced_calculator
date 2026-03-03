from app.operations import OperationFactory


def test_add():
    op = OperationFactory.create_operation("add")
    assert op.execute(2, 3) == 5


def test_subtract():
    op = OperationFactory.create_operation("subtract")
    assert op.execute(5, 3) == 2


def test_multiply():
    op = OperationFactory.create_operation("multiply")
    assert op.execute(4, 3) == 12


def test_divide():
    op = OperationFactory.create_operation("divide")
    assert op.execute(10, 2) == 5

import pytest
from app.exceptions import OperationError


def test_divide_by_zero():
    op = OperationFactory.create_operation("divide")
    with pytest.raises(OperationError):
        op.execute(10, 0)

def test_power():
    op = OperationFactory.create_operation("power")
    assert op.execute(2, 3) == 8