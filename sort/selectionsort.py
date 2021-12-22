def selection_sort(arr):
  print('_______________')
  print('SELECTION SORT')
  print('_______________')
  size = len(arr)
  comparisions = 0
  for i in range(size-1):
    min_index = i
    for j in range(min_index+1, size):
      comparisions = comparisions +1
      if arr[j]<arr[min_index]:
        min_index=j
    if i != min_index:
      arr[i],arr[min_index] = arr[min_index],arr[i]
    print(f'after {i} pass SELECTION SORT: {arr}')
  print(f'No of Comparisions SELECTION SORT: {comparisions}')
      
