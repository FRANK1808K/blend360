"""Soluciones de referencia de ejercicios.py (con la complejidad de cada una).

Hay muchas soluciones correctas; estas priorizan claridad + eficiencia razonable,
que es lo que se valora en una prueba técnica.
"""
from collections import Counter, defaultdict


# ---------------------------------------------------------------- Básicos

def is_even(n):
    return n % 2 == 0                                    # O(1)


def reverse_string(s):
    return s[::-1]                                       # O(n)


def is_palindrome(s):
    cleaned = [c.lower() for c in s if c.isalnum()]      # O(n)
    return cleaned == cleaned[::-1]


def count_vowels(s):
    return sum(1 for c in s.lower() if c in "aeiou")     # O(n)


def fizzbuzz(n):
    result = []
    for i in range(1, n + 1):
        if i % 15 == 0:                                  # primero el caso más específico
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return result


def sum_digits(n):
    total = 0
    while n > 0:                                         # O(número de dígitos)
        total += n % 10                                  # último dígito
        n //= 10                                         # quitar el último dígito
    return total
    # alternativa en una línea: sum(int(d) for d in str(n))


def max_without_builtin(nums):
    if not nums:
        return None
    best = nums[0]
    for x in nums[1:]:                                   # O(n)
        if x > best:
            best = x
    return best


# ---------------------------------------------------------------- Listas y strings

def remove_duplicates(items):
    seen = set()                                         # set → búsqueda O(1)
    result = []
    for x in items:
        if x not in seen:
            seen.add(x)
            result.append(x)
    return result                                        # O(n)
    # alternativa: list(dict.fromkeys(items))


def word_frequency(text):
    for ch in ".,!?":
        text = text.replace(ch, "")
    return dict(Counter(text.lower().split()))           # O(n)


def longest_word(text):
    best = ""
    for word in text.split():
        if len(word) > len(best):                        # ">" estricto → en empate se queda la primera
            best = word
    return best
    # alternativa: max(text.split(), key=len)  (max también devuelve la primera en empate)


def are_anagrams(a, b):
    clean = lambda s: s.replace(" ", "").lower()
    return Counter(clean(a)) == Counter(clean(b))        # O(n); con sorted() sería O(n log n)


def second_largest(nums):
    first = second = None
    for x in set(nums):                                  # O(n), una sola pasada
        if first is None or x > first:
            first, second = x, first
        elif second is None or x > second:
            second = x
    return second


def flatten(list_of_lists):
    return [x for sub in list_of_lists for x in sub]


def transpose(matrix):
    return [list(col) for col in zip(*matrix)]           # zip(*m) agrupa por columnas


def compress(s):
    if not s:
        return ""
    parts = []
    current, count = s[0], 1
    for ch in s[1:]:
        if ch == current:
            count += 1
        else:
            parts.append(f"{current}{count}")
            current, count = ch, 1
    parts.append(f"{current}{count}")                    # no olvidar el último grupo
    return "".join(parts)                                # join es O(n); concatenar con + en bucle es peor


# ---------------------------------------------------------------- Datos (estilo análisis)

def count_by(records, key):
    counts = {}
    for r in records:
        counts[r[key]] = counts.get(r[key], 0) + 1
    return counts


def average_by(records, group_key, value_key):
    sums = defaultdict(float)
    counts = defaultdict(int)
    for r in records:
        sums[r[group_key]] += r[value_key]
        counts[r[group_key]] += 1
    return {g: round(sums[g] / counts[g], 2) for g in sums}


def top_n(scores, n):
    ordered = sorted(scores.items(), key=lambda kv: (-kv[1], kv[0]))  # valor desc, nombre asc
    return [name for name, _ in ordered[:n]]


def filter_records(records, field, threshold):
    return [r for r in records if r.get(field) is not None and r[field] > threshold]


def merge_sum(d1, d2):
    result = dict(d1)                                    # copia: no modificar la entrada
    for k, v in d2.items():
        result[k] = result.get(k, 0) + v
    return result


def clean_numbers(values):
    result = []
    for v in values:
        if v is None:
            continue
        try:
            result.append(float(str(v).strip()))
        except ValueError:                               # "abc" y "" lanzan ValueError
            continue
    return result


# ---------------------------------------------------------------- Matemática y recursión

def is_prime(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:                                    # basta probar hasta √n → O(√n)
        if n % i == 0:
            return False
        i += 1
    return True


def primes_up_to(n):
    if n < 2:
        return []
    is_p = [True] * (n + 1)
    is_p[0] = is_p[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if is_p[i]:
            for multiple in range(i * i, n + 1, i):      # tachar múltiplos
                is_p[multiple] = False
    return [i for i, p in enumerate(is_p) if p]          # O(n log log n)


def factorial(n):
    if n < 0:
        raise ValueError("n must be non-negative")
    if n <= 1:                                           # caso base
        return 1
    return n * factorial(n - 1)                          # caso recursivo


def fibonacci(n):
    seq = []
    a, b = 0, 1
    for _ in range(n):                                   # iterativo O(n); el recursivo ingenuo es O(2^n)
        seq.append(a)
        a, b = b, a + b
    return seq
