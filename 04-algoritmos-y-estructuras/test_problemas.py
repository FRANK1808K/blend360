"""Grader for problemas.py (no dependencies) / Corrector de problemas.py (sin dependencias).

    python3 test_problemas.py              # grades your answers / corrige tus respuestas
    python3 test_problemas.py soluciones   # checks the reference solutions / verifica las soluciones de referencia
"""
import importlib
import random
import sys

CASES = {
    "two_sum": [(([2, 7, 11, 15], 9), [0, 1]), (([3, 2, 4], 6), [1, 2]), (([3, 3], 6), [0, 1]),
                (([1, 2], 7), [])],
    "first_unique_char": [(("blendblend360",), 10), (("aabb",), -1), (("x",), 0)],
    "missing_number": [(([3, 0, 1],), 2), (([0, 1],), 2), (([1],), 0)],
    "move_zeros": [(([0, 1, 0, 3, 12],), [1, 3, 12, 0, 0]), (([0],), [0]), (([1, 2],), [1, 2])],
    "rotate_right": [(([1, 2, 3, 4, 5], 2), [4, 5, 1, 2, 3]), (([1, 2], 5), [2, 1]),
                     (([1, 2, 3], 0), [1, 2, 3]), (([], 3), [])],
    "max_profit": [(([7, 1, 5, 3, 6, 4],), 5), (([7, 6, 4, 3, 1],), 0), (([2, 4, 1, 7],), 6)],
    "valid_parentheses": [(("([]{})",), True), (("(]",), False), (("((",), False), ((")",), False),
                          (("",), True), (("{[()()]}",), True)],
    "binary_search": [(([1, 3, 5, 7, 9], 7), 3), (([1, 3, 5, 7, 9], 4), -1), (([], 1), -1),
                      (([5], 5), 0)],
    "bubble_sort": [(([5, 1, 4, 2],), [1, 2, 4, 5]), (([],), []), (([3, 3, 1],), [1, 3, 3])],
    "merge_sorted": [(([1, 4, 9], [2, 3, 10]), [1, 2, 3, 4, 9, 10]), (([], [1]), [1]), (([], []), [])],
    "merge_sort": [(([38, 27, 43, 3, 9, 82, 10],), [3, 9, 10, 27, 38, 43, 82]), (([],), []),
                   (([2, 1],), [1, 2])],
    "max_subarray_sum": [(([-2, 1, -3, 4, -1, 2, 1, -5, 4],), 6), (([-3, -1, -2],), -1), (([5],), 5)],
    "longest_unique_substring": [(("abcabcbb",), 3), (("bbbbb",), 1), (("pwwkew",), 3), (("",), 0),
                                 (("abba",), 2)],
    "group_anagrams": [((["eat", "tea", "tan", "ate", "nat", "bat"],),
                        [["ate", "eat", "tea"], ["bat"], ["nat", "tan"]]), (([],), [])],
    "top_k_frequent": [(([1, 1, 1, 2, 2, 3], 2), [1, 2]), (([4, 4, 5, 5, 6], 2), [4, 5]), (([7], 1), [7])],
    "climb_stairs": [((1,), 1), ((2,), 2), ((4,), 5), ((10,), 89)],
    "count_islands": [((["110", "010", "001"],), 2), ((["000"],), 0),
                      ((["11000", "11000", "00100", "00011"],), 3)],
    "shortest_path": [((["..#", "#..", "..."],), 4), (([".#", "#."],), -1), ((["."],), 0)],
}


def _linked(values, node_cls):
    head = None
    for v in reversed(values):
        head = node_cls(v, head)
    return head


def _to_list(head):
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out


def _check_special(module, name):
    if name == "MinStack":
        s = module.MinStack()
        for x in (5, 3, 7, 3, 1):
            s.push(x)
        assert s.get_min() == 1, "get_min should be 1 / debería ser 1"
        assert s.pop() == 1 and s.get_min() == 3, "after pop, get_min should be 3 / tras pop, debería ser 3"
        s.pop()
        assert s.get_min() == 3 and s.top() == 7, "min is still 3 (there is another 3) / el mínimo 3 sigue (hay otro 3)"
        s.pop()
        s.pop()
        assert s.get_min() == 5 and s.top() == 5
    elif name == "reverse_linked_list":
        for values in ([1, 2, 3], [], [9]):
            got = _to_list(module.reverse_linked_list(_linked(values, module.ListNode)))
            assert got == values[::-1], f"{values} → {got}"
    elif name == "bubble_sort":
        data = [3, 1, 2]
        module.bubble_sort(data)
        assert data == [3, 1, 2], "bubble_sort must not modify the input / no debe modificar la lista original"
    elif name == "merge_sort":
        rng = random.Random(360)
        for _ in range(50):
            data = [rng.randint(-50, 50) for _ in range(rng.randint(0, 30))]
            assert module.merge_sort(data) == sorted(data), f"merge_sort fails with / falla con {data}"


def run(module_name):
    module = importlib.import_module(module_name)
    names = list(CASES) + ["MinStack", "reverse_linked_list"]
    passed = failed = pending = 0
    for name in names:
        try:
            for args, expected in CASES.get(name, []):
                got = getattr(module, name)(*args)
                if got != expected:
                    raise AssertionError(f"{name}{args} → {got!r}, expected / se esperaba {expected!r}")
            _check_special(module, name)
        except NotImplementedError:
            pending += 1
            print(f"  · {name}: pending / pendiente")
            continue
        except Exception as exc:  # noqa: BLE001
            failed += 1
            print(f"  ✗ {name}: {exc}")
            continue
        passed += 1
        print(f"  ✓ {name}")
    print(f"\n{module_name}.py → {passed}/{len(names)} correct / correctos, {failed} failed / con errores, {pending} pending / pendientes")
    return failed == 0 and pending == 0


if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "problemas"
    sys.exit(0 if run(target) else 1)
