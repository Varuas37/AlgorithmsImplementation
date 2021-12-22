# Python program for implementation of MergeSort
comparisions = 0
def mergeSort(arr,comparisions):
    comparisions = comparisions+1
    if len(arr) > 1:
         # Finding the mid of the array
        mid = len(arr)//2
        # Dividing the array elements
        L = arr[:mid]
        # into 2 halves
        R = arr[mid:]
        # Sorting the first half
        mergeSort(L,comparisions)
        # Sorting the second half
        mergeSort(R,comparisions)
        i = j = k = 0
        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
        print(f'after {i} pass MERGE SORT: {arr}')
    
# Code to print the list
mergeSearchElements = [89,45,68,90,29,34,17]

  
def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()
mergeSort(mergeSearchElements,0)