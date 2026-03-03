class CalculatorError(Exception):
    """Base exception for calculator application."""
    pass


class OperationError(CalculatorError):
    """Raised when an invalid mathematical operation occurs."""
    pass


class ValidationError(CalculatorError):
    """Raised when input validation fails."""
    pass


class HistoryError(CalculatorError):
    """Raised for undo/redo related issues."""
    pass


class ConfigurationError(CalculatorError):
    """Raised when configuration loading fails."""
    pass