from app.observer import Observer
from app.logger import get_logger


class LoggingObserver(Observer):
    """
    Logs each calculation to file.
    """

    def __init__(self):
        self.logger = get_logger()

    def update(self, calculation):
        message = (
            f"Operation: {calculation.operation}, "
            f"Operands: ({calculation.operand1}, {calculation.operand2}), "
            f"Result: {calculation.result}"
        )

        self.logger.info(message)