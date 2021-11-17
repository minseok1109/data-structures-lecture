import random
import copy
import time

def sequential_search(A, key):
    for i in range(len(A)):
        if A[i] == key:
            return i
    return -1

def binary_search(A, key):
    low = 0
    high = len(A) - 1
    while low <= high:
        mid = (low + high) // 2
        if A[mid] == key:
            return mid
        elif key < A[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1

n = int(input("Enter a number of data: "))
data = []
for i in range(n):
    numbers = random.randint(0, n)
    data.append(numbers)
    
unsortedList = copy.deepcopy(data)
sortList = copy.deepcopy(data)

startTime = time.time()
sortList.sort()
endTime = time.time()
print("Python sort elapsed time: %.3f seconds" %(endTime - startTime))
print()

while True:
    n = int(input("Enter a number to search: "))
    if n == -1:
        break
    SstartTime = time.time()
    sresult = sequential_search(unsortedList,n)
    SendTime = time.time()
    if sresult == -1:
        print(f"{n} is not in the list")
        print("Sequential search elapsed time: %.3f seconds" %(SendTime - SstartTime))
    else:
        print(f"{n} is in the list at index {sresult}")
        print("Sequential search elapsed time: %.3f seconds" %(SendTime - SstartTime))
        
    BstartTime = time.time()
    bresult = binary_search(sortList,n)
    BendTime = time.time()
    
    if bresult == -1:
        print(f"{n} is not in the list")
        print("Binary search elapsed time: %.3f seconds" %(BendTime - BstartTime))
        print()
    else:
        print(f"{n} is in the list at index {bresult}")
        print("Binary search elapsed time: %.3f seconds" %(BendTime - BstartTime))
        print()
    
        
