import os
import subprocess
import sys
import time

def create_python_template(project_name='project_x'):
    # Create the main project directory
    os.makedirs(project_name, exist_ok=True)

    # Create subdirectories
    os.makedirs(os.path.join(project_name, 'src'), exist_ok=True)
    os.makedirs(os.path.join(project_name, 'tests'), exist_ok=True)

    # Create main files
    with open(os.path.join(project_name, 'requirements.txt'), 'w') as f:
        f.write('''
numpy==2.1.2
pandas==2.2.3
python-dateutil==2.9.0.post0
pytz==2024.2
requests
six==1.16.0
tabulate
termcolor==2.5.0
tzdata==2024.2
''')

    with open(os.path.join(project_name, 'README.md'), 'w') as f:
        f.write(f"# {project_name}\n")  # Create a basic README.md file
        f.write("## Python Version\n")
        f.write("This project requires Python 3.12 or higher.\n")  # Specify Python requirement
        f.write("This project requires Python 3.12 or higher.\n")

    # Create .gitignore file
    with open(os.path.join(project_name, '.gitignore'), 'w') as f:
        f.write(".venv/\n")  # Ignore the virtual environment

    print(f"Project structure for '{project_name}' created successfully.")

def create_virtual_environment(project_name):
    # Create a virtual environment
    virtual_env = os.path.join(project_name, '.venv')
    subprocess.run([sys.executable, '-m', 'venv', virtual_env])
    print(f"Virtual environment created at '{virtual_env}'.")
    time.sleep(1)
    
    # Install requirements using the pip from the virtual environment
    pip_path = os.path.join(virtual_env, 'bin', 'pip')
    subprocess.run([pip_path, 'install', '-r', os.path.join(project_name, 'requirements.txt')])
    print("Requirements installed successfully.")
    time.sleep(1)

def python_template_setup():
    print('\nThis will create a Python project structure in the current directory.')
    while True:
        answer = input('Do you want to continue? (y/n) ').lower()
        if answer == 'y':
            project_name = "project_x"  # Change the name if you wish
            create_python_template(project_name)
            create_virtual_environment(project_name)
            print('''
-----------------------
''')
            break
        elif answer == 'n':
            print('\nOK! Maybe next time...')
            time.sleep(1)
            print('''
-----------------------
''')            
            break
        else:
            print('Invalid answer. Try again...')

if __name__ == "__main__":
    python_template_setup()
