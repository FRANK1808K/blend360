# 04 · Basic algorithms and data structures

[Español](README.md) · **English**

> The syllabus says **"skills in basic algorithms, data structures and problem solving"**. In 90-minute tests this usually shows up in two ways:
>
> 1. **Multiple choice:** "what is the complexity?", "which data structure would you use?", "what does this pseudocode return?".
> 2. **Coding problems** at *easy/medium* level (LeetCode/HackerRank style).
>
> This module covers both.

| File | Content |
|---|---|
| This README | Theory: Big O, data structures, algorithms, patterns, pseudocode tracing |
| [problemas.py](problemas.py) | 20 classic problems to solve (statements in English and Spanish) |
| [soluciones.py](soluciones.py) | Explained solutions, with their complexity |
| [test_problemas.py](test_problemas.py) | Grader: `python3 test_problemas.py` or `python3 test_problemas.py soluciones` |
| [Python lab](../simulator/README.en.md#code-lab) | The same 20 problems in the browser, with the same tests |

---

## 1. Complexity: Big O notation

Big O describes **how** the time (or memory) of an algorithm **grows** when the input size `n` grows. Keep the dominant term and ignore constants: `3n² + 5n + 2` → **O(n²)**.

| Big O | Name | Example | n = 1,000 → approx. operations |
|---|---|---|---|
| O(1) | Constant | Access `list[i]`, look up a dict/set | 1 |
| O(log n) | Logarithmic | Binary search | 10 |
| O(n) | Linear | Traverse a list once | 1,000 |
| O(n log n) | Linearithmic | Merge sort, `sorted()` | 10,000 |
| O(n²) | Quadratic | Two nested loops over n | 1,000,000 |
| O(2ⁿ) | Exponential | Naive recursive Fibonacci, all subsets | astronomical |
| O(n!) | Factorial | All permutations | astronomical |

**Quick rules to calculate it:**

- **Sequential** loops → add up: O(n) + O(n) = O(n).
- **Nested** loops → multiply: O(n) × O(n) = O(n²).
- If you **halve the problem** at each step → O(log n).
- Recursion → (number of calls) × (work per call).
- **Space:** the extra memory. Creating a new list of size n = O(n); using a few variables = O(1).

**What complexity does the test allow?** (about 10⁸ simple operations per second in C++; Python is ~10–50 times slower):

| Size of n | Maximum reasonable complexity |
|---|---|
| n ≤ 20 | O(2ⁿ) |
| n ≤ 1,000 | O(n²) |
| n ≤ 100,000 | O(n log n) |
| n ≤ 10,000,000 | O(n) |

## 2. Data structures

| Structure | Access | Search | Insert | Delete | In Python | Use it when… |
|---|---|---|---|---|---|---|
| **Array / list** | O(1) | O(n) | O(1) at the end, O(n) in the middle | O(n) | `list` | You need order and indexes |
| **Linked list** | O(n) | O(n) | O(1) if you have the node | O(1) if you have the node | (implemented with classes) | Many inserts/deletes in the middle |
| **Stack** — LIFO | O(1) top | — | O(1) `push` | O(1) `pop` | `list` (`append`/`pop`) | Undo, parentheses, recursion, DFS |
| **Queue** — FIFO | O(1) front | — | O(1) `enqueue` | O(1) `dequeue` | `collections.deque` | Turns, BFS, processing in order |
| **Hash table** | — | O(1) average | O(1) average | O(1) average | `dict`, `set` | Fast lookups, counts, "have I seen it?" |
| **Heap** | O(1) the minimum | O(n) | O(log n) | O(log n) the minimum | `heapq` | Top-k, priority, dynamic minimum |
| **Binary search tree (BST)** | — | O(log n) balanced / O(n) worst case | O(log n) | O(log n) | (classes) | Dynamic sorted data |
| **Graph** | — | BFS/DFS O(V + E) | — | — | dict of lists (adjacency list) | Networks, routes, relationships |

**Tree concepts that are asked:**

```text
        8          ← root
      /   \
     3     10      ← 3 and 10 are children of 8
    / \      \
   1   6      14   ← 1, 6 and 14 are leaves: they have no children
```

- **BST:** everything on the left < node < everything on the right.
- **Height:** number of levels (3 here).
- **Traversals:**
  - **In-order** (left, node, right) → `1 3 6 8 10 14`: in a BST it comes out **sorted**.
  - **Pre-order** (node, left, right) → `8 3 1 6 10 14`.
  - **Post-order** (left, right, node) → `1 6 3 14 10 8`.
  - **Level order** (BFS) → `8 3 10 1 6 14`.

**Stack vs. queue: a tracing example**

```text
Stack: push 1, push 2, push 3, pop, push 4, pop, pop  → out: 3, 4, 2
Queue: enqueue 1, enqueue 2, enqueue 3, dequeue, enqueue 4, dequeue → out: 1, 2
```

## 3. Searching algorithms

| Algorithm | Requirement | Complexity |
|---|---|---|
| Linear search | None | O(n) |
| Binary search | **Sorted** list | O(log n) |

```python
def binary_search(arr, target):
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            lo = mid + 1          # discard the left half
        else:
            hi = mid - 1          # discard the right half
    return -1
```

> At most how many comparisons does binary search need with 1,000 elements? ⌈log₂ 1000⌉ = **10**. With 1,000,000 → **20**.

## 4. Sorting algorithms

| Algorithm | Best | Average | Worst | Space | Stable | Idea |
|---|---|---|---|---|---|---|
| Bubble sort | O(n) | O(n²) | O(n²) | O(1) | ✓ | Swaps out-of-order neighbors; the largest "bubbles up" to the end |
| Selection sort | O(n²) | O(n²) | O(n²) | O(1) | ✗ | Finds the minimum and puts it at the start |
| Insertion sort | O(n) | O(n²) | O(n²) | O(1) | ✓ | Inserts each element in its place (like cards in your hand). Very good with almost-sorted data |
| Merge sort | O(n log n) | O(n log n) | O(n log n) | O(n) | ✓ | Splits in half, sorts each half and **merges** |
| Quick sort | O(n log n) | O(n log n) | O(n²) | O(log n) | ✗ | Picks a pivot, puts smaller elements on the left and larger ones on the right |
| Heap sort | O(n log n) | O(n log n) | O(n log n) | O(1) | ✗ | Uses a heap |
| Timsort (Python's `sorted()`) | O(n) | O(n log n) | O(n log n) | O(n) | ✓ | Hybrid of merge + insertion |

- **Stable:** keeps the relative order of equal elements.
- The lower bound for **comparison-based** sorting is O(n log n).
- Quick sort's worst case: the pivot is always the minimum or the maximum (e.g., the first element on already-sorted data).

**Tracing bubble sort** on `[5, 1, 4, 2]`:

```text
Pass 1: [1,5,4,2] → [1,4,5,2] → [1,4,2,5]   (5 reached the end)
Pass 2: [1,4,2,5] → [1,2,4,5]
Pass 3: no swaps → done
```

## 5. Recursion

Every recursive function needs:

1. A **base case** that stops it.
2. A **recursive case** that gets closer to the base case.

Without a base case → `RecursionError` (stack overflow). Python has a default limit of ~1,000 calls.

```python
def sum_list(nums):
    if not nums:                  # base case
        return 0
    return nums[0] + sum_list(nums[1:])   # recursive case
```

**Memoization:** storing results that were already computed. It turns Fibonacci from O(2ⁿ) into O(n):

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    return n if n < 2 else fib(n - 1) + fib(n - 2)
```

## 6. Patterns that solve 80 % of the problems

| If the problem says… | Think of… | Example |
|---|---|---|
| "Is there a pair that adds up to X?", "has it appeared?", "count frequencies" | **Hash map / set** | Two Sum, first non-repeated character |
| **Sorted** array, pairs, reverse, palindrome | **Two pointers** | Two Sum on a sorted array, remove duplicates |
| "Longest/shortest **contiguous** subarray/substring that…" | **Sliding window** | Longest substring without repeats |
| Sorted array + "search", "minimum that satisfies" | **Binary search** | Find an element, integer square root |
| Parentheses, "the most recent", undo | **Stack** | Balanced parentheses |
| Shortest path in an **unweighted** grid/graph | **BFS** (queue) | Maze |
| Explore everything, islands, connected components | **DFS** (recursion/stack) | Count islands |
| "The k largest/most frequent" | **Heap** or sort | Top-k frequent |
| "Number of ways", "minimum cost", repeated subproblems | **Dynamic programming** | Stairs, coin change |
| Choosing the locally best option works | **Greedy** | Max stock profit, intervals |
| Repeated range sums | **Prefix sum** | Sum of subarray i..j in O(1) |

### Code Blueprints for Key Patterns

In a timed 90-minute test, there is no time to reinvent the wheel. These are the exact mental templates to apply:

#### 1. Two Pointers — Sorted arrays or palindromes

```python
def two_pointers(arr, target):
    left, right = 0, len(arr) - 1
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1       # Sum too small → increment left
        else:
            right -= 1      # Sum too large → decrement right
    return []
```

#### 2. Dynamic Sliding Window — Contiguous substrings/subarrays

```python
def sliding_window(s):
    left = 0
    freq = {}
    max_len = 0

    for right in range(len(s)):
        # 1. Expand: include s[right]
        char = s[right]
        freq[char] = freq.get(char, 0) + 1

        # 2. Contract: while window violates condition (e.g. repeated characters)
        while freq[char] > 1:
            left_char = s[left]
            freq[left_char] -= 1
            left += 1

        # 3. Record best result for current valid window
        max_len = max(max_len, right - left + 1)

    return max_len
```

#### 3. Fast & Slow Pointers (Tortoise & Hare) — Cycle detection

```python
def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next         # Moves 1 step
        fast = fast.next.next    # Moves 2 steps
        if slow == fast:
            return True          # Pointers met → cycle detected
    return False
```

#### 4. BFS (Queue) vs DFS (Recursion/Stack)

| Criterion | BFS (Breadth-First Search) | DFS (Depth-First Search) |
|---|---|---|
| **Data structure** | **Queue (`collections.deque`)** | **Stack** or call stack (recursion) |
| **Exploration** | Level by level (expanding ring) | As deep as possible before backtracking |
| **Guarantee** | **Shortest path** in unweighted graphs/grids | Does not guarantee shortest path |
| **Typical use** | Shortest distance, mazes, minimum moves | Counting islands, finding all paths, permutations |

```python
from collections import deque

def bfs_shortest_path(start, target, get_neighbors):
    visited = {start}
    queue = deque([(start, 0)])   # (current_node, distance)
    while queue:
        node, dist = queue.popleft()
        if node == target:
            return dist
        for neighbor in get_neighbors(node):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, dist + 1))
    return -1
