import paramiko

def ssh_connect(hostname, username, password, command):
    # Create an SSH client
    ssh = paramiko.SSHClient()

    try:
        # Automatically add the server's host key
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        
        # Connect to the remote server
        ssh.connect(hostname, username=username, password=password)

        # Execute a command (change as needed)
        stdin, stdout, stderr = ssh.exec_command(command)

        # Print the output of the command
        print("Command Output:")
        print(stdout.read().decode('utf-8'))

    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Close the SSH connection
        ssh.close()

# Replace the following with your own information
hostname = '10.9.34.235'
username = 'root'
password = 'pass'
command = 'df -h'  # Example command, change as needed

ssh_connect(hostname, username, password, command)

