"""Algorithms :: Merge sort

Notes from reviewing merge sort in lecture.
"""

arr1 = [5, 9, 3, 7, 2, 8, 1, 6]

arr2 = [[5, 9, 3, 7], [2, 8, 1, 6]]

arr3_2 = [[5, 9], [3, 7], [2, 8], [1, 6]]

# Single-item arrays are sorted
arr3_2 = [[5], [9], [3], [7], [2], [8], [1], [6]]


def merge(arrA: list, arrB: list):
    elements = len(arrA, arrB)
    merged_arr = [0] * elements
    # TODO: Put arrays back to gether
    # Sorting happens here

    # Instantiate initial cursor values
    a = 0  # arrA
    b = 0  # arrB
    # k = 0  # merged_arr
    # Can instantiate `k` in loop
    for k in range(0, elements):
        # if a is out of range, push b and iterate
        if a >= len(arrA):  # We're done with a, push b
            merged_arr[k] = arrB[b]
            b += 1
        # if b is out of range, push a and iterate
        elif b >= len(arrB):
            merged_arr[k] = arrA[a]
            a += 1
        # If a is smaller, put in array and iterate both
        elif arrA[a] < arrB[b]:
            merged_arr[k] = arrA[a]
            a += 1
        # If b is smaller, put in array and iterate both
        else:
            merged_arr[k] = arrB[b]
            b += 1

    return merged_arr


def merge_sort(arr: list):
    # TODO: Split arrays
    # Base case if array > 1
    if len(arr) > 1:
        # Find the middle of array

        # Put stuff to left in left
        left = merge_sort(arr[0 : len(arr) // 2])
        # Put stuff to right in right
        right = merge_sort(arr[len(arr) // 2 :])
        # Merge left and right
        arr = merge(left, right)

    return arr
