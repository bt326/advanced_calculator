import os
import pandas as pd
from app.calculation import Calculation
from app.calculator_memento import CalculatorMemento
from app.exceptions import HistoryError


class History:
    """
    Manages calculation history with undo/redo functionality
    and CSV persistence.
    """

    def __init__(self, max_size=100):
        self._history = []
        self._undo_stack = []
        self._redo_stack = []
        self._max_size = max_size

    #  Core History 

    def add(self, calculation):
        """Add new calculation and save state for undo."""
        self._undo_stack.append(self._save_state())
        self._redo_stack.clear()

        self._history.append(calculation)

        if len(self._history) > self._max_size:
            self._history.pop(0)

    def get_all(self):
        return list(self._history)

    def clear(self):
        self._undo_stack.append(self._save_state())
        self._history.clear()

    # Undo / Redo

    def undo(self):
        if not self._undo_stack:
            raise HistoryError("No actions to undo.")

        self._redo_stack.append(self._save_state())
        memento = self._undo_stack.pop()
        self._restore_state(memento)

    def redo(self):
        if not self._redo_stack:
            raise HistoryError("No actions to redo.")

        self._undo_stack.append(self._save_state())
        memento = self._redo_stack.pop()
        self._restore_state(memento)

    def _save_state(self):
        return CalculatorMemento(self._history)

    def _restore_state(self, memento):
        self._history = memento.get_state()

    #  CSV Persistence #

    def save_to_csv(self, file_path, encoding="utf-8"):
        """Save full history to CSV file."""
        data = [
            {
                "operation": calc.operation,
                "operand1": calc.operand1,
                "operand2": calc.operand2,
                "result": calc.result,
                "timestamp": calc.timestamp.isoformat(),
            }
            for calc in self._history
        ]

        df = pd.DataFrame(data)
        df.to_csv(file_path, index=False, encoding=encoding)

    def load_from_csv(self, file_path, encoding="utf-8"):
        """Load history from CSV file."""
        if not os.path.exists(file_path):
            raise HistoryError("History file not found.")

        df = pd.read_csv(file_path, encoding=encoding)

        self._undo_stack.append(self._save_state())
        self._history.clear()

        for _, row in df.iterrows():
            calc = Calculation(
                row["operation"],
                float(row["operand1"]),
                float(row["operand2"]),
                float(row["result"]),
            )
            self._history.append(calc)