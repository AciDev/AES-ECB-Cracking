def getBlockLength(AES_Encrypt, block_size):
    letter = "A"
    for i in range(block_size):
        string = letter * i
        if len(AES_Encrypt(string)) != block_size:
            break

    return i-1
