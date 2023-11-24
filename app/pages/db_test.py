import paramiko
import streamlit as st
from utils.app_utils_rec_epic_5 import *

# SSH connection parameters
hostname = st.secrets['SSH_HOST']
port = st.secrets['SSH_PORT']
username = st.secrets['SSH_USERNAME']
private_key_path = st.secrets['SSH_PRIVATE_KEY']

# Create an SSH client
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    private_key = paramiko.Ed25519Key(filename=private_key_path)
    ssh.connect(hostname, port, username, pkey=private_key)

    # Set up port forwarding
    local_port = st.secrets['LOCAL_PORT']
    remote_host = st.secrets['REMOTE_HOST']
    remote_port = st.secrets['REMOTE_PORT']
    transport = ssh.get_transport()
    transport.request_port_forward(('', local_port), (remote_host, remote_port))

    # Your code that uses the forwarded port goes here
    try:
        conn = connect_db(local=False)
        st.write("Connection successful!")
    except Exception as e:
        st.write(e)

    # Close the SSH connection
    ssh.close()

except Exception as e:
    print(e)
    ssh.close()
