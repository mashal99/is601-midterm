"""
Unit test for the MenuCommand in the calculator application.

This module tests the MenuCommand functionality, ensuring that it displays
the available commands correctly.
"""

import pytest
from calculator.plugins.menu import MenuCommand
from calculator.commands import CommandHandler

@pytest.fixture
def command_handler():
    """Fixture to initialize CommandHandler if needed."""
    return CommandHandler()  # Or mock as needed

def test_menu_command(command_handler, capfd):
    """Test execution of the MenuCommand and output format."""
    command = MenuCommand(command_handler)
    command.execute()

    # Capture printed output
    captured = capfd.readouterr()
    assert "Available Commands:" in captured.out  # Adjust as needed to match expected output
