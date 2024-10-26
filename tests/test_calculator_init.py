"""
Unit tests for functionality in calculator/__init__.py.
"""
import os
import logging  # Standard library imports
from unittest import mock

import pytest  # Third-party imports

from calculator import CalculatorApp  # Local imports
from calculator.commands import CommandHandler
from calculator.plugins.history import HistoryManager
from calculator.plugins import PluginManager


@pytest.fixture
def app():
    """Fixture to initialize the CalculatorApp for testing."""
    return CalculatorApp()


def test_initialization(app):
    """Test initialization of CalculatorApp and dependencies."""
    assert isinstance(app.command_handler, CommandHandler)
    assert isinstance(app.plugin_manager, PluginManager)
    assert isinstance(app.history_manager, HistoryManager)
    assert app.settings is not None  # Environment settings should be loaded


@mock.patch('calculator.os.path.exists', return_value=True)
@mock.patch('calculator.logging.config.fileConfig')
def test_configure_logging_file(mock_file_config, mock_exists, app):
    """Test logging configuration when logging.conf file exists."""
    app.configure_logging()
    mock_file_config.assert_called_once()


@mock.patch('calculator.os.path.exists', return_value=False)
@mock.patch('calculator.logging.basicConfig')
def test_configure_logging_basic(mock_basic_config, mock_exists, app):
    """Test logging configuration when logging.conf file does not exist."""
    app.configure_logging()
    mock_basic_config.assert_called_once_with(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


@mock.patch.dict(os.environ, {"ENVIRONMENT": "test"})
def test_get_environment_variable(app):
    """Test fetching a specific environment variable."""
    app.load_environment_variables = mock.Mock(return_value={"ENVIRONMENT": "test"})
    app.settings = app.load_environment_variables()  # Update settings with mocked env vars
    assert app.get_environment_variable("ENVIRONMENT") == "test"
    assert app.get_environment_variable("NON_EXISTENT_VAR") is None


@mock.patch('builtins.input', side_effect=['menu', 'exit'])
def test_start_menu_command(mock_input, app, caplog):
    """Test start method with 'menu' and 'exit' commands."""
    with mock.patch.object(CalculatorApp, 'configure_logging', return_value=None), \
         mock.patch.object(CalculatorApp, 'load_environment_variables', return_value={}), \
         mock.patch.object(PluginManager, 'load_plugins', return_value=None):
        with caplog.at_level(logging.INFO):
            app.start()
    assert "Application started." in caplog.text
    assert "Exiting application." in caplog.text


@mock.patch('builtins.input', side_effect=['invalid_command', 'exit'])
@mock.patch.object(CommandHandler, 'execute_command')
def test_unknown_command(mock_execute_command, mock_input, app, caplog):
    """Test unknown command handling."""
    with caplog.at_level(logging.ERROR):
        app.start()
    assert "Unknown command: 'invalid_command'" in caplog.text
    mock_execute_command.assert_not_called()


@mock.patch('builtins.input', side_effect=['add', '5', '10', 'exit'])
@mock.patch.object(CommandHandler, 'execute_command', return_value=15)
@mock.patch.object(HistoryManager, 'save_to_history')
def test_add_command(mock_save_to_history, mock_execute_command, mock_input, app, capsys):
    """Test addition command and history saving."""
    app.start()
    captured = capsys.readouterr()
    assert "Result: 15" in captured.out
    mock_execute_command.assert_called_once_with('add', 5, 10)
    mock_save_to_history.assert_called_once_with('add', 5, 10, 15)


@mock.patch('builtins.input', side_effect=['divide', '5', '0', 'exit'])
@mock.patch.object(CommandHandler, 'execute_command', side_effect=ZeroDivisionError("division by zero"))
def test_divide_by_zero(mock_execute_command, mock_input, app, caplog):
    """Test divide by zero error handling."""
    with caplog.at_level(logging.ERROR):
        app.start()
    assert "Error: division by zero" in caplog.text
    mock_execute_command.assert_called_once_with('divide', 5, 0)


@mock.patch('builtins.input', side_effect=['clearhistory', 'exit'])
@mock.patch.object(CommandHandler, 'execute_command')
def test_clear_history_command(mock_execute_command, mock_input, app):
    """Test clear history command."""
    app.start()
    mock_execute_command.assert_any_call('clearhistory')
