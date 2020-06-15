from string import printable
from random import randint


def randomKey(number):
    numPrintable = len(printable.strip())
    key = ':'
    for i in range(number-1):
        key = key + printable[randint(0, numPrintable)-1]
    return key
