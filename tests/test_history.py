"""
Unit tests for history management commands in the calculator application.

This module tests the functionality of the HistoryManager class, including initializing
the history file, saving entries, loading history, and clearing entries.
"""
import os
import pytest
import pandas as pd
from calculator.plugins.history import HistoryManager

@pytest.fixture
def history_manager(tmp_path):
    """Fixture for HistoryManager, using a temporary directory for testing."""
    # Override the default file location to a temporary path
    temp_history_file = tmp_path / "history.csv"
    manager = HistoryManager()
    manager.history_file = str(temp_history_file)
    manager.initialize_history_file()  # Ensure the temp file is created
    return manager

def test_initialize_history_file(history_manager):
    """Test initialization of the history file."""
    # Check if the file was created and has the correct structure
    assert os.path.exists(history_manager.history_file)
    df = pd.read_csv(history_manager.history_file)
    assert list(df.columns) == ['Operation', 'Operand1', 'Operand2', 'Result']

def test_save_to_history(history_manager):
    """Test saving an entry to history and verifying its presence."""
    # Save a new history entry and verify it in the CSV file
    history_manager.save_to_history("add", 5, 3, 8)
    history = history_manager.load_history()
    assert not history.empty
    assert len(history) == 1
    assert history.iloc[0].to_dict() == {
        'Operation': 'add',
        'Operand1': 5,
        'Operand2': 3,
        'Result': 8
    }

def test_clear_history(history_manager):
    """Test clearing all entries from the history."""
    # Add an entry, clear history, and check if the CSV is empty
    history_manager.save_to_history("add", 5, 3, 8)
    history_manager.clear_history()
    history = history_manager.load_history()
    assert history.empty

def test_load_history_with_no_data(history_manager):
    """Test loading history when the history file is empty."""
    history_manager.clear_history()  # Ensure history is empty
    history = history_manager.load_history()
    assert history.empty  # Should be an empty DataFrame

def test_save_to_history_multiple_entries(history_manager):
    """Test saving multiple entries to history and loading them."""
    history_manager.save_to_history("add", 1, 2, 3)
    history_manager.save_to_history("subtract", 5, 3, 2)
    history = history_manager.load_history()
    assert len(history) == 2
    assert history.iloc[0].to_dict() == {
        'Operation': 'add',
        'Operand1': 1,
        'Operand2': 2,
        'Result': 3
    }
    assert history.iloc[1].to_dict() == {
        'Operation': 'subtract',
        'Operand1': 5,
        'Operand2': 3,
        'Result': 2
    }
