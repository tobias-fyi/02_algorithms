"""
Algorithms :: Iterative sorting
"""

# %%
# Import time to track algorithm runtime
import time

# %%
# Test list to use while writing functionality
unsorted = [18, 70, 1, 54, 84, 48, 7, 28, 96, 13, 2, 77, 63, 46, 87, 73, 52, 29]

# %%
# Implement the Bubble Sort function below
def bubble_sort(arr: list):
    """Simple implementation of the Bubble Sort algorithm.
    Loops through the array, comparing the value at each index, `i`, with that
    of its neighbor, `i + 1`. If `i` is greater, swap the two values.
    
    :param arr (list) : List to be sorted.
    :return (list) : Sorted list.
    """
    # Variable to keep track of if the algorithm should continue or stop
    swap_count = 0
    # Loop through n-1 elements
    for i in range(0, len(arr) - 1):
        # Compare with neighbor
        if arr[i] > arr[i + 1]:  # Lower index is higher value - swap
            # Pop first item out of list into temporary variable
            tmp_val = arr.pop(i)
            # Insert popped value after current index (which now holds i+1's value)
            arr.insert(i + 1, tmp_val)
            swap_count += 1  # Count as a swap
        # else:  # Lower index is lower value - don't swap
    # If a swap occurred during the loop, restart it - aka call the function again
    if swap_count > 0:
        bubble_sort(arr)

    return arr


start = time.time()
bubble_sorted_list = bubble_sort(unsorted)
end = time.time()

print(bubble_sorted_list)
print(f"Runtime: {end - start}")


# %%
# TODO: Complete the selection_sort() function below
def selection_sort(arr: list):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # Find next smallest element
        for j in range(cur_index + 1, len(arr)):
            if arr[j] < arr[cur_index]:
                smallest_index = j

        # TODO: swap
        # To swap, first get the values at the two indices in question
        cur_index_val = arr[cur_index]
        smallest_index_val = arr[smallest_index]
        # Then, assign each to the other's index
        arr[cur_index] = smallest_index_val
        arr[smallest_index] = cur_index_val

    return arr


start = time.time()
select_sorted_list = selection_sort(unsorted)
end = time.time()

print(select_sorted_list)
print(f"Runtime: {end - start}")

# %%
# Confirm the sorting resulted in the same order
assert bubble_sorted_list == select_sorted_list

# %%
# TODO: STRETCH - Implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr
