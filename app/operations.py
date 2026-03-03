from abc import ABC, abstractmethod


class Operation(ABC):
    @abstractmethod
    def execute(self, a: float, b: float) -> float:
        pass


class AddOperation(Operation):
    def execute(self, a: float, b: float) -> float:
        return a + b


class SubtractOperation(Operation):
    def execute(self, a: float, b: float) -> float:
        return a - b


class MultiplyOperation(Operation):
    def execute(self, a: float, b: float) -> float:
        return a * b


class DivideOperation(Operation):
    def execute(self, a: float, b: float) -> float:
        if b == 0:
            raise ValueError("Division by zero is not allowed.")
        return a / b


class OperationFactory:
    operations = {
        "add": AddOperation,
        "subtract": SubtractOperation,
        "multiply": MultiplyOperation,
        "divide": DivideOperation,
    }

    @classmethod
    def create_operation(cls, operation_name: str):
        operation = cls.operations.get(operation_name)
        if not operation:
            raise ValueError("Invalid operation")
        return operation()