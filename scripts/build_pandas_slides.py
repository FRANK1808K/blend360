"""Builds the pandas deck and notebooks / Genera la presentación y los cuadernos de pandas.

Sources / Fuentes (presentaciones/pandas/):
  datos/ventas_mercado_pacifico.csv, datos/clientes.csv   practice data (datos/generar_datos.py)
  ejercicios.json                                         35 exercises: statement, solution, steps, key idea
  comprobar.py                                            grader shared by the notebook and the deck

Outputs / Salidas:
  index.html                          the JSON block (data, grader, exercises, expected results) for the deck
  cuaderno_pandas.ipynb               exercises to solve in VS Code / Jupyter
  cuaderno_pandas_soluciones.ipynb    the same notebook, solved

Every solution is run with pandas and must return a result. The expected results are embedded so the deck can
show them even where Python cannot run in the browser.

Usage / Uso:
    python3 scripts/build_pandas_slides.py           # writes the outputs / escribe las salidas
    python3 scripts/build_pandas_slides.py --check   # fails if any output is out of date (CI)
"""
import ast
import html
import json
import re
import sys
import warnings
from pathlib import Path

if sys.stdout.encoding != "utf-8" and hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
warnings.simplefilter("ignore")

ROOT = Path(__file__).resolve().parent.parent
DECK = ROOT / "presentaciones" / "pandas"
sys.path.insert(0, str(DECK))
import comprobar  # noqa: E402

HTML = DECK / "index.html"
START = '<script type="application/json" id="deck-data">'
END = "</script><!-- DECK-DATA-END -->"
LEVELS = {"basico", "limpieza", "agrupar", "tiempo", "reto"}
MAX_ROWS = 60

# Notebook sections: (first exercise, title, explanation) / Secciones del cuaderno.
SECTIONS = [
    (1, "1 · Explorar, seleccionar y filtrar",
     "Un **DataFrame** es una tabla: filas con un índice y columnas con nombre. Cada columna es una **Series**.\n\n"
     "- Explorar: `df.shape`, `df.head()`, `df.info()`, `df.describe()`, `df['col'].value_counts()`.\n"
     "- Seleccionar: `df['col']` (Series), `df[['a', 'b']]` (DataFrame), `df.loc[filas, columnas]` por etiqueta, `df.iloc[i, j]` por posición.\n"
     "- Filtrar con máscaras: `df[(cond1) & (cond2)]`. Usa `&`, `|`, `~` y paréntesis, nunca `and`/`or`.\n"
     "- Columnas nuevas: operaciones vectorizadas (`df['a'] * df['b']`), `assign`, `np.where`, `pd.cut`."),
    (12, "2 · Limpieza de datos",
     "`clientes.csv` viene sucio a propósito: municipios con espacios y mayúsculas mezcladas, segmentos en minúscula, "
     "correos vacíos y filas duplicadas.\n\n"
     "- Faltantes: `isna().sum()`, `fillna(valor)`, `dropna()`.\n"
     "- Duplicados: `duplicated()`, `drop_duplicates()`.\n"
     "- Texto: `.str.strip()`, `.str.title()`, `.str.lower()`, `.replace({...})`.\n"
     "- Tipos: `astype()`, `pd.to_datetime()`."),
    (17, "3 · Agrupar y unir (groupby y merge)",
     "**Dividir → aplicar → combinar:** `df.groupby('clave')['col'].sum()` parte la tabla por clave, calcula y junta.\n\n"
     "- Varias métricas con nombre: `.agg(ingreso=('ingreso', 'sum'), pedidos=('pedido_id', 'nunique'))`.\n"
     "- `transform` devuelve un valor por fila (como una función de ventana en SQL).\n"
     "- `merge(otra, on='clave', how='left')` es el JOIN. Revisa que la clave no esté duplicada en la tabla derecha."),
    (24, "4 · Fechas y reorganizar tablas",
     "- Accesor `.dt`: `.dt.month`, `.dt.quarter`, `.dt.day_name()`.\n"
     "- `resample('MS')` agrupa por mes (la fecha debe estar en el índice).\n"
     "- `pct_change()`, `shift()`, `rolling(n)`, `cumsum()`: crecimiento, fila anterior, promedios móviles y acumulados.\n"
     "- `pivot_table` (largo → ancho), `melt` (ancho → largo) y `pd.crosstab` (conteos cruzados)."),
    (31, "5 · Retos tipo entrevista", "Combinan todo lo anterior. Intenta resolverlos en menos de 10 minutos cada uno."),
]


