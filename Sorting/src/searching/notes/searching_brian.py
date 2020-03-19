"""
Algorithms :: Search
"""


def binary_search(arr, val):
    left = 0
    middle = len(arr) // 2
    right = len(arr) - 1

    while left < right:
        if arr[middle] == val:
            return True
        elif val < arr[middle]:
            right = middle - 1
        else:
            left = middle + 1

    return False
