from app.exceptions import OperationError
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
            raise OperationError("Division by zero is not allowed.")
        return a / b

class PowerOperation(Operation):
    def execute(self, a: float, b: float) -> float:
        return a ** b

class RootOperation(Operation):
    def execute(self, a: float, b: float) -> float:
        if b == 0:
            raise OperationError("Root degree cannot be zero.")

        # Even root of negative number not allowed
        if a < 0 and b % 2 == 0:
            raise OperationError("Even root of negative number is not allowed.")

        return a ** (1 / b)

class ModulusOperation(Operation):
    def execute(self, a: float, b: float) -> float:
        if b == 0:
            raise OperationError("Modulus by zero is not allowed.")
        return a % b


class IntegerDivideOperation(Operation):
    def execute(self, a: float, b: float) -> float:
        if b == 0:
            raise OperationError("Integer division by zero is not allowed.")
        return a // b


class PercentOperation(Operation):
    def execute(self, a: float, b: float) -> float:
        if b == 0:
            raise OperationError("Cannot calculate percentage with zero.")
        return (a / b) * 100


class AbsoluteDifferenceOperation(Operation):
    def execute(self, a: float, b: float) -> float:
        return abs(a - b)

class OperationFactory:
    operations = {
        "add": AddOperation,
        "subtract": SubtractOperation,
        "multiply": MultiplyOperation,
        "divide": DivideOperation,
        "power": PowerOperation,
        "root": RootOperation,
        "modulus": ModulusOperation,
        "int_divide": IntegerDivideOperation,
        "percent": PercentOperation,
        "abs_diff": AbsoluteDifferenceOperation,
    }

    @classmethod
    def create_operation(cls, operation_name: str):
        operation = cls.operations.get(operation_name)
        if not operation:
            raise OperationError("Invalid operation")
        return operation()