def expected(items, ventas, clientes):
    out = {}
    for e in items:
        value = comprobar.ejecutar(e["code"], ventas, clientes)
        assert value is not None, f"exercise {e['id']}: the solution returns nothing / la solución no devuelve nada"
        t = comprobar.tabla(value)
        t["filas"] = t["filas"][:MAX_ROWS]
        out[e["id"]] = t
    return out


def demos(page, ventas, clientes):
    """Live code blocks of the deck (<pre class="live" data-demo="x">) / Bloques en vivo de la presentación."""
    out = {}
    for name, code in re.findall(r'<pre class="live[^"]*"[^>]*?data-demo="([\w-]+)"[^>]*><code[^>]*>(.*?)</code></pre>', page, re.S):
        code = html.unescape(code).strip("\n")
        t = comprobar.tabla(comprobar.ejecutar(code, ventas, clientes))
        t["filas"] = t["filas"][:MAX_ROWS]
        out[name] = t
    return out


def deck_json(page, items, ventas, clientes) -> str:
    data = {
        "ventas": (DECK / "datos" / "ventas_mercado_pacifico.csv").read_text(encoding="utf-8"),
        "clientes": (DECK / "datos" / "clientes.csv").read_text(encoding="utf-8"),
        "grader": (DECK / "comprobar.py").read_text(encoding="utf-8"),
        "items": items,
        "expected": expected(items, ventas, clientes),
        "demos": demos(page, ventas, clientes),
    }
    return json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")


# ---------------------------------------------------------------- notebooks / cuadernos
def md(text):
    return {"cell_type": "markdown", "metadata": {}, "source": text.splitlines(keepends=True)}


def code(text):
    return {"cell_type": "code", "execution_count": None, "metadata": {}, "outputs": [], "source": text.splitlines(keepends=True)}


def as_result(src: str) -> str:
    """Assigns the last expression to `resultado` / Asigna la última expresión a `resultado`."""
    last = ast.parse(src).body[-1]
    assert isinstance(last, ast.Expr)
    lines = src.splitlines()
    i = last.lineno - 1
    lines[i] = "resultado = " + lines[i]
    return "\n".join(lines)


INTRO = """# pandas desde Quibdó · cuaderno de práctica

35 ejercicios sobre **Mercado del Pacífico**, una tienda en línea de Quibdó (Chocó) que vende cosechas, pescado, \
bebidas y artesanías durante 2024. Son los mismos de la presentación «pandas desde Quibdó».

**Archivos:** `datos/ventas_mercado_pacifico.csv` (una fila por producto vendido en un pedido), `datos/clientes.csv` \
(sucio a propósito, para limpiar) y `comprobar.py` (revisa tus respuestas).

## Cómo abrirlo en Visual Studio Code

1. Instala [Python 3.10 o superior](https://www.python.org/downloads/) y [VS Code](https://code.visualstudio.com/).
2. En VS Code instala las extensiones **Python** y **Jupyter** (de Microsoft).
3. *Archivo → Abrir carpeta…* y elige esta carpeta (la que tiene este cuaderno y la carpeta `datos`).
4. Abre una terminal (*Terminal → Nueva terminal*) y crea el entorno:
   - Windows: `python -m venv .venv` y luego `.venv\\Scripts\\activate`
   - macOS / Linux: `python3 -m venv .venv` y luego `source .venv/bin/activate`
   - Después: `pip install -r requirements.txt`
5. Abre este cuaderno, pulsa **Seleccionar kernel** (arriba a la derecha) y elige `.venv`.
6. Ejecuta cada celda con **Shift + Enter**.

## Cómo practicar

En cada ejercicio escribe tu código y deja el resultado en la variable `resultado`. La celda termina con \
`comprobar(n, resultado)`, que imprime ✓ o ✗ con el motivo. Si te trabas: `pista(n)`; para ver la respuesta: `solucion(n)`.
"""

