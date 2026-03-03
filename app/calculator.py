from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Calculation:
    """
    Represents a single calculator operation.
    Stores operation details and timestamp.
    """

    operation: str
    operand1: float
    operand2: float
    result: float
    timestamp: datetime = field(default_factory=datetime.now)

    def to_dict(self) -> dict:
        """
        Convert Calculation object to dictionary format
        for CSV serialization.
        """
        return {
            "operation": self.operation,
            "operand1": self.operand1,
            "operand2": self.operand2,
            "result": self.result,
            "timestamp": self.timestamp.isoformat(),
        }