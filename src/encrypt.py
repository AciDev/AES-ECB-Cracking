from Crypto.Cipher import AES
from Crypto.Util.Padding import pad


def encryptString(text):
    key = "Sixteenbytekey12".encode()
    cipher = AES.new(key, AES.MODE_ECB)
    ciphertext = cipher.encrypt(pad(text.encode(), 16))
    return ciphertext.hex()
