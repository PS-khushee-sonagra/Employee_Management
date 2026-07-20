"""Validation utilities for the Employee Management application."""

import re

def validate_non_empty_string(value: str, field_name: str) -> str:
    """Validate that value is a non-empty, non-whitespace string.
    
    Args:
        value: The string to validate.
        field_name: The name of the field for error reporting.
        
    Returns:
        The stripped, validated string.
        
    Raises:
        TypeError: If value is not a string.
        ValueError: If value is empty or only contains whitespace.
    """
    if not isinstance(value, str):
        raise TypeError(f"{field_name} must be a string.")
    
    stripped_value = value.strip()
    if not stripped_value:
        raise ValueError(f"{field_name} cannot be empty.")
    
    return stripped_value


def validate_positive_number(value: float, field_name: str) -> float:
    """Validate that value is a float or int greater than zero.
    
    Args:
        value: The number to validate.
        field_name: The name of the field for error reporting.
        
    Returns:
        The validated float/int.
        
    Raises:
        TypeError: If value is not a number.
        ValueError: If value is less than or equal to zero.
    """
    if not isinstance(value, (int, float)) or isinstance(value, bool):
        raise TypeError(f"{field_name} must be a number.")
    
    if value <= 0:
        raise ValueError(f"{field_name} must be greater than zero.")
    
    return value


def validate_positive_integer(value: int, field_name: str) -> int:
    """Validate that value is an integer greater than zero.
    
    Args:
        value: The integer to validate.
        field_name: The name of the field for error reporting.
        
    Returns:
        The validated integer.
        
    Raises:
        TypeError: If value is not an integer.
        ValueError: If value is less than or equal to zero.
    """
    if not isinstance(value, int) or isinstance(value, bool):
        raise TypeError(f"{field_name} must be an integer.")
    
    if value <= 0:
        raise ValueError(f"{field_name} must be greater than zero.")
    
    return value


def validate_email(value: str, field_name: str = "Email") -> str:
    """Validate that value is a valid email format.
    
    Args:
        value: The email string to validate.
        field_name: The name of the field for error reporting.
        
    Returns:
        The validated and stripped email string.
        
    Raises:
        TypeError: If value is not a string.
        ValueError: If value does not match valid email pattern.
    """
    email_str = validate_non_empty_string(value, field_name)
    
    # Simple regex pattern for email validation
    email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    if not re.match(email_regex, email_str):
        raise ValueError(f"Invalid {field_name} format: '{email_str}'")
        
    return email_str
