# Iterative Binary Search Function
# It returns index of x in given array arr if present,
# else returns -1
def binary_search(arr, x):
    print('_______________')
    print('BINARY SEARCH')
    print('_______________')
    low = 0
    high = len(arr) - 1
    mid = 0
    comparisions = 0
    while low <= high:
        comparisions = comparisions +1
        mid = (high + low) // 2
        # If x is greater, ignore left half
        if arr[mid] < x:
            low = mid + 1
 
        # If x is smaller, ignore right half
        elif arr[mid] > x:
            high = mid - 1
 
        # means x is present at mid
        else:
            return mid
    print(f'No of Comparisions in BINARY SEARCH: {comparisions}')
    # If we reach here, then the element was not present
    return -1

print(binary_search([3,14,27,31,39,42,55,70,74,81,85,93,98],31))