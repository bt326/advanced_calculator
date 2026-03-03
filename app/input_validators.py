from app.exceptions import ValidationError


def validate_numeric(value):
    """
    Ensures value can be converted to float.
    """
    try:
        return float(value)
    except (TypeError, ValueError):
        raise ValidationError(f"Invalid numeric input: {value}")


def validate_max_value(value: float, max_value: float):
    """
    Ensures value does not exceed maximum allowed limit.
    """
    if abs(value) > max_value:
        raise ValidationError(
            f"Input {value} exceeds maximum allowed value of {max_value}"
        )
    return value