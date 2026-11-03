"""Builds the data of the SQL slide deck / Genera los datos de la presentación de SQL.

The deck (presentaciones/sql/index.html) teaches SQL with a Spanish practice database set in Quibdó, Chocó
(«Mercado del Pacífico») and runs its 35 exercises in the browser (SQLite via sql.js). The database and the
exercises live in presentaciones/sql/mercado_pacifico.sql and ejercicios.json; this script checks that every
solution runs and returns rows, and embeds both as JSON in the deck.
La presentación enseña SQL con una base de práctica en español ambientada en Quibdó, Chocó, y ejecuta sus 35
ejercicios en el navegador. Este script verifica que cada solución corre y devuelve filas, y los incrusta como JSON.

Usage / Uso:
    python3 scripts/build_slides.py           # writes the JSON into the deck / lo escribe en la presentación
    python3 scripts/build_slides.py --check   # fails if the deck is out of date (CI) / falla si está desactualizada
"""
import json
import sqlite3
import sys
from pathlib import Path

if sys.stdout.encoding != "utf-8" and hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parent.parent
DECK = ROOT / "presentaciones" / "sql"
HTML = DECK / "index.html"
START = '<script type="application/json" id="deck-data">'
END = "</script><!-- DECK-DATA-END -->"
LEVELS = {"basico", "joins", "ventanas", "reto"}


def build() -> str:
    schema = (DECK / "mercado_pacifico.sql").read_text(encoding="utf-8")
    items = json.loads((DECK / "ejercicios.json").read_text(encoding="utf-8"))
    db = sqlite3.connect(":memory:")
    db.executescript(schema)
    for i, item in enumerate(items, 1):
        assert item["id"] == str(i), f"exercise {i}: id {item['id']} out of order / fuera de orden"
        assert item.get("pasos"), f"exercise {i}: missing reasoning steps / faltan los pasos"
        assert item["nivel"] in LEVELS, f"exercise {i}: unknown level / nivel desconocido {item['nivel']}"
        rows = db.execute(item["sql"]).fetchall()
        assert rows, f"exercise {i}: the solution returns no rows / la solución no devuelve filas"
    return json.dumps({"schema": schema, "items": items}, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")


def main() -> int:
    html = HTML.read_text(encoding="utf-8")
    head, rest = html.split(START, 1)
    _, tail = rest.split(END, 1)
    new = head + START + build() + END + tail
    rel = HTML.relative_to(ROOT).as_posix()
    if "--check" in sys.argv:
        if new != html:
            print(f"✗ {rel} is out of date / está desactualizada: python3 scripts/build_slides.py")
            return 1
        print(f"✓ {rel} up to date / al día")
        return 0
    HTML.write_text(new, encoding="utf-8")
    print(f"✓ {rel} written / escrita")
    return 0


if __name__ == "__main__":
    sys.exit(main())
