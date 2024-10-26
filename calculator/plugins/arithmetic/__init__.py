from calculator.commands import Command

class AddCommand(Command):
    def execute(self, a, b):
        try:
            return a + b
        except TypeError as e:
            print(f"Error: {e}")
            raise ValueError("Invalid input: both values must be numbers.")

class SubtractCommand(Command):
    def execute(self, a, b):
        try:
            return a - b
        except TypeError as e:
            print(f"Error: {e}")
            raise ValueError("Invalid input: both values must be numbers.")

class MultiplyCommand(Command):
    def execute(self, a, b):
        try:
            return a * b
        except TypeError as e:
            print(f"Error: {e}")
            raise ValueError("Invalid input: both values must be numbers.")

class DivideCommand(Command):
    def execute(self, a, b):
        try:
            if b == 0:
                error_message = "Cannot divide by zero."
                print(f"Error: {error_message}")
                raise ZeroDivisionError(error_message)
            return a / b
        except TypeError as e:
            print(f"Error: {e}")
            raise ValueError("Invalid input: both values must be numbers.")
