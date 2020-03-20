"""
Algorithms :: Spring challenge - analysis of algorithms

Using a loop to calculate runtimes for increasing number of inputs.
"""

# %%
import time

# %%
# a)
for n in range(1, 100000, 1000):
    start_time = time.time()
    a = 0
    while a < n * n * n:
        a = a + n * n
    end_time = time.time()
    print(n, end_time - start_time)


# %%
# b)
for n in range(1, 100000, 1000):
    start = time.time()
    total = 0
    for i in range(n):
        j = 1
        while j < n:
            j *= 2
            total += 1
    end = time.time()
    print(n, end - start)

# %%
# c)
def bunny_ears(bunnies):
    if bunnies == 0:
        return 0

    return 2 + bunny_ears(bunnies - 1)


for n in range(1, 1000, 100):
    start = time.time()
    bunny_ears(n)
    end = time.time()
    print(n, end - start)


# %%
