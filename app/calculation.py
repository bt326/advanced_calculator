from dataclasses import dataclass
from datetime import datetime


@dataclass
class Calculation:
    operation: str
    operand1: float
    operand2: float
    result: float
    timestamp: datetime = datetime.now()

    def __str__(self):
        return (
            f"{self.operation.upper()} | "
            f"{self.operand1} , {self.operand2} = {self.result} "
            f"({self.timestamp.strftime('%Y-%m-%d %H:%M:%S')})"
        )