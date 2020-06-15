from Crypto.Cipher import AES
from Crypto.Util.Padding import pad


def encryptString(text, key):
    cipher = AES.new(key.encode(), AES.MODE_ECB)
    ciphertext = cipher.encrypt(pad((text + key).encode(), 16))
    return ciphertext.hex()


def decryptString(ciphertext, key):
    ciphertext = bytes.fromhex(ciphertext)
    cipher = AES.new(key.encode(), AES.MODE_ECB)
    plaintext = cipher.decrypt(ciphertext)
    return plaintext
