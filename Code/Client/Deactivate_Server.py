import paramiko

#Raspberry Pi Credentials
hostname = "192.168.1.4"
username = "pi"
password = "raspberry"

commands = ["sudo reboot"]

try:
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())


    ssh.connect(hostname, username=username, password=password)
    print(f"Connected to {hostname}")

    for command in commands:
        print(f"Executing: {command}")
        stdin, stdout, stderr = ssh.exec_command(command)

        output = stdout.read().decode()
        errors = stderr.read().decode()

        if output:
            print(f"OUTPUT:\n{output}")
        if errors:
            print(f"ERRORS:\n{errors}")

    
    ssh.close()
    print("Connection Closed.")

except Exception as e:
    print(f"An error occurred: {e}")