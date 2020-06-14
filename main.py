from src.encrypt import encryptString
from src.randomKey import randomKey
from src.getBlocks import getBlocks
from src.getBlockLength import getBlockLength
from string import printable


def main():
    key = randomKey(16)
    block_size = 32
    minimum_length = 15
    secret = list()
    for _ in range(16):
        starting_string = "A" * (minimum_length - len(secret))
        first_blocks = getBlocks(encryptString(
            starting_string, key), block_size)
        for i in printable:
            print("trying chracter", i)
            new_string = starting_string + ''.join(secret) + i
            new_blocks = getBlocks(encryptString(new_string, key), block_size)
            print("\n".join(new_blocks))
            if first_blocks[0] == new_blocks[0]:
                print("We got a match")
                secret.append(i)
                break
        if len(secret) == 16:
            print("We found the key: {0}".format(''.join(secret)))
            print(key)


if __name__ == "__main__":
    main()
