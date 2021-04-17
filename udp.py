
# Text: udp_lives_matters
# RST{d79e58503580cbb6c0764c3d1175b866c70efece1c255db43519c60c3120262b}

import socket

UDP_IP = "0.0.0.0"
UDP_PORT = 9999

sock = socket.socket(socket.AF_INET,    # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    if data:
        sent = sock.sendto("RST{d79e58503580cbb6c0764c3d1175b866c70efece1c255db43519c60c3120262b}", addr)
