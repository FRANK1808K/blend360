"""Ejecuta cada solución SQL de ejercicios.md y verifica el "Resultado esperado".

Uso:
    python3 check_solutions.py           # verifica (lo usa la CI)
    python3 check_solutions.py --write   # regenera los bloques de resultado esperado

Formato en ejercicios.md: un bloque ```sql dentro de <details>, seguido (opcionalmente)
de una línea "Resultado esperado:" y un bloque ```text.
"""
import re
import sqlite3
import sys
from pathlib import Path

from setup_db import HERE, build

MD_PATH = HERE / "ejercicios.md"
SOLUTION_RE = re.compile(
    r"(?P<sql>```sql\n(?P<query>.*?)```\n)"
    r"(?:\nResultado esperado:\n\n```text\n(?P<expected>.*?)```\n)?",
    re.S,
)


def fmt(value) -> str:
    if value is None:
        return "NULL"
    if isinstance(value, float):
        return f"{value:.2f}"
    return str(value)


def render(conn: sqlite3.Connection, query: str) -> str:
    cur = conn.execute(query)
    headers = [d[0] for d in cur.description]
    rows = [[fmt(v) for v in row] for row in cur.fetchall()]
    widths = [max(len(h), *(len(r[i]) for r in rows)) if rows else len(h)
              for i, h in enumerate(headers)]
    lines = [" | ".join(h.ljust(w) for h, w in zip(headers, widths)).rstrip()]
    lines.append("-+-".join("-" * w for w in widths))
    lines += [" | ".join(c.ljust(w) for c, w in zip(r, widths)).rstrip() for r in rows]
    lines.append(f"({len(rows)} fila{'s' if len(rows) != 1 else ''})")
    return "\n".join(lines) + "\n"


def main() -> int:
    conn = build(HERE / "check.db")
    text = MD_PATH.read_text(encoding="utf-8")
    write = "--write" in sys.argv
    failures, count = [], 0

    def replace(match: re.Match) -> str:
        nonlocal count
        count += 1
        query = match["query"]
        try:
            actual = render(conn, query)
        except sqlite3.Error as exc:
            failures.append(f"Solución #{count}: error SQL: {exc}\n{query}")
            return match.group(0)
        if not write and match["expected"] is not None and match["expected"] != actual:
            failures.append(f"Solución #{count}: resultado distinto.\nEsperado:\n"
                            f"{match['expected']}\nObtenido:\n{actual}")
        return f"{match['sql']}\nResultado esperado:\n\n```text\n{actual}```\n"

    new_text = SOLUTION_RE.sub(replace, text)
    conn.close()
    (HERE / "check.db").unlink()

    if write:
        MD_PATH.write_text(new_text, encoding="utf-8")
        print(f"{count} soluciones ejecutadas; resultados escritos en {MD_PATH.name}")
    for failure in failures:
        print(failure, end="\n\n")
    if not write:
        print(f"{count - len(failures)}/{count} soluciones correctas")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
