"""
Unit tests for Command and CommandHandler classes in calculator/commands.
"""

import pytest
from calculator.commands import Command, CommandHandler

class SampleCommand(Command):
    """A sample command for testing."""
    def execute(self, *args):
        return "sample executed"

def test_command_handler_register_and_execute():
    """Test registering and executing a command using CommandHandler."""
    handler = CommandHandler()
    command = SampleCommand()
    handler.register_command("sample", command)
    result = handler.execute_command("sample")
    assert result == "sample executed"

def test_command_handler_invalid_command():
    """Test that CommandHandler raises an error for an invalid command."""
    handler = CommandHandler()
    with pytest.raises(KeyError):
        handler.execute_command("nonexistent")  # Should raise an error
