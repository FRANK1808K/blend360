# 03 · Python — what you need for the technical test

🌐 [Español](README.md) · **English**

> According to candidate reports, Blend360's online test usually includes **Python (or R) programming problems together with SQL**, with limited time. There may also be multiple-choice questions such as "what does this code print?". This module covers both.

**Material in this module:**

| File | Purpose |
|---|---|
| This README | Theory + typical traps + "what is the output?" quiz |
| [ejercicios.py](ejercicios.py) | 25 functions for **you** to implement (statements in English and Spanish) |
| [soluciones.py](soluciones.py) | Commented solutions (open them only after trying) |
| [test_ejercicios.py](test_ejercicios.py) | Automatic grader |
| [pandas.en.md](pandas.en.md) | Data analysis with pandas (SQL equivalents) |

```bash
cd 03-python
python3 test_ejercicios.py              # grades YOUR answers (ejercicios.py)
python3 test_ejercicios.py soluciones   # checks the reference solutions
```

---

## Contents

1. [Data types and operators](#1-data-types-and-operators)
2. [Strings](#2-strings)
3. [Lists, tuples, sets and dictionaries](#3-lists-tuples-sets-and-dictionaries)
4. [Control flow](#4-control-flow)
5. [Functions](#5-functions)
6. [Comprehensions](#6-comprehensions)
7. [Tools that save time in the test](#7-tools-that-save-time-in-the-test)
8. [Errors and exceptions](#8-errors-and-exceptions)
9. [Classes (basic OOP)](#9-classes-basic-oop)
10. [Mutability and references (trap #1)](#10-mutability-and-references-trap-1)
11. [Quiz: what is the output?](#11-quiz-what-is-the-output)

---

## 1. Data types and operators

| Type | Example | Mutable |
|---|---|---|
| `int` | `42` | — |
| `float` | `3.14` | — |
| `bool` | `True`, `False` (they are a subclass of `int`: `True + True == 2`) | — |
| `str` | `"hello"` | ❌ No |
| `list` | `[1, 2, 3]` | ✅ Yes |
| `tuple` | `(1, 2, 3)` — a one-element tuple is `(1,)` | ❌ No |
| `set` | `{1, 2, 3}` — no order, no duplicates. **`{}` is an empty dict**; empty set = `set()` | ✅ Yes |
| `dict` | `{"a": 1}` — keeps insertion order (Python 3.7+) | ✅ Yes |
| `None` | Absence of a value | — |

| Operator | Result | Watch out |
|---|---|---|
| `7 / 2` | `3.5` | `/` **always** returns a float |
| `7 // 2` | `3` | Floor division: `-7 // 2 == -4` |
| `7 % 2` | `1` | Modulo (remainder). `n % 2 == 0` → even |
| `2 ** 10` | `1024` | Power |
| `==` vs `is` | `==` compares **value**; `is` compares **identity** (same object) | Use `is` only with `None`: `x is None` |
| `and`, `or`, `not` | They return one of the operands: `0 or "x"` → `"x"` | Short-circuit evaluation |

**"Falsy" values** (they behave like `False`): `0`, `0.0`, `""`, `[]`, `{}`, `set()`, `None`, `False`. Everything else is "truthy".

## 2. Strings

```python
s = "Blend360 Data"
s[0]        # 'B'
s[-1]       # 'a'           (negative indexes count from the end)
s[0:5]      # 'Blend'       (the end is NOT included)
s[::-1]     # 'ataD 063dnelB'  (reverse)
s.lower(), s.upper()
s.split()             # ['Blend360', 'Data']    (by whitespace)
"a,b,,c".split(",")   # ['a', 'b', '', 'c']
"-".join(["a", "b"])  # 'a-b'
s.replace("Data", "AI")
s.strip()             # removes leading/trailing whitespace
s.startswith("Bl"), s.endswith("ta")
s.find("360")         # 5   (-1 if not found)
"360" in s            # True
s.isdigit(), s.isalpha(), s.isalnum()
f"{3.14159:.2f}"      # '3.14'  (f-strings)
```

> Strings are **immutable**: `s[0] = "b"` → `TypeError`. You have to create a new one.

## 3. Lists, tuples, sets and dictionaries

```python
# LISTS
nums = [5, 3, 8]
nums.append(1)          # [5, 3, 8, 1]
nums.extend([7, 7])     # [5, 3, 8, 1, 7, 7]
nums.insert(0, 9)       # inserts at position 0
nums.pop()              # removes and returns the last one
nums.remove(7)          # removes the FIRST occurrence of the value 7
nums.sort()             # sorts IN-PLACE, returns None
sorted(nums)            # returns a NEW sorted list
nums.reverse()          # reverses in-place
len(nums), sum(nums), min(nums), max(nums)
nums.index(8), nums.count(7)

# SETS: O(1) membership and set operations
a, b = {1, 2, 3}, {2, 3, 4}
a | b   # union                {1, 2, 3, 4}
a & b   # intersection         {2, 3}
a - b   # difference           {1}
a ^ b   # symmetric difference {1, 4}

# DICTIONARIES
d = {"ana": 3, "luis": 5}
d["maria"] = 2              # add/update
d.get("pedro", 0)           # 0 if missing (d["pedro"] → KeyError)
d.keys(), d.values(), d.items()
for k, v in d.items(): ...
"ana" in d                  # searches the KEYS, O(1)
d.pop("ana")
{k: v for k, v in sorted(d.items(), key=lambda kv: kv[1], reverse=True)}  # sort by value
```

## 4. Control flow

```python
for i in range(5):          # 0,1,2,3,4      range(start, exclusive_end, step)
    if i == 3:
        break               # exits the loop
    if i % 2 == 0:
        continue            # jumps to the next iteration
else:
    print("runs only if there was NO break")

while n > 0:
    n -= 1

x = "even" if n % 2 == 0 else "odd"    # ternary operator
```

## 5. Functions

```python
def greet(name, greeting="Hello", *args, **kwargs):
    """Docstring: describes the function."""
    return f"{greeting}, {name}"

greet("Ana")                         # 'Hello, Ana'
greet(greeting="Hi", name="Ana")     # keyword arguments

square = lambda x: x ** 2            # anonymous function
sorted(words, key=len)               # a lambda/function as the sort criterion
```

- A function without `return` returns `None`.
- `*args` receives extra positional arguments as a **tuple**; `**kwargs` receives extra keyword arguments as a **dict**.
- ⚠️ **Mutable default argument:** `def f(x, lst=[])` shares the **same** list between calls. Use `lst=None` and inside `if lst is None: lst = []`.
- **Scope (LEGB):** Local → Enclosing → Global → Built-in.

## 6. Comprehensions

```python
squares   = [x**2 for x in range(10)]
evens     = [x for x in nums if x % 2 == 0]
labels    = ["even" if x % 2 == 0 else "odd" for x in nums]   # if-else goes BEFORE the for
transpose = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
flat      = [x for row in matrix for x in row]                # flatten
counts    = {c: word.count(c) for c in set(word)}             # dict comprehension
unique    = {x % 3 for x in nums}                             # set comprehension
gen       = (x**2 for x in range(10**6))                      # generator: uses almost no memory
```

## 7. Tools that save time in the test

```python
from collections import Counter, defaultdict, deque
import heapq, itertools, math

Counter("banana")                  # Counter({'a': 3, 'n': 2, 'b': 1})
Counter(words).most_common(2)      # [('x', 5), ('y', 3)]

groups = defaultdict(list)         # no KeyError: creates [] automatically
for name, dept in pairs:
    groups[dept].append(name)

q = deque([1, 2]); q.append(3); q.popleft()    # O(1) queue at both ends

heapq.nlargest(3, nums); heapq.nsmallest(3, nums)
heapq.heappush(h, x); heapq.heappop(h)         # min-heap

for i, x in enumerate(lst): ...                # index + value
for a, b in zip(list1, list2): ...             # iterate in parallel
any(x > 10 for x in nums); all(x > 0 for x in nums)
sorted(people, key=lambda p: (-p["age"], p["name"]))  # sort by several criteria
math.inf, math.sqrt(16), math.ceil(2.1), math.floor(2.9)
itertools.combinations([1, 2, 3], 2)          # (1,2) (1,3) (2,3)
itertools.permutations([1, 2, 3], 2)
```

## 8. Errors and exceptions

```python
try:
    result = 10 / int(value)
except ValueError:
    print("not a number")
except ZeroDivisionError as e:
    print("division by zero:", e)
else:
    print("no errors")         # only if there was no exception
finally:
    print("always runs")

raise ValueError("message")    # raise an exception
```

The most common ones: `TypeError` (wrong type, e.g. `"a" + 1`), `ValueError` (right type, invalid value, e.g. `int("x")`), `KeyError`, `IndexError`, `ZeroDivisionError`, `AttributeError`, `NameError`.

## 9. Classes (basic OOP)

```python
class Account:
    rate = 0.01                         # CLASS attribute (shared)

    def __init__(self, owner, balance=0):
        self.owner = owner              # INSTANCE attributes
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("invalid amount")
        self.balance += amount
        return self.balance

    def __repr__(self):
        return f"Account({self.owner!r}, {self.balance})"

class SavingsAccount(Account):          # inheritance
    def deposit(self, amount):          # override
        return super().deposit(amount * (1 + self.rate))
```

The 4 pillars: **encapsulation**, **abstraction**, **inheritance** and **polymorphism**.

## 10. Mutability and references (trap #1)

```python
a = [1, 2, 3]
b = a            # b points to the SAME list
b.append(4)
print(a)         # [1, 2, 3, 4]  ← a changed too!

c = a.copy()     # shallow copy (also a[:] or list(a))
import copy
d = copy.deepcopy(matrix)   # deep copy (lists inside lists)

m = [[0] * 3] * 3   # ⚠️ 3 references to the SAME row
m[0][0] = 1         # [[1,0,0],[1,0,0],[1,0,0]]
m = [[0] * 3 for _ in range(3)]   # ✅ the right way
```

## 11. Quiz: what is the output?

This type of question is very common in multiple-choice tests. Answer them **without running the code**, then check.

```python
# Q1
print(type(7 / 7))

# Q2
x = [1, 2, 3]
y = x
y += [4]
print(len(x))

# Q3
print("data"[1:3] * 2)

# Q4
def f(a, lst=[]):
    lst.append(a)
    return lst
f(1)
print(f(2))

# Q5
print(bool([]) or 0 or "ok")

# Q6
d = {"a": 1, "b": 2}
d["a"] += d.get("c", 10)
print(d["a"])

# Q7
print([i * 2 for i in range(5) if i % 2 == 1])

# Q8
s = {3, 1, 3, 2, 1}
print(len(s))

# Q9
t = (1, 2, [3])
t[2].append(4)
print(t)

# Q10
print(-7 // 2, -7 % 2)

# Q11
nums = [3, 1, 2]
print(nums.sort())

# Q12
print(sorted(["banana", "Apple", "cherry"]))
```

<details>
<summary>Answers</summary>

| # | Output | Why |
|---|---|---|
| 1 | `<class 'float'>` | `/` always returns a float |
| 2 | `4` | `y` and `x` are the same list; `+=` on lists modifies in-place |
| 3 | `atat` | `"data"[1:3]` = `"at"`; `* 2` repeats it |
| 4 | `[1, 2]` | The mutable default argument is shared between calls |
| 5 | `ok` | `[]` and `0` are falsy; `or` returns the first truthy value |
| 6 | `11` | `get` returns 10 because "c" does not exist → 1 + 10 |
| 7 | `[2, 6]` | Odd `i`: 1 and 3 → 2 and 6 |
| 8 | `3` | The set removes duplicates: {1, 2, 3} |
| 9 | `(1, 2, [3, 4])` | The tuple is immutable, but the list inside it **can** be modified |
| 10 | `-4 1` | `//` rounds toward −∞; `-4 * 2 + 1 = -7` |
| 11 | `None` | `.sort()` sorts in-place and returns `None` |
| 12 | `['Apple', 'banana', 'cherry']` | Uppercase letters come before lowercase ones in Unicode order |

</details>

---

**Next:** solve [ejercicios.py](ejercicios.py), then go to [pandas.en.md](pandas.en.md).
