import os
import pkgutil
import importlib
import logging
from calculator.commands import Command

class PluginManager:
    def __init__(self, command_handler):
        self.command_handler = command_handler
        self.plugins_package = 'app.plugins'
        self.plugins_path = self.plugins_package.replace('.', '/')

        # Ensure the plugins path exists
        if not os.path.exists(self.plugins_path):
            logging.warning(f"Plugins directory '{self.plugins_path}' not found.")
        else:
            logging.info(f"Plugins path '{self.plugins_path}' found. Ready to load plugins.")

    def load_plugins(self):
        """
        Dynamically load all available plugins from the app.plugins directory.
        Plugins must be packages (subdirectories) containing a __init__.py file.
        """
        if not os.path.exists(self.plugins_path):
            logging.warning(f"Plugins directory '{self.plugins_path}' not found.")
            return

        logging.info(f"Loading plugins from '{self.plugins_path}'...")
        
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
        :param plugin_module: The imported module representing the plugin.
        :param plugin_name: The name of the plugin package.
        """
        for item_name in dir(plugin_module):
            item = getattr(plugin_module, item_name)
            if isinstance(item, type) and issubclass(item, Command) and item is not Command:
                # Register the command with the command name being the plugin folder name
                self.command_handler.register_command(plugin_name, item())
                logging.info(f"Command '{plugin_name}' from plugin '{plugin_name}' registered.")
