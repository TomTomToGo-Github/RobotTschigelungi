# See https://pyshine.com/Socket-Programming-send-receive-live-audio/
# Make sure to also pip install python_dotenv, keras, opencv-python, numpy,
# matplotlib, sounddevice, soundfile, tensorflow
#  
# Usage: run "python .\audio_socket_server.py" and then from another terminal
# "python .\audio_socket_client.py"
import socket
import pickle
import struct
import pyshine as ps

mode = 'get'
name = 'CLIENT RECEIVING AUDIO'
audio, context = ps.audioCapture(mode=mode)
ps.showPlot(context, name)

# create socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host_ip = '192.168.1.101'  # run ipconfig -> check wlan IP4v4 Address
port = 4982

socket_address = (host_ip, port)
client_socket.connect(socket_address)
print("CLIENT CONNECTED TO", socket_address)
data = b""
payload_size = struct.calcsize("Q")
while True:
    while len(data) < payload_size:
        packet = client_socket.recv(4 * 1024)  # 4K
        if not packet:
            break
        data += packet
    packed_msg_size = data[:payload_size]
    data = data[payload_size:]
    msg_size = struct.unpack("Q", packed_msg_size)[0]

    while len(data) < msg_size:
        data += client_socket.recv(4 * 1024)
    frame_data = data[:msg_size]
    data = data[msg_size:]
    frame = pickle.loads(frame_data)
    audio.put(frame)

client_socket.close()
