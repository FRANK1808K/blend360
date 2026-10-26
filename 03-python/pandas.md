# 03b · pandas para análisis de datos

> Blend360 es una empresa de **analítica de datos**, así que en la prueba (o en la entrevista técnica) te pueden pedir que limpies, agregues o unas datos en Python. pandas es la herramienta estándar para eso. Si ya sabes SQL, pandas es lo mismo con otra sintaxis.

**Práctica ejecutable:** [`pandas_practica.py`](pandas_practica.py) resuelve en pandas varias preguntas del módulo de SQL usando la misma base de datos:

```bash
pip install pandas
python3 pandas_practica.py
```

---

## 1. Conceptos base

| Concepto | Qué es |
|---|---|
| `Series` | Una columna: arreglo 1D con índice |
| `DataFrame` | Una tabla: varias Series que comparten índice |
| Índice | Etiquetas de las filas (por defecto 0, 1, 2…) |
| `NaN` / `None` | Valor faltante (equivale al `NULL` de SQL) |

```python
import pandas as pd

df = pd.read_csv("ventas.csv")            # también: read_excel, read_sql, read_parquet, read_json
df.head(), df.tail(), df.sample(5)
df.shape                                  # (filas, columnas)
df.info()                                 # tipos + nulos
df.describe()                             # estadísticas de columnas numéricas
df.dtypes, df.columns
df["col"].value_counts()                  # frecuencia de cada valor
df["col"].nunique(), df["col"].unique()
```

## 2. Equivalencias SQL ↔ pandas

| SQL | pandas |
|---|---|
| `SELECT a, b FROM t` | `t[["a", "b"]]` |
| `WHERE x > 5` | `t[t["x"] > 5]` o `t.query("x > 5")` |
| `WHERE x > 5 AND y = 'A'` | `t[(t["x"] > 5) & (t["y"] == "A")]` ← usa `&`, `\|`, `~` **con paréntesis** |
| `WHERE y IN ('A','B')` | `t[t["y"].isin(["A", "B"])]` |
| `WHERE y IS NULL` | `t[t["y"].isna()]` |
| `WHERE name LIKE '%Desk%'` | `t[t["name"].str.contains("Desk")]` |
| `ORDER BY x DESC` | `t.sort_values("x", ascending=False)` |
| `LIMIT 5` | `t.head(5)` |
| `SELECT DISTINCT y` | `t["y"].drop_duplicates()` o `t["y"].unique()` |
| `COUNT(*) ... GROUP BY y` | `t.groupby("y").size()` |
| `SUM(x) ... GROUP BY y` | `t.groupby("y")["x"].sum()` |
| Varias agregaciones | `t.groupby("y").agg(total=("x", "sum"), prom=("x", "mean"))` |
| `HAVING SUM(x) > 100` | `g = t.groupby("y")["x"].sum(); g[g > 100]` |
| `INNER JOIN ... ON a.k = b.k` | `a.merge(b, on="k")` (por defecto `how="inner"`) |
| `LEFT JOIN` | `a.merge(b, on="k", how="left")` |
| Claves con nombre distinto | `a.merge(b, left_on="cust_id", right_on="id")` |
| `UNION ALL` | `pd.concat([a, b])` |
| `UNION` | `pd.concat([a, b]).drop_duplicates()` |
| `CASE WHEN` | `np.where(cond, "si", "no")`, `np.select(...)`, `pd.cut(...)` o `.apply(func)` |
| `COALESCE(x, 0)` | `t["x"].fillna(0)` |
| `ROW_NUMBER() OVER (PARTITION BY g ORDER BY x)` | `t.groupby("g")["x"].rank(method="first")` |
| `DENSE_RANK()` | `.rank(method="dense", ascending=False)` |
| `LAG(x)` | `t["x"].shift(1)` (o `t.groupby("g")["x"].shift(1)`) |
| `SUM(x) OVER (ORDER BY fecha)` | `t.sort_values("fecha")["x"].cumsum()` |
| `x / SUM(x) OVER ()` | `t["x"] / t["x"].sum()` |
| `SUM(x) OVER (PARTITION BY g)` | `t.groupby("g")["x"].transform("sum")` |

## 3. Selección: `loc` vs `iloc`

