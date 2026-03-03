import os
import tempfile
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


def test_redo_empty():
    history = History()

    with pytest.raises(HistoryError):
        history.redo()


def test_clear_history():
    history = History()
    calc = Calculation("add", 2, 3, 5)

    history.add(calc)
    history.clear()

    assert len(history.get_all()) == 0


def test_max_size_limit():
    history = History(max_size=1)

    history.add(Calculation("add", 1, 1, 2))
    history.add(Calculation("add", 2, 2, 4))

    assert len(history.get_all()) == 1


def test_save_and_load_csv():
    history = History()
    calc = Calculation("add", 2, 3, 5)
    history.add(calc)

    temp_file = tempfile.NamedTemporaryFile(delete=False)
    file_path = temp_file.name
    temp_file.close()

    history.save_to_csv(file_path)

    new_history = History()
    new_history.load_from_csv(file_path)

    assert len(new_history.get_all()) == 1
    assert new_history.get_all()[0].result == 5

    os.remove(file_path)


def test_load_non_existing_file():
    history = History()

    with pytest.raises(HistoryError):
        history.load_from_csv("non_existing_file.csv")