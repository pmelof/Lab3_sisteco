import hashlib
import os
from Crypto.Cipher import AES
from cryptography.fernet import Fernet

####AES#####

IV_SIZE = 16    # 128 bit, fixed for the AES algorithm
KEY_SIZE = 32   # 256 bit meaning AES-256, can also be 128 or 192 bits
SALT_SIZE = 16  # This size is arbitrary

cleartext = "Hola mundo"
password = b'highly secure encryption password'
salt = os.urandom(SALT_SIZE)
derived = hashlib.pbkdf2_hmac('sha256', password, salt, 100000, dklen=IV_SIZE + KEY_SIZE)
iv = derived[0:IV_SIZE]
key = derived[IV_SIZE:]

encrypted = salt + AES.new(key, AES.MODE_CFB, iv).encrypt(cleartext.encode('utf-8'))
print(encrypted)

cleartext = AES.new(key, AES.MODE_CFB, iv).decrypt(encrypted[SALT_SIZE:])
print(cleartext.decode())


###FERNET####

texto = "Hola mundo"
key = Fernet.generate_key()  # Keep this secret!
#print(type(key))  # bytes
print("LLave:")
print(key)  # base64 encoded 32 bytes}
print("")
my_fernet = Fernet(key)
encrypted_bytes = my_fernet.encrypt(texto.encode())
print("Encriptado:")
print(encrypted_bytes)
print("")

# Decrypt
clear_text = my_fernet.decrypt(encrypted_bytes)
print("Desencriptado:")
print(clear_text.decode())
print("")