from app.observer import Observer
from app.operations import OperationFactory
from app.input_validators import validate_numeric, validate_max_value
from app.calculation import Calculation
from app.history import History
from app.calculator_config import CalculatorConfig


class Calculator:
    """
    Main calculator controller.
    Integrates operations, validation, config, and history.
    """

    def __init__(self):
        self.config = CalculatorConfig()
        self.history = History(self.config.max_history_size)
        self._observers = []

    def perform_operation(self, operation_name, a, b):
        # Validate numeric
        a = validate_numeric(a)
        b = validate_numeric(b)

        # Validate max input value
        a = validate_max_value(a, self.config.max_input_value)
        b = validate_max_value(b, self.config.max_input_value)

        # Create operation using factory
        operation = OperationFactory.create_operation(operation_name)

        # Execute operation
        result = operation.execute(a, b)

        # Apply precision from config
        result = round(result, self.config.precision)

        # Store calculation
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