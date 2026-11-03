"""Genera los CSV de práctica de pandas: Mercado del Pacífico (Quibdó, Chocó), año 2024.

    python3 generar_datos.py      # escribe ventas_mercado_pacifico.csv y clientes.csv en esta carpeta

Los datos son inventados pero con forma real:
  * ventas_mercado_pacifico.csv: una fila por producto vendido dentro de un pedido (≈ 600 filas).
    Las ventas de artesanías y bebidas suben durante las Fiestas de San Pacho (20 sep – 4 oct) y en diciembre.
  * clientes.csv: 42 filas con problemas a propósito para practicar limpieza:
    municipios con espacios y mayúsculas mezcladas, segmentos en minúscula, correos vacíos y 2 filas duplicadas.
    Cuatro clientes (27, 38, 39 y 40) nunca compraron (anti-join).
La semilla es fija: siempre se generan los mismos datos.
"""
import csv
import random
from datetime import date, timedelta
from pathlib import Path

HERE = Path(__file__).resolve().parent
rng = random.Random(1808)

PRODUCTOS = [  # nombre, categoría, precio de lista (COP), cantidad típica (mín, máx)
    ("Borojó (unidad)", "Cosechas", 6000, (2, 20)),
    ("Chontaduro (racimo)", "Cosechas", 15000, (1, 8)),
    ("Plátano primitivo (racimo)", "Cosechas", 12000, (1, 10)),
    ("Bocachico (kg)", "Pescados", 18000, (1, 12)),
    ("Pargo rojo (kg)", "Pescados", 35000, (1, 8)),
    ("Camarón de río (kg)", "Pescados", 40000, (1, 5)),
    ("Canasto de werregue", "Artesanías", 420000, (1, 2)),
    ("Mochila de damagua", "Artesanías", 60000, (1, 3)),
    ("Aretes de chaquira", "Artesanías", 25000, (1, 4)),
    ("Tambora de chirimía", "Artesanías", 280000, (1, 1)),
    ("Viche (botella)", "Bebidas", 45000, (1, 6)),
    ("Arrechón (botella)", "Bebidas", 38000, (1, 6)),
]
MUNICIPIOS = [  # municipio, departamento, peso
    ("Quibdó", "Chocó", 12), ("Istmina", "Chocó", 5), ("Tadó", "Chocó", 3), ("Condoto", "Chocó", 3),
    ("Bahía Solano", "Chocó", 3), ("Nuquí", "Chocó", 2), ("Acandí", "Chocó", 2), ("Riosucio", "Chocó", 1),
    ("Medellín", "Antioquia", 4), ("Turbo", "Antioquia", 2), ("Cali", "Valle del Cauca", 3), ("Bogotá", "Cundinamarca", 3),
]
NOMBRES = ["Yeison", "Leidy", "Darwin", "Yuranis", "Neyla", "Wilmer", "Katherine", "Edwin", "Ana Lucía", "Jhon Freddy",
           "Yesenia", "Harold", "Luz Marina", "Jeferson", "Dayana", "Brayan", "Nelly", "Faustino", "Marleny", "Arley"]
APELLIDOS = ["Mosquera", "Palacios", "Córdoba", "Rentería", "Valencia", "Murillo", "Perea", "Cuesta", "Moreno", "Asprilla",
             "Hinestroza", "Copete", "Mena", "Lloreda", "Ibargüen", "Chaverra", "Bejarano", "Rivas", "Lemos", "Serna"]
SEGMENTOS = ["Hogar", "Hogar", "Hogar", "Restaurante", "Tienda"]
CANALES = ["WhatsApp", "WhatsApp", "Web", "Tienda física"]


