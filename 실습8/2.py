import random
import copy
import time


def bubbleSort(A):
    n = len(A)
    for i in range(n-1):
        for j in range(n - 1, i, -1):
            if A[j-1] > A[j]:
                A[j-1], A[j] = A[j], A[j-1]


def selectionSort(A):
    n = len(A)
    n = len(A)
    for i in range(n-1):
        least = i
        for j in range(i+1, n):
            if A[j] < A[least]:
                least = j
        A[i], A[least] = A[least], A[i]


def insertionSort(A):
    n = len(A)
    for i in range(1, n):
        key = A[i]
        j = i - 1
        while j >= 0 and A[j] > key:
            A[j+1] = A[j]
            j -= 1
        A[j+1] = key


while True:
    n = int(input("Enter a number of data: "))
    if n == -1:
        break
    data = []
    for i in range(n):
        numbers = random.randint(0, n)
        data.append(numbers)

    bubbleList = copy.deepcopy(data)
    selectionList = copy.deepcopy(data)
    insertionList = copy.deepcopy(data)
    sortList = copy.deepcopy(data)

    startTime = time.time()
    bubbleSort(bubbleList)
    endTime = time.time()
    print("Bubble sort elapsed time: %.3f seconds" % (endTime - startTime))

    startTime = time.time()
    selectionSort(selectionList)
    endTime = time.time()
    print("Seleciton sort elapsed time: %.3f seconds" % (endTime - startTime))

    startTime = time.time()
    insertionSort(insertionList)
    endTime = time.time()
    print("Insertion sort elapsed time: %.3f seconds" % (endTime - startTime))
    
    startTime = time.time()
    sortList.sort()
    endTime = time.time()
    print("Python sort elapsed time: %.3f seconds" %(endTime - startTime))
    print()

