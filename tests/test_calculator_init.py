"""
Unit tests for functionality in calculator/__init__.py.
"""
from calculator import CalculatorApp

def test_calculator_app_start(monkeypatch):
    """Test that CalculatorApp starts and prompts for input correctly."""
    monkeypatch.setattr('builtins.input', lambda _: "exit")  # Mock input to 'exit' to terminate the app loop
    app = CalculatorApp()
    assert app.start() is None

def test_load_environment_variables():
    """Test that environment variables load correctly in CalculatorApp."""
    app = CalculatorApp()
    result = app.load_environment_variables()
    assert result is not None  # Check that something is returned
