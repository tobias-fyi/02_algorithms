"""
Algorithms :: Practice - recursion
"""

# %%
def foo1(x=3):
    def foo2(y=2):
        def foo3(z=1):
            return z

        return foo3() + y

    return foo2() + x


print(foo1())


# %%
def summ(n: int) -> int:
    if n == 1:
        return n
    else:
        return n + summ(n - 1)


print(summ(4))


# %%
def factorial(n: int) -> int:
    # Base case
    if n == 1:
        print(f"Base case frame: n = {n}")
        return n
    print(f"Pre-recursive: n = {n} | Calling `{n} * factorial({n - 1})`")
    # Recursive case
    r = factorial(n - 1)
    print(f"Post-recursive: r = {r}")
    return n * r


print(factorial(7))


# %%
def dec_to_bin(n):
    if n == 0:
        print(f"Base case frame: n == {n}")
        return 0
    else:
        print(f"Pre-recursive: n = {n}")
        r = 10 * dec_to_bin(int(n / 2))
        print(f"Post-recursive: r = {r}")
        return n % 2 + r


print(dec_to_bin(7))

# %%
# Greatest common denominator - iterative solution
def gcd_iter(a, b):
    counter = 1
    print(f"step = {counter}")
    while b:
        print(f"before: a = {a}, b = {b}, a % b = {a % b}")
        a, b = b, a % b
        print(f"after : a = {a}, b = {b}")
        counter += 1
    return a


print(gcd_iter(12, 20))


# %%
# Greatest common denominator - recursive solution
def gcd_recur(a, b):
    if b == 0:
        return a
    else:
        return gcd_recur(b, a % b)


print(gcd_recur(12, 20))


# %%
"""
Implement a recursive algorithm itos() that converts a number, digit by digit, to a string.

- Don’t convert the entire integer to a string and return it - that’s cheating!
- The final returned result should be a single string representing the entire number.
  - For example, if we passed the integer 1234 to itos(), the function would return
  '1234' such that type('1234') == str.
- You can break this problem down into three parts.
  - How do you identify your base case?
  - The pre-recursive work:
    - How do you get to that base case?
    - How do you need to seed your frames on the way to the base case?
  - The post-recursive work:
    - What would you add to the base case as it works its way back through the
    recursed calls?
    - Does the order of what is returned and what is added matter?
- Annotate your solution with print statements that show, at each frame:
  - the state of the function, specifying what is being passed and
  what is being returned
  - a counter that tracks the frames as they are opened and closed
"""
# %%
frame = 1
print(f"At global frame = {frame}")


def itos(n: int) -> str:
    global frame
    frame += 1
    # TODO: Base case
    if n % 10 == n:
        print(f"Base case frame = {frame}, n = {n}")
        return str(n)
    # TODO: Recursive case
    print(f"pre-recursive: n = {n}")
    digit = n % 10  # Extract last digit
    print(f"Last digit: {digit}")
    rest = n // 10  # `Pop` last digit off of number
    print(f"Rest of number: {rest}")
    r = itos(rest)  # recurse into rest of number
    frame -= 1
    print(f"post-recursive: r = {r}")

    return r + str(digit)


print(f"Result: {itos(1234)} (type of {type(itos(1234))})")


# %%
def itos(n: int) -> str:
    # Base case: one digit number
    if n % 10 == n:  # Clever way of saying `if n < 10`
        return str(n)
    # Recursive case
    digit = n % 10  # Extract last digit
    rest = n // 10  # `Pop` last digit off of number
    print(f"{n} -> itos({rest}) + str({digit})")
    r = itos(rest)  # recurse into rest of number

    return r + str(digit)


result = itos(54321)
print(f"Result: {result} (type of {type(result)})")


# %%
