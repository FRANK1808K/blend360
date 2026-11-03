"""Comprobador de los ejercicios de pandas (Mercado del Pacífico).

Lo usan el cuaderno de Jupyter y la presentación (que lo ejecuta en el navegador con Pyodide):

    from comprobar import comprobar, pista, solucion
    resultado = ventas.shape
    comprobar(1, resultado)     # ✓ o ✗ con el motivo

Compara valores, no nombres: el índice con nombre (por ejemplo `categoria` en un groupby) cuenta como columna,
un índice numérico sin nombre se ignora y los decimales se comparan redondeados a 2.
"""
import ast
import json
import math
from pathlib import Path

import numpy as np
import pandas as pd

HERE = Path(__file__).resolve().parent
_EJ = None


def ejercicios():
    global _EJ
    if _EJ is None:
        _EJ = {e["id"]: e for e in json.loads((HERE / "ejercicios.json").read_text(encoding="utf-8"))}
    return _EJ


def cargar(carpeta=None):
    """Lee los dos CSV igual que el cuaderno: devuelve (ventas, clientes)."""
    datos = Path(carpeta) if carpeta else HERE / "datos"
    ventas = pd.read_csv(datos / "ventas_mercado_pacifico.csv", parse_dates=["fecha"])
    clientes = pd.read_csv(datos / "clientes.csv", parse_dates=["fecha_registro"])
    return ventas, clientes


def ejecutar(codigo, ventas, clientes):
    """Ejecuta una celda y devuelve el valor de su última expresión (como Jupyter)."""
    ns = {"pd": pd, "np": np, "ventas": ventas.copy(), "clientes": clientes.copy()}
    arbol = ast.parse(codigo)
    ultima = None
    if arbol.body and isinstance(arbol.body[-1], ast.Expr):
        ultima = ast.Expression(arbol.body.pop().value)
    exec(compile(arbol, "<celda>", "exec"), ns)
    return eval(compile(ultima, "<celda>", "eval"), ns) if ultima else None


def _celda(v):
    if isinstance(v, (pd.Timestamp, np.datetime64)):
        return pd.Timestamp(v).strftime("%Y-%m-%d")
    try:
        if pd.isna(v):
            return None
    except (TypeError, ValueError):
        pass
    if isinstance(v, (bool, np.bool_)):
        return bool(v)
    if isinstance(v, (int, np.integer)):
        return int(v)
    if isinstance(v, (float, np.floating)):
        f = float(v)
        return int(f) if f.is_integer() and abs(f) < 1e15 else round(f, 4)
    if isinstance(v, pd.Interval):
        return str(v)
    return str(v)


def tabla(obj):
    """Convierte un resultado (DataFrame, Series, tupla o escalar) en {tipo, cols, filas}."""
    if isinstance(obj, pd.DataFrame):
        tipo, df = "DataFrame", obj.copy()
    elif isinstance(obj, pd.Series):
        tipo, df = "Series", obj.to_frame(name=obj.name if obj.name is not None else "valor")
    elif isinstance(obj, (tuple, list)):
        tipo, df = type(obj).__name__, pd.DataFrame([list(obj)], columns=[f"[{i}]" for i in range(len(obj))])
    elif obj is None:
        return {"tipo": "None", "cols": [], "filas": []}
    else:
        tipo, df = type(obj).__name__, pd.DataFrame([[obj]], columns=["valor"])
    idx = df.index
    if isinstance(idx, pd.MultiIndex) or any(n is not None for n in idx.names) or not pd.api.types.is_integer_dtype(idx):
        df = df.reset_index()
    else:
        df = df.reset_index(drop=True)
    cols = [" · ".join(map(str, c)) if isinstance(c, tuple) else str(c) for c in df.columns]
    filas = [[_celda(v) for v in fila] for fila in df.itertuples(index=False, name=None)]
    return {"tipo": tipo, "cols": cols, "filas": filas}


def _clave(fila):
    return json.dumps([round(v, 2) if isinstance(v, float) else v for v in fila], ensure_ascii=False)


