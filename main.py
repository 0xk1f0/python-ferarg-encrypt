import base64
import argon2
from cryptography.fernet import Fernet

def get_hash(password):
    hash = argon2.hash_password(password.encode(), salt="saltysaltysalty".encode())
    encoded_hash = base64.urlsafe_b64encode(hash.decode("utf-8").split("$")[-1][:32].encode())
    return encoded_hash

def data_encrypt(data):
    encryptor = Fernet(get_hash(input("Enter encryption password: ")))
    return encryptor.encrypt(data.encode())

def data_decrypt(cipher):
    try:
        encryptor = Fernet(get_hash(input("Enter encryption password: ")))
        return encryptor.decrypt(cipher).decode("utf-8")
    except:
        print("Error: Wrong Password!")
        return False

ciphertext = data_encrypt("Hello World")
print(ciphertext)
result = data_decrypt(ciphertext)
print(result)
