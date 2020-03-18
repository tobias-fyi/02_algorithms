"""
Algorithms :: Recursive sorting
"""


def merge(arrA, arrB):
    """Merge two sorted arrays
    :param arrA (list): First/left list to be merged.
    :param arrB (list): Second/right list to be merged.
    :return merged_arr (list): Resulting merged list.
    """
    merged_arr = []  # Start with a blank list
    while arrA and arrB:  # Loop until at least one has length 0
        # Pop the first value of the array which has the lower first value
        # And append that to the results list
        merged_arr.append((arrA if arrA[0] <= arrB[0] else arrB).pop(0))
    # Clean up any extra items, in case arrays are not the same length
    merged_arr = merged_arr + arrA + arrB
    return merged_arr


# === Test out merge function === #
# arr_1 = [0, 2, 5, 7]
# arr_2 = [1, 3, 5]
# merge(arr_1, arr_2)


def merge_sort(arr: list):
    """A recursive merge sort algorithm.
    Splits the input array into halves until each item is in its own array.
    The individual item arrays are considered "sorted" and are then merged together.
    
    :param arr (list) : List to be sorted.
    :return (list) : Sorted list.
    """
    if len(arr) < 2:  # Base case: array is length 1 or 0
        return arr
    # Find middle index to slice lists into halves
    mid = len(arr) // 2
    # Recurse to sort left and right arrays
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    # Merge together the sorted arrays
    arr = merge(left, right)

    return arr


# # === Test out merge sort === #
# unsorted_arr = [18, 70, 1, 54, 84, 48, 7, 28, 96, 13, 2, 77, 63, 46, 87, 73, 52, 29]
# sorted_arr = merge_sort(unsorted_arr)
# print(sorted_arr)


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr: list, start, mid, end):
    # TODO

    return arr


def merge_sort_in_place(arr: list, l, r):
    # TODO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
