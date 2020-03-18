"""
Algorithms :: Recursion

LSCS :: Unit 1, Sprint 2, Module 2
"""

# # %%
# def this_recursion(n: int):
#     print(n)
#     if n == 5:
#         return
#     this_recursion(n + 1)


# this_recursion(1)

# %%
# def this_recursion(n: int):
#     print(n)
#     if n == 100:
#         return

#     this_recursion(n + 1)
#     this_recursion(n + 1)


# this_recursion(1)

# %%
from functools import lru_cache


# %%

# === Fibonacci === #
def recurfib(n: int):
    # Base case
    # TODO: Test for negatives

    if n == 0:  # If n is 0, return 0
        return 0
    if n == 1:  # If n is 1, return 1
        return 1

    n_minus_1 = recurfib(n - 1)
    n_minus_2 = recurfib(n - 2)

    # If not base case, return recursion of n-1 + n-2
    return n_minus_1 + n_minus_2


print(recurfib(5))

# %%
# Quick sort
[5, 9, 3, 7]

# === Plan === #

# Base case
# if array length less than 2
# return array
# else:
# Pik pivot - pick first one bc unsorted
# Put anything smaller into left array
# Put anything bigger into right array
# return quicksort(left) + quicksort(right)
