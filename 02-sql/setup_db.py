"""Crea practice.db (SQLite) a partir de schema.sql.

Uso:
    python3 setup_db.py            # crea/recrea practice.db
    python3 setup_db.py --shell    # además abre una consola SQL interactiva

Abre la base también con: sqlite3 practice.db   (o con DB Browser for SQLite / DBeaver)
"""
import sqlite3
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
DB_PATH = HERE / "practice.db"


def build(db_path: Path = DB_PATH) -> sqlite3.Connection:
    if db_path.exists():
        db_path.unlink()
    conn = sqlite3.connect(db_path)
    conn.executescript((HERE / "schema.sql").read_text(encoding="utf-8"))
    conn.commit()
    return conn


def shell(conn: sqlite3.Connection) -> None:
    print("Consola SQL. Termina cada consulta con ';'. Escribe .salir para terminar.")
    buffer = ""
    while True:
        try:
            line = input("sql> " if not buffer else "...> ")
        except EOFError:
            break
        if line.strip() == ".salir":
            break
        buffer += line + "\n"
        if not sqlite3.complete_statement(buffer):
            continue
        try:
            cur = conn.execute(buffer)
            if cur.description:
                headers = [d[0] for d in cur.description]
                print(" | ".join(headers))
                print("-" * (len(" | ".join(headers))))
                for row in cur.fetchall():
                    print(" | ".join("NULL" if v is None else str(v) for v in row))
        except sqlite3.Error as exc:
            print(f"Error: {exc}")
        buffer = ""


if __name__ == "__main__":
    connection = build()
    tables = [r[0] for r in connection.execute(
        "SELECT name FROM sqlite_master WHERE type='table' ORDER BY name")]
    print(f"Base creada en {DB_PATH} con tablas: {', '.join(tables)}")
    if "--shell" in sys.argv:
        shell(connection)
