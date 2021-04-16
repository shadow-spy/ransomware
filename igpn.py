#!/usr/bin/python
#coding:utf-8
from cryptography.fernet import Fernet
import os, ctypes, sys

# GET THE ENVIRONMENT VARIABLES
letter_drive = os.environ["SystemDrive"]
current_user = os.environ["USERNAME"]

# fonction arret du chiffrement
def kill_init():
    try:
        cmd = "taskkill /IM crypt_init.exe /f"
        os.system(cmd)
    except:
        pass
kill_init()

# definir le chemin a localiser et definir la clef
path = "{}\\Users\\{}\\AppData\\Roaming\\DriversManager\\convert.key".format(letter_drive, current_user)
file = open(path,"rb")
key = file.read()
file.close()

# definir les chemins a décrypté
def filelist():
    mylist_src = []
    source_dir = ["\\Users\\"]
    for element in source_dir:
        for root, dirs, files in os.walk(element):
            for file in files:
                if file.endswith(".police"):
                    mylist_src.append(os.path.join(root, file))
        return mylist_src

# Fonction déchiffrer les dossiers
def file_decrypt(key, files):
    for name in files:
        with open(name, 'rb') as f:
            data = f.read()

        fernet = Fernet(key)
        decrypted = fernet.decrypt(data)
        decrypted_file = name.replace('.police', '')
        try:
            with open(decrypted_file, 'wb') as f:
                f.write(decrypted)
                os.remove(name)
        except:
            continue

# code principal
file_decrypt(key, filelist())
