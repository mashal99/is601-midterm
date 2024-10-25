import os
import pkgutil
import importlib
import logging
import inspect
from calculator.commands import Command

class PluginManager:
    def __init__(self, command_handler):
        self.command_handler = command_handler
        self.plugins_package = 'calculator.plugins'
        self.plugins_path = self.plugins_package.replace('.', '/')

    def load_plugins(self):
        """
        Dynamically load all available plugins from the app.plugins directory.
        Plugins must be packages (subdirectories) containing a __init__.py file.
        """
        if not os.path.exists(self.plugins_path):
            logging.warning(f"Plugins directory '{self.plugins_path}' not found.")
            return

        logging.info(f"Loading plugins from '{self.plugins_path}'...")

        # Iterate over all modules in the plugins path
        for _, plugin_name, is_pkg in pkgutil.iter_modules([self.plugins_path]):
            if is_pkg:
                try:
                    plugin_module = importlib.import_module(f'{self.plugins_package}.{plugin_name}')
                    self.register_plugin_commands(plugin_module, plugin_name)
                except ImportError as e:
                    logging.error(f"Error importing plugin '{plugin_name}': {e}")

    def register_plugin_commands(self, plugin_module, plugin_name):
        """
        Register all command classes in a plugin module with the command handler.
        Each command should be registered under its specific name (e.g., 'add', 'subtract').
        If the command requires a 'command_handler' or other parameters, we pass them.
        """
        for item_name in dir(plugin_module):
            item = getattr(plugin_module, item_name)
            if isinstance(item, type) and issubclass(item, Command) and item is not Command:
                # Use inspect to check the constructor's parameters
                init_signature = inspect.signature(item.__init__)
                
                if 'command_handler' in init_signature.parameters:
                    # Pass 'command_handler' when instantiating the command
                    command_instance = item(self.command_handler)
                else:
                    # Instantiate the command without additional arguments
                    command_instance = item()
                
                # Register the command using the class name (e.g., 'AddCommand' -> 'add')
                command_name = item_name.replace('Command', '').lower()
                self.command_handler.register_command(command_name, command_instance)
                logging.info(f"Command '{command_name}' from plugin '{plugin_name}' registered.")

        logging.info(f"Successfully loaded '{plugin_name}' plugin.")
