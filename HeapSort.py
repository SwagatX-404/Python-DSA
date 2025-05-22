# ✅ What is Heap Sort?
# Heap Sort uses a Binary Heap data structure (specifically a Max-Heap).
# Steps:
#     Build a Max Heap from the array.
#     Swap the first (largest) element with the last element.
#     Heapify the reduced heap.
#     Repeat steps 2–3 until the array is sorted.
# 🧠 What is a Max-Heap?
# A Max-Heap is a binary tree where:
#     The parent is always greater than its children.
#     The largest element is always at the root (index 0).

def heapify(arr, n, i):
    largest = i        # Initialize largest as root
    left = 2 * i + 1    # Left child
    right = 2 * i + 2   # Right child

    # See if left child exists and is greater than root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # See if right child exists and is greater than current largest
    if right < n and arr[right] > arr[largest]:
        largest = right

    # Change root if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap
        heapify(arr, n, largest)  # Heapify the root again recursively

def heap_sort(arr):
    n = len(arr)

    # Build a max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # One by one extract elements
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]  # Swap max to the end
        heapify(arr, i, 0)  # Heapify the reduced heap

# Example usage
arr = [64, 34, 25, 12, 22, 11, 90]
heap_sort(arr)
print("Sorted array:", arr)
