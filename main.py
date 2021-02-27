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

from inspect import getmembers, isfunction
from importlib import import_module
import sys
import os


def get_args()->tuple:
    """
    Parse the user given arguments
    """
    if len(sys.argv) == 1 or len(sys.argv) == 2 and sys.argv[2] == 'help':
        usage = "<module_file> <output_file> <existing_tests> <tests_count>"
        print(f"Usage: pytest {usage}")
    module_file = sys.argv[1]
    output_file = 'tests.py'
    test_file = None
    test_count = 5
    if len(sys.argv) > 2:
        output_file = sys.argv[2]
    if len(sys.argv) > 3:
        test_file = sys.argv[3] if len(sys.argv[3].strip()) > 0 else None
    if len(sys.argv) > 4:
        test_count = int(sys.argv[4])
    return (module_file, output_file, test_count, test_file)


def create_test_lines(module_name: str, test_count: int, existing_tests: dict)\
        ->list:
    """
    Creating the contents of the test file
    """
    module = import_module(module_name)
    output_lines = existing_tests.get("__headers", [])
    output_lines.extend(existing_tests.get("__imports",
        ["import unittest", "import {}".format(module_name)]) + [""])
    for func_name, _ in getmembers(module, isfunction):
        output_lines.append("\nclass Test{}(unittest.TestCase):\n".format(
            "".join(part.capitalize() for part in func_name.split("_"))))
        for i in range(1, test_count + 1):
            func_line = f"    def test_{func_name}_{i}(self):"
            func_body = []
            output_lines.append(func_line)
            if func_line not in existing_tests.keys():
                func_line = f"    def test_{func_name}_1(self):"
                func_body.append('        #INCOMPLETE')
            func_body.extend(existing_tests.get(func_line, ['        pass']))
            output_lines.append("\n".join(func_body+[""]))
    output_lines.append("\nif __name__ == \"__main__\":")
    output_lines.append("    unittest.main()")
    return output_lines


def get_existing_tests(test_file: str)->dict:
    """
    Parse an existing tests file for available tests
    """
    if test_file is None or not os.path.exists(test_file):
        return {}
    existing_tests = {
        "__headers": [],
        "__imports": []
    }
    headers_complete = False
    with open(test_file) as file:
        file_lines = file.readlines()
        test_case = None
        for line in file_lines:
            if line[:4] == "from":
                headers_complete = True
                existing_tests["__imports"].append(line.rstrip())
            if len(line.strip()) == 0:
                test_case = None
            if test_case is not None:
                existing_tests[test_case].append(line.rstrip())
            if line[:7] == "    def":
                headers_complete = True
                test_case = line.rstrip()
                existing_tests[test_case] = []
            if not headers_complete:
                existing_tests["__headers"].append(line)
    return existing_tests


def main()->None:
    """
    Run the pytest tool
    """
    sys.path.insert(0, os.getcwd())
    module_file, output_file, test_count, test_file = get_args()
    module_name = module_file.split(".")[0]
    existing_tests = get_existing_tests(test_file)
    output_lines = create_test_lines(module_name, test_count, existing_tests)
    with open(output_file, 'w') as file:
        file.write("\n".join(output_lines))


if __name__ == '__main__':
    main()
