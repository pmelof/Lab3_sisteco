import hashlib
import os
from Crypto.Cipher import AES
from cryptography.fernet import Fernet

####AES#####

IV_SIZE = 16    # 128 bit, fixed for the AES algorithm
KEY_SIZE = 32   # 256 bit meaning AES-256, can also be 128 or 192 bits
SALT_SIZE = 16  # This size is arbitrary

cleartext = "Hola mundo"
text2="Holamundo"
password = b'clave super mega dificil pasaremos sisteco'
salt = os.urandom(SALT_SIZE)
derived = hashlib.pbkdf2_hmac('sha256', password, salt, 100000, dklen=IV_SIZE + KEY_SIZE)
iv = derived[0:IV_SIZE]
key = derived[IV_SIZE:]

encrypted = salt + AES.new(key, AES.MODE_CFB, iv).encrypt(cleartext.encode('utf-8'))
print(encrypted)
encriptado2 = salt+AES.new(key, AES.MODE_CFB, iv).encrypt(text2.encode('utf-8'))
print(encriptado2)

cleartext = AES.new(key, AES.MODE_CFB, iv).decrypt(encrypted[SALT_SIZE:])
print(cleartext.decode())