def clientes():
    rows, usados = [], set()
    for cid in range(1, 41):
        while True:
            nombre = f"{rng.choice(NOMBRES)} {rng.choice(APELLIDOS)}"
            if nombre not in usados:
                usados.add(nombre)
                break
        mun, dep, _ = rng.choices(MUNICIPIOS, weights=[m[2] for m in MUNICIPIOS])[0]
        alta = date(2023, 6, 1) + timedelta(days=rng.randint(0, 520))
        correo = nombre.lower().split()[0].replace("í", "i").replace("é", "e") + f"{cid}@correo.co"
        rows.append({"cliente_id": cid, "nombre": nombre, "correo": correo, "municipio": mun,
                     "departamento": dep, "segmento": rng.choice(SEGMENTOS), "fecha_registro": alta.isoformat()})
    # Problemas a propósito / mess on purpose
    for cid, sucio in ((3, "  quibdó"), (8, "ISTMINA "), (12, "quibdo"), (17, "Bahia Solano"), (25, " Quibdó ")):
        rows[cid - 1]["municipio"], rows[cid - 1]["departamento"] = sucio, "Chocó"
    for cid in (5, 21, 33):
        rows[cid - 1]["correo"] = ""
    for cid in (9, 14, 30):
        rows[cid - 1]["segmento"] = rows[cid - 1]["segmento"].lower()
    rows.insert(15, dict(rows[6]))   # cliente 7 duplicado
    rows.append(dict(rows[22]))      # cliente 22 duplicado
    return rows


def fecha_pedido():
    while True:
        d = date(2024, 1, 1) + timedelta(days=rng.randint(0, 365))
        if d.year != 2024:
            continue
        peso = 1.0
        if date(2024, 9, 20) <= d <= date(2024, 10, 4):
            peso = 3.0                      # Fiestas de San Pacho
        elif d.month == 12:
            peso = 2.0
        if rng.random() < peso / 3:
            return d


def ventas(n_clientes=37, n_pedidos=230):
    rows = []
    pedidos = sorted((fecha_pedido(), rng.randint(1, n_clientes)) for _ in range(n_pedidos))
    for pid, (f, cid) in enumerate(pedidos, 1):
        san_pacho = date(2024, 9, 20) <= f <= date(2024, 10, 4)
        estado = rng.choices(["entregado", "enviado", "cancelado"], weights=[85, 7, 8])[0]
        if f >= date(2024, 12, 24) and estado == "entregado":
            estado = "enviado"
        canal = rng.choice(CANALES)
        pesos = [3 if (san_pacho or f.month == 12) and p[1] in ("Artesanías", "Bebidas") else 1 for p in PRODUCTOS]
        elegidos = []
        for _ in range(rng.choices([1, 2, 3, 4], weights=[35, 35, 20, 10])[0]):
            p = rng.choices(PRODUCTOS, weights=pesos)[0]
            if p not in elegidos:
                elegidos.append(p)
        calif = "" if estado != "entregado" or rng.random() < 0.3 else rng.choices([1, 2, 3, 4, 5], weights=[3, 5, 15, 37, 40])[0]
        for nombre, cat, precio, (lo, hi) in elegidos:
            descuento = rng.random() < 0.12
            rows.append({"pedido_id": pid, "fecha": f.isoformat(), "cliente_id": cid, "canal": canal,
                         "producto": nombre, "categoria": cat, "cantidad": rng.randint(lo, hi),
                         "precio_unitario": int(precio * 0.9) if descuento else precio,
                         "estado": estado, "calificacion": calif})
    return rows


def write(name, rows):
    with open(HERE / name, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]), lineterminator="\n")
        w.writeheader()
        w.writerows(rows)


if __name__ == "__main__":
    cli = clientes()
    ven = ventas()
    lugar = {c["cliente_id"]: (c["municipio"].strip().title().replace("Quibdo", "Quibdó").replace("Bahia", "Bahía"), c["departamento"]) for c in cli}
    for v in ven:   # en ventas el municipio ya viene limpio / sales carry the clean municipality
        mun, dep = lugar[v["cliente_id"]]
        v_items = list(v.items())
        v.clear()
        for k, val in v_items:
            v[k] = val
            if k == "cliente_id":
                v["municipio"], v["departamento"] = mun, dep
    write("clientes.csv", cli)
    write("ventas_mercado_pacifico.csv", ven)
    print(f"clientes.csv: {len(cli)} filas · ventas_mercado_pacifico.csv: {len(ven)} filas")
