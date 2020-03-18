# Algorithms FAQ

## Contents

- [Contents](#contents)
- [Questions](#questions)
  - [What's the difference between space and time complexity?](#whats-the-difference-between-space-and-time-complexity)
  - [What's an easy way to swap two values?](#whats-an-easy-way-to-swap-two-values)

## Questions

### What's the difference between space and time complexity?

Space complexity refers to how memory usage increaes as the size of input increases. Time complexity refers to how the number of operations an algorithm requires to finish increases as the size of input increases.

Many solutions will involve trade-offs between space & time complexity - the low memory solution will require more time and the faster algorithm might require more space.

---

### What's an easy way to swap two values?

```python
# With a temp variable...
a = 42
b = 21

temp = a
a = b
b = temp

# OR in a single line...
a = 42
b = 21

a, b = b, a
```

---
