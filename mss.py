
import timeit
import random

#File full of int arrys to be opened when the prgram executes
CONST_FILE_NAME = "MSS_PROBLEMS.txt"


def printArray(array, begSub, endSub, maxSum, functionName):
    print("\n=================")
    print(functionName)
    print("=================")
    print(array)
    subArray = []
    for j in range(begSub, endSub+1):
        subArray.append(array[j])
    print(subArray)
    print("Max: "),
    print(maxSum)

def enumeration(a, n):
    sum = 0
    current = 0
    nowMaxBeg = 0
    nowMaxEnd = 0

    for i in range(0,n):
        for j in range(0, n):
            sum = 0
            for k in range(i, j+1):
                sum = sum + a[k]
                if sum > current:
                    nowMaxBeg = i
                    nowMaxEnd = j
                    current = sum
    return nowMaxBeg, nowMaxEnd, current;


def betterEnumeration(a, n):
    sum = 0
    current = 0
    nowMaxBeg = 0
    nowMaxEnd = 0

    for i in range(0, n):
        sum = 0
        for j in range(i, n):
            sum = sum + a[j]
            if sum > current:
                current = sum
                nowMaxBeg = i
                nowMaxEnd = j

    return nowMaxBeg, nowMaxEnd, current


def linearTime(myArray, n):
    max = 0
    currSum = 0
    nowMaxBeg = 0
    nowMaxEnd = 0

    for i in range(0, n):
        if currSum < 0:
            currSum = myArray[i]
            nowMaxBeg = i
        else:
            currSum = currSum + myArray[i]
        if max < currSum:
            max = currSum
            nowMaxEnd = i
    return nowMaxBeg, nowMaxEnd, max


def crossingsubarray(A, low, mid, high):

    negetiveinfinity = -10000000000
    summ = 0
    for i in range(mid, low - 1, -1):
        summ = summ + A[i]
        if summ > negetiveinfinity:
            negetiveinfinity = summ
            leftindex = i
    left = negetiveinfinity

    negetiveinfinity = -10000000000
    summ = 0

    for j in range(mid+1, high+1):
        summ = summ + A[j]
        if summ > negetiveinfinity:
            negetiveinfinity = summ
            rightindex = j
    right = negetiveinfinity

    return(leftindex, rightindex, left + right)


def findmaxarray(alist, low, high):

    if high == low:
        return low, high, alist[low]

    else:

        mid = (low+high)/2

        leftlow, lefthigh, leftsum = findmaxarray(alist, low, mid)
        rightlow, righthigh, rightsum = findmaxarray(alist, mid + 1, high)
        crosslow, crosshigh, crosssum = crossingsubarray(alist, low, mid, high)

        if leftsum >= rightsum and leftsum >= crosssum:
            return leftlow, lefthigh, leftsum
        elif rightsum >= leftsum and rightsum >= crosssum:
            return rightlow, righthigh, rightsum
        else:
            return crosslow, crosshigh, crosssum


with open(CONST_FILE_NAME, "r") as ins:
    #index to hold the line number
    idx = 0
    nowMaxBeg = 0
    nowMaxEnd = 0
    sum = 0

    for line in ins:

        #strip string of extra characters
        for ch in [",","[","]"]:
            if ch in line:
                line = line.replace(ch," ")
        #Convert to int array
        line = map(int, line.split())
        if len(line) > 0:
                    idx += 1
                    print("\n\n\n\n\t\t\tTESTING ARRAY NUMBER:"),
                    print(idx),
                    print("(n = "),
                    print(len(line)),
                    print(")")


                    setup = "from __main__ import betterEnumeration, enumeration, linearTime, findmaxarray, line"
                    enum = "enumeration(line, len(line))"

                    nowMaxBeg, nowMaxEnd, maxSum = enumeration(line, len(line))
                    printArray(line, nowMaxBeg, nowMaxEnd, maxSum, 'Enumeration:')
                    print timeit.timeit(enum, setup, number=1),
                    print("microseconds")

                    nowMaxBeg, nowMaxEnd, maxSum = betterEnumeration(line, len(line))
                    printArray(line, nowMaxBeg, nowMaxEnd, maxSum, 'Better Enumeration:')
                    print timeit.timeit("betterEnumeration(line, len(line))", setup, number=1),
                    print("microseconds")

                    nowMaxBeg, nowMaxEnd, maxSum = linearTime(line, len(line))
                    printArray(line, nowMaxBeg, nowMaxEnd, maxSum, 'Linear Time:')
                    print timeit.timeit("linearTime(line, len(line))", setup, number=1),
                    print("microseconds")

                    nowMaxBeg, nowMaxEnd, maxSum = findmaxarray(line, 0, len(line) - 1)
                    printArray(line, nowMaxBeg, nowMaxEnd, maxSum, 'Divide and Conquer:')
                    print timeit.timeit("findmaxarray(line, 0, len(line) - 1)", setup, number=1),
                    print("microseconds")
