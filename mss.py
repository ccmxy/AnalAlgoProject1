


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

    print("\n============")
    print("Enumeration:")
    print("============")
    print("Start:"),
    print(nowMaxBeg),
    print("End:"),
    print(nowMaxEnd),
    print("Max:"),
    print(current)

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
    print("\n============")
    print("Better Enumeration:")
    print("============")
    print("Start:"),
    print(nowMaxBeg),
    print("End:"),
    print(nowMaxEnd),
    print("Max:"),
    print(current)


def linearTime(myArray, n):
    sum = 0
    x = 0
    nowMaxBeg = 0
    nowMaxEnd = 0

    for i in range(0, n):
        if x < 0:
            x = myArray[i]
            nowMaxBeg = i
        else:
            x = x + myArray[i]
        if sum < x:
            sum = x
            nowMaxEnd = i

    print("\n============")
    print("Linear Time:")
    print("============")
    print("Start: "),
    print(nowMaxBeg),
    print("End: "),
    print(nowMaxEnd),
    print("Max: "),
    print(sum)


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




with open("MSS_Problems.txt", "r") as ins:
    #index to hold the line number
    idx = 0
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
                    print(idx)
                    print(line)
                    enumeration(line, len(line))
                    betterEnumeration(line, len(line))
                    linearTime(line, len(line))
                    L,H,maxi = findmaxarray(line, 0, len(line) - 1)
                    print("\n============")
                    print("Divide and Conquer:")
                    print("============")
                    print("Start: "),
                    print(L),
                    print("End: "),
                    print(H),
                    print("Max: "),
                    print(maxi)
