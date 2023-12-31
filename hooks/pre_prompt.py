import json
import sys
import os
import subprocess

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

with open('cookiecutter.json') as f:
    cookiecutter_json = json.load(f)
    cookiecutter_json['conda_base_dir'] = find_conda_base_path()
    cookiecutter_json['current_directory'] = os.getcwd()
    
    json.dumps(cookiecutter_json, indent=2)