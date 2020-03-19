"""
Algorithms :: Notes - Writing Better Solutions
"""

cache = {0: 1, 1: 1}


def rec_fib(n: int) -> int:
    # Base case is in cache
    if n in cache:
        return cache[n]

    # If not in the cache, calculate it
    n_minus_1 = rec_fib(n - 1)
    n_minus_2 = rec_fib(n - 2)

    cache[n] = n_minus_1 + n_minus_2

    return cache[n]


print(rec_fib(12))

