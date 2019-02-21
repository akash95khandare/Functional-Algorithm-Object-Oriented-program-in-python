import math
import numpy as np
import random
import datetime


def getInput(msg=None, n=None):
    if n == None:
        print(msg)
    elif msg == None:
        print(n)
    else:
        print(msg, " ", n)
    return input()


def stringReplace():
    str = "Hello <<UserName>>, How are you?"
    name = input("Enter your name : ")
    str = str.replace("<<UserName>>", name)
    print(str)


def leapYear(n):
    if n % 100 == 0:
        if n % 400 == 0:
            print("Year is leap")
        else:
            print("Year is not leap year")
    elif n % 4 == 0:
        print("Year is leap Year")
    else:
        print("Year is not leap year")


def powerOfTwo(power):
    for i in range(power + 1):
        if power <= 31:
            print(i, " is power of 2 is : ", int(math.pow(2, i)))
        else:
            print("Range exceeded")


def harmonicValue(n):
    value = 0;
    for i in range(1, n + 1):
        value = value + 1 / n
    return value


def isPrime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def primeFactor(n):
    print("Prime factor is : ")
    for i in range(2, n):
        if isPrime(i):
            if n % i == 0:
                print(i, " ")


def sumOfThree(n):
    for i in range(len(n)):
        for j in range(i + 1, len(n)):
            for k in range(j + 1, len(n)):
                if (n[i] + n[j] + n[k] == 0):
                    print(n[i], " + ", n[j], " + ", n[k], " = 0")


def euclideanDistance(x, y):
    return math.sqrt(math.pow(x, x) + math.pow(y, y))


def rootOfX(a, b, c):
    delta = b * b - 4 * a * c
    x1 = (b + math.sqrt(abs(delta))) / (2 * a)
    x2 = (-b - math.sqrt(abs(delta))) / (2 * a)
    # x1 = (5+math.sqrt(delta))/(2*a)
    # x2 = (­-5-math.sqrt(delta))/(2*a)
    return x1, x2


def weather(t, v):
    w = 35.74 + 0.6215 * t + (0.4275 * t - 35.75) * math.pow(v, 0.16)
    return w


def getTwoDArr(r, c):
    print("Enter a list : ")
    arr = np.zeros((r, c))
    for i in range(r):
        for j in range(c):
            arr[i][j] = chr(input())
    return arr


def displayTwoDArr(arr):
    print(arr)


def ticTacToe():
    arr = np.zeros((3, 3))
    player = int(input("If you want to play first then enter 1 else 2. "))
    cnt = 0;
    while cnt < 9:
        if player == 1:
            printArr(arr)
            playerCall(arr)
            cnt += 1
            player = 2
            if winCheck(arr, 'X') == -1: player = -1
        elif player == 2:
            computer(arr)
            cnt += 1
            player = 1
            if winCheck(arr, 'O') == -1: player = -1
        else:
            printArr(arr)
            break;


