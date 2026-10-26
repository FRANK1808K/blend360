"""Creates practice.db (SQLite) from schema.sql / Crea practice.db (SQLite) a partir de schema.sql.

Usage / Uso:
    python3 setup_db.py            # creates/recreates practice.db / crea o recrea practice.db
    python3 setup_db.py --shell    # also opens an interactive SQL console / además abre una consola SQL

You can also open it with / También puedes abrirla con: sqlite3 practice.db (or DB Browser for SQLite / DBeaver)
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
    print("SQL console / Consola SQL. End each query with / Termina cada consulta con ';'. Type / Escribe .exit to quit / para salir.")
    buffer = ""
    while True:
        try:
            line = input("sql> " if not buffer else "...> ")
        except EOFError:
            break
        if line.strip() in (".exit", ".salir"):
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
    print(f"Database created / Base creada: {DB_PATH} — tables / tablas: {', '.join(tables)}")
    if "--shell" in sys.argv:
        shell(connection)
