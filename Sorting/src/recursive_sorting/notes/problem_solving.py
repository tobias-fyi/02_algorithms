# Print factorial of n


def recursive_factorial(n: int):
    print(n)
    # Base case
    if n <= 1:
        return 1

    # Recursive case
    prev = n * recursive_factorial(n - 1)
    return n * prev


print(recursive_factorial(5))

