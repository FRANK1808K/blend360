# Cheat sheet: algorithms and data structures (1 page)

[Español](algoritmos.md) · **English**

**Big O (best to worst):** O(1) < O(log n) < O(n) < O(n log n) < O(n²) < O(2ⁿ) < O(n!)
Sequential loops → **add**. Nested loops → **multiply**. Halving at each step → **log n**.

| Structure | Key | Operations | Python |
|---|---|---|---|
| List/array | Index | Access O(1), search O(n), insert in the middle O(n) | `list` |
| Stack | **LIFO** | push/pop O(1) | `list.append/pop` |
| Queue | **FIFO** | enqueue/dequeue O(1) | `deque.append/popleft` |
| Hash table | Key → value | Search/insert O(1) average | `dict`, `set` |
| Heap | Minimum on top | Peek min O(1), push/pop O(log n) | `heapq` |
| BST | Left < node < right | O(log n) balanced, O(n) worst case | — |
| Graph | Nodes + edges | BFS/DFS O(V + E) | `dict` of lists |

| Sorting | Average | Worst | Stable | Note |
|---|---|---|---|---|
| Bubble / Insertion | O(n²) | O(n²) | ✓ | O(n) if already sorted |
| Selection | O(n²) | O(n²) | ✗ | |
| **Merge** | O(n log n) | **O(n log n)** | ✓ | O(n) space |
| **Quick** | O(n log n) | **O(n²)** | ✗ | Bad pivot |
| Heap | O(n log n) | O(n log n) | ✗ | O(1) space |

**Binary search:** requires **sorted** data, O(log n): ~10 steps for 1,000 elements and ~20 for 1,000,000.

**Tree traversals:** in-order (L-N-R, comes out **sorted** in a BST) · pre-order (N-L-R) · post-order (L-R-N) · level order (BFS).

| Signal in the statement | Pattern |
|---|---|
| "pair that adds up", "has it appeared?", "frequency" | Hash map / set |
| Sorted array, pairs, palindrome | Two pointers |
| Longest **contiguous** substring/subarray | Sliding window |
| Parentheses, "the most recent" | Stack |
| Shortest path without weights | BFS + queue |
| Islands, components, explore everything | DFS |
| Top k | Heap / sort |
| "Number of ways", "minimum cost" | Dynamic programming |
| Range sums | Prefix sum |

**Recursion:** base case + recursive case. Memoization: Fibonacci from O(2ⁿ) to O(n).
**Edge case checklist:** empty · one element · duplicates · negatives/zero · already sorted · None · ties · off-by-one.
