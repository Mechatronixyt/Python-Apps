import pyqrcode
from tkinter import *
import random

name = None

def erzeugen():

	data = e.get()

	name = random.randint(100000000, 999999999)

	name = str(name) + ".png"

	url = pyqrcode.create(data, error = 'H')

	print(url.png(name, module_color = (0, 0, 0, 255), background = (0, 0, 0, 0), scale = 5))

	name = None 

root = Tk()

root.title("QR Code Maker")

lab = Label(root, text="QR Code Massege: ")

lab.grid(row = 0)

e = Entry(root)

e.grid(row=0, column=1)

btn = Button(root, text = "Erzeugen", command = erzeugen)

btn.grid(row = 2, column = 0, sticky = W, pady = 4)

root.mainloop()