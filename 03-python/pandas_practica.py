"""Práctica de pandas con la MISMA base de datos del módulo de SQL.

    pip install pandas         # si no lo tienes
    python3 pandas_practica.py

Cada bloque resuelve en pandas una pregunta que ya resolviste en SQL
(ver ../02-sql/ejercicios.md). Compara los resultados.
"""
import sqlite3
import sys
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "02-sql"))
from setup_db import build  # noqa: E402

pd.set_option("display.width", 120)
db_path = Path(__file__).resolve().parent / "pandas_practice.db"
conn = build(db_path)
customers = pd.read_sql("SELECT * FROM customers", conn)
products = pd.read_sql("SELECT * FROM products", conn)
orders = pd.read_sql("SELECT * FROM orders", conn, parse_dates=["order_date"])
items = pd.read_sql("SELECT * FROM order_items", conn)
employees = pd.read_sql("SELECT * FROM employees", conn)
conn.close()
db_path.unlink()


def show(title, df):
    print(f"\n=== {title} ===")
    print(df.to_string(index=False) if isinstance(df, pd.DataFrame) else df)


# 1) Explorar
show("Forma y tipos", f"{customers.shape}\n{customers.dtypes}")
show("Nulos por columna", customers.isna().sum())

# 2) Filtrar y ordenar  (SQL ej. 1)
show("Electronics por precio",
     products.loc[products["category"] == "Electronics", ["name", "price"]]
             .sort_values("price", ascending=False))

# 3) Conteo por grupo  (SQL ej. 4)
show("Clientes por país",
     customers.groupby("country").size().reset_index(name="customers")
              .sort_values("customers", ascending=False))

# 4) Merge (JOIN) + columna calculada + filtro + groupby  (SQL ej. 10)
sales = (items.merge(orders, on="order_id")
              .merge(products[["product_id", "category"]], on="product_id"))
sales["revenue"] = sales["quantity"] * sales["unit_price"]
valid = sales[sales["status"] != "cancelled"]
show("Ingresos por categoría",
     valid.groupby("category", as_index=False)["revenue"].sum()
          .sort_values("revenue", ascending=False))

# 5) Anti-join: clientes sin pedidos  (SQL ej. 12)
merged = customers.merge(orders, on="customer_id", how="left", indicator=True)
show("Clientes sin pedidos", merged.loc[merged["_merge"] == "left_only", ["customer_id", "name"]])

# 6) Varias agregaciones a la vez (agg con nombre)
show("Resumen por departamento",
     employees.groupby("department").agg(
         employees=("emp_id", "count"),
         avg_salary=("salary", "mean"),
         max_salary=("salary", "max"),
     ).round(2).reset_index())

# 7) Top 1 por grupo con rank  (SQL ej. 26)
employees["rk"] = employees.groupby("department")["salary"].rank(method="dense", ascending=False)
show("Mejor pagado por departamento", employees.loc[employees["rk"] == 1, ["department", "name", "salary"]])

# 8) Serie mensual + crecimiento  (SQL ej. 28)
monthly = (valid.groupby(valid["order_date"].dt.to_period("M"))["revenue"].sum()
                .reset_index(name="revenue"))
monthly["prev_revenue"] = monthly["revenue"].shift(1)          # = LAG
monthly["mom_growth_pct"] = (monthly["revenue"].pct_change() * 100).round(1)
show("Ingresos mensuales", monthly)

# 9) Acumulado  (SQL ej. 27)
per_order = valid.groupby(["order_id", "order_date"], as_index=False)["revenue"].sum()
per_order = per_order.sort_values(["order_date", "order_id"])
per_order["running_revenue"] = per_order["revenue"].cumsum()
show("Acumulado", per_order.tail(3))

# 10) Pivot table: ingresos por categoría (filas) y estado (columnas)
show("Pivot categoría × estado",
     sales.pivot_table(index="category", columns="status", values="revenue",
                       aggfunc="sum", fill_value=0).reset_index())

# 11) Limpieza de datos
clean = customers.copy()
clean["city"] = clean["city"].fillna("Unknown")
clean["email"] = clean["email"].str.lower()
clean["signup_month"] = pd.to_datetime(clean["signup_date"]).dt.strftime("%Y-%m")
clean = clean.drop_duplicates(subset=["email"]).rename(columns={"name": "customer_name"})
show("Clientes limpios", clean[["customer_name", "city", "signup_month"]].head())

# 12) apply / map / CASE WHEN
products["bucket"] = pd.cut(products["price"], bins=[0, 40, 300, float("inf")],
                            labels=["Low", "Medium", "High"], right=False)
show("Buckets de precio", products[["name", "price", "bucket"]])
