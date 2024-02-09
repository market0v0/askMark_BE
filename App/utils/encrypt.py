from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from base64 import b64encode, b64decode
import os

def encrypt(plaintext):
    key = os.getenv("SECRET_KEY")
    cipher = AES.new(key.encode('utf-8'), AES.MODE_CBC)
    ciphertext = cipher.encrypt(pad(plaintext.encode('utf-8'), AES.block_size))
    iv = b64encode(cipher.iv).decode('utf-8')
    encrypted_text = b64encode(ciphertext).decode('utf-8')
    return iv + encrypted_text

def decrypt(encrypted_text):
    key = os.getenv("SECRET_KEY")
    iv = b64decode(encrypted_text[:24])  # IV is the first 24 characters
    ciphertext = b64decode(encrypted_text[24:])
    cipher = AES.new(key.encode('utf-8'), AES.MODE_CBC, iv)
    decrypted_text = unpad(cipher.decrypt(ciphertext), AES.block_size).decode('utf-8')
    return decrypted_text