import socket
import Tkinter as Tk
import ImageTk
from PIL import Image

basewidth = 2
my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
my_socket.sendto('hp', ('10.38.18.99', 3670))

root = Tk.Tk()  # get GUI
img = ImageTk.PhotoImage(Image.open("d:\welcome.jpg"))  # create img from shot screen
panel = Tk.Label(root, image=img)
panel.pack()  # display image


def screenshot():
    (a, source) = my_socket.recvfrom(1000000)
    dublin = open("d:\screen1.jpg", "wb")
    dublin.write(a)
    dublin.close()
    image = Image.open('d:\screen1.jpg')
    wsize = int(float(image.size[0]) * float(basewidth))
    hsize = int(float(image.size[1]) * float(basewidth))
    image = image.resize((wsize, hsize), Image.ANTIALIAS)
    image.save('d:\screen2.jpg')

    try:
        image = ImageTk.PhotoImage(Image.open('d:\screen2.jpg'))
        panel.configure(image=image)  # critical code --> update the configure new img
        panel.image = image  # update the img
        print 'hi'
    except:
        print 'here'
        pass

    root.after(100, screenshot)


root.after(500, screenshot)
root.mainloop()  # play GUI