def comparar(t_usuario, t_esperado, ordenado):
    """(ok, mensaje) comparando dos tablas."""
    if len(t_usuario["cols"]) != len(t_esperado["cols"]):
        return False, f"Se esperaban {len(t_esperado['cols'])} columnas ({', '.join(t_esperado['cols'])}) y hay {len(t_usuario['cols'])}."
    if len(t_usuario["filas"]) != len(t_esperado["filas"]):
        return False, f"Se esperaban {len(t_esperado['filas'])} filas y hay {len(t_usuario['filas'])}."
    a = [_clave(f) for f in t_usuario["filas"]]
    b = [_clave(f) for f in t_esperado["filas"]]
    if a == b:
        return True, "Correcto."
    if sorted(a) == sorted(b):
        return (False, "Los valores son correctos pero el orden no: revisa el ordenamiento.") if ordenado else (True, "Correcto.")
    return False, "Mismo tamaño, pero algunos valores no coinciden. Revisa filtros, agrupaciones y cálculos."


def esperado(n, ventas=None, clientes=None):
    if ventas is None:
        ventas, clientes = cargar()
    return ejecutar(ejercicios()[str(n)]["code"], ventas, clientes)


def comprobar(n, resultado):
    """Imprime ✓ o ✗ comparando tu resultado con el de la solución del ejercicio n."""
    e = ejercicios()[str(n)]
    if resultado is None:
        print(f"… Ejercicio {n} · {e['titulo']}: todavía no hay respuesta. Guarda tu resultado en la variable `resultado`.")
        return False
    ok, msg = comparar(tabla(resultado), tabla(esperado(n)), e.get("ordenado", False))
    print(("✓ " if ok else "✗ ") + f"Ejercicio {n} · {e['titulo']}: {msg}")
    return ok


def pista(n):
    """Muestra los pasos para pensar el ejercicio n."""
    e = ejercicios()[str(n)]
    print(f"Ejercicio {n} · {e['titulo']}")
    for i, paso in enumerate(e["pasos"], 1):
        print(f"  {i}. {paso.replace('`', '')}")


def solucion(n):
    """Muestra el código de la solución y la idea clave."""
    e = ejercicios()[str(n)]
    print(e["code"])
    print("\nClave:", e["nota"].replace("`", ""))


# ---------------------------------------------------------------- para la presentación (Pyodide)
_CACHE = {}


def _navegador(codigo, n=None):
    """Ejecuta código del navegador y devuelve JSON con el resultado (y la comparación si hay ejercicio)."""
    import contextlib
    import io
    import traceback
    salida = io.StringIO()
    res = {}
    try:
        if "datos" not in _CACHE:
            _CACHE["datos"] = cargar("datos")
        ventas, clientes = _CACHE["datos"]
        with contextlib.redirect_stdout(salida):
            valor = ejecutar(codigo, ventas, clientes)
        res["tabla"] = tabla(valor)
        res["texto"] = None if isinstance(valor, (pd.DataFrame, pd.Series)) or valor is None else repr(valor)
        if n is not None:
            if n not in _CACHE:
                _CACHE[n] = tabla(ejecutar(ejercicios()[n]["code"], ventas, clientes))
            ok, msg = comparar(res["tabla"], _CACHE[n], ejercicios()[n].get("ordenado", False))
            if valor is None:
                ok, msg = False, "La última línea no devuelve nada: termina con la expresión del resultado (por ejemplo, el DataFrame)."
            res["ok"], res["msg"] = ok, msg
    except Exception as exc:  # noqa: BLE001 - se muestra al usuario
        linea = traceback.format_exception_only(type(exc), exc)[-1].strip()
        res["error"] = linea
    res["stdout"] = salida.getvalue()[-3000:]
    return json.dumps(res, ensure_ascii=False, default=str)


if __name__ == "__main__":
    v, c = cargar()
    malos = [n for n in ejercicios() if not comparar(tabla(esperado(n, v, c)), tabla(esperado(n, v, c)), True)[0]]
    print("Todas las soluciones corren" if not malos else f"Fallan: {malos}")
