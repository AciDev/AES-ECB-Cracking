from src.encrypt import encryptString


def main():
    testString = bytes("AAAAAAAA".encode())
    print(encryptString(testString))


if __name__ == "__main__":
    main()
