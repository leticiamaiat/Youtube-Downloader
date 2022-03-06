from pytube import YouTube
from tkinter import *

window = Tk()

window.title("Youtube Video Downloader")

window.geometry('400x200')

lbl = Label(window, text="Introduce youtube URL")

lbl.grid(column=1, row=1)

txt = Entry(window,width=40)

txt.grid(column=1, row=2)

def clicked():
    VIDEO_URL = txt.get()

    yt = YouTube(VIDEO_URL)

    for stream in yt.streams:   
        video = yt.streams.get_highest_resolution()
        video.download()
    res = "Sucessfully Downloaded: " + yt.title

    lbl.configure(text= res)

btn = Button(window, text="OK", command=clicked)

btn.grid(column=1, row=3)

window.mainloop()



#print(yt.title,"salvo com sucesso")