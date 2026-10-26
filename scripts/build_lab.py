"""Builds the data of the simulator's code lab / Genera los datos del laboratorio de código del simulador.

The lab (simulator/index.html) runs SQL and Python in the browser. Its exercises are not
written twice: this script reads them from the repository and embeds them as JSON.
El laboratorio ejecuta SQL y Python en el navegador. Sus ejercicios no se escriben dos veces:
este script los lee del repositorio y los incrusta como JSON.

Sources / Fuentes:
  02-sql/schema.sql, 02-sql/ejercicios(.en).md          → SQL exercises and solutions
  03-python/ejercicios.py, soluciones.py, test_ejercicios.py
  04-algoritmos-y-estructuras/problemas.py, soluciones.py, test_problemas.py

Usage / Uso:
    python3 scripts/build_lab.py           # writes the JSON into simulator/index.html / lo escribe
    python3 scripts/build_lab.py --check   # fails if index.html is out of date (CI) / falla si está desactualizado
"""
import ast
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HTML = ROOT / "simulator" / "index.html"
START = '<script type="application/json" id="lab-data">'
END = "</script><!-- LAB-DATA-END -->"
ORDER_WORDS = re.compile(r"sorted|sort by|alphabetical order|\bmost\b.*\bfirst\b|highest to lowest|ordered by", re.I)
# Statements that do not say which columns to show ("Find the customers who…"): any subset of the
# solution's columns that identifies the same rows is accepted.
# Enunciados que no dicen qué columnas mostrar: se acepta cualquier subconjunto que identifique las mismas filas.
FLEXIBLE_COLUMNS = {3, 5, 12, 13, 15, 17, 18, 20, 26, 34}
LEVELS = {"🟢": "basic", "🟡": "joins", "🟠": "windows", "🔴": "challenge"}


# ---------------------------------------------------------------- SQL

def sql_exercises(path: Path) -> list:
    """One entry per exercise: title, statement, translation, solutions and their notes."""
    text = path.read_text(encoding="utf-8")
    out, level = [], None
    for chunk in re.split(r"^(?=## |### )", text, flags=re.M):
        if chunk.startswith("## "):
            level = LEVELS.get(chunk[3:4], level)
            continue
        if not chunk.startswith("### "):
            continue
        head, body = chunk.split("\n", 1)
        num, title = re.match(r"### (\d+)\. (.+)", head).groups()
        intro, details = body.split("<details>", 1)
        lines = [l.strip() for l in intro.strip().splitlines() if l.strip()]
        statement = lines[0].strip("*")
        translation = lines[1].strip("*") if len(lines) > 1 else ""
        details = details.split("</details>", 1)[0]
        parts = []
        for block in re.split(r"(?=```sql\n)", details)[1:]:
            query = re.match(r"```sql\n(.*?)```", block, re.S)[1]
            notes = [l[2:] for l in block.splitlines() if l.startswith("> ")]
            parts.append({"sql": query.strip(), "note": " ".join(notes)})
        out.append({"n": int(num), "level": level, "title": title, "q": statement,
                    "tr": translation, "parts": parts})
    return out


def sql_data() -> dict:
    en = sql_exercises(ROOT / "02-sql" / "ejercicios.en.md")
    es = sql_exercises(ROOT / "02-sql" / "ejercicios.md")
    assert [e["n"] for e in en] == [e["n"] for e in es], "ES/EN exercises differ / difieren"
    items = []
    for e, s in zip(en, es):
        strip = lambda q: re.sub(r"--[^\n]*", "", q).split()  # comments are translated / los comentarios se traducen
        assert [strip(p["sql"]) for p in e["parts"]] == [strip(p["sql"]) for p in s["parts"]], f"SQL #{e['n']} ES≠EN"
        for i, part in enumerate(e["parts"]):
            items.append({
                "id": f"{e['n']}" + (f"-{i + 1}" if len(e["parts"]) > 1 else ""),
                "n": e["n"], "part": i + 1, "parts": len(e["parts"]), "level": e["level"],
                "title": {"en": e["title"], "es": s["title"]},
                "q": e["q"], "es": s["tr"] or e["tr"],
                # Row order is only graded when the statement asks for it / El orden de las filas
                # solo se califica cuando el enunciado lo pide.
                "ordered": bool(ORDER_WORDS.search(e["q"])),
                "flexCols": e["n"] in FLEXIBLE_COLUMNS,
                "sql": {"en": part["sql"], "es": s["parts"][i]["sql"]}, "note": {"en": part["note"], "es": s["parts"][i]["note"]},
            })
    schema = (ROOT / "02-sql" / "schema.sql").read_text(encoding="utf-8")
    return {"schema": schema, "items": items}


