"""
Unit tests for the CalculatorApp functionality in the calculator application.

This module tests core features of CalculatorApp, including starting the app
and loading environment variables.
"""


from calculator import CalculatorApp

def test_calculator_start(monkeypatch):
    """Test that CalculatorApp starts correctly without user input."""
    monkeypatch.setattr('builtins.input', lambda _: "exit")  # Mock input to exit immediately
    app = CalculatorApp()
    assert app.start() is None  # Assuming start() runs the app without return


def test_environment_variable_loading():
    """Test that CalculatorApp loads environment variables correctly."""
    app = CalculatorApp()
    assert app.load_environment_variables() is not None
