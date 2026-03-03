import logging
import os
from app.calculator_config import CalculatorConfig


def get_logger():
    """
    Configure and return application logger.
    """
    config = CalculatorConfig()

    log_dir = "logs"
    os.makedirs(log_dir, exist_ok=True)

    log_file = os.path.join(log_dir, "calculator.log")

    logger = logging.getLogger("calculator_logger")

    if not logger.handlers:
        logger.setLevel(logging.INFO)

        file_handler = logging.FileHandler(
            log_file,
            encoding=config.default_encoding
        )

        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s"
        )

        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger