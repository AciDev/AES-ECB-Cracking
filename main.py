from src.encrypt import encryptString, decryptString
from src.randomKey import randomKey
from src.getBlocks import getBlocks
from src.getBlockLength import getBlockLength
from string import printable


def main():
    key = randomKey(16)
    secretText = encryptString("This is a very secret message for my dad", key)
    block_size = 32
    minimum_length = 15
    secret = list()
    for _ in range(16):
        starting_string = "A" * (minimum_length - len(secret))
        first_blocks = getBlocks(encryptString(
            starting_string, key), block_size)
        for i in printable:
            new_string = starting_string + ''.join(secret) + i
            new_blocks = getBlocks(encryptString(new_string, key), block_size)
            if first_blocks[0] == new_blocks[0]:
                print("We got a match: {0}".format(i))
                secret.append(i)
                break
        if len(secret) == 16:
            print("We found the key: {0}".format(''.join(secret)))

            original_key = decryptString(secretText, key)
            cracked_key = decryptString(secretText, ''.join(secret))
            if original_key == cracked_key:
                print("Decoded text matches the secret message is: {0}".format(
                    cracked_key.decode().split(':')[0]))


if __name__ == "__main__":
    main()
