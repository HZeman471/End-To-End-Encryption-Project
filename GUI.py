import tkinter
from tkinter import *
from PomocneFunkcije import *
import os
import threading
def OpenStorage():
	os.startfile(r'C:\Users\Hrvoje\OneDrive - Univerza v Mariboru\Namizje\Library of Congress\Moji prispevki\AES Enkripcija\uploads')
	
def AddFile():
	my_thread = threading.Thread(target=UploadThreadJob)
	my_thread.start()

def UploadThreadJob():
	from tkinter import filedialog
	
	file_path = filedialog.askopenfilename()
	target_file = GetEncryptedFilePath(file_path)
	file_name = ConvertToRandomName(os.path.basename(target_file))
	
	with open(target_file, "rb") as target_file_encrypted:
		files = {"file": (file_name, target_file_encrypted, "application/octet-stream")}
	 
		response = requests.post(target_url, files=files)
	
	if response.ok:
		print(response.text)
	else:
		print("Something went wrong")


UploadThread = threading.Thread(target=UploadThreadJob)

GlavniProzor = tkinter.Tk()
GlavniProzor.state('zoomed')
GlavniProzor.title("AES Enkripcija")

menubar = Menu(GlavniProzor)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Odpri shranilni direktorij", command=OpenStorage)
filemenu.add_command(label="Dodaj novo datoteko", command=AddFile)
filemenu.add_command(label="Exit", command=GlavniProzor.quit)
menubar.add_cascade(label="File", menu=filemenu)
GlavniProzor.config(menu=menubar)

GlavniProzor.grid_rowconfigure(0, weight=1)
GlavniProzor.grid_columnconfigure(0, weight=1)  # Sidebar (left)
GlavniProzor.grid_columnconfigure(1, weight=9)  # Main area (right)

screen_width = GlavniProzor.winfo_screenwidth()
screen_height = GlavniProzor.winfo_screenheight()

LeviOkvir = Frame(GlavniProzor, bg='#061938')
LeviOkvir.grid(row=0, column=0, sticky="nsew")

DesniOkvir = Frame(GlavniProzor, bg='#03132b')
DesniOkvir.grid(row=0, column=1, sticky="nsew")

LeviOkvir.pack_propagate(False)
DesniOkvir.pack_propagate(False)

sidebar_buttons = ["Moje datoteke", "Nastavitve", "Račun"]
for name in sidebar_buttons:
	btn = tkinter.Button(
		LeviOkvir,
		text=name,
		bg='#061938',
		fg='white',
		borderwidth=0,
		pady=10,
		activebackground='#092e69',
		activeforeground='white'
	)
	btn.pack(fill=tkinter.X)

SeznamVrsticParov = open("Pairs.txt").readlines()
for i, name in enumerate(SeznamVrsticParov):
	btn = tkinter.Button(
		DesniOkvir,
		text=name.split(", ")[-1].replace(")", ""),
		bg='#03132b',
		fg='#ffffff',
		padx=5,
		pady=5,
		borderwidth=0,
		activebackground='#092e69',
		activeforeground='white',
		relief = SUNKEN,
		anchor=tkinter.CENTER
	)
	btn.grid(row=i, column=0, pady=5, padx=5, sticky="w")

GlavniProzor.mainloop()