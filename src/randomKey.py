from string import printable
from random import randint


def randomKey(number):
    numPrintable = len(printable.strip())
    key = ''
    for i in range(number):
        key = key + printable[randint(0, numPrintable)-1]
    return key
