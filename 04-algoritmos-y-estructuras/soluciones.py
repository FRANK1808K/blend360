"""Solutions for problemas.py, with the key idea and the complexity of each one.
Soluciones de problemas.py, con la idea clave y la complejidad de cada una.
"""
from collections import Counter, defaultdict, deque


class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


# ------------------------------------------------------------ Hash map / arrays

def two_sum(nums, target):
    # Idea: for each x, have I already seen its complement (target - x)? → dict value→index.
    # Idea: para cada x, ¿ya vi su complemento (target - x)? → dict valor→índice.
    # Time O(n), space O(n). (Brute force with two loops is O(n²).)
    seen = {}
    for i, x in enumerate(nums):
        if target - x in seen:
            return [seen[target - x], i]
        seen[x] = i
    return []


def first_unique_char(s):
    # Two passes: count, then find the first with count 1. O(n).
    # Dos pasadas: contar y luego buscar el primero con conteo 1. O(n).
    counts = Counter(s)
    for i, ch in enumerate(s):
        if counts[ch] == 1:
            return i
    return -1


def missing_number(nums):
    # Expected sum of 0..n minus the real sum (Gauss's formula). O(n), O(1) space.
    # Suma esperada de 0..n menos la suma real (fórmula de Gauss). O(n), espacio O(1).
    n = len(nums)
    return n * (n + 1) // 2 - sum(nums)


def move_zeros(nums):
    # Two pointers: "write" marks where the next non-zero goes. O(n).
    # Dos punteros: "write" marca dónde va el siguiente no-cero. O(n).
    result = list(nums)
    write = 0
    for x in result[:]:
        if x != 0:
            result[write] = x
            write += 1
    for i in range(write, len(result)):
        result[i] = 0
    return result


def rotate_right(nums, k):
    # k % n avoids useless rotations (rotating n times = not rotating). O(n).
    # k % n evita rotaciones innecesarias (rotar n veces = no rotar). O(n).
    if not nums:
        return []
    k %= len(nums)
    return nums[-k:] + nums[:-k] if k else list(nums)


def max_profit(prices):
    # Greedy: remember the minimum price so far and the best profit so far. O(n).
    # Greedy: recuerda el precio mínimo visto y la mejor ganancia hasta ahora. O(n).
    min_price = float("inf")
    best = 0
    for p in prices:
        min_price = min(min_price, p)
        best = max(best, p - min_price)
    return best


# ------------------------------------------------------------ Stack / search / sorting — Pila / búsqueda / ordenamiento

def valid_parentheses(s):
    # Stack: each closing bracket must match the last pending opening one. O(n).
    # Pila: cada cierre debe coincidir con la última apertura pendiente. O(n).
    pairs = {")": "(", "]": "[", "}": "{"}
    stack = []
    for ch in s:
        if ch in "([{":
            stack.append(ch)
        elif ch in pairs:
            if not stack or stack.pop() != pairs[ch]:
                return False
    return not stack            # unclosed openings left → False / aperturas sin cerrar → False


def binary_search(arr, target):
    lo, hi = 0, len(arr) - 1
    while lo <= hi:             # O(log n)
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1


def bubble_sort(nums):
    arr = list(nums)            # copy: do not modify the input / copia: no modificar la entrada
    n = len(arr)
    for i in range(n - 1):      # O(n²) worst case, O(n) if already sorted / O(n) si ya está ordenada
        swapped = False
        for j in range(n - 1 - i):          # the last i are already in place / los últimos i ya están en su lugar
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


def merge_sorted(a, b):
    i = j = 0
    result = []
    while i < len(a) and j < len(b):        # O(n + m)
        if a[i] <= b[j]:                    # "<=" keeps it stable / mantiene la estabilidad
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    result.extend(a[i:])                    # whatever is left in either list / lo que sobre de cualquiera
    result.extend(b[j:])
    return result


class MinStack:
    # Trick: store, next to each value, the minimum up to that point.
    # Truco: guardar junto a cada valor el mínimo que había hasta ese punto.
    def __init__(self):
        self._stack = []        # pairs (value, min_so_far) / pares (valor, mínimo_hasta_aquí)

    def push(self, x):
        current_min = min(x, self._stack[-1][1]) if self._stack else x
        self._stack.append((x, current_min))

    def pop(self):
        return self._stack.pop()[0]

    def top(self):
        return self._stack[-1][0]

    def get_min(self):
        return self._stack[-1][1]


