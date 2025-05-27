"""Binary Search"""

def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2  # Avoids overflow

        if arr[mid] == target:
            return mid  # Element found
        elif arr[mid] < target:
            left = mid + 1  # Search in the right half
        else:
            right = mid - 1  # Search in the left half

    return -1  # Element not found

"""Driver Code"""
arr = [2, 3, 4, 10, 40]
target = 40
result = binary_search(arr, target)

print("Element found at index:", result if result != -1 else "Not found")
