# See https://pyshine.com/Socket-Programming-send-receive-live-audio/
# Make sure to also pip install python_dotenv, keras, opencv-python, numpy,
# matplotlib, sounddevice, soundfile, tensorflow
#  
# Usage: run "python .\audio_socket_strea_local.py"
# # import socket
# # import pickle
# # import struct
# # import pyshine as ps
# # import time

# https://python-sounddevice.readthedocs.io/en/0.3.3/


import sounddevice
sounddevice.query_devices()  # get list of devices
sounddevice.default.device  # get list of ids (int) of devices [microphone_id, 
# speaker_id]


# # # # Use audio stream without sending through socket
# # # audio_send, context_send = ps.audioCapture(mode='send')
# # # # audio_get, context_get = ps.audioCapture(mode='get')

# # # # name = 'ReceivingAudioLocal'
# # # # ps.showPlot(context_get, name)
# # # # payload_size = struct.calcsize("Q")

# # # time_start = time.time_ns()
# # # time_passed = time_start
# # # while (time_passed - time_start) / (10**9) > 10:
# # #     # Audio input stream
# # #     frame = audio_send.get()
# # #     print(frame)
# # #     # Pickle and send data
# # #     # a = pickle.dumps(frame)
# # #     # message = struct.pack("Q", len(a)) + a

# # #     # Receive data
# # #     # while len(data) < payload_size:
# # #     #     packet = client_socket.recv(4 * 1024)  # 4K
# # #     #     if not packet:
# # #     #         break
# # #     #     data += packet
# # #     # packed_msg_size = data[:payload_size]
# # #     # data = data[payload_size:]
# # #     # msg_size = struct.unpack("Q", packed_msg_size)[0]

# # #     # while len(data) < msg_size:
# # #     #     data += client_socket.recv(4 * 1024)
# # #     # frame_data = data[:msg_size]
# # #     # # frame_data = message
# # #     # data = data[msg_size:]
# # #     # frame = pickle.loads(frame_data)


# # #     # audio_get.put(frame)
# # #     time_passed = time.time_ns()
