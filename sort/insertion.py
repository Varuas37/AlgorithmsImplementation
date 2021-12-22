def insertionSort(arr):
    print('_______________')
    print('INSERTION SORT')
    print('_______________')
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key
        print(f'after {i} pass: {arr}')
    return arr
  
  
def insertionSort2(arr):
    print('_______________')
    print('INSERTION SORT2')
    print('_______________')
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)-1):
        j = i-1
        while j >=0 and arr[j] > arr[j+1]:
          arr[j+1],arr[j] = arr[j],arr[j+1]
          j = j-1
        print(f'after {i} pass: {arr}');
    return arr
    
insertionSortElements= [34, 8, 64, 50, 32, 20]
insertionSortElements2= [89,45,68,90,29,34,17]

insertionSort(insertionSortElements)
# insertionSort2(insertionSortElements2)