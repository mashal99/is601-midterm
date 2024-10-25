"""
Unit tests for arithmetic commands in the calculator application.

This module contains pytest unit tests for AddCommand, SubtractCommand, MultiplyCommand,
and DivideCommand, verifying that each command performs the correct operation and raises
appropriate errors for invalid input.
"""

import pytest
from calculator.plugins.arithmetic import AddCommand, SubtractCommand, MultiplyCommand, DivideCommand

def test_add_command():
    """Test addition operation and error handling in AddCommand."""
    command = AddCommand()
    assert command.execute(5, 3) == 8
    assert command.execute(-5, 5) == 0

    with pytest.raises(ValueError):
        command.execute("5", 3)  # Invalid input type

def test_subtract_command():
    """Test subtraction operation and error handling in SubtractCommand."""
    command = SubtractCommand()
    assert command.execute(5, 3) == 2
    assert command.execute(3, 5) == -2

    with pytest.raises(ValueError):
        command.execute(5, "three")  # Invalid input type

def test_multiply_command():
    """Test multiplication operation in MultiplyCommand."""
    command = MultiplyCommand()
    assert command.execute(5, 3) == 15
    assert command.execute(-1, 3) == -3

def test_divide_command():
    """Test division operation and error handling in DivideCommand."""
    command = DivideCommand()
    assert command.execute(9, 3) == 3
    assert command.execute(5, -1) == -5

    with pytest.raises(ZeroDivisionError):
        command.execute(5, 0)  # Division by zero

    with pytest.raises(ValueError):
        command.execute(5, "three")  # Invalid input type
