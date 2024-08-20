import subprocess
import yaml

RED = '\033[91m'

#Output Banner
def Banner():
    print( RED + "Volatility Automation Script")

#Load yaml file
def yaml_load(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

#Execute Subprocess commands
def execute_command(command):
    subprocess.run(command, shell=True, check=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

#Main functions
def main():
    config_file = yaml_load('commands.yaml')
    commands = config_file.get('commands', [])
    for i in commands:
        execute_command(i)

if __name__ == "__main__":
    Banner()
    main()

