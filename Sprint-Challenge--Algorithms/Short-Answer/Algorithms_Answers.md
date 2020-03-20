# Analysis of Algorithms: Short Answers

> Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n)

```python
a = 0
  while (a < n * n * n):
    a = a + n * n
```

In every iteration of the while loop, the runtime increases by `n * n * n = n^3`. Inside the loop, `a` increases by `n * n = n^2`. The resulting overall runtime can be derived by finding how many iterations need to happen before the conditional is met and the loop is broken. In this case, this can be calculated by dividing the loop's runtime by the rate at which `a` increases to meet the conditional.

    O(n^3) / O(n^2) = O(n)

The result is that the loop would have to iterate `n` times to meet the conditional. Thus, the runtime complexity of this snippet is `O(n)`.

b) O(n^2)

```python
sum = 0
for i in range(n):
  j = 1
  while j < n:
    j *= 2
    sum += 1
```

The input size `n` is used to instantiate an iterator in line 2. The iterator loops through every value of n, thus adding `n` to the runtime complexity. The `while` loop starting on line 4 sees a doubling in `j` every iteration. As `j` increases logarithmically, resulting in a runtime complexity of `O(log(n)).

As the loops are nested, the total runtime is the result of the product of the two: `O(n • log(n))` . Thus, the runtime complexity of this snippet is `O(n log(n))`.

c) O(n)

```python
def bunnyEars(bunnies):
  if bunnies == 0:
    return 0

  return 2 + bunnyEars(bunnies-1)
```

As `bunnyEars()` is a recursive function, the runtime complexity depends on the number of calls to itself are added to the stack with every successive call. In this instance, every call adds one additional call to the stack, or another `n`, which ultimately to `n + 1` calls of `bunnyEars()`. Therefore, it is linear with respect to the input size `n`.

Thus, the runtime complexity is `O(n)`

## Exercise II

- Choose a constant number of eggs to drop (or throw) off of each floor
- Start on the first floor and toss the eggs off, keeping track of how many break
- Repeat this process on each floor until floor `n` is reached
- Once floor `n` is reached, review the number of eggs broken at each floor
- Find the floor which resulted in the fewest eggs broken
- If more than one floor, choose the lowest one

As this method would lead to throwing eggs off of every floor up to floor `n`, the runtime complexity is `O(n)`.

A more efficient algorithm to find the value f that minimizes the egg breakage would be:

- Start on the floor that is the midpoint between ground level and floor `n`
  - `middle_floor = n // 2`
- Toss an egg off
  - If it breaks, that means the egg will (probably) also break when thrown from any floor above the current one
    - Repeat step 1, this time considering the floor from the previous iteration as floor n
    - i.e. find the middle floor between floor 0 and the new floor n, and toss an egg off
    - Repeat until the optimal floor `f` is found
  - If it doesn't break, that means the egg will (probably) not break when thrown from any floor below the current one
    - Repeat step 1, this time considering the floor from the previous iteration as floor 0
    - i.e. find the middle floor between the new floor 0 and floor n, and toss an egg off
    - Repeat until the optimal floor `f` is found
