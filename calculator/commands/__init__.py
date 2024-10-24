from abc import ABC, abstractmethod

class Command(ABC):
    """
    Base class for all commands. This enforces a common interface for all commands,
    ensuring they all implement the `execute` method.
    """

    @abstractmethod
    def execute(self, *args):
        """
        This method must be implemented by each specific command.
        It will take variable arguments based on the needs of the command.
        """
        pass

class CommandHandler:
    """
    A command handler class to manage and execute commands dynamically.
    """

    def __init__(self):
        self.commands = {}

    def register_command(self, name, command):
        """
        Register a new command by its name.
        :param name: Command name (string) that can be called by the REPL or other components.
        :param command: An instance of a class inheriting from Command.
        """
        self.commands[name] = command

    def execute_command(self, name, *args):
        """
        Execute a command by its name with the provided arguments.
        :param name: Command name (string)
        :param args: Arguments to pass to the command's execute method
        :return: Result of the command execution
        """
        if name not in self.commands:
            raise KeyError(f"Command '{name}' not found.")
        
        command = self.commands[name]
        return command.execute(*args)
