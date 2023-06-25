# Pytest

## Pytest v0.1-alpha

Pytest is an easy way to create test cases for all your functions.
Using only a file with all your declared functions, pytest can create a tests
file using the unittest module. pytest can also utilize/ modify an existing
test files to create the outline using existing tests.

### Usage:
> pytest <module_file> <output_file> <existing_tests> <tests_count>

### Quick Setup (Only supported on MacOS/Linux Systems):
> python3 setup.py

### Setup:
#### MacOS / Linux:
Update .zshrc / .bashrc in the root directory with the following line:
> alias "pytest"="python3 \<path to pytest>"'
#### Windows:
Run the command in command prompt (Required to run on every instance)
> doskey "pytest"="python3 \<path to pytest> $*"
