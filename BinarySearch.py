# Binary Search Implementation in Python
# This code performs a binary search on a sorted array to find the index of a target element.

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

arr = [2, 3, 4, 10, 15, 20, 30]
targate = 10
result = binary_search(arr, targate)
if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found in the array")