def reverse_linked_list(head):
    # Three pointers: prev, current, next. O(n) time, O(1) space.
    # Tres punteros: prev, current, next. O(n) tiempo, O(1) espacio.
    prev = None
    current = head
    while current:
        nxt = current.next      # save the next node before breaking the link / guardar el siguiente antes de romper el enlace
        current.next = prev     # reverse the link / invertir el enlace
        prev = current
        current = nxt
    return prev


# ------------------------------------------------------------ Patterns / Patrones

def merge_sort(nums):
    # Divide and conquer: always O(n log n), O(n) space. / Divide y vencerás.
    if len(nums) <= 1:
        return list(nums)
    mid = len(nums) // 2
    return merge_sorted(merge_sort(nums[:mid]), merge_sort(nums[mid:]))


def max_subarray_sum(nums):
    # Kadane: at each position, is it better to extend the subarray or to start again? O(n).
    # Kadane: en cada posición, ¿conviene extender el subarreglo o empezar de nuevo? O(n).
    best = current = nums[0]
    for x in nums[1:]:
        current = max(x, current + x)
        best = max(best, current)
    return best


def longest_unique_substring(s):
    # Sliding window [left, i]; last_seen stores the last position of each character. O(n).
    # Ventana deslizante [left, i]; last_seen guarda la última posición de cada carácter. O(n).
    last_seen = {}
    left = best = 0
    for i, ch in enumerate(s):
        if ch in last_seen and last_seen[ch] >= left:
            left = last_seen[ch] + 1            # move the window start past the repeat / mover el inicio tras el repetido
        last_seen[ch] = i
        best = max(best, i - left + 1)
    return best


def group_anagrams(words):
    # Key = the word with its letters sorted: anagrams share the key.
    # Clave = la palabra con sus letras ordenadas: los anagramas comparten la clave.
    groups = defaultdict(list)
    for w in words:
        groups["".join(sorted(w))].append(w)
    return sorted(sorted(g) for g in groups.values())


def top_k_frequent(nums, k):
    counts = Counter(nums)
    ordered = sorted(counts, key=lambda x: (-counts[x], x))   # O(n log n); with a heap: O(n log k)
    return ordered[:k]


def climb_stairs(n):
    # To reach n you come from n-1 or n-2 → ways(n) = ways(n-1) + ways(n-2) (it is Fibonacci!).
    # Para llegar a n vienes de n-1 o de n-2 → ways(n) = ways(n-1) + ways(n-2) (¡es Fibonacci!).
    a, b = 1, 1                 # ways to reach steps 0 and 1 / formas de llegar a los escalones 0 y 1
    for _ in range(n - 1):
        a, b = b, a + b
    return b if n >= 1 else 1


def count_islands(grid):
    # DFS: when you find unvisited land, count one island and "sink" the whole island. O(rows × cols).
    # DFS: al encontrar tierra no visitada, cuenta una isla y "hunde" toda la isla. O(filas × columnas).
    if not grid:
        return 0
    rows, cols = len(grid), len(grid[0])
    seen = set()

    def sink(r, c):
        stack = [(r, c)]        # iterative DFS (avoids the recursion limit) / DFS iterativo (evita el límite de recursión)
        while stack:
            r, c = stack.pop()
            if (r, c) in seen or not (0 <= r < rows and 0 <= c < cols) or grid[r][c] != "1":
                continue
            seen.add((r, c))
            stack.extend([(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)])

    islands = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1" and (r, c) not in seen:
                islands += 1
                sink(r, c)
    return islands


def shortest_path(grid):
    # BFS explores level by level, so the first time it reaches the target is via the shortest path.
    # BFS explora por niveles: la primera vez que llega al destino es por el camino más corto.
    rows, cols = len(grid), len(grid[0])
    if grid[0][0] == "#" or grid[rows - 1][cols - 1] == "#":
        return -1
    queue = deque([(0, 0, 0)])  # (row, col, distance) / (fila, columna, distancia)
    seen = {(0, 0)}
    while queue:
        r, c, dist = queue.popleft()
        if (r, c) == (rows - 1, cols - 1):
            return dist
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "." and (nr, nc) not in seen:
                seen.add((nr, nc))
                queue.append((nr, nc, dist + 1))
    return -1
