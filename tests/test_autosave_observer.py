import os
from app.autosave_observer import AutoSaveObserver
from app.calculator import Calculator


def test_autosave_disabled(tmp_path):
    calc = Calculator(register_default_observers=False)
    calc.config.auto_save = False

    file_path = tmp_path / "history.csv"
    observer = AutoSaveObserver(calc, history_file=file_path)

    observer.update(None)

    assert not file_path.exists()


def test_autosave_enabled_creates_file(tmp_path):
    calc = Calculator(register_default_observers=False)
    calc.config.auto_save = True

    file_path = tmp_path / "history.csv"
    observer = AutoSaveObserver(calc, history_file=file_path)

    calc.register_observer(observer)
    calc.perform_operation("add", 2, 3)

    assert file_path.exists()


def test_autosave_overwrites_existing_file(tmp_path):
    calc = Calculator(register_default_observers=False)
    calc.config.auto_save = True

    file_path = tmp_path / "history.csv"

    with open(file_path, "w") as f:
        f.write("old")

    observer = AutoSaveObserver(calc, history_file=file_path)
    calc.register_observer(observer)

    calc.perform_operation("add", 5, 5)

    assert file_path.exists()