def printArr(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if int(arr[i][j]) != 0:
                print(chr(int(arr[i][j])), end="  ")
            else:
                print("-", end="  ")
        print()


def playerCall(arr):
    print("Enter position with x and y co-ordinate")
    posX, posY = int(input()), int(input())
    while True:
        if arr[posX][posY] == 0:
            arr[posX][posY] = ord('X')
            break;
        else:
            print("This position already marked.")
            printArr(arr)
            playerCall()


def computer(arr):
    while True:
        posX = random.randrange(0, 3, 1)
        posY = random.randrange(0, 3, 1)
        if arr[posX][posY] == 0:
            arr[posX][posY] = ord('O')
            break;


def winCheck(arr, ch):
    c = ord(ch)
    if (arr[0][0] == c and arr[0][1] == c and arr[0][2] == c) \
            or (arr[1][0] == c and arr[1][1] == c and arr[1][2] == c) \
            or (arr[2][0] == c and arr[2][1] == c and arr[2][2] == c) \
            or (arr[0][0] == c and arr[1][0] == c and arr[2][0] == c) \
            or (arr[0][1] == c and arr[1][1] == c and arr[2][1] == c) \
            or (arr[0][2] == c and arr[1][2] == c and arr[2][2] == c) \
            or (arr[0][0] == c and arr[1][1] == c and arr[2][2] == c) \
            or (arr[0][2] == c and arr[1][1] == c and arr[2][0] == c):
        if ch == 'X':
            print("Player won")
            return -1;
        else:
            print("Computer won")
            return -1


def startWatch():
    start = datetime.datetime.now().microsecond
    return start


def stopWatch(start):
    stop = datetime.datetime.now().microsecond
    return stop - start


def swap(str, l, r):
    str = list(str)
    str[l], str[r] = str[r], str[l]
    return ''.join(str)


def permutation(str, l, r):
    if l == r:
        print(str)
    else:
        for i in range(l, r):
            str = swap(str, l, i)
            permutation(str, l + 1, r)
            str = swap(str, l, i)


def couponGenerator(n):
    li = [None] * n
    c = random.randrange(100, 500, 5)
    li[0] = int(c)
    j = 0
    while j < n:
        c = random.randrange(100, 500, 5)
        for i in range(j):
            if li[i] == c:
                c = random.randrange(100, 500, 5)
                i = 0
        li[j] = int(c)
        j += 1
    return li


def gambler(goal):
    doller = 1
    win, loss = 0, 0
    while True:
        n = int(input("You guess some number between 1 to 3"))
        g = random.randrange(1, 4, 1)
        if n == g:
            doller += 1;
            win += 1
            print("You won this bet.")
        else:
            print("You loss this bet.")
            doller -= 1
            loss += 1
        if doller == 0:
            print("You loss your all doller.")
            break;
        elif doller == goal:
            print("You achived your goal.")
            break


# print("Percentage of win : ",((win*100)/win+loss))
# print("Percentage of loss : ",((loss*100)/win+loss))

def flipCoin(n):
    for i in range(n):
        rand = random.random()
    if rand < 0.5:
        print("Percentage of Head : ", int(rand * 100))
    else:
        print("Percentage of Tail : ", int(rand * 100))


# 
# Algorithm
# 
def isAnagram(str1, str2):
    if len(str1) == len(str2):
        arr = np.full((len(str2)), False)
        cnt = 0
        for i in range(len(str1)):
            for j in range(len(str2)):
                if str1[i] == str2[j] and arr[j] == False:
                    arr[j] = True
                    cnt += 1
                    break
    else:
        return False
    if cnt == len(str1):
        return True


def isPrime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def isPalindrome(n):
    new = n
    reverse = 0
    while new != 0:
        temp = int(new % 10)
        new = int(new / 10)
        reverse = (reverse * 10) + temp
    if n == reverse:
        return True
    else:
        return False


def getPrimeNumber(rng):
    arr = []
    for i in range(2, rng + 1):
        if isPrime(i):
            arr.append(i)
    return arr


def getPalindrome(arr):
    newArr = []
    for i in arr:
        if isPalindrome(i):
            newArr.append(i)
    return newArr


def getAnagram(arr):
    newArr = []
    for i in range(len(arr) - 1):
        for j in range(1 + i, len(arr)):
            if isAnagram(str(arr[i]), str(arr[j])):
                newArr.append(arr[i])
                newArr.append(arr[j])
    return newArr


def insertionSort(arr):
    for i in range(1, len(arr)):
        j = i - 1
        while j > -1:
            if arr[i] < arr[j]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
            j -= 1
    return arr


def insertionSort(arr):
    for i in range(1, len(arr)):
        j = i - 1
        while j > -1:
            if arr[j + 1] < arr[j]:
                arr[j + 1], arr[j] = arr[j], arr[j + 1]
            j -= 1
    return arr


def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
    return arr


def mergeSort(arr, s, l):
    if s < l:
        mid = int((s + l) / 2)
        mid = int((s + (l - 1)) / 2)
        mergeSort(arr, s, mid)
        mergeSort(arr, mid + 1, l)
        merge(arr, s, mid, l)


def merge(arr, s, mid, l):
    n1 = mid - s + 1
    n2 = l - mid
    print(n1, n2)
    left = [0] * n1
    right = [0] * n2
    n = s

    for i in range(n1):
        left[i] = arr[n + i]

    for i in range(n1):
        right[i] = arr[mid + i]

    i, j = 0, 0
    k = s
    while i < n1 and j < n2:
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = left[i]
        i += 1
        s += 1
    while j < n2:
        arr[k] = right[j]
        j += 1
        s += 1


def binary(arr, start, last, key):
    while start <= last:
        mid = int((start + last) / 2)
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            start = mid + 1
        elif arr[mid] > key:
            last = mid - 1


def vendingMachine(change):
    arr = (1000, 500, 100, 50, 10, 5, 2, 1)
    for i in arr:
        if change == 0:
            return 0
        elif change >= i:
            print(i)
            change = vendingMachine(change - i)


def week(i):
    switcher = {
        0: "Sunday",
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday"
    }
    return switcher.get(i)


def dayOfWeek(d, m, y):
    y0 = y - (14 - m) / 12
    x = y0 + y0 / 4 - y0 / 100 + y0 / 400
    m0 = m + 12 * ((14 - m) / 12) - 2
    d0 = (d + x + 31 * m0 / 12) % 7
    return week(int(d0))


def toBinary(n):
    tm = np.zeros(8)
    res = np.zeros(8)
    i = 0
    while n != 0:
        temp = int(n % 2)
        n = int(n / 2)
        tm[i] = temp
        i += 1
    i = 8
    for j in tm:
        i -= 1
        res[i] = j
    return res


def toDecimal(binary):
    j = 7
    res = 0
    for i in binary:
        if i == 1:
            res = res + math.pow(2, j)
        j -= 1
    return int(res)


def swapNibbles(binary):
    j = 4
    for i in range(4):
        binary[i], binary[j] = binary[j], binary[i]
        j += 1
    return binary
