import socket
from PIL import Image
from PIL import ImageGrab
basewidth = 2

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(('0.0.0.0', 3670))

(client_name, client_address) = server.recvfrom(1024)

while True:
    im = ImageGrab.grab()
    wsize = int(float(im.size[0]) / float(basewidth))
    hsize = int(float(im.size[1]) / float(basewidth))
    im = im.resize((wsize, hsize), Image.ANTIALIAS)
    
    im.save(r'd:\screen.jpg')
    f = open(r"d:\screen.jpg", "rb")
    a = f.read()
    f.close()
    try:
        server.sendto(a, client_address)
        print 'hi'
    except:
        print 'here'
        pass
