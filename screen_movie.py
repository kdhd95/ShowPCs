#------replace images------------
from Tkinter import Label, Tk
import ImageTk
import Image
import threading
from PIL import ImageGrab


im = ImageGrab.grab()  # shot the screen
im.save(r'd:\screen.png')  # save the shot screen
path = 'd:\screen.png'
root = Tk()  # get GUI
img = ImageTk.PhotoImage(Image.open(path))  # create img from shot screen
panel = Label(root, image=img)
panel.pack()  # display image


def screenshot():
        im1 = ImageGrab.grab()
        im1.save(r'd:\screen.png')
        img1 = ImageTk.PhotoImage(Image.open('d:\screen.png'))
        panel.configure(image=img1)  # critical code --> update the configure new img
        panel.image = img1  # update the img
        root.after(40, screenshot)  # recursive function delay 40ms

root.after(500, screenshot)  # call function after 500ms
root.mainloop()  # play GUI
