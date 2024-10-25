import os
import pandas as pd
import logging
from calculator.commands import Command

class HistoryManager:
    """
    This class handles saving, loading, and clearing the calculation history.
    """
    def __init__(self):
        self.history_file = 'data/history.csv'  # Path to the CSV file for history

        # If the file doesn't exist, create an empty CSV with the appropriate columns
        if not os.path.exists(self.history_file):
            self.initialize_history_file()

    def initialize_history_file(self):
        """
        Initialize the CSV file if it doesn't exist.
        """
        df = pd.DataFrame(columns=['Operation', 'Operand1', 'Operand2', 'Result'])
        df.to_csv(self.history_file, index=False)
        logging.info("History file initialized.")

    def save_to_history(self, operation, operand1, operand2, result):
        """
        Save a new calculation to the history file.
        """
        new_entry = pd.DataFrame({
            'Operation': [operation],
            'Operand1': [operand1],
            'Operand2': [operand2],
            'Result': [result]
        })
        new_entry.to_csv(self.history_file, mode='a', header=False, index=False)
        logging.info(f"Saved to history: {operation}({operand1}, {operand2}) = {result}")

    def load_history(self):
        """
        Load and return the history as a Pandas DataFrame.
        """
        if os.path.exists(self.history_file):
            return pd.read_csv(self.history_file)
        else:
            logging.warning("History file not found.")
            return pd.DataFrame(columns=['Operation', 'Operand1', 'Operand2', 'Result'])

    def clear_history(self):
        """
        Clear the history by reinitializing the history file.
        """
        self.initialize_history_file()
        logging.info("History cleared.")


# Command to display history
class ShowHistoryCommand(Command):
    def __init__(self):
        self.history_manager = HistoryManager()  # Initialize HistoryManager here

    def execute(self, *args):
        history = self.history_manager.load_history()
        if history.empty:
            print("No history available.")
        else:
            print("Calculation History:")
            print(history)


# Command to clear history
class ClearHistoryCommand(Command):
    def __init__(self):
        self.history_manager = HistoryManager()  # Initialize HistoryManager here

    def execute(self, *args):
        self.history_manager.clear_history()
        print("History has been cleared.")
