import streamlit as st
import pandas as pd
from datetime import date
import paramiko
import subprocess

# Streamlit UI
st.title('Database connection test')

# Replace these with your own values
hostname = st.secrets['HOSTNAME']
port = st.secrets['PORT']
username = st.secrets['USERNAME']
private_key_secret_name = st.secrets['PRIVATE_KEY_SECRET_NAME']

# Retrieve the private key from Streamlit secrets
private_key = st.secrets[private_key_secret_name]

# Create an SSH client
ssh = paramiko.SSHClient()

# Automatically load the system's known host keys
ssh.load_system_host_keys()

# Connect to the remote server using key-based authentication
ssh.connect(hostname, port, username, key_filename=private_key)

# Execute a command on the remote server
stdin, stdout, stderr = ssh.exec_command('ls')

# Print the output of the command
print("Output:")
print(stdout.read().decode())

# Close the SSH connection
ssh.close()




   