# ---------------------------------------------------------------- Python

def members(path: Path):
    """Top-level functions/classes with their source, section (comment banner) and imports."""
    src = path.read_text(encoding="utf-8")
    tree = ast.parse(src)
    lines = src.splitlines()
    banners = [(i + 1, re.sub(r"^#\s*-+\s*", "", l).strip()) for i, l in enumerate(lines) if re.match(r"#\s*-{10,}", l)]
    imports = [ast.get_source_segment(src, n) for n in tree.body if isinstance(n, (ast.Import, ast.ImportFrom))]
    found = {}
    for node in tree.body:
        if isinstance(node, (ast.FunctionDef, ast.ClassDef)):
            section = next((name for line, name in reversed(banners) if line < node.lineno), "")
            found[node.name] = {"src": ast.get_source_segment(src, node), "section": section,
                                "doc": ast.get_docstring(node) or ""}
    return found, imports


def with_imports(code: str, imports: list) -> str:
    used = [imp for imp in imports if any(re.search(rf"\b{re.escape(name.strip())}\b", code)
                                          for name in re.sub(r"^(from \S+ )?import ", "", imp).split(","))]
    return "\n".join(used + ([""] if used else []) + [code])


def python_set(folder: str, exercises: str, grader: str, prelude: str = "") -> dict:
    stubs, _ = members(ROOT / folder / exercises)
    sols, imports = members(ROOT / folder / "soluciones.py")
    items = []
    for name, info in stubs.items():
        if name == prelude:
            continue
        # Helpers the solution calls (e.g. merge_sort uses merge_sorted) go first / Primero las funciones que usa.
        helpers = [h for h in sols if h not in (name, prelude) and re.search(rf"\b{h}\(", sols[name]["src"])]
        code = "\n\n\n".join([sols[h]["src"] for h in helpers] + [sols[name]["src"]])
        items.append({"name": name, "section": info["section"], "doc": info["doc"],
                      "stub": info["src"], "solution": with_imports(code, imports)})
    return {"items": items, "grader": (ROOT / folder / grader).read_text(encoding="utf-8"),
            "prelude": stubs[prelude]["src"] if prelude else ""}


def build() -> str:
    data = {
        "sql": sql_data(),
        "py": python_set("03-python", "ejercicios.py", "test_ejercicios.py"),
        "algo": python_set("04-algoritmos-y-estructuras", "problemas.py", "test_problemas.py", prelude="ListNode"),
    }
    return json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")


def main() -> int:
    html = HTML.read_text(encoding="utf-8")
    pattern = re.compile(re.escape(START) + ".*?" + re.escape(END), re.S)
    if not pattern.search(html):
        print(f"Markers not found in / No se encontraron los marcadores en {HTML}")
        return 1
    new_html = pattern.sub(lambda _: START + build() + END, html)
    if "--check" in sys.argv:
        if new_html != html:
            print("simulator/index.html is out of date: run / está desactualizado: ejecuta python3 scripts/build_lab.py")
            return 1
        print("Lab data up to date / Datos del laboratorio al día")
        return 0
    HTML.write_text(new_html, encoding="utf-8")
    data = json.loads(build().replace("<\\/", "</"))
    print(f"Lab data written / escritos: {len(data['sql']['items'])} SQL, "
          f"{len(data['py']['items'])} Python, {len(data['algo']['items'])} algorithms")
    return 0


if __name__ == "__main__":
    sys.exit(main())
