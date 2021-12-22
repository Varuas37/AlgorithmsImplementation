import sort.selectionsort as slection
import sort.bubblesort as bubble
import sort.stringmatch as stringMatch
import sort.insertion as insertion
import sort.merge as merge
import search.sequential as sequential
import search.binary as binary

if __name__ == '__main__':
  selectionSortElements= [44,36,46,32,38,52,30,26]
  bubbleSortElements= [34,3,23,12,5,1]
  
  sequentialSearchElements = [89,45,68,90,29,34,17]
  mergeSearchElements = [89,45,68,90,29,34,17]
  binarySearchElements = [18,22,28,34,42,44,58,64,86]
  fullString = "It is never too late to have a happychildhood"
  stringToMatch = "happy"

# >>>>>BRUTE FORCE<<<<<<
  # Selection Sort
  slection.selection_sort(selectionSortElements)
  # String Match
  print(stringMatch.BruteForceStringMatch(fullString,stringToMatch))
  # Bubble Sort
  bubble.bubble_sort(bubbleSortElements)
  # MERGE SORT 
  # merge.mergeSort(mergeSearchElements,0)
# >>>>>>>>DECREASE AND CONQUER<<<<<<
insertionSortElements= [89,45,68,90,29,34,17]
insertionSortElements2= [89,45,68,90,29,34,17]
insertion.insertionSort(insertionSortElements)
insertion.insertionSort2(insertionSortElements)

# >>>>>>>SEARCH<<<<<<<<<<<<
sequential.Sequential_Search(sequentialSearchElements,34)
print(binary.binary_search(binarySearchElements,34))