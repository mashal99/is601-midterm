from calculator.commands import Command

class AddCommand(Command):
    def execute(self, a, b):
        try:
            return a + b
        except TypeError:
            raise ValueError("Invalid input: both values must be numbers.")

class SubtractCommand(Command):
    def execute(self, a, b):
        try:
            return a - b
        except TypeError:
            raise ValueError("Invalid input: both values must be numbers.")

class MultiplyCommand(Command):
    def execute(self, a, b):
        try:
            return a * b
        except TypeError:
            raise ValueError("Invalid input: both values must be numbers.")

class DivideCommand(Command):
    def execute(self, a, b):
        try:
            if b == 0:
                raise ZeroDivisionError("Cannot divide by zero.")
            return a / b
        except TypeError:
            raise ValueError("Invalid input: both values must be numbers.")
