"""
Algorithms :: Sorting notes
"""

import random
import time

my_range = 1000000
my_size = 1000000
search_for = 77

my_rand = random.sample(range(my_range), my_size)


def find_in_number(arr, num):
    for i in range(len(my_rand)):
        if arr[i] == num:
            return True

    return False


def find_value_binary(arr, num):
    if len(arr) < 2:
        # TODO: hangle edge
        pass

    first = 0
    last = len(arr) - 1

    found = False

    while first <= last and not found:
        # Find middle using floor division
        middle = (first + last) // 2

        if arr[middle] == num:
            found = True
        elif num < arr[middle]:
            # Search lower half of remainder
            last = middle - 1
        else:  # Search upper half of remainder
            first = middle + 1

    return found


print("\nLinear")
start = time.time()
print(find_in_number(my_rand, search_for))
end = time.time()
print(f"Runtime: {end - start}")

print("\nBinary")
start = time.time()
my_rand.sort()
print(find_in_number(my_rand, search_for))
end = time.time()
print(f"Runtime: {end - start}")

print("\nBinary after sort")
start = time.time()
print(find_in_number(my_rand, search_for))
end = time.time()
print(f"Runtime: {end - start}")
