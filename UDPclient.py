import socket

my = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
my.sendto('portnoy and hadad', ('10.38.18.99', 8801))
(data, source) = my.recvfrom(100000)
dublin = open("d:\image.jpg", "wb")
dublin.write(data)
dublin.close()
my.close()
