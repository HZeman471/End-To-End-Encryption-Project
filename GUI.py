import tkinter
from tkinter import *
import os
def OpenStorage():
	os.startfile(r'C:\Windows')

GlavniProzor = tkinter.Tk()
GlavniProzor.state('zoomed')
GlavniProzor.title("AES Enkripcija")

screen_width = GlavniProzor.winfo_screenwidth()
screen_height = GlavniProzor.winfo_screenheight()

DesniOkvir = Frame(GlavniProzor, bg='#170121', width=screen_width * 0.7, height=screen_height) # TODO: express width as percentage of the screen width
DesniOkvir.pack(side=RIGHT)

LeviOkvir = Frame(GlavniProzor, bg='#0c0354', width=screen_width * 0.3, height=screen_height) # TODO: express width as percentage of the screen width
LeviOkvir.pack(side=LEFT)

menubar = Menu(GlavniProzor)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Open storage directory", command=OpenStorage)
filemenu.add_command(label="Exit", command=GlavniProzor.quit)
menubar.add_cascade(label="File", menu=filemenu)
GlavniProzor.config(menu=menubar)

GlavniProzor.mainloop()