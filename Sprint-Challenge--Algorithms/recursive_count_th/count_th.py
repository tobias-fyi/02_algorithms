"""
Algorithms :: Sprint Challenge - "th" counter

Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
"""


def count_th(word: str) -> int:
    if len(word) == 2:  # Base case: length of string is 2
        if word == "th":
            return 1
    if len(word) < 2:  # Base case: length of word less than 2
        return 0

    counter = 0  # Keep track of "th" occurrences (this will be return value)
    # Recursive case: reduces length of string to get to base case
    first_two_letters = word[:2]  # Extract first two letters to check
    if first_two_letters == "th":
        counter += 1  # If current first two are "th"
    # Pass string without first letter into recursive call
    counter += count_th(word[1:])

    return counter


print(count_th("this THeory hath something."))  # Should return 3
