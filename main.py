from src.encrypt import encryptString
from src.getBlocks import getBlocks
from src.getBlockLength import getBlockLength
from string import printable


def main():
    block_size = 32
    minimum_length = 15
    starting_string = "A" * minimum_length
    first_blocks = getBlocks(encryptString(starting_string), block_size)
    print("\n".join(first_blocks))
    for i in printable:
        #print("trying chracter", i)
        new_string = "A" * minimum_length + i
        new_blocks = getBlocks(encryptString(new_string), block_size)
        # print("\n".join(new_blocks))
        if first_blocks[0] == new_blocks[1]:
            print("We got a match")
            break


if __name__ == "__main__":
    main()
