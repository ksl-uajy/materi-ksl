#!/usr/bin/python3

#Contoh penggunaan block cipher sederhana menggunakan python

#Ditulis oleh Natan

#Pastikan sudah install library blowfish
import blowfish

#Fungsi ini untuk mengecek nilai string dalam bytes
def checkBytes(text):
    return len(text.encode('utf-8')) 

#Fungsi ini untuk membuat key
def makeKey(key):
    return blowfish.Cipher(str.encode(key))

#Fungsi untuk mengenkripsi/dekripsi teks
def encrypt(string, key, kondisi):
    key2=makeKey(key)

    if kondisi==1:
        return key2.encrypt_block(str.encode(string))
    elif kondisi==2:
        return key2.decrypt_block(string)
    else:
        return null

text=""

while True:
    text=input("Masukan teks (8 bytes): ")
    if checkBytes(text) == 8:
        break

key = ""

while True:
    key=input("Masukan Key (4-56 bytes): ")
    if checkBytes(key) >=4 or checkBytes(key)<=56:
        break

print("Teks yang dimasukan: " + text)
print("Key yang digunakan: " + key)
enkrip = encrypt(text, key, 1)
print("Setelah dienkripsi: ")
print(enkrip)
print("Setelah didekripsi: ")
print(encrypt(enkrip, key, 2))
