import copy
data = [24, 15, 29, 11, 47, 12]

bubbleList = copy.deepcopy(data)
selectionList = copy.deepcopy(data)
insertionList = copy.deepcopy(data)



def bubbleSort(A):
    print("Before sorting")
    print(A)
    print()
    n = len(A)
    print("After bubble sorting")
    for i in range(n-1):
        for j in range(n - 1, i, -1):
            if A[j-1] > A[j]:
                A[j-1], A[j] = A[j], A[j-1]
        print(f"Pass {i+1}: {A}")
    print()
    
def selectionSort(A):
    print("Before sorting")
    print(A)
    print()
    n = len(A)
    print("After selection sorting")
    n = len(A)
    for i in range(n-1):
        least = i
        for j in range(i+1, n):
            if A[j] < A[least]:
                least = j
        A[i], A[least] = A[least], A[i]
        print(f"Pass {i+1}: {A}")
    print()

def insertionSort(A):
    print("Before sorting")
    print(A)
    print()
    n = len(A)
    print("After insertion sorting")
    for i in range(1, n):
        key = A[i]
        j = i -1
        while j >=0 and A[j] > key:
            A[j+1] = A[j]
            j-=1
        A[j+1] = key
        print(f"Pass {i}: {A}")

        
        

bubbleSort(bubbleList)
selectionSort(selectionList)
insertionSort(insertionList)