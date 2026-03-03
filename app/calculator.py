from app.observer import Observer
from app.operations import OperationFactory
from app.input_validators import validate_numeric, validate_max_value
from app.calculation import Calculation
from app.history import History
from app.calculator_config import CalculatorConfig
from app.logging_observer import LoggingObserver
from app.autosave_observer import AutoSaveObserver


class Calculator:
    """
    Main calculator controller.
    """

    def __init__(self, register_default_observers=True):
        self.config = CalculatorConfig()
        self.history = History(self.config.max_history_size)
        self._observers = []

        if register_default_observers:
            self.register_observer(LoggingObserver())
            self.register_observer(AutoSaveObserver(self))

    def perform_operation(self, operation_name, a, b):
        a = validate_numeric(a)
        b = validate_numeric(b)

        a = validate_max_value(a, self.config.max_input_value)
        b = validate_max_value(b, self.config.max_input_value)

        operation = OperationFactory.create_operation(operation_name.lower())

        result = operation.execute(a, b)
        result = round(result, self.config.precision)

        calculation = Calculation(operation_name, a, b, result)
        self.history.add(calculation)

        self._notify_observers(calculation)

        return result

    def register_observer(self, observer: Observer):
        self._observers.append(observer)

    def _notify_observers(self, calculation):
        for observer in self._observers:
            observer.update(calculation)

    def undo(self):
        self.history.undo()

    def redo(self):
        self.history.redo()

    def get_history(self):
        return self.history.get_all()

    def clear_history(self):
        self.history.clear()


def run_repl():  # pragma: no cover
    calc = Calculator()

    print("Advanced Calculator")
    print("Type 'help' for commands. Type 'exit' to quit.")

    while True:
        user_input = input(">> ").strip()

        if user_input.lower() == "exit":
            print("Exiting calculator...")
            break

        parts = user_input.split()

        if len(parts) != 3:
            print("Invalid input format. Example: add 2 3")
            continue

        operation, a, b = parts

        try:
            result = calc.perform_operation(operation, a, b)
            print("Result:", result)
        except Exception as e:
            print("Error:", e)


if __name__ == "__main__":  # pragma: no cover
    run_repl()