```

## 7. Pseudocode tracing (very common in multiple choice)

Practice "being the computer": make a table with each variable and update it line by line.

```text
function mystery(n):
    result ← 0
    while n > 0:
        result ← result * 10 + (n mod 10)
        n ← n div 10
    return result

mystery(1230) = ?
```

| Iteration | n mod 10 | result | n |
|---|---|---|---|
| start | — | 0 | 1230 |
| 1 | 0 | 0 | 123 |
| 2 | 3 | 3 | 12 |
| 3 | 2 | 32 | 1 |
| 4 | 1 | 321 | 0 |

**Answer: 321** (it reverses the digits; the trailing 0 is lost).

### Your turn

```text
A) x ← 1
   for i from 1 to 4:
       x ← x * i
   print x

B) a ← [3, 8, 1, 9, 4]
   m ← a[0]
   for each v in a:
       if v < m: m ← v
   print m

C) counter ← 0
   for i from 1 to n:
       for j from 1 to n:
           counter ← counter + 1
   Final value of counter and complexity?

D) function f(n):
       if n ≤ 1: return 1
       return f(n - 1) + f(n - 2)
   f(5) = ?

E) i ← 1
   while i < n:
       i ← i * 2
   Complexity?
```

<details>
<summary>Answers</summary>

- **A)** `24` (it calculates 4! = 1·2·3·4).
- **B)** `1` (it is the minimum).
- **C)** `n²` iterations → **O(n²)**.
- **D)** f(0)=1, f(1)=1, f(2)=2, f(3)=3, f(4)=5, f(5)=**8**. Complexity O(2ⁿ) without memoization.
- **E)** `i` doubles at each step → **O(log n)**.

</details>

## 8. Quick conceptual questions

<details>
<summary>1. Why is searching a <code>set</code> faster than searching a <code>list</code>?</summary>

A `set` uses a hash table: it computes the hash of the value and goes straight to its "slot", in O(1) on average. A list has to check element by element, in O(n).

</details>

<details>
<summary>2. Which data structure would you use to implement an "Undo" button?</summary>

A **stack** (LIFO): the last action performed is the first one undone.

</details>

<details>
<summary>3. Which data structure would you use to handle requests in arrival order?</summary>

A **queue** (FIFO).

</details>

<details>
<summary>4. What is a collision in a hash table?</summary>

When two different keys produce the same index (hash). It is solved with *chaining* (a list in each slot) or *open addressing* (finding another free slot). With many collisions, lookups degrade toward O(n).

</details>

<details>
<summary>5. When is a linked list better than an array?</summary>

When you insert or delete many elements at the beginning or in the middle and you do not need index access. The array has to shift elements (O(n)); the linked list only reconnects pointers (O(1), if you already have the node).

</details>

<details>
<summary>6. Difference between BFS and DFS</summary>

**BFS** (breadth-first) explores level by level using a **queue** and finds the shortest path in unweighted graphs. **DFS** (depth-first) goes as deep as possible before backtracking, using a **stack** or recursion; it is used to explore components, detect cycles and do backtracking. Both are O(V + E).

</details>

---

**Next:** solve [problemas.py](problemas.py), then study [07 · Problem solving](../07-resolucion-de-problemas/README.en.md).
