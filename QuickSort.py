def quick_sort(arr):
    if len(arr) <= 1:
        return arr  # Base case: already sorted

    pivot = arr[len(arr) // 2]  # Choose the middle element as pivot
    left = [x for x in arr if x < pivot]      # Elements less than pivot
    middle = [x for x in arr if x == pivot]   # Elements equal to pivot
    right = [x for x in arr if x > pivot]     # Elements greater than pivot

    return quick_sort(left) + middle + quick_sort(right)

# Example usage
arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = quick_sort(arr)
print("Sorted array:", sorted_arr)
# This code implements the QuickSort algorithm, which is a divide-and-conquer sorting algorithm.
# It works by selecting a 'pivot' element from the array and partitioning the other elements into two sub-arrays,
# according to whether they are less than or greater than the pivot. The sub-arrays are then sorted recursively.
# The time complexity of QuickSort is O(n log n) on average, but it can b
# e O(n^2) in the worst case (e.g., when the array is already sorted).
