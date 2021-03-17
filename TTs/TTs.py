from gtts import gTTS
from playsound import playsound
from tkinter import *
import random
import os

name = None

text = ""

language = "de"

def play():

	text = e.get()

	tts = gTTS(text = text, lang = language, slow = False)

	name = random.randint(100000000, 999999999)

	tts.save(str(name) + ".mp3")

	playsound(str(name) + ".mp3")

	os.remove(str(name) + ".mp3")

	name = None

def save_play():

	text = e.get()

	tts = gTTS(text = text, lang = language, slow = False)

	name = random.randint(100000000, 999999999)

	tts.save(str(name) + ".mp3")

	playsound(str(name) + ".mp3")

	name = None

root = Tk()

root.title("Text to Speech")

lab = Label(root, text="Text to Speech Text: ")

lab.grid(row = 0)

e = Entry(root)

e.grid(row=0, column=1)

btn1 = Button(root, text = "Play", command = play)

btn1.grid(row = 2, column = 0, sticky = W, pady = 4)

btn2 = Button(root, text = "Save & Play", command = save_play)

btn2.grid(row = 2, column = 1, sticky = W, pady = 4)

root.mainloop()
