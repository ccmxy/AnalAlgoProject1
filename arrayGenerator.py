#This generated the file we used for testing
import random

def generateArrays(numbersPerArray, numberOfArrays, min, max):
    for i in range(0, numberOfArrays):
        print("["),
        for j in range(0, numbersPerArray):
            print(random.randrange(min, max)),
        print("]")

generateArrays(1, 10, -200, 200)
generateArrays(10, 10, -200, 200)
generateArrays(20, 10, -200, 200)
generateArrays(50, 10, -200, 200)
generateArrays(100, 10, -200, 200)
generateArrays(200, 10, -200, 200)
generateArrays(300, 10, -200, 200)
generateArrays(400, 10, -200, 200)
generateArrays(500, 10, -200, 200)
generateArrays(600, 10, -200, 200)
generateArrays(700, 10, -200, 200)
generateArrays(800, 10, -200, 200)
generateArrays(900, 10, -200, 200)
generateArrays(1000, 10, -200, 200)
generateArrays(10000, 10, -200, 200)
