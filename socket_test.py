# -*- coding: UTF-8 -*-

import socket

host = ''
port = 2000

s = socket.socket()
s.bind((host, port))

while True:
    s.listen(5)

    acc_socket, address = s.accept()
    request = acc_socket.recv(1024)

    print('request == {} ip == {}'.format(request.decode('utf-8'), address))
    acc_socket.sendall(b'<p>Python Socket</p>')
    acc_socket.close()
