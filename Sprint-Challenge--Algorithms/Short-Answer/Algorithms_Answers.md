# Analysis of Algorithms: Short Answers

> Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(1)

```python
a = 0
  while (a < n * n * n):
    a = a + n * n
```

Line 1 is constant. On line 2, the input size `n` is used only to calculate and compare, not as a range over which the code iterates. Although as `n` increases the calculation gets larger, the actual runtime complexity stays constant.

Thus, the runtime complexity of this snippet is `O(1)`.

b) O(n)

```python
sum = 0
for i in range(n):
  j = 1
  while j < n:
    j *= 2
    sum += 1
```

The input size `n` is used to instantiate an iterator in line 2. The iterator loops through every value of n, thus adding `n` to the runtime complexity. Instantiating `j` on line 3 is constant at `1`. The `while` loop starting on line 4 is only a comparison, and so does not look through every single value of the input again.

The result of the sum of constant (e.g. `1`) and linear (e.g. `n`) is linear with respect to the input size `n`, or simply `n`. Thus, the runtime complexity of this snippet is `O(n)`.

c) O(n^2)

```python
def bunnyEars(bunnies):
  if bunnies == 0:
    return 0

  return 2 + bunnyEars(bunnies-1)
```

As `bunnyEars()` is a recursive function, the runtime complexity depends on the number of calls to itself are added to the stack with every successive call. In this instance, every call adds one more call to the stack, or another `n`, which leads to `n * n` or `n^2`. Therefore, it is expenential with respect to the input size `n`.

Thus, the runtime complexity is `O(n^2)`

## Exercise II

Answer 1:

    If floor is less than f, then the number of dropped and broken eggs is minimized.

The runtime complexity of this algorithm is constant, or `O(1)`.

Or, answer 2:

    Choose a constant number of eggs to drop (or throw) off of each floor
    Start on the first floor and toss the eggs off, keeping track of how many break
    Repeat this process on each floor until floor `n` is reached
    Once floor `n` is reached, review the number of eggs broken at each floor
    Find the floor which resulted in the fewest eggs broken
    If more than one floor, choose the lowest one

As this method would lead to throwing eggs off of every floor up to floor `n`, the runtime complexity is `O(n)`.
