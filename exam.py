import socket
import base64
import Tkinter as tk
import ImageTk, Image

my_socket=socket.socket()
my_socket.connect(('127.0.0.1',3680))


a= my_socket.recv(10000000)

dublin=open("d:\screen1.jpg","wb")
dublin.write(a.decode("base64"))
dublin.close()

root = tk.Tk() #get GUI
img = ImageTk.PhotoImage(Image.open("d:\screen1.jpg")) #create img from shot screen
panel = tk.Label(root, image = img)
panel.pack() #display image

def screenshot():
    a= my_socket.recv(10000000)

    dublin=open("d:\screen1.jpg","wb")
    dublin.write(a.decode("base64"))
    dublin.close()

    try:
        img = ImageTk.PhotoImage(Image.open('d:\screen1.jpg'))
        panel.configure(image = img) #critical code --> update the configure new img
        panel.image = img #update the img
    except:
        pass
    root.after(500, screenshot)
    
root.after(500, screenshot)
root.mainloop() #play GUI

