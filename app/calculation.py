from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Calculation:
    operation: str
    operand1: float
    operand2: float
    result: float
    timestamp: datetime = field(default_factory=datetime.now)

    def __str__(self):
        return (
            f"{self.operation.upper()} | "
            f"{self.operand1} , {self.operand2} = {self.result} "
            f"({self.timestamp.strftime('%Y-%m-%d %H:%M:%S')})"
        )

    def to_dict(self):
        return {
            "operation": self.operation,
            "operand1": self.operand1,
            "operand2": self.operand2,
            "result": self.result,
            "timestamp": self.timestamp.isoformat(),
        }