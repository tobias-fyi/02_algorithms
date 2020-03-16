"""
Algorithms :: Sorting
"""

the_list = [4, 5, 8, 2, 1, 8, 9, 3, 5]


def insertion_sort(arr):
    # Separate first element, think of it as sorted

    # For all other indices, starting at 1
    for i in range(1, len(arr)):
        # Put current number in a temp var
        temp = arr[i]
        # Look left, until we find where it belongs
        j = i
        while j > 0 and temp < arr[j - 1]:

            # As we look left, shift items to the right as we iterate
            arr[j] = arr[j - 1]
            j -= 1

        # When left is smaller than temp, or we're at 0, put at this spot
        arr[j] = temp

    return arr


(insertion_sort(the_list))

