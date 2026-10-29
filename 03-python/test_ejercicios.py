"""Grader for ejercicios.py (no dependencies) / Corrector de ejercicios.py (sin dependencias: no necesitas pytest).

    python3 test_ejercicios.py              # grades your answers / corrige tus respuestas
    python3 test_ejercicios.py soluciones   # checks the reference solutions / verifica las soluciones de referencia
"""
import importlib
import sys

TESTS = {
    "is_even": [((4,), True), ((7,), False), ((0,), True), ((-2,), True)],
    "reverse_string": [(("data",), "atad"), (("",), ""), (("a",), "a")],
    "is_palindrome": [(("A man, a plan, a canal: Panama",), True), (("Data",), False),
                      (("",), True), (("No 'x' in Nixon",), True)],
    "count_vowels": [(("Blend360 Analytics",), 4), (("xyz",), 0), (("AEIOU aeiou",), 10)],
    "fizzbuzz": [((5,), ["1", "2", "Fizz", "4", "Buzz"]), ((0,), []),
                 ((15,), ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz",
                          "11", "Fizz", "13", "14", "FizzBuzz"])],
    "sum_digits": [((2024,), 8), ((0,), 0), ((9999,), 36)],
    "max_without_builtin": [(([3, 9, 2],), 9), (([],), None), (([-5, -2, -9],), -2)],
    "remove_duplicates": [(([3, 1, 3, 2, 1],), [3, 1, 2]), (([],), []), ((["b", "a", "b"],), ["b", "a"])],
    "word_frequency": [(("Data is good. DATA is power!",), {"data": 2, "is": 2, "good": 1, "power": 1}),
                       (("",), {})],
    "longest_word": [(("we love big data",), "love"), (("a bb cc",), "bb"), (("python",), "python")],
    "are_anagrams": [(("Listen", "Silent"), True), (("Dormitory", "dirty room"), True),
                     (("abc", "abd"), False), (("aab", "abb"), False)],
    "second_largest": [(([5, 9, 9, 7],), 7), (([4, 4],), None), (([],), None), (([-1, -3],), -3)],
    "flatten": [(([[1, 2], [3], []],), [1, 2, 3]), (([],), [])],
    "transpose": [(([[1, 2, 3], [4, 5, 6]],), [[1, 4], [2, 5], [3, 6]]), (([[7]],), [[7]])],
    "compress": [(("aaabccdd",), "a3b1c2d2"), (("",), ""), (("z",), "z1"), (("abab",), "a1b1a1b1")],
    "count_by": [(([{"city": "Cali"}, {"city": "Bogotá"}, {"city": "Cali"}], "city"),
                  {"Cali": 2, "Bogotá": 1}), (([], "x"), {})],
    "average_by": [(([{"d": "A", "s": 10}, {"d": "A", "s": 20}, {"d": "B", "s": 5}], "d", "s"),
                    {"A": 15.0, "B": 5.0}),
                   (([{"g": 1, "v": 1}, {"g": 1, "v": 2}, {"g": 1, "v": 2}], "g", "v"), {1: 1.67})],
    "top_n": [(({"ana": 90, "luis": 95, "bea": 90}, 2), ["luis", "ana"]),
              (({"x": 1}, 5), ["x"]), (({}, 3), [])],
    "filter_records": [(([{"v": 5}, {"v": None}, {}, {"v": 12}], "v", 6), [{"v": 12}]),
                       (([{"v": 6}], "v", 6), [])],
    "merge_sum": [(({"a": 1, "b": 2}, {"b": 3, "c": 4}), {"a": 1, "b": 5, "c": 4}),
                  (({}, {"x": 1}), {"x": 1})],
    "clean_numbers": [((["3", " 4.5 ", None, "abc", "", 7],), [3.0, 4.5, 7.0]), (([],), [])],
    "is_prime": [((13,), True), ((1,), False), ((2,), True), ((25,), False), ((97,), True), ((0,), False)],
    "primes_up_to": [((20,), [2, 3, 5, 7, 11, 13, 17, 19]), ((1,), []), ((2,), [2])],
    "factorial": [((5,), 120), ((0,), 1), ((1,), 1), ((10,), 3628800)],
    "fibonacci": [((7,), [0, 1, 1, 2, 3, 5, 8]), ((0,), []), ((1,), [0]), ((2,), [0, 1])],
}


def run(module_name):
    module = importlib.import_module(module_name)
    passed = pending = failed = 0
    for name, cases in TESTS.items():
        func = getattr(module, name)
        try:
            for args, expected in cases:
                got = func(*args)
                if got != expected:
                    raise AssertionError(f"{name}{args} → {got!r}, expected / se esperaba {expected!r}")
            _check_special(module, name)
        except NotImplementedError:
            pending += 1
            print(f"  · {name}: pending / pendiente")
            continue
        except Exception as exc:  # noqa: BLE001 - mostrar cualquier fallo al estudiante
            failed += 1
            print(f"  ✗ {name}: {exc}")
            continue
        passed += 1
        print(f"  ✓ {name}")
    total = len(TESTS)
    print(f"\n{module_name}.py → {passed}/{total} correct / correctos, {failed} failed / con errores, {pending} pending / pendientes")
    return failed == 0 and pending == 0


def _check_special(module, name):
    """Extra checks beyond input → output (also used by the simulator's Python lab)."""
    if name == "factorial":
        try:
            module.factorial(-1)
        except ValueError:
            return
        raise AssertionError("factorial(-1) should raise ValueError / debería lanzar ValueError")
    if name == "max_without_builtin":
        _check_no_builtin(module.max_without_builtin)


def _check_no_builtin(func):
    import builtins
    original_max, original_sorted = builtins.max, builtins.sorted

    def forbidden(*_a, **_k):
        raise AssertionError("max_without_builtin must not use max() or sorted() / no debe usar max() ni sorted()")

    builtins.max, builtins.sorted = forbidden, forbidden
    try:
        func([1, 5, 3])
    finally:
        builtins.max, builtins.sorted = original_max, original_sorted


if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "ejercicios"
    sys.exit(0 if run(target) else 1)
