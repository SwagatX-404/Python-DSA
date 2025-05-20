def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # Assume the current element is the minimum
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Swap the found minimum with the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# Example usage
arr = [64, 25, 12, 22, 11]
selection_sort(arr)
print("Sorted array:", arr)
# Output: Sorted array: [11, 12, 22, 25, 64]
# This code sorts an array using the selection sort algorithm, which divides the input list into two parts: a sorted part and an unsorted part. It repeatedly selects the smallest (or largest, depending on the order) element from the unsorted part and moves it to the end of the sorted part.
