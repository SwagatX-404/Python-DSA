# Bubble Sort Implementation in Python
# This code sorts an array using the bubble sort algorithm, which repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order.

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Track if a swap was made
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        # If no two elements were swapped in the inner loop, then the array is already sorted
        if not swapped:
            break

    
arr = [64, 25, 12, 22, 11]
print("Original array:", arr)

bubble_sort(arr)
    
print("Sorted array:", arr)