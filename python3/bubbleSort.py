# Bubble sort to sort given array in ascending order. 
def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            # comparision operator ( > ) should be replaced with < to sort array in descending order. 
            if arr[j] > arr[j+1] : arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr;

bubbleSort([5, 1, -19, 3, 0, -1])