SETUP = """import numpy as np
import pandas as pd
from comprobar import comprobar, pista, solucion

ventas = pd.read_csv('datos/ventas_mercado_pacifico.csv', parse_dates=['fecha'])
clientes = pd.read_csv('datos/clientes.csv', parse_dates=['fecha_registro'])
ventas.head()"""

BONUS = """# Bonus: un gráfico rápido del ingreso mensual (necesita matplotlib)
v = ventas[ventas['estado'] != 'cancelado'].assign(ingreso=lambda d: d['cantidad'] * d['precio_unitario'])
mensual = v.groupby(v['fecha'].dt.month)['ingreso'].sum() / 1e6
ax = mensual.plot(kind='bar', figsize=(10, 4), color='#0b6fa4', title='Ingreso mensual 2024 (millones de COP)')
ax.set_xticklabels(['ene', 'feb', 'mar', 'abr', 'may', 'jun', 'jul', 'ago', 'sep', 'oct', 'nov', 'dic'], rotation=0)
ax.set_xlabel('');"""


def notebook(items, solved: bool) -> str:
    cells = [md(INTRO), code(SETUP)]
    starts = {s[0]: s for s in SECTIONS}
    for e in items:
        n = int(e["id"])
        if n in starts:
            _, title, text = starts[n]
            cells.append(md(f"## {title}\n\n{text}"))
        steps = "\n".join(f"{i}. {p}" for i, p in enumerate(e["pasos"], 1))
        cells.append(md(f"### Ejercicio {n} · {e['titulo']}\n\n**{e['en']}**\n\n*{e['es']}*\n\n"
                        f"<details><summary>Cómo pensarlo</summary>\n\n{steps}\n\n</details>"))
        if solved:
            cells.append(code(f"{as_result(e['code'])}\n\ncomprobar({n}, resultado)\nresultado"))
            cells.append(md(f"> **Clave:** {e['nota']}"))
        else:
            cells.append(code(f"# Ejercicio {n}: escribe tu código y guarda la respuesta en `resultado`\n"
                              f"resultado = None\n\ncomprobar({n}, resultado)"))
    cells.append(md("## Bonus · Visualizar"))
    cells.append(code(BONUS))
    nb = {"cells": cells, "metadata": {"kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
                                       "language_info": {"name": "python"}}, "nbformat": 4, "nbformat_minor": 5}
    return json.dumps(nb, ensure_ascii=False, indent=1) + "\n"


def main() -> int:
    items = json.loads((DECK / "ejercicios.json").read_text(encoding="utf-8"))
    for i, e in enumerate(items, 1):
        assert e["id"] == str(i), f"exercise {i}: id out of order / fuera de orden"
        assert e["nivel"] in LEVELS and e["pasos"], f"exercise {i}: level or steps / nivel o pasos"
    ventas, clientes = comprobar.cargar()
    page = HTML.read_text(encoding="utf-8")
    head, rest = page.split(START, 1)
    _, tail = rest.split(END, 1)
    outputs = {
        HTML: head + START + deck_json(page, items, ventas, clientes) + END + tail,
        DECK / "cuaderno_pandas.ipynb": notebook(items, solved=False),
        DECK / "cuaderno_pandas_soluciones.ipynb": notebook(items, solved=True),
    }
    stale = [p for p, text in outputs.items() if not p.exists() or p.read_text(encoding="utf-8") != text]
    if "--check" in sys.argv:
        for p in stale:
            print(f"✗ {p.relative_to(ROOT).as_posix()} is out of date / está desactualizado: python3 scripts/build_pandas_slides.py")
        if not stale:
            print("✓ pandas deck and notebooks up to date / presentación y cuadernos al día")
        return 1 if stale else 0
    for p in stale:
        p.write_text(outputs[p], encoding="utf-8")
        print(f"✓ {p.relative_to(ROOT).as_posix()} written / escrito")
    return 0


if __name__ == "__main__":
    sys.exit(main())
