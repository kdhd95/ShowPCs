#------replace images------------
import Tkinter as tk
import ImageTk
import Image
import threading
from PIL import ImageGrab
import socket
import base64
my_socket=socket.socket()
my_socket.connect(('127.0.0.1',3342))


path ='d:\start.jpg'
root = tk.Tk() #get GUI
img = ImageTk.PhotoImage(Image.open(path)) #create img from shot screen
panel = tk.Label(root, image = img)
panel.pack(side = "bottom", fill = "both", expand = "yes") #display image

def call(e):
        my_socket.send("screenshot")
        threading.Thread(target=screenshot).start()
        threading.Thread(target=get_image).start()

def screenshot():
        img = ImageTk.PhotoImage(Image.open('d:\screen.jpg'))
        panel.configure(image = img) #critical code --> update the configure new img
        panel.image = img #update the img
        root.after(40, screenshot) #recursive function delay 40ms

def get_image():
    data= my_socket.recv(10000000)
    dublin=open("d:\screen.jpg","wb")
    dublin.write(data.decode("base64"))
    dublin.close()
    root.after(40, get_image)

        
root.bind("<Return>", call) #call function after 500ms
root.mainloop() #play GUI
