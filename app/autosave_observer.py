import os
import pandas as pd
from app.observer import Observer
from app.calculator_config import CalculatorConfig


class AutoSaveObserver(Observer):
    """
    Automatically saves calculation history to CSV.
    """

    def __init__(self):
        self.config = CalculatorConfig()
        self.history_file = "calculator_history.csv"

    def update(self, calculation):
        data = {
            "operation": calculation.operation,
            "operand1": calculation.operand1,
            "operand2": calculation.operand2,
            "result": calculation.result,
            "timestamp": calculation.timestamp.isoformat(),
        }

        df = pd.DataFrame([data])

        if os.path.exists(self.history_file):
            df.to_csv(self.history_file, mode="a", header=False, index=False)
        else:
            df.to_csv(self.history_file, index=False)