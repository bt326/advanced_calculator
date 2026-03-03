import os
from dotenv import load_dotenv
from app.exceptions import ConfigurationError


load_dotenv()


class CalculatorConfig:
    """
    Loads and validates environment configuration.
    """

    def __init__(self):
        try:
            self.max_history_size = int(
                os.getenv("CALCULATOR_MAX_HISTORY_SIZE", 100)
            )
            self.auto_save = os.getenv("CALCULATOR_AUTO_SAVE", "true").lower() == "true"
            self.precision = int(os.getenv("CALCULATOR_PRECISION", 5))
            self.max_input_value = float(
                os.getenv("CALCULATOR_MAX_INPUT_VALUE", 1_000_000)
            )
            self.default_encoding = os.getenv(
                "CALCULATOR_DEFAULT_ENCODING", "utf-8"
            )

        except ValueError as e:
            raise ConfigurationError("Invalid configuration value") from e