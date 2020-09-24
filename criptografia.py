import hashlib
import os
from Crypto.Cipher import AES
from time import time

# Definición del tamaño del vector de inicialización, tamaño de la llave y tamaño de la sal

IV_SIZE = 16    # Tamaño IV 128 bits
KEY_SIZE = 32   # Tamaño llave: 256 bits (AES-256), puede ser también de 128 bits o de 192 bits
SALT_SIZE = 16  # Tamaño arbitrario de sal


# Funcion de encriptación
def encryp(password, text):
    start_time = time()

    # Sal para aumentar la complejidad del ataque de diccionario
    salt = os.urandom(SALT_SIZE)

    # Obtención de la llave y vector de inicialización (iv) a partir de la contraseña
    derived = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000, dklen=IV_SIZE + KEY_SIZE)
    iv = derived[0:IV_SIZE]
    key = derived[IV_SIZE:]

    # Encriptación del texto
    encrypted_text = salt + AES.new(key, AES.MODE_CFB, iv).encrypt(text.encode('utf-8'))

    end_time = time() - start_time

    print("Texto encriptado:")
    print(encrypted_text.hex())
    print("\nTiempo: ", end_time)
    print("")

    # Retorno del texto encriptado
    return encrypted_text


def decrypt(password, encrypted_text):
    # Obtención de la sal del texto encriptado
    salt = encrypted_text[0:SALT_SIZE]

    # Obtención de la llave y vector de inicialización (iv) a partir de la contraseña
    derived = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000, dklen=IV_SIZE + KEY_SIZE)
    iv = derived[0:IV_SIZE]
    key = derived[IV_SIZE:]

    # Desencriptación del texto cifrado
    decrypted_text = AES.new(key, AES.MODE_CFB, iv).decrypt(encrypted_text[SALT_SIZE:])
    print("Texto desencriptado:")
    print(decrypted_text.decode())
    print("")


if __name__ == '__main__':
    # Clave para el cifrador simétrico AES
    password = "clave mega supercalifragilisticoespialidosa"

    # Textos para encriptar y probar efecto avalancha
    text_1 = "Hola mundo"
    text_2 = "Holamundo"
    text_3 = "Hola mudo"

    encrypted_text_1 = encryp(password, text_1)
    encrypted_text_2 = encryp(password, text_2)
    encrypted_text_3 = encryp(password, text_3)

    decrypt(password, encrypted_text_1)
    decrypt(password, encrypted_text_2)
    decrypt(password, encrypted_text_3)



