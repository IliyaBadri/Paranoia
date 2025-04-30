from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Util.Padding import pad, unpad
import base64

BLOCK_SIZE = 16

def encrypt(plain_text: str, password: str) -> str: 
    padded_base64_plain_text_bytes = pad(base64.b64encode(plain_text.encode('utf-8')), BLOCK_SIZE)

    salt = get_random_bytes(16)
    key = PBKDF2(password, salt, dkLen=32, count=1000000)
    iv = get_random_bytes(16)
    
    cipher = AES.new(key, AES.MODE_CBC, iv)

    encrypted_bytes = cipher.encrypt(padded_base64_plain_text_bytes)

    return base64.b64encode(salt + iv + encrypted_bytes).decode('utf-8')

def decrypt(encrypted_text: str, password: str) -> str:
    encrypted_data_bytes = base64.b64decode(encrypted_text.encode('utf-8'))

    salt = encrypted_data_bytes[:16]
    iv = encrypted_data_bytes[16:32]
    encrypted_bytes = encrypted_data_bytes[32:]

    key = PBKDF2(password, salt, dkLen=32, count=1000000)

    cipher = AES.new(key, AES.MODE_CBC, iv)

    base64_plain_text_bytes = unpad(cipher.decrypt(encrypted_bytes), BLOCK_SIZE)

    return base64.b64decode(base64_plain_text_bytes).decode('utf-8')
