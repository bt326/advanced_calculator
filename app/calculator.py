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
    Integrates operations, validation, config, history, and observers.
    """

    def __init__(self):
        self.config = CalculatorConfig()
        self.history = History(self.config.max_history_size)
        self._observers = []

        # Automatically register observers
        self.register_observer(LoggingObserver())
        self.register_observer(AutoSaveObserver(self))

    def perform_operation(self, operation_name, a, b):
        # Validate numeric
        a = validate_numeric(a)
        b = validate_numeric(b)

        # Validate max input value
        a = validate_max_value(a, self.config.max_input_value)
        b = validate_max_value(b, self.config.max_input_value)

        # Create operation
        operation = OperationFactory.create_operation(operation_name.lower())

        # Execute
        result = operation.execute(a, b)

        # Apply precision
        result = round(result, self.config.precision)

        # Save calculation
        calculation = Calculation(operation_name, a, b, result)
        self.history.add(calculation)

        # Notify observers
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


# REPL

def run_repl():
    calc = Calculator()

    print("Advanced Calculator")
    print("Type 'help' for commands. Type 'exit' to quit.")

    while True:
        user_input = input(">> ").strip()

        if user_input.lower() == "exit":
            print("Exiting calculator...")
            break

        if user_input.lower() == "help":
            print("\nAvailable commands:")
            print("add, subtract, multiply, divide")
            print("power, root, modulus, int_divide, percent, abs_diff")
            print("history, undo, redo, clear, help, exit\n")
            continue

        if user_input.lower() == "history":
            history = calc.get_history()
            if not history:
                print("No history available.")
            else:
                for item in history:
                    print(item)
            continue

        if user_input.lower() == "undo":
            try:
                calc.undo()
                print("Undo successful.")
            except Exception as e:
                print("Error:", e)
            continue

        if user_input.lower() == "redo":
            try:
                calc.redo()
                print("Redo successful.")
            except Exception as e:
                print("Error:", e)
            continue

        if user_input.lower() == "clear":
            calc.clear_history()
            print("History cleared.")
            continue

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


if __name__ == "__main__":
    run_repl()