import PIL
from PIL import Image
import socket
basewidth = 2

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(('0.0.0.0', 8801))
(client_name, client_address) = server.recvfrom(1024)

img = Image.open('d:\image.jpg')
wsize = int(float(img.size[0]) / float(basewidth))
hsize = int(float(img.size[1]) / float(basewidth))
img = img.resize((wsize, hsize), PIL.Image.ANTIALIAS)
img.save('d:\image1.jpg')

f = open(r"d:\image1.jpg", "rb")
a = f.read()
f.close()
server.sendto(a, client_address)
server.close()
