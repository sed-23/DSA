# Bubble sort to sort given array in ascending order. 
def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            # comparision operator ( > ) should be replaced with < to sort array in descending order. 
            if arr[j] > arr[j+1] : arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr;

bubbleSort([5, 1, -19, 3, 0, -1])

'''
Time complexity: O(n^2) 
Best case time complexity : O(n) - already sorted array
Worst case time complexity : O(n^2) - completely unsorted array.

Space complexity : O(1) - temp variable.
'''