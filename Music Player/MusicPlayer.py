# creator: @Mechatronix
# date: 20.03.2021
# lisencs: MIT
# contact: mechatronix@mail.de

from tkinter import Tk, Label, Button, filedialog

from pygame import mixer

vol = 0.5

def play_song():

    filename = filedialog.askopenfilename(title = "Select a Song")

    current_song = filename

    song_title = filename.split("/")

    song_title = song_title[-1]

    try:

        mixer.init()

        mixer.music.load(current_song)

        mixer.music.set_volume(vol)

        mixer.music.play()

        lab4.config(fg = "green", text = "Now playing: " + str(song_title))

        lab6.config(text = "Volume: " + str(vol))

    except Exception as e:

        print(e)
        lab4.config(fg = "red", text = "Error playing track")

def reduce_volume():
    try:
        global vol

        if vol <= 0:

            lab6.config(text="Volume: Muted")

            return

        vol = vol - 0.1

        vol = round(vol, 1)

        mixer.music.set_volume(vol)

        lab6.config(text="Volume: " + str(vol))

        if vol == 0:

            lab6.config(text="Volume: Muted")

    except Exception as e:

        print(e)

        lab4.config(fg="red", text="Track hasn't been selected yet")

def increase_volume():

    try:

        global vol
        if vol >= 1:

            lab6.config(text="Volume: Max")

            return

        vol = vol + 0.1

        vol = round(vol, 1)

        mixer.music.set_volume(vol)

        lab6.config(text="Volume: " + str(vol))

        if vol == 1:

            lab6.config(text="Volume: Max")

    except Exception as e:

        print(e)

        lab4.config(fg="red",text="Track hasn't been selected yet")

def pause():

    try:

        mixer.music.pause()

    except Exception as e:

        print(e)

        lab4.config(fg="red", text="Track hasn't been selected yet")

def resume():

    try:

        mixer.music.unpause()

    except Exception as e:

        print(e)

        lab4.config(fg="red", text="Track hasn't been selected yet")

root = Tk()

root.title("Mechas Music Player")

root.resizable(0, 0)

lab1 = Label(root, text = "Mechas Music Player", font = ("Arial", 20), fg = "red")

lab1.grid(sticky = "N", row = 0, padx = 120, pady = 20)

lab2 = Label(root, text = "Select a Music title to play", font = ("Arial", 12), fg = "blue")

lab2.grid(sticky = "N", row = 1, padx = 120, pady = 5)

lab3 = Label(root, font = ("Arial", 12), fg = "blue")

lab3.grid(sticky = "N", row = 3, padx = 120, pady = 5)

lab4 = Label(root, font = ("Arial", 12), fg = "blue")

lab4.grid(sticky = "N", row = 3, padx = 120, pady = 5)

lab5 = Label(root, text = "Volume", font = ("Arial", 15), fg = "red")

lab5.grid(sticky = "N", row = 4, padx = 120, pady = 2)

lab6 = Label(root, font = ("Arial", 12), fg = "blue")

lab6.grid(sticky = "N", row = 5, padx = 120, pady = 5)

btn1 = Button(root, text = "Select Song", font = ("Arial", 12), fg = "blue", command = play_song)

btn1.grid(sticky = "N", row = 2, padx = 120, pady = 5)

btn2 = Button(root, text = "Pause", font = ("Arial", 12), fg = "blue", command = pause)

btn2.grid(sticky = "E", row = 3, padx = 5, pady = 5)

btn3 = Button(root, text = "Resume", font = ("Arial", 12), fg = "blue", command = resume)

btn3.grid(sticky = "W", row = 3, padx = 5, pady = 5)

btn4 = Button(root, text = "+", font = ("Arial", 12), width = 5, fg = "blue", command = increase_volume)

btn4.grid(sticky = "E", row = 5, padx = 120, pady = 5)

btn5 = Button(root, text = "-", font = ("Arial", 12), width = 5, fg = "blue", command = reduce_volume)

btn5.grid(sticky = "W", row = 5, padx = 120, pady = 5)

root.mainloop()
