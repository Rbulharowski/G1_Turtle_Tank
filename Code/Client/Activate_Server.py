import paramiko
import time

# Raspberry Pi Credentials
hostname = "192.168.1.4"
username = "pi"
password = "raspberry"

commands = [
    "cd G1_Turtle_Tank-1/Code/Server && ls && sudo python main.py -tn &"  # Add '&' to run in background
]

def run_command(ssh, command):
    try:
        print(f"Executing: {command}")
        stdin, stdout, stderr = ssh.exec_command(command)
        
        # Wait for the command to complete and collect output
        output = stdout.read().decode()
        errors = stderr.read().decode()
        
        # If there are outputs or errors, print them
        if output:
            print(f"OUTPUT:\n{output}")
        if errors:
            print(f"ERRORS:\n{errors}")

        return output, errors
    except Exception as e:
        print(f"Error during command execution: {e}")
        return None, str(e)

try:
    # Set up SSH connection
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    ssh.connect(hostname, username=username, password=password)
    print(f"Connected to {hostname}")

    # Run each command in the list
    for command in commands:
        output, errors = run_command(ssh, command)
        if errors:
            print(f"An error occurred while executing the command: {errors}")
            break  # Stop further commands if there's an error

    print("Finished Commands")
    
    # Ensure to close the connection
    ssh.close()
    print("Connection Closed.")

except Exception as e:
    print(f"An error occurred: {e}")
