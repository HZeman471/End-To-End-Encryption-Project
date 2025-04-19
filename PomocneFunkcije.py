import requests
import os
import keyring
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
from tkinter import filedialog
import secrets

SERVICE_NAME = "Encryptav0.1Service"
USERNAME = "Encryptav0.1User"



def GetEncryptedFilePath(PotDoDatoteke):
	key = keyring.get_password(SERVICE_NAME, USERNAME)
	if key is None:
		key = os.urandom(32)  # AES-256 key
		keyring.set_password(SERVICE_NAME, USERNAME, key.hex())
	else:
		key = bytes.fromhex(key)
	
	iv = os.urandom(16)
	cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
	encryptor = cipher.encryptor()
	
	with open(PotDoDatoteke, "rb") as f:
		data = f.read()
	
	padder = padding.PKCS7(128).padder()
	padded_data = padder.update(data) + padder.finalize()
	encrypted_data = encryptor.update(padded_data) + encryptor.finalize()
	
	with open(PotDoDatoteke, "wb") as f:
		f.write(iv + encrypted_data)
	
	return PotDoDatoteke

target_url = "https://locust-notable-terrier.ngrok-free.app/upload"


def RemoveFileFromSystem(FIlePath):
	# find file alias
    FileListLog = open("Pairs.txt").readlines()
	for i in range(0, len(FileListLog)):
		TrenutnaDatoteka = FileListLog[i].split(", ")[1]
		if TrenutnaDatoteka == os.path.basename(FIlePath):
			os.remove(FIlePath)
		# TODO: Recreate the pairs file, because we can't delete only one row from the file.
	
def ConvertToRandomName(Filename: str):
	random_filename = secrets.token_hex(5)  # Generate cryptographically secure filename, create (random name, actual name) pairs for storage of actual names
	KeyNamePairs = open("Pairs.txt", 'a')
	StringZaZapisati= "(%s, %s)\n" % (random_filename, Filename)
	KeyNamePairs.write(StringZaZapisati)
	KeyNamePairs.close()
	return random_filename

def CheckFileExistence():
	FileListDirectory = os.listdir(r"C:\Users\Hrvoje\OneDrive - Univerza v Mariboru\Namizje\Library of Congress\Moji prispevki\AES Enkripcija\uploads")
	FileListLog = open("Pairs.txt").readlines()
	if len(FileListLog) != len(FileListDirectory):
		return False
	RealFilesName = []
	for i in range(len(FileListLog)):
		RealFilesName.append(FileListLog[i].split(", ")[1])
	
	for i in range(len(RealFilesName)):
		TrenutnaDatotekaDirektorij = FileListDirectory[i]
		if TrenutnaDatotekaDirektorij in RealFilesName:
			pass
		else:
			return False # TODO: add more agressive measures of notification due to file misalignment
		
	
# file_path = filedialog.askopenfilename()
# target_file = GetEncryptedFilePath(file_path)
# file_name = ConvertToRandomName(os.path.basename(target_file))
#
# with open(target_file, "rb") as target_file_encrypted:
#     files = {"file": (file_name, target_file_encrypted, "application/octet-stream")}
#
#     response = requests.post(target_url, files=files)
#
# if response.ok:
#     print(response.text)
# else:
#     print("Something went wrong")
