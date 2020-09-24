import hashlib
import os
from Crypto.Cipher import AES

# Definición del tamaño del vector de inicialización, tamaño de la llave y tamaño de la sal
IV_SIZE = 16    # 128 bits
KEY_SIZE = 32   # Tamaño llave: 256 bits (AES-256), puede ser también de 128 bits o de 192 bits
SALT_SIZE = 16  # Tamaño arbitrario de sal

# Textos para encriptar y probar efecto avalancha
text_1 = "Hola mundo"
text_2 = "Holamundo"
text_3 = "Hola mudo"

# Clave para el cifrado simétrico AES
password = "clave mega supercalifragilisticoespialidosa"

# Sal para aumentar la complejidad del ataque de diccionario
salt = os.urandom(SALT_SIZE)
print("Salto:")
print(salt.hex())
print("")

# Obtención de la llave y vector de inicialización (iv)
derived = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000, dklen=IV_SIZE + KEY_SIZE)
iv = derived[0:IV_SIZE]
key = derived[IV_SIZE:]

# Encriptación del texto 1
text_1_encrypted = salt + AES.new(key, AES.MODE_CFB, iv).encrypt(text_1.encode('utf-8'))
print("Texto 1 encriptado:")
print(text_1_encrypted.hex())
print("")

# Encriptación del texto 2
text_2_encrypted = salt + AES.new(key, AES.MODE_CFB, iv).encrypt(text_2.encode('utf-8'))
print("Texto 2 encriptado:")
print(text_2_encrypted.hex())
print("")

# Encriptación del texto 3
text_3_encrypted = salt + AES.new(key, AES.MODE_CFB, iv).encrypt(text_3.encode('utf-8'))
print("Texto 3 encriptado:")
print(text_3_encrypted.hex())
print("")

# Desencriptación del texto 1
text_1_decrypted = AES.new(key, AES.MODE_CFB, iv).decrypt(text_1_encrypted[SALT_SIZE:])
print("Texto 1 desencriptado:")
print(text_1_decrypted.decode())
