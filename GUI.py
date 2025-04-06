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

# Configure the layout
GlavniProzor.grid_rowconfigure(0, weight=1)
GlavniProzor.grid_columnconfigure(0, weight=1)  # Sidebar (left)
GlavniProzor.grid_columnconfigure(1, weight=9)  # Main area (right)

screen_width = GlavniProzor.winfo_screenwidth()
screen_height = GlavniProzor.winfo_screenheight()

# Sidebar frame (left)
LeviOkvir = Frame(GlavniProzor, bg='#061938')
LeviOkvir.grid(row=0, column=0, sticky="nsew")

# Main content frame (right)
DesniOkvir = Frame(GlavniProzor, bg='#03132b')
DesniOkvir.grid(row=0, column=1, sticky="nsew")

# Prevent resizing based on content
LeviOkvir.pack_propagate(False)
DesniOkvir.pack_propagate(False)

# Sidebar buttons
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

# Main frame buttons (example)
main_buttons = ["Encrypt", "Decrypt", "Browse"]
for i, name in enumerate(main_buttons):
	btn = tkinter.Button(
		DesniOkvir,
		text=name,
		bg='#03132b',
		fg='#ffffff',
		padx=20,
		pady=10,
		borderwidth=0,
	)
	btn.grid(row=i, column=0, pady=10, padx=20, sticky="w")

GlavniProzor.mainloop()