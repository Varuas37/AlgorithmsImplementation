def partition(arr, low, high):
	i = (low-1)
	pivot = arr[high]
	for j in range(low, high):
		if arr[j] <= pivot:
			i = i+1
			arr[i], arr[j] = arr[j], arr[i]
	arr[i+1], arr[high] = arr[high], arr[i+1]
	return (i+1)

def quickSort(arr, low, high):
	if len(arr) == 1:
		return arr
	if low < high:
		partitionIndex = partition(arr, low, high)

		quickSort(arr, low, partitionIndex-1)
		quickSort(arr, partitionIndex+1, high)

arr = [20, 96, 4, 60, 68, 56, 16]
n = len(arr)
quickSort(arr, 0, n-1)
print(f'Sorted Array: {arr}');

