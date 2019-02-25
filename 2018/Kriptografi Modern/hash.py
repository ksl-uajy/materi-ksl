#! /usr/bin/python3

#Contoh penggunaan hash untuk autentikasi string (bisa digunakan autentikasi password)

import hashlib

def hashing(string):
    return hashlib.md5(string.encode())

text1 = input("Masukan text1: ")
text1Hash = hashing(text1).hexdigest()
print("Nilai hash dari " + text1 + " adalah " + text1Hash)

text2 = input("Masukan text2: ")
text2Hash = hashing(text2).hexdigest()
print("Nilai hash dari " + text2 + " adalah " + text2Hash)

if text1Hash==text2Hash:
    print("Text1 dan Text2 adalah sama")
else:
    print("Text1 dan text2 tidak sama")

