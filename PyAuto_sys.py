import time
import subprocess
import glob
import os
import pyzipper
import sys

#Variables
flag = sys.argv[1]
print(flag)
program_path = "C:/Users/User/Documents/Malware Samples/Samples"
compressed_pattern = "*.zip"
file_patterns = ["*.exe", "*.bat", "*.ps1", "*.xlsx", "*.xls", "*.csv", "*.pptx", "*.ppt"]
full_path = ""
####

#Needed here for bulding path to file
folder = f"/Malware Sample {flag}"
full_path = program_path + folder
os.makedirs(full_path, exist_ok=True)

def run_exe_as_admin(executable_path):
        try:
                subprocess.run([
                        'powershell',
                        '-Command',
                        f'Start-Process "{executable_path}" -Verb RunAs'
                ], check = True)
        except subprocess.CalledProcessError as e:
                print(f"Execution failed with error: {e}")

def run_command(command):
        cmd_command = f"cmd.exe /c {command}"
        try:
                result = subprocess.run(cmd_command)
                if result.returncode == 0 or 1:
                        print("\nCommand executed successfully.")
                else:
                        print(f"Command failed with return code {result.returncode}.")
                        print("Error:")
                        print(result.stderr)
        except:
                print("Catching non-zero return for subprocess.")

def execute_ps1(file_path):
        try:
                subprocess.run([
                'powershell.exe',
                '-ExecutionPolicy', 'Bypass',  # Optional: Allow script execution
                '-File', file_path
                ], check=True)
        except subprocess.CalledProcessError as e:
                print(f"Execution failed with error: {e}")

def open_file(file_path):
         os.startfile(file_path)

def unzip_file():
        zip_files = glob.glob(os.path.join(full_path, compressed_pattern))

        if not zip_files:
                print("No ZIP files found in the directory.")
        else:
                for zip_file_path in zip_files:
                        print(f"Found ZIP file: {zip_file_path}")
                        try:
                                with pyzipper.AESZipFile(zip_file_path, 'r') as zip_ref:
                                        zip_ref.pwd = b'infected'
                                        zip_ref.extractall(full_path)
                                        print(f"\nSuccessfully extracted contents of {zip_file_path} \nto {full_path}")
                        except Exception as e:
                                print(f"\nAn unecpected error occured while extracting {zip_file_path}: {e}")

def execute_file():
        try:
                for pattern in file_patterns:
                        file_to_execute = glob.glob(os.path.join(full_path, pattern))
                        if file_to_execute:
                                print(f"\nFound {len(file_to_execute)} file(s) matching pattern '{pattern}':\n")
                                for file_path in file_to_execute:
                                        print(f"File: {file_path}")
                                        # Get file extension
                                        file_ext = os.path.splitext(file_path)[1].lower()

                                        if file_ext in ('.ps1'):
                                                # Execute as admin if it's a PowerShell script
                                                execute_ps1(file_path)
                                        elif file_ext in('.exe', '.bat'):
                                                # Execute as admin if it's an executable, or batch
                                                run_exe_as_admin(file_path)
                                        elif file_ext in ('.xlsx', '.xls', '.csv', '.pptx', '.ppt'):
                                                # Open the file with the default application if it's an Excel or PowerPoint file
                                                open_file(file_path)
                                        else:
                                                print(f"\nUnsupported file extension for execution: {file_ext}\n")
        except Exception as e:
                print(f"\nError occured while trying to execute or open file: {e}")


unzip_file()

execute_file()

time.sleep(15)

print("\n")
command = f"cd {full_path} && C:/Users/User/Downloads/winpmem_mini_x64_rc2.exe physmem.raw"

run_command(command)

command = f"cd {full_path} && scp physmem.raw remnux@10.0.0.130:/home/remnux/Documents/test"

run_command(command)

print("\nScript is finished.")
