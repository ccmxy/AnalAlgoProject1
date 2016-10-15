import random

def generateArrays(numbersPerArray, numberOfArrays, min, max):
    for i in range(0, numberOfArrays):
        print("["),
        for j in range(0, numbersPerArray):
            print(random.randrange(min, max)),
        print("]")

generateArrays(100, 10, -100, 100)
