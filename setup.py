"""
Pytest v0.1-alpha

Pytest is an easy way to create test cases for all your functions.
Using only a file with all your declared functions, pytest can create a tests
file using the unittest module. pytest can also utilize/ modify an existing
test files to create the outline using existing tests.

Usage:
    pytest <module_file> <output_file> <existing_tests> <tests_count>

Quick Setup (Only supported on MacOS/Linux Systems):
    MacOS / Linux:
        python3 setup.py

Setup:
    MacOS / Linux:
        update .zshrc / .bashrc in the root directory with the following line:
        echo 'alias "pytest"="python3 <path to pytest>"' >> ~.zshrc
    Windows:
        Run the command in command prompt (Required to run on every instance)
        doskey "pytest"="python3 <path to pytest> $*"
"""

import platform
import os


def main()->None:
    """
    Run the automatic setup for pytest
    """
    pytest_file = os.path.join(os.getcwd(), "main.py")
    cur_platform = platform.system()
    if cur_platform == 'Linux':
        cmd = "echo 'alias \"pytest\"=\"python3 {}\"' >> ~/.bashrc"
        os.system(cmd.format(pytest_file))
        print("Pytest setup complete! Restart terminal to use pytest.")
    elif cur_platform == 'Darwin':
        cmd = "echo 'alias \"pytest\"=\"python3 {}\"' >> ~/.zshrc"
        os.system(cmd.format(pytest_file))
        print("Pytest setup complete! Restart terminal to use pytest.")
    else:
        print(f"Platform {cur_platform} not supported for quick setup")


if __name__ == '__main__':
    main()
