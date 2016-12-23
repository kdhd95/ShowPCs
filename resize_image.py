import PIL
from PIL import Image

basewidth = 2

img = Image.open('d:\screen1.jpg')
wsize = int(float(img.size[0]) * float(basewidth))
hsize = int(float(img.size[1]) * float(basewidth))
img = img.resize((wsize, hsize), PIL.Image.ANTIALIAS)
img.save('d:\screen2.jpg')
