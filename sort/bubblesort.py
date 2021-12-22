def bubble_sort(arr):
  print('_______________')
  print('BUBBLE SORT')
  print('_______________')
  size = len(arr)
  noOfComparisions = 0
  for i in range(size-1):
    for j in range(size-1):
      noOfComparisions = noOfComparisions+1
      if arr[j]>arr[j+1]:
        tmp = arr[j]
        arr[j] = arr[j+1]
        arr[j+1] = tmp
    print(f'after {i} pass BUBBLE SORT: {arr}')
  print("No of inner loops for Regular: %s" %(noOfComparisions))

def efficient_bubble_sort(arr):
  print('_______________')
  print('EFFICIENT BUBBLE SORT')
  print('_______________') 
  size = len(arr)
  noOfComparisions = 0
  swapped = False
  for i in range(size-1):
# Here since the last elements are already in place we only go till size-1-i
    noOfComparisions = noOfComparisions+1
    for j in range(size-1-i):
      
      if arr[j]>arr[j+1]:
        
        tmp = arr[j]
        arr[j] = arr[j+1]
        arr[j+1] = tmp
        swapped = True
    if not swapped:
      break
  print("No of inner loops for Efficient: %s" %(noOfComparisions))
 

if __name__ == '__main__':
  elements1= [89,45,68,90,29,34,17]
  elements2= [89,45,68,90,29,34,17]
  sorted1= [44,26,46,30,38,32,52,36]
  sorted2= [1,2,3,4,5,6,7]
  # selectin_sort(elements)
  efficient_bubble_sort(sorted1)
  # bubble_sort(sorted2)
  
        