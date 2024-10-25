from calculator.commands import Command

class MenuCommand(Command):
    """
    Command to display all available commands dynamically.
    """
    def __init__(self, command_handler):
        self.command_handler = command_handler

    def execute(self, *args):
        print("Available Commands:")
        for command_name in self.command_handler.commands.keys():
            print(f"- {command_name}")
