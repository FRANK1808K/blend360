"""25 technical-test-style Python exercises / 25 ejercicios de Python tipo prueba técnica.

Instructions:
  1. Replace each `raise NotImplementedError` with your implementation.
  2. Run `python3 test_ejercicios.py` to grade yourself.
  3. Try to solve each one in 5 minutes or less (the real test gives you no more time).
  4. Only then look at soluciones.py.

Instrucciones:
  1. Reemplaza cada `raise NotImplementedError` por tu implementación.
  2. Ejecuta `python3 test_ejercicios.py` para corregirte.
  3. Intenta resolver cada uno en 5 minutos o menos (en la prueba real no hay más tiempo).
  4. Solo después mira soluciones.py.

Each statement is in English (like the test), followed by a short Spanish translation.
Cada enunciado está en inglés (como en la prueba), seguido de una traducción corta.
"""


# ---------------------------------------------------------------- Basics / Básicos

def is_even(n):
    """Return True if n is even, False otherwise.
    Devuelve True si n es par.
    >>> is_even(4)
    True
    """
    raise NotImplementedError


def reverse_string(s):
    """Return the string reversed.  Invierte el texto.
    >>> reverse_string("data")
    'atad'
    """
    raise NotImplementedError


def is_palindrome(s):
    """Return True if s reads the same backwards, ignoring case, spaces and
    punctuation (keep only letters and digits).
    Palíndromo ignorando mayúsculas, espacios y signos.
    >>> is_palindrome("A man, a plan, a canal: Panama")
    True
    """
    raise NotImplementedError


def count_vowels(s):
    """Count the vowels (a, e, i, o, u; upper or lower case) in s.
    Cuenta las vocales (sin tildes).
    >>> count_vowels("Blend360 Analytics")
    4
    """
    raise NotImplementedError


def fizzbuzz(n):
    """Return a list of strings for numbers 1..n: "Fizz" for multiples of 3,
    "Buzz" for multiples of 5, "FizzBuzz" for multiples of both, otherwise the number.
    >>> fizzbuzz(5)
    ['1', '2', 'Fizz', '4', 'Buzz']
    """
    raise NotImplementedError


def sum_digits(n):
    """Return the sum of the digits of a non-negative integer.
    Suma de los dígitos.
    >>> sum_digits(2024)
    8
    """
    raise NotImplementedError


def max_without_builtin(nums):
    """Return the largest number WITHOUT using max() or sorted().
    Return None if the list is empty.
    El mayor de la lista sin usar max() ni sorted(); None si está vacía.
    >>> max_without_builtin([3, 9, 2])
    9
    """
    raise NotImplementedError


# ---------------------------------------------------------------- Lists and strings / Listas y strings

def remove_duplicates(items):
    """Remove duplicates keeping the ORIGINAL order of first appearance.
    Quita duplicados conservando el orden original.
    >>> remove_duplicates([3, 1, 3, 2, 1])
    [3, 1, 2]
    """
    raise NotImplementedError


def word_frequency(text):
    """Return a dict {word: count}. Words are case-insensitive and the
    characters . , ! ? must be ignored.
    Frecuencia de palabras (sin distinguir mayúsculas, ignorando . , ! ?).
    >>> word_frequency("Data is good. DATA is power!")
    {'data': 2, 'is': 2, 'good': 1, 'power': 1}
    """
    raise NotImplementedError


def longest_word(text):
    """Return the longest word in the text. If there is a tie, return the
    first one. Palabra más larga (en empate, la primera).
    >>> longest_word("we love big data")
    'love'
    """
    raise NotImplementedError


def are_anagrams(a, b):
    """Return True if a and b are anagrams (ignore case and spaces).
    ¿Son anagramas? (ignorando mayúsculas y espacios)
    >>> are_anagrams("Listen", "Silent")
    True
    """
    raise NotImplementedError


def second_largest(nums):
    """Return the second largest DISTINCT value, or None if it does not exist.
    Segundo valor más grande (distinto); None si no existe.
    >>> second_largest([5, 9, 9, 7])
    7
    """
    raise NotImplementedError


