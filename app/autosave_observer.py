import os
import pandas as pd
from app.observer import Observer
from app.calculator_config import CalculatorConfig


class AutoSaveObserver(Observer):
    """
   saves full calculation history to CSV.
    """

    def __init__(self, calculator):
        self.config = CalculatorConfig()
        self.calculator = calculator

        self.history_dir = "history"
        os.makedirs(self.history_dir, exist_ok=True)

        self.history_file = os.path.join(
            self.history_dir,
            "calculator_history.csv"
        )

    def update(self, calculation):
        if not self.config.auto_save:
            return

        history_list = self.calculator.get_history()

        data = [
            {
                "operation": calc.operation,
                "operand1": calc.operand1,
                "operand2": calc.operand2,
                "result": calc.result,
                "timestamp": calc.timestamp.isoformat(),
            }
            for calc in history_list
        ]

        df = pd.DataFrame(data)
        df.to_csv(
            self.history_file,
            index=False,
            encoding=self.config.default_encoding
        )