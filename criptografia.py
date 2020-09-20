import Crypto
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

random_generator = Crypto.Random.new().read
private_key = RSA.generate(1024, random_generator)
cipher_rsa = PKCS1_OAEP.new(private_key)

texto = "hola mundo"
enc_data = cipher_rsa.encrypt(texto.encode(encoding='utf-8'))
print("Encriptado:")
print(enc_data)
print("")

dec_data = cipher_rsa.decrypt(enc_data)
print("Desencriptado:")
print(dec_data.decode())