```python
df.loc[fila_etiqueta, "col"]          # por ETIQUETA (incluye el final en rangos)
df.loc[df["x"] > 5, ["a", "b"]]       # filtro + columnas: la forma recomendada
df.iloc[0:3, 0:2]                     # por POSICIÓN (excluye el final, como en Python)
df.at[0, "col"], df.iat[0, 0]         # un solo valor (rápido)
```

> ⚠️ **`SettingWithCopyWarning`:** evita `df[df.x > 5]["y"] = 0`. Usa `df.loc[df.x > 5, "y"] = 0`.

## 4. Limpieza de datos (siempre preguntan)

```python
df.isna().sum()                               # nulos por columna
df.dropna(subset=["email"])                   # quitar filas con nulos en una columna
df["city"] = df["city"].fillna("Unknown")      # rellenar nulos
df["age"] = df["age"].fillna(df["age"].median())   # imputar con mediana (robusta a outliers)
df.duplicated().sum(); df.drop_duplicates()
df["price"] = pd.to_numeric(df["price"], errors="coerce")   # lo inválido → NaN
df["date"] = pd.to_datetime(df["date"], errors="coerce")
df["name"] = df["name"].str.strip().str.title()
df = df.rename(columns={"old": "new"})
df = df.drop(columns=["tmp"])
df["col"] = df["col"].astype("category")
```

**Outliers con IQR** (rango intercuartílico):

```python
q1, q3 = df["x"].quantile([0.25, 0.75])
iqr = q3 - q1
outliers = df[(df["x"] < q1 - 1.5 * iqr) | (df["x"] > q3 + 1.5 * iqr)]
```

## 5. Columnas nuevas

```python
df["revenue"] = df["quantity"] * df["unit_price"]          # vectorizado: rápido
df["is_big"] = df["revenue"] > 1000
df["bucket"] = pd.cut(df["price"], bins=[0, 40, 300, float("inf")], labels=["Low", "Medium", "High"])
df["segment"] = df["revenue"].apply(lambda r: "VIP" if r > 2000 else "Regular")   # más lento
df["month"] = df["date"].dt.to_period("M")                   # también .dt.year, .dt.month, .dt.day_name()
df["domain"] = df["email"].str.split("@").str[1]
```

> 💡 **Vectoriza.** Las operaciones sobre columnas completas (`df["a"] * df["b"]`) son mucho más rápidas que recorrer filas con `for` o `iterrows()`. Si en la entrevista dices esto, suma puntos.

## 6. Reshape: pivot y melt

```python
# largo → ancho
pd.pivot_table(df, index="category", columns="status", values="revenue", aggfunc="sum", fill_value=0)
# ancho → largo
pd.melt(wide, id_vars=["category"], var_name="status", value_name="revenue")
pd.crosstab(df["segment"], df["country"])   # tabla de frecuencias
```

## 7. Mini-ejercicios (con solución)

Usa los DataFrames de `pandas_practica.py` (`customers`, `orders`, `items`, `products`, `employees`).

1. ¿Cuántos clientes por segmento hay en Colombia?
2. Ingreso total por cliente (nombre) en pedidos no cancelados, de mayor a menor.
3. Agrega a `employees` una columna con el salario promedio de su departamento y otra con la diferencia frente a ese promedio.
4. ¿Qué porcentaje de pedidos está cancelado?

<details>
<summary>Soluciones</summary>

```python
# 1
customers[customers["country"] == "Colombia"].groupby("segment").size()

# 2
sales = items.merge(orders, on="order_id").merge(customers[["customer_id", "name"]], on="customer_id")
sales["revenue"] = sales["quantity"] * sales["unit_price"]
(sales[sales["status"] != "cancelled"]
     .groupby("name")["revenue"].sum()
     .sort_values(ascending=False))

# 3  (transform devuelve un valor POR FILA, como una función de ventana)
employees["dept_avg"] = employees.groupby("department")["salary"].transform("mean")
employees["diff_vs_avg"] = employees["salary"] - employees["dept_avg"]

# 4
(orders["status"] == "cancelled").mean() * 100   # la media de un booleano = proporción de True
```

</details>

---

**Siguiente:** [04 · Algoritmos y estructuras de datos](../04-algoritmos-y-estructuras/README.md)
