from src.encrypt import encryptString
from src.getBlocks import getBlocks
from src.getBlockLength import getBlockLength
from string import printable


def main():
    block_size = 32
    minimum_length = 15
    secret = list()
    for _ in range(16):
        starting_string = "A" * \
            (minimum_length - len(secret)) + ''.join(secret)
        print(starting_string)
        print(secret)
        print(minimum_length - len(secret))
        first_blocks = getBlocks(encryptString(starting_string), block_size)
        for i in printable:
            #print("trying chracter", i)
            new_string = starting_string + i
            new_blocks = getBlocks(encryptString(new_string), block_size)
            # print("\n".join(new_blocks))
            if first_blocks[0] == new_blocks[0]:
                print("We got a match")
                secret.append(i)
                break


if __name__ == "__main__":
    main()
