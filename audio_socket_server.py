# See https://pyshine.com/Socket-Programming-send-receive-live-audio/
# Make sure to also pip install python_dotenv, keras, opencv-python, numpy,
# matplotlib, sounddevice, 
# run "python .\audio_socket_server.py" and then from another terminal
# "python .\audio_socket_client.py"
import socket
import pickle
import struct
import pyshine as ps

mode = 'send'
name = 'SERVER TRANSMITTING AUDIO'
audio, context = ps.audioCapture(mode=mode)
# ps.showPlot(context,name)

# Socket Create
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host_ip = '192.168.1.101'  # run ipconfig -> check wlan IP4v4 Address
port = 4982
backlog = 5
socket_address = (host_ip, port)
print('STARTING SERVER AT', socket_address, '...')
server_socket.bind(socket_address)
server_socket.listen(backlog)

while True:
    client_socket, addr = server_socket.accept()
    print('GOT CONNECTION FROM:', addr)
    if client_socket:

        while (True):
            frame = audio.get()

            a = pickle.dumps(frame)
            message = struct.pack("Q", len(a)) + a
            client_socket.sendall(message)

    else:
        break

client_socket.close()
