"""
This module configures pytest to support dynamic test case generation based on command-line options.
It adds the project root directory to `sys.path` to ensure modules within the project can be imported 
during testing. This setup allows the user to specify test parameters, such as the number of test 
records, directly through command-line arguments.
"""

import sys
from pathlib import Path

# Add the project root directory to sys.path
project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_root))
