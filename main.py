"""
Module: main

This script initializes and runs the main application by creating an instance of the `App` class 
and invoking its `start` method. 
The `Calculator` class is responsible for loading plugins, handling commands, 
and managing the application's core logic.
"""
from calculator import CalculatorApp

if __name__ == "__main__":
    CalculatorApp().start()  # Run the app without assigning the return since it's not needed.
