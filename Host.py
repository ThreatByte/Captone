import subprocess
import os
import sys

def run_vm_command(command):
    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error: {result.stderr}")
    else:
        print(f"\nOutput: {result.stdout}")
    return result

def start_vm(vmrun_path, vm_path):
  command = [vmrun_path, "start", vm_path, "gui"]
  print(f"Starting VM with command: {command}")
  result = run_vm_command(command)
  if result.returncode == 0:
      print("VM started successfully.")
      
def stop_vm(vmrun_path, vm_path, mode):
    try:
        if mode == 'hard':
            command = [vmrun_path, 'stop', vm_path, 'hard']
        else:
            command = [vmrun_path, 'stop', vm_path, 'soft']
            
        print(f"Stopping VM with command: {command}")
        result = run_vm_command(command)
        
        if result.returncode == 0:
            print(f"VM stopped {'forcefully' if mode == 'hard' else 'gracefully'}.")
        else:
            print(f"Failed to stop VM: {result.stderr}")
            
    except Exception as e:
        print(f"Failed to stop VM: {e}")  

def revert_snapshot(vmrun_path, vm_path, snapshot_name):
    command = [vmrun_path, "-T", "ws", "revertToSnapshot", vm_path, snapshot_name]
    try:
        subprocess.check_output(command)
        print("VM reverted to snapshot '{}' successfully.\n".format(snapshot_name))
    except subprocess.CalledProcessError as e:
        print("Error:", e)
      
#Variable Setup
vmrun_path ="C:\\Program Files (x86)\\VMware\\VMware Workstation\\vmrun.exe"
vm_path = "" #Path to .vmx file  
snapshot_name = "PreDetonation" #Pre Detonation

#Check if vmrun_path is correct
if not os.path.isfile(vmrun_path):
    print(f"vmrun executable not found at: {vmrun_path}")
    sys.exit(1)
#Check if vm_path is correct
if not os.path.isfile(vm_path):
    print(f"VMX file not found at: {vm_path}")
    sys.exit(1)

    #Revert to specified snapshot 
revert_snapshot(vmrun_path, vm_path, snapshot_name)

    #Start the VM
start_vm(vmrun_path, vm_path)

user_input = 0

while(user_input != 1):
    user_input = int(input("Enter 1 to stop the VM: "))

    #Stop the VM
stop_vm(vmrun_path, vm_path, "hard")
    