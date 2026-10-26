"""pandas practice with the SAME database as the SQL module.
Práctica de pandas con la MISMA base de datos del módulo de SQL.

    pip install pandas         # if you don't have it / si no lo tienes
    python3 pandas_practica.py

Each block solves in pandas a question you already solved in SQL
(see ../02-sql/ejercicios.en.md). Compare the results.
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


# 1) Explore / Explorar
show("Shape and types / Forma y tipos", f"{customers.shape}\n{customers.dtypes}")
show("Nulls per column / Nulos por columna", customers.isna().sum())

# 2) Filter and sort / Filtrar y ordenar  (SQL ex. 1)
show("Electronics by price / Electronics por precio",
     products.loc[products["category"] == "Electronics", ["name", "price"]]
             .sort_values("price", ascending=False))

# 3) Count per group / Conteo por grupo  (SQL ex. 4)
show("Customers per country / Clientes por país",
     customers.groupby("country").size().reset_index(name="customers")
              .sort_values("customers", ascending=False))

# 4) Merge (JOIN) + computed column + filter + groupby  (SQL ex. 10)
sales = (items.merge(orders, on="order_id")
              .merge(products[["product_id", "category"]], on="product_id"))
sales["revenue"] = sales["quantity"] * sales["unit_price"]
valid = sales[sales["status"] != "cancelled"]
show("Revenue per category / Ingresos por categoría",
     valid.groupby("category", as_index=False)["revenue"].sum()
          .sort_values("revenue", ascending=False))

# 5) Anti-join: customers without orders / clientes sin pedidos  (SQL ex. 12)
merged = customers.merge(orders, on="customer_id", how="left", indicator=True)
show("Customers without orders / Clientes sin pedidos", merged.loc[merged["_merge"] == "left_only", ["customer_id", "name"]])

# 6) Several aggregations at once / Varias agregaciones a la vez (named agg)
show("Summary per department / Resumen por departamento",
     employees.groupby("department").agg(
         employees=("emp_id", "count"),
         avg_salary=("salary", "mean"),
         max_salary=("salary", "max"),
     ).round(2).reset_index())

# 7) Top 1 per group with rank / Top 1 por grupo  (SQL ex. 26)
employees["rk"] = employees.groupby("department")["salary"].rank(method="dense", ascending=False)
show("Top earner per department / Mejor pagado por departamento", employees.loc[employees["rk"] == 1, ["department", "name", "salary"]])

# 8) Monthly series + growth / Serie mensual + crecimiento  (SQL ex. 28)
monthly = (valid.groupby(valid["order_date"].dt.to_period("M"))["revenue"].sum()
                .reset_index(name="revenue"))
monthly["prev_revenue"] = monthly["revenue"].shift(1)          # = LAG
monthly["mom_growth_pct"] = (monthly["revenue"].pct_change() * 100).round(1)
show("Monthly revenue / Ingresos mensuales", monthly)

# 9) Running total / Acumulado  (SQL ex. 27)
per_order = valid.groupby(["order_id", "order_date"], as_index=False)["revenue"].sum()
per_order = per_order.sort_values(["order_date", "order_id"])
per_order["running_revenue"] = per_order["revenue"].cumsum()
show("Running total / Acumulado", per_order.tail(3))

# 10) Pivot table: revenue by category (rows) and status (columns) / ingresos por categoría y estado
show("Pivot category × status / Pivot categoría × estado",
     sales.pivot_table(index="category", columns="status", values="revenue",
                       aggfunc="sum", fill_value=0).reset_index())

# 11) Data cleaning / Limpieza de datos
clean = customers.copy()
clean["city"] = clean["city"].fillna("Unknown")
clean["email"] = clean["email"].str.lower()
clean["signup_month"] = pd.to_datetime(clean["signup_date"]).dt.strftime("%Y-%m")
clean = clean.drop_duplicates(subset=["email"]).rename(columns={"name": "customer_name"})
show("Clean customers / Clientes limpios", clean[["customer_name", "city", "signup_month"]].head())

# 12) apply / map / CASE WHEN
products["bucket"] = pd.cut(products["price"], bins=[0, 40, 300, float("inf")],
                            labels=["Low", "Medium", "High"], right=False)
show("Price buckets / Buckets de precio", products[["name", "price", "bucket"]])
