import os
import sys
import logging
import logging.config
from dotenv import load_dotenv
from calculator.commands import CommandHandler
from calculator.plugins import PluginManager

class CalculatorApp:
    def __init__(self):
        os.makedirs('logs', exist_ok=True)
        self.configure_logging()

        # Load environment variables
        load_dotenv()
        self.settings = self.load_environment_variables()

        # Initialize the command handler and plugin manager
        self.command_handler = CommandHandler()
        self.plugin_manager = PluginManager(self.command_handler)

    def configure_logging(self):
        """
        Configure logging based on the logging.conf file. If the file is missing, configure basic logging.
        """
        logging_conf_path = 'logging.conf'
        if os.path.exists(logging_conf_path):
            logging.config.fileConfig(logging_conf_path, disable_existing_loggers=False)
        else:
            logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
        logging.info("Logging configured.")

    def load_environment_variables(self):
        """
        Load all environment variables into a dictionary.
        """
        settings = {key: value for key, value in os.environ.items()}
        logging.info("Environment variables loaded.")
        return settings

    def get_environment_variable(self, env_var: str = 'ENVIRONMENT'):
        """
        Retrieve a specific environment variable.
        :param env_var: The name of the environment variable to retrieve.
        :return: The value of the environment variable or None if not found.
        """
        return self.settings.get(env_var, None)

    def start(self):
        """
        Load plugins and start the REPL for command input.
        """

        self.plugin_manager.load_plugins()

        logging.info("Application started. Type 'exit' to exit or 'menu' to display available commands.")
        
        try:
            while True:
                # Step 1: Choose an operation
                command_name = input("Choose a command or 'menu' to see available commands (or 'exit' to quit): ").strip().lower()

                if command_name == 'exit':
                    logging.info("Exiting application.")
                    break

                if command_name not in self.command_handler.commands:
                    logging.error(f"Unknown command: '{command_name}'")
                    continue

                if command_name == 'menu':
                    # Execute the menu command to display available commands
                    self.command_handler.execute_command('menu')
                    continue

                try:
                    # Step 2: Enter the first number
                    first_number = float(input("Enter the first number: ").strip())
                    
                    # Step 3: Enter the second number
                    second_number = float(input("Enter the second number: ").strip())
                    
                    # Step 4: Execute the command
                    result = self.command_handler.execute_command(command_name, first_number, second_number)
                    print(f"Result: {result}")
                    
                except ValueError:
                    logging.error("Invalid input. Please enter valid numbers.")
                except ZeroDivisionError as e:
                    logging.error(f"Error: {e}")
                except KeyError:
                    logging.error(f"Unknown command: '{command_name}'")
        
        except KeyboardInterrupt:
            logging.info("Application interrupted by user. Exiting...")
        
        finally:
            logging.info("Application shutdown.")