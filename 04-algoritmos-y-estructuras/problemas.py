"""20 classic algorithm and data structure problems.
20 problemas clásicos de algoritmos y estructuras de datos.

Replace each `raise NotImplementedError` and run:  python3 test_problemas.py
Goal: 🟢 problems in ≤ 10 min, 🟡 problems in ≤ 20 min. When you finish, say the
complexity of your solution out loud in English: "Time complexity is O(n), space is O(1)".

Reemplaza cada `raise NotImplementedError` y corre:  python3 test_problemas.py
Meta: los 🟢 en ≤ 10 min, los 🟡 en ≤ 20 min. Al terminar, di en voz alta (¡en inglés!)
la complejidad de tu solución: "Time complexity is O(n), space is O(1)".
"""


class ListNode:
    """Singly linked list node / Nodo de lista enlazada simple."""

    def __init__(self, val, next=None):
        self.val = val
        self.next = next


# ------------------------------------------------------------ 🟢 Hash map / arrays

def two_sum(nums, target):
    """🟢 Return the indices [i, j] (i < j) of the two numbers that add up to
    target, or [] if none. Each input has at most one solution.
    Índices de los dos números que suman target.
    >>> two_sum([2, 7, 11, 15], 9)
    [0, 1]
    """
    raise NotImplementedError


def first_unique_char(s):
    """🟢 Return the index of the first non-repeating character, or -1.
    Índice del primer carácter que no se repite.
    >>> first_unique_char("blendblend360")
    10
    """
    raise NotImplementedError


def missing_number(nums):
    """🟢 nums contains n distinct numbers from the range [0, n]. Return the
    one that is missing.  Falta un número del rango 0..n.
    >>> missing_number([3, 0, 1])
    2
    """
    raise NotImplementedError


def move_zeros(nums):
    """🟢 Return a list with all the zeros moved to the end, keeping the
    relative order of the non-zero elements.
    Mueve los ceros al final conservando el orden de los demás.
    >>> move_zeros([0, 1, 0, 3, 12])
    [1, 3, 12, 0, 0]
    """
    raise NotImplementedError


def rotate_right(nums, k):
    """🟢 Rotate the list to the right by k steps (k may be larger than len).
    Rota la lista k posiciones a la derecha.
    >>> rotate_right([1, 2, 3, 4, 5], 2)
    [4, 5, 1, 2, 3]
    """
    raise NotImplementedError


def max_profit(prices):
    """🟢 prices[i] is a stock price on day i. Buy once and sell once later.
    Return the maximum profit (0 if no profit is possible).
    Máxima ganancia comprando un día y vendiendo un día posterior.
    >>> max_profit([7, 1, 5, 3, 6, 4])
    5
    """
    raise NotImplementedError


# ------------------------------------------------------------ 🟢 Stack / search / sorting — Pila / búsqueda / ordenamiento

def valid_parentheses(s):
    """🟢 Return True if every bracket ()[]{} is closed in the correct order.
    ¿Paréntesis balanceados?
    >>> valid_parentheses("([]{})")
    True
    """
    raise NotImplementedError


def binary_search(arr, target):
    """🟢 arr is sorted ascending. Return the index of target or -1. Must be O(log n).
    Búsqueda binaria.
    >>> binary_search([1, 3, 5, 7, 9], 7)
    3
    """
    raise NotImplementedError


def bubble_sort(nums):
    """🟢 Return a NEW sorted list implementing bubble sort (no sorted()/sort()).
    Implementa bubble sort sin modificar la lista original.
    >>> bubble_sort([5, 1, 4, 2])
    [1, 2, 4, 5]
    """
    raise NotImplementedError


def merge_sorted(a, b):
    """🟢 Merge two sorted lists into one sorted list in O(n + m).
    Mezcla dos listas ordenadas (el paso clave de merge sort).
    >>> merge_sorted([1, 4, 9], [2, 3, 10])
    [1, 2, 3, 4, 9, 10]
    """
    raise NotImplementedError


class MinStack:
    """🟡 Stack that supports push, pop, top and get_min, ALL in O(1).
    Pila que devuelve su mínimo en O(1).
    """

    def __init__(self):
        raise NotImplementedError

    def push(self, x):
        raise NotImplementedError

    def pop(self):
        raise NotImplementedError

    def top(self):
        raise NotImplementedError

    def get_min(self):
        raise NotImplementedError


def reverse_linked_list(head):
    """🟡 Reverse a singly linked list and return the new head.
    Invierte una lista enlazada.
    1 -> 2 -> 3   =>   3 -> 2 -> 1
    """
    raise NotImplementedError


# ------------------------------------------------------------ 🟡 Patterns / Patrones

def merge_sort(nums):
    """🟡 Return a NEW sorted list using merge sort (divide and conquer).
    Implementa merge sort.
    >>> merge_sort([38, 27, 43, 3, 9, 82, 10])
    [3, 9, 10, 27, 38, 43, 82]
    """
    raise NotImplementedError


def max_subarray_sum(nums):
    """🟡 Return the largest sum of a contiguous, non-empty subarray (Kadane).
    Mayor suma de un subarreglo contiguo.
    >>> max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4])
    6
    """
    raise NotImplementedError


def longest_unique_substring(s):
    """🟡 Return the LENGTH of the longest substring without repeating
    characters (sliding window).
    Longitud del substring más largo sin caracteres repetidos.
    >>> longest_unique_substring("abcabcbb")
    3
    """
    raise NotImplementedError


def group_anagrams(words):
    """🟡 Group words that are anagrams. Return a list of groups where each
    group is sorted alphabetically and the groups are sorted by their first word.
    Agrupa anagramas.
    >>> group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    [['ate', 'eat', 'tea'], ['bat'], ['nat', 'tan']]
    """
    raise NotImplementedError


def top_k_frequent(nums, k):
    """🟡 Return the k most frequent elements, most frequent first. Ties are
    broken by the smaller value first.
    Los k elementos más frecuentes.
    >>> top_k_frequent([1, 1, 1, 2, 2, 3], 2)
    [1, 2]
    """
    raise NotImplementedError


def climb_stairs(n):
    """🟡 You can climb 1 or 2 steps at a time. In how many distinct ways can
    you reach step n? (dynamic programming)
    ¿De cuántas formas subes n escalones dando pasos de 1 o 2?
    >>> climb_stairs(4)
    5
    """
    raise NotImplementedError


def count_islands(grid):
    """🟡 grid is a list of strings of '1' (land) and '0' (water). Count the
    islands (groups of '1' connected horizontally or vertically). DFS/BFS.
    Cuenta las islas.
    >>> count_islands(["110", "010", "001"])
    2
    """
    raise NotImplementedError


def shortest_path(grid):
    """🟡 grid is a list of strings: '.' = open cell, '#' = wall. Return the
    minimum number of moves (up/down/left/right) from the top-left to the
    bottom-right cell, or -1 if impossible. BFS.
    Camino más corto en un laberinto.
    >>> shortest_path(["..#", "#..", "..."])
    4
    """
    raise NotImplementedError
