"""Runs every SQL solution in ejercicios.md / ejercicios.en.md and checks its expected result.
Ejecuta cada solución SQL de ejercicios.md / ejercicios.en.md y verifica su resultado esperado.

Usage / Uso:
    python3 check_solutions.py           # verify (used by CI) / verifica (lo usa la CI)
    python3 check_solutions.py --write   # regenerate expected results / regenera los resultados esperados

Format: a ```sql block inside <details>, followed by an "Expected result:" (EN) or
"Resultado esperado:" (ES) line and a ```text block.
"""
import re
import sqlite3
import sys

from setup_db import HERE, build

# file → (label before the expected block, word for "rows")
FILES = {
    "ejercicios.md": ("Resultado esperado:", "fila"),
    "ejercicios.en.md": ("Expected result:", "row"),
}


def fmt(value) -> str:
    if value is None:
        return "NULL"
    if isinstance(value, float):
        return f"{value:.2f}"
    return str(value)


def render(conn: sqlite3.Connection, query: str, row_word: str) -> str:
    cur = conn.execute(query)
    headers = [d[0] for d in cur.description]
    rows = [[fmt(v) for v in row] for row in cur.fetchall()]
    widths = [max(len(h), *(len(r[i]) for r in rows)) if rows else len(h)
              for i, h in enumerate(headers)]
    lines = [" | ".join(h.ljust(w) for h, w in zip(headers, widths)).rstrip()]
    lines.append("-+-".join("-" * w for w in widths))
    lines += [" | ".join(c.ljust(w) for c, w in zip(r, widths)).rstrip() for r in rows]
    lines.append(f"({len(rows)} {row_word}{'s' if len(rows) != 1 else ''})")
    return "\n".join(lines) + "\n"


def check_file(conn, name, label, row_word, write):
    path = HERE / name
    pattern = re.compile(
        r"(?P<sql>```sql\n(?P<query>.*?)```\n)"
        rf"(?:\n{re.escape(label)}\n\n```text\n(?P<expected>.*?)```\n)?",
        re.S,
    )
    failures, count = [], 0

    def replace(match: re.Match) -> str:
        nonlocal count
        count += 1
        query = match["query"]
        try:
            actual = render(conn, query, row_word)
        except sqlite3.Error as exc:
            failures.append(f"{name} #{count}: SQL error: {exc}\n{query}")
            return match.group(0)
        if not write:
            if match["expected"] is None:
                failures.append(f"{name} #{count}: missing expected result (run --write)")
            elif match["expected"] != actual:
                failures.append(f"{name} #{count}: different result.\nExpected:\n"
                                f"{match['expected']}\nGot:\n{actual}")
        return f"{match['sql']}\n{label}\n\n```text\n{actual}```\n"

    new_text = pattern.sub(replace, path.read_text(encoding="utf-8"))
    if write:
        path.write_text(new_text, encoding="utf-8")
    return count, failures


def main() -> int:
    write = "--write" in sys.argv
    conn = build(HERE / "check.db")
    all_failures = []
    try:
        for name, (label, row_word) in FILES.items():
            count, failures = check_file(conn, name, label, row_word, write)
            all_failures += failures
            print(f"{name}: {count - len(failures)}/{count} OK" + (" (written)" if write else ""))
    finally:
        conn.close()
        (HERE / "check.db").unlink()
    for failure in all_failures:
        print(failure, end="\n\n")
    return 1 if all_failures else 0


if __name__ == "__main__":
    sys.exit(main())
