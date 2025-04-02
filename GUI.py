import tkinter
from tkinter import *
from PomocneFunkcije import *
import os
import threading
def OpenStorage():
	os.startfile(r'C:\Windows')
	
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

screen_width = GlavniProzor.winfo_screenwidth()
screen_height = GlavniProzor.winfo_screenheight()

DesniOkvir = Frame(GlavniProzor, bg='#170121', width=screen_width * 0.7, height=screen_height)

LeviOkvir = Frame(GlavniProzor, bg='#0c0354', width=screen_width * 0.3, height=screen_height)

DesniOkvir.pack(side=RIGHT)
LeviOkvir.pack(side=LEFT)

menubar = Menu(GlavniProzor)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Odpri shranilni direktorij", command=OpenStorage)
filemenu.add_command(label="Dodaj novo datoteko", command=AddFile)
filemenu.add_command(label="Exit", command=GlavniProzor.quit)
menubar.add_cascade(label="File", menu=filemenu)
GlavniProzor.config(menu=menubar)

GlavniProzor.mainloop()