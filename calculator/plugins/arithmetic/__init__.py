class AddCommand:
    def execute(self, a, b):
        try:
            return a + b
        except TypeError:
            raise ValueError("Invalid input: both values must be numbers.")

class SubtractCommand:
    def execute(self, a, b):
        try:
            return a - b
        except TypeError:
            raise ValueError("Invalid input: both values must be numbers.")

class MultiplyCommand:
    def execute(self, a, b):
        try:
            return a * b
        except TypeError:
            raise ValueError("Invalid input: both values must be numbers.")

class DivideCommand:
    def execute(self, a, b):
        try:
            if b == 0:
                raise ZeroDivisionError("Cannot divide by zero.")
            return a / b
        except TypeError:
            raise ValueError("Invalid input: both values must be numbers.")

# A function to load the available commands
def get_arithmetic_commands():
    return {
        'add': AddCommand(),
        'subtract': SubtractCommand(),
        'multiply': MultiplyCommand(),
        'divide': DivideCommand(),
    }
