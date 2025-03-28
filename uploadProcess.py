import requests
import os
import keyring
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
import tkinter as tk
from tkinter import filedialog
import secrets
SERVICE_NAME = "Encryptav0.1Service"
USERNAME = "Encryptav0.1User"

def get_or_create_key():
    key = keyring.get_password(SERVICE_NAME, USERNAME)
    if key is None:
        key = os.urandom(32)  # AES-256 key
        keyring.set_password(SERVICE_NAME, USERNAME, key.hex())
    else:
        key = bytes.fromhex(key)
    return key

def GetEncryptedFilePath(PotDoDatoteke):
    key = get_or_create_key()
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    
    with open(PotDoDatoteke, "rb") as f:
        data = f.read()
    
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(data) + padder.finalize()
    encrypted_data = encryptor.update(padded_data) + encryptor.finalize()
    
    with open(PotDoDatoteke + ".enc", "wb") as f:
        f.write(iv + encrypted_data)
    
    return PotDoDatoteke + ".enc"

target_url = "https://locust-notable-terrier.ngrok-free.app/upload"


def ConvertToRandomName(Filename: str):
    random_filename = secrets.token_hex(5)  # Generate cryptographically secure filename, create (random name, actual name) pairs for storage of actual names
    KeyNamePairs = open("Pairs.txt", 'a')
    StringZaZapisatio = "(%s, %s) \n" % (random_filename, Filename)
    KeyNamePairs.write(StringZaZapisatio)
    KeyNamePairs.close()
    return random_filename

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()
target_file = GetEncryptedFilePath(file_path)
file_name = ConvertToRandomName(os.path.basename(target_file))

with open(target_file, "rb") as target_file_encrypted:
    files = {"file": (file_name, target_file_encrypted, "application/octet-stream")}
    
    # Send the request
    response = requests.post(target_url, files=files)

# check the result
if response.ok:
    print(response.text)
else:
    print("Something went wrong")
