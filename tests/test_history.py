import pytest
from app.history import History
from app.calculation import Calculation
from app.exceptions import HistoryError


def test_add_and_get():
    history = History()
    calc = Calculation("add", 2, 3, 5)

    history.add(calc)
    assert len(history.get_all()) == 1


def test_undo():
    history = History()
    calc = Calculation("add", 2, 3, 5)

    history.add(calc)
    history.undo()

    assert len(history.get_all()) == 0


def test_redo():
    history = History()
    calc = Calculation("add", 2, 3, 5)

    history.add(calc)
    history.undo()
    history.redo()

    assert len(history.get_all()) == 1


def test_undo_empty():
    history = History()
    with pytest.raises(HistoryError):
        history.undo()