def flatten(list_of_lists):
    """Flatten ONE level of nesting.  Aplana un nivel.
    >>> flatten([[1, 2], [3], []])
    [1, 2, 3]
    """
    raise NotImplementedError


def transpose(matrix):
    """Return the transpose of a rectangular matrix (list of rows).
    Traspuesta de una matriz.
    >>> transpose([[1, 2, 3], [4, 5, 6]])
    [[1, 4], [2, 5], [3, 6]]
    """
    raise NotImplementedError


def compress(s):
    """Run-length encoding: each character followed by how many times it
    repeats consecutively.  Compresión por repeticiones consecutivas.
    >>> compress("aaabccdd")
    'a3b1c2d2'
    """
    raise NotImplementedError


# ---------------------------------------------------------------- Data (analysis style) / Datos (estilo análisis)

def count_by(records, key):
    """Given a list of dicts, count how many records there are for each value
    of `key`.  Cuenta registros por el valor de una clave (como un GROUP BY + COUNT).
    >>> count_by([{"city": "Cali"}, {"city": "Bogotá"}, {"city": "Cali"}], "city")
    {'Cali': 2, 'Bogotá': 1}
    """
    raise NotImplementedError


def average_by(records, group_key, value_key):
    """Return {group: average of value_key}, rounded to 2 decimals.
    Promedio por grupo (GROUP BY + AVG), redondeado a 2 decimales.
    >>> average_by([{"d": "A", "s": 10}, {"d": "A", "s": 20}, {"d": "B", "s": 5}], "d", "s")
    {'A': 15.0, 'B': 5.0}
    """
    raise NotImplementedError


def top_n(scores, n):
    """Given {name: score}, return the list of the n names with the highest
    score. Ties are broken alphabetically by name.
    Los n nombres con mayor puntaje; los empates se ordenan alfabéticamente.
    >>> top_n({"ana": 90, "luis": 95, "bea": 90}, 2)
    ['luis', 'ana']
    """
    raise NotImplementedError


def filter_records(records, field, threshold):
    """Return the records whose `field` is strictly greater than threshold.
    Records where the field is missing or None must be skipped.
    Registros cuyo campo es mayor que el umbral (ignora los que no lo tienen o es None).
    >>> filter_records([{"v": 5}, {"v": None}, {}, {"v": 12}], "v", 6)
    [{'v': 12}]
    """
    raise NotImplementedError


def merge_sum(d1, d2):
    """Merge two dicts adding the values of common keys.
    Fusiona dos diccionarios sumando los valores de las claves comunes.
    >>> merge_sum({"a": 1, "b": 2}, {"b": 3, "c": 4})
    {'a': 1, 'b': 5, 'c': 4}
    """
    raise NotImplementedError


def clean_numbers(values):
    """Convert a messy list to floats. Skip None, empty strings and values
    that cannot be converted. Strings may contain surrounding spaces.
    Limpia una lista "sucia" y devuelve solo los números como float.
    >>> clean_numbers(["3", " 4.5 ", None, "abc", "", 7])
    [3.0, 4.5, 7.0]
    """
    raise NotImplementedError


# ---------------------------------------------------------------- Math and recursion / Matemática y recursión

def is_prime(n):
    """Return True if n is a prime number.  ¿Es primo?
    >>> is_prime(13)
    True
    """
    raise NotImplementedError


def primes_up_to(n):
    """Return all primes <= n (tip: Sieve of Eratosthenes).
    Todos los primos hasta n (criba de Eratóstenes).
    >>> primes_up_to(20)
    [2, 3, 5, 7, 11, 13, 17, 19]
    """
    raise NotImplementedError


def factorial(n):
    """Return n! using RECURSION. Raise ValueError if n < 0.
    Factorial recursivo; ValueError si n es negativo.
    >>> factorial(5)
    120
    """
    raise NotImplementedError


def fibonacci(n):
    """Return a list with the first n Fibonacci numbers, starting 0, 1.
    Los primeros n números de Fibonacci.
    >>> fibonacci(7)
    [0, 1, 1, 2, 3, 5, 8]
    """
    raise NotImplementedError
