from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2
import base64

def pad(text):
    while len(text) % 16 != 0:
        text += ' '
    return text

def encrypt(plain_text, password):
    salt = get_random_bytes(16)
    key = PBKDF2(password, salt, dkLen=32, count=1000000)
    iv = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    encrypted_bytes = cipher.encrypt(pad(plain_text).encode('utf-8'))
    return base64.b64encode(salt + iv + encrypted_bytes).decode('utf-8')

def decrypt(encrypted_text, password):
    encrypted_data = base64.b64decode(encrypted_text)
    salt = encrypted_data[:16]
    iv = encrypted_data[16:32]
    encrypted_bytes = encrypted_data[32:]
    key = PBKDF2(password, salt, dkLen=32, count=1000000)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_bytes = cipher.decrypt(encrypted_bytes)
    return decrypted_bytes.decode('utf-8').rstrip()
