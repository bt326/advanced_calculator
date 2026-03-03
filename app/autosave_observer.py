import os
import pandas as pd
from app.observer import Observer


class AutoSaveObserver(Observer):
    """
    Automatically saves full calculation history to CSV.
    """

    def __init__(self, calculator, history_file=None):
        self.calculator = calculator
        self.config = calculator.config  

        if history_file:
            self.history_file = history_file
        else:
            history_dir = "history"
            os.makedirs(history_dir, exist_ok=True)
            self.history_file = os.path.join(
                history_dir,
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

        directory = os.path.dirname(self.history_file)
        if directory:
            os.makedirs(directory, exist_ok=True)

        df.to_csv(
            self.history_file,
            index=False,
            encoding=self.config.default_encoding
        )