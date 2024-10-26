# Advanced Python Calculator

## Project Overview

This Advanced Python Calculator is a command-line application designed for modularity, extensibility, and professional code standards. It provides basic arithmetic operations with history tracking, menu-driven navigation, and a plugin-based architecture. The project includes automated testing, environment variable management, and comprehensive logging.

## Features

- **Basic Arithmetic Operations**: Addition, subtraction, multiplication, and division with error handling.
- **History Management**: Tracks all calculations in a CSV file.
- **Environment Configuration**: Manages configurations securely with environment variables.
- **Error Handling**: Handles invalid input, division by zero, and unexpected interruptions.
- **Plugin Architecture**: Easily extendable commands through plugins.
- **Automated Testing**: Comprehensive tests covering core functionality and edge cases.

## Project Structure

```plaintext
is601-midterm/
├── calculator/
│   ├── __init__.py           # CalculatorApp main class
│   ├── commands/             # Command handling logic
│   ├── plugins/              # Arithmetic, history, and menu plugins
├── tests/                    # Unit tests for CalculatorApp and plugins
│   ├── test_calculator_app.py
│   ├── test_calculator_config.py
│   ├── test_history_enhanced.py
│   ├── test_calculator_init_additional.py
├── data/
│   ├── config.env            # Environment configuration file
│   ├── history.csv           # Operation history (generated)
├── requirements.txt          # Project dependencies
├── pytest.ini                # Pytest configuration
└── README.md                 # Project documentation
```

## Getting Started

### Prerequisites

- **Python 3.11** or higher
- **pip** for package management

### Installation

1. **Clone the repository**:

   ```bash
   git clone <repository-url>
   cd is601-midterm
   ```

2. **Set up a virtual environment**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # For MacOS/Linux
   venv\Scripts\activate     # For Windows
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Configuration**:
   - Copy `data/config.env.example` to `data/config.env` and modify as needed.

5. **Initialize History File (Optional)**:
   - If `data/history.csv` doesn’t exist, it will be created automatically.

## Usage

Run the calculator application with:

```bash
python main.py
```

The following commands are available:

- **`add`** - Add two numbers.
- **`subtract`** - Subtract two numbers.
- **`multiply`** - Multiply two numbers.
- **`divide`** - Divide two numbers (handles division by zero).
- **`menu`** - Display available commands.
- **`showhistory`** - Show calculation history.
- **`clearhistory`** - Clear the calculation history.

**Example**:

```plaintext
Choose 'exit' to exit or 'menu' for options: add
Enter the first number: 10
Enter the second number: 5
Result: 15
```

## Design Patterns

This project uses design patterns to organize code efficiently:

- **Command Pattern**: Each operation (e.g., add, subtract) is implemented as a command that can be easily extended.
  - **[Link to Command Pattern Implementation](calculator/commands/__init__.py)**.
- **Singleton Pattern**: Singleton-like management of command and history instances within the app.
  - **[Link to Singleton Implementation](calculator/__init__.py)**.

## Environment Variables

Environment variables are used to control configurations, promoting flexibility and security.

- **Configuration Loading**: The `CalculatorApp` loads environment variables using the `load_environment_variables` function.
- **.env Example**: Below is a sample `.env` file configuration for this application:

  ```plaintext
  ENVIRONMENT=production
  ```

- **[Link to Environment Variable Implementation](calculator/__init__.py)**

## Logging

Logging is configured to track application usage, errors, and overall performance.

- **Logging Setup**: Logging is configured within `configure_logging()` in `CalculatorApp`. It defaults to basic logging if no configuration file is available.
- **Log Levels**: The application logs information (`INFO`) and errors (`ERROR`) to provide detailed insights.
- **[Link to Logging Implementation](calculator/__init__.py)**

## Exception Handling

This project uses two primary exception-handling philosophies:

1. **Look Before You Leap (LBYL)**:
   - Example: Checking if `logging.conf` exists before attempting to configure logging from the file.
   - **[Link to LBYL Implementation](calculator/__init__.py#L35)**

2. **Easier to Ask for Forgiveness than Permission (EAFP)**:
   - Example: In the `start()` method, `try-except` blocks handle potential errors during runtime, including `ValueError` for invalid inputs and `ZeroDivisionError` for division operations.
   - **[Link to EAFP Implementation](calculator/__init__.py#L78)**

## Testing

Automated tests cover core functionalities, error handling, and edge cases.

Run all tests with:

```bash
pytest --pylint --cov
```

### Key Test Files

- **`test_calculator_config.py`**: Tests for environment variable loading and logging configuration.
- **`test_history_enhanced.py`**: Tests initialization, saving, and loading of history records.
- **`test_calculator_init_additional.py`**: Covers scenarios like division by zero and invalid commands.

## Video Demonstration

A video demonstration of the calculator application, showing its key features and functionalities, is available here:

- **[Video Demonstration Link](https://youtu.be/_SgwREqofa8)**

## Contributing

Contributions are welcome! Follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Make changes and commit (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Create a pull request.

## License

This project is licensed under the MIT License.
