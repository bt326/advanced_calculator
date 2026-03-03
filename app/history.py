from app.calculator_memento import CalculatorMemento
from app.exceptions import HistoryError


class History:
    """
    Manages calculation history with undo/redo functionality.
    """

    def __init__(self, max_size=100):
        self._history = []
        self._undo_stack = []
        self._redo_stack = []
        self._max_size = max_size

    def add(self, calculation):
        """
        Add new calculation and save state for undo.
        """
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