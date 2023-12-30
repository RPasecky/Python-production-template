import os
import subprocess
import re
import sys
from cookiecutter.main import cookiecutter



MODULE_REGEX = r'^[_a-zA-Z][_a-zA-Z0-9]+$'

def find_conda_base_path():
    try:
        # Use 'where' on Windows, 'which' on Unix-like systems
        command = 'which' 
        result = subprocess.check_output([command, 'conda']).decode().strip()
        print(result)
        # Split the output and get the first result
        conda_path = result.splitlines()[0]
        print(conda_path)
        # Extract the base path (two levels up from the actual 'conda' executable)
        base_path = os.path.dirname(os.path.dirname(conda_path))

        print(f"Conda base path value: {base_path}")
        return base_path
    except subprocess.CalledProcessError:
        print("Conda is not installed or not in the PATH.")
        sys.exit(1)

conda_base_dir = find_conda_base_path()
cookiecutter(
    'cookiecutter-pypackage',
    extra_context={'conda_base_dir': conda_base_dir}
)

# Get the current directory
current_directory = os.getcwd()
print(f"Current directory value: {current_directory}")

module_name = '{{ cookiecutter.pkg_name}}'

if not re.match(MODULE_REGEX, module_name):
    print('ERROR: The pkg name (%s) is not a valid Python module name. Please do not use a - and use _ instead' % module_name)

    #Exit to cancel project
    sys.exit(1)
