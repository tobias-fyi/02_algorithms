"""
Algorithms :: Practice - making change
"""

# %%
import sys


# %%
def making_change(amt: int, coins: list) -> int:
    """Iterative implementation of the making change algorithm.
    
    :param amt (int) : Amount, in cents, to be made into change.
    :param coins (list) : List of coin denominations
    :return (int) : Number of different combinations of change.
    """
    # calc[i] represents the number of ways to get to amount i
    calc = [0] * (amt + 1)

    # 1 way to get zero
    calc[0] = 1

    # Pick all coins one by one and update calc[] values after the
    # index greater than or equal to the value of the picked coin
    for coin_val in coins:
        for j in range(coin_val, amt + 1):
            calc[j] += calc[j - coin_val]

    return calc[amt]


making_change(100, [1, 5, 10, 25, 50])


# %%
def making_change_recursive(amt: int, denominations: list) -> int:
    """Recursive implementation of the making change algorithm.
    TODO: Fix the max recursion error for large initial amounts
    
    :param amt (int) : Amount, in cents, to be made into change.
    :param coins (list) : List of coin denominations
    :return (int) : Number of different combinations of change.
    """
    # === Base case === #
    if amt == 0:  # Only one way to make 0
        return 1
    if amt < 0:  # No way to make negative
        return 0

    # Keep track of results
    count = 0
    cache = []

    # === Recursive case === #
    # Loop through the coins
    for i in range(len(denominations)):
        coin_val = denominations[i]  # Current coin's value
        # Find remaining value after current coin value is accounted for
        # I.e. what still has to be broken up (made into change)
        remaining_val = amt - coin_val
        if remaining_val not in cache:  # Check if calculation has already been done
            # Number of combinations of current is sum of current and successive coins
            count += making_change_recursive(remaining_val, denominations[i:])
            cache.append(remaining_val)  # Add the current calculation to cache

    return count


# No max recursion error
making_change_recursive(100, [1, 5, 10, 25, 50])

# Still gives max recursion error
# making_change_recursive(9590, [1, 5, 10, 25, 50])


# %%
if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python making_change.py [amount]` with different amounts
    if len(sys.argv) > 1:
        denominations = [1, 5, 10, 25, 50]
        amount = int(sys.argv[1])
        print(
            "There are {ways} ways to make {amount} cents.".format(
                ways=making_change(amount, denominations), amount=amount
            )
        )
    else:
        print("Usage: making_change.py [amount]")
