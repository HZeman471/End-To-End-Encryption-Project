import tkinter
from tkinter import *
import os
def OpenStorage():
	os.startfile(r'C:\Windows')

GlavniProzor = tkinter.Tk()
GlavniProzor.state('zoomed')
GlavniProzor.title("AES Enkripcija")

DesniOkvir = Frame(GlavniProzor, bg='#170121', width=1600, height=1000) # TODO: express width as percentage of the screen width
DesniOkvir.pack(side=RIGHT)

LeviOkvir = Frame(GlavniProzor, bg='#0c0354', width=320, height=1000) # TODO: express width as percentage of the screen width
LeviOkvir.pack(side=LEFT)

LabelTitleRIght = Label(DesniOkvir)
LabelTitleRIght.pack()

menubar = Menu(GlavniProzor)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Open storage directory", command=OpenStorage)
filemenu.add_command(label="Exit", command=GlavniProzor.quit)
menubar.add_cascade(label="File", menu=filemenu)
GlavniProzor.config(menu=menubar)

GlavniProzor.mainloop()