from Crypto.Cipher import AES
from Crypto.Util.Padding import pad


def encryptString(text):
    key = b'Sixteen byte key'
    cipher = AES.new(key, AES.MODE_ECB)
    ciphertext = cipher.encrypt(pad(text, 16))
    return ciphertext
