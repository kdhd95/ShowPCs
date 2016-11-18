import socket
import base64
from PIL import ImageGrab
import time

server=socket.socket()
server.bind(('0.0.0.0',3680))
server.listen(5)
(client_socket, client_address) = server.accept()

while True:
    im = ImageGrab.grab()
    im.save(r'd:\screen.jpg')
    with open("d:\screen.jpg", "rb") as imageFile:
        a = base64.b64encode(imageFile.read())

    try:
        client_socket.send(a)
    except: 
        pass
    time.sleep(0.5)

