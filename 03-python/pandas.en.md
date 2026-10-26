# 03b · pandas for data analysis

> Blend360 is a **data analytics** company: in the test (or in the technical interview) you may be asked to clean, aggregate or join data in Python. pandas is the standard tool for that. If you already know SQL, pandas is the same thing with a different syntax.

**Runnable practice:** [`pandas_practica.py`](pandas_practica.py) solves several questions from the SQL module in pandas, using the same database:

```bash
pip install pandas
python3 pandas_practica.py
```

---

## 1. Core concepts

| Concept | What it is |
|---|---|
| `Series` | One column: a 1D array with an index |
| `DataFrame` | A table: several Series that share an index |
| Index | Row labels (0, 1, 2… by default) |
| `NaN` / `None` | Missing value (the equivalent of SQL's `NULL`) |

```python
import pandas as pd

df = pd.read_csv("sales.csv")             # also: read_excel, read_sql, read_parquet, read_json
df.head(), df.tail(), df.sample(5)
df.shape                                  # (rows, columns)
df.info()                                 # types + nulls
df.describe()                             # statistics of the numeric columns
df.dtypes, df.columns
df["col"].value_counts()                  # frequency of each value
df["col"].nunique(), df["col"].unique()
```

## 2. SQL ↔ pandas equivalents

| SQL | pandas |
|---|---|
| `SELECT a, b FROM t` | `t[["a", "b"]]` |
| `WHERE x > 5` | `t[t["x"] > 5]` or `t.query("x > 5")` |
| `WHERE x > 5 AND y = 'A'` | `t[(t["x"] > 5) & (t["y"] == "A")]` ← use `&`, `\|`, `~` **with parentheses** |
| `WHERE y IN ('A','B')` | `t[t["y"].isin(["A", "B"])]` |
| `WHERE y IS NULL` | `t[t["y"].isna()]` |
| `WHERE name LIKE '%Desk%'` | `t[t["name"].str.contains("Desk")]` |
| `ORDER BY x DESC` | `t.sort_values("x", ascending=False)` |
| `LIMIT 5` | `t.head(5)` |
| `SELECT DISTINCT y` | `t["y"].drop_duplicates()` or `t["y"].unique()` |
| `COUNT(*) ... GROUP BY y` | `t.groupby("y").size()` |
| `SUM(x) ... GROUP BY y` | `t.groupby("y")["x"].sum()` |
| Several aggregations | `t.groupby("y").agg(total=("x", "sum"), avg=("x", "mean"))` |
| `HAVING SUM(x) > 100` | `g = t.groupby("y")["x"].sum(); g[g > 100]` |
| `INNER JOIN ... ON a.k = b.k` | `a.merge(b, on="k")` (`how="inner"` by default) |
| `LEFT JOIN` | `a.merge(b, on="k", how="left")` |
| Keys with different names | `a.merge(b, left_on="cust_id", right_on="id")` |
| `UNION ALL` | `pd.concat([a, b])` |
| `UNION` | `pd.concat([a, b]).drop_duplicates()` |
| `CASE WHEN` | `np.where(cond, "yes", "no")`, `np.select(...)`, `pd.cut(...)` or `.apply(func)` |
| `COALESCE(x, 0)` | `t["x"].fillna(0)` |
| `ROW_NUMBER() OVER (PARTITION BY g ORDER BY x)` | `t.groupby("g")["x"].rank(method="first")` |
| `DENSE_RANK()` | `.rank(method="dense", ascending=False)` |
| `LAG(x)` | `t["x"].shift(1)` (or `t.groupby("g")["x"].shift(1)`) |
| `SUM(x) OVER (ORDER BY date)` | `t.sort_values("date")["x"].cumsum()` |
| `x / SUM(x) OVER ()` | `t["x"] / t["x"].sum()` |
| `SUM(x) OVER (PARTITION BY g)` | `t.groupby("g")["x"].transform("sum")` |

## 3. Selection: `loc` vs `iloc`

```python
df.loc[row_label, "col"]              # by LABEL (includes the end in ranges)
df.loc[df["x"] > 5, ["a", "b"]]       # filter + columns: the recommended way
df.iloc[0:3, 0:2]                     # by POSITION (excludes the end, like Python)
df.at[0, "col"], df.iat[0, 0]         # a single value (fast)
```

> ⚠️ **`SettingWithCopyWarning`:** avoid `df[df.x > 5]["y"] = 0`. Use `df.loc[df.x > 5, "y"] = 0`.

## 4. Data cleaning (always asked)

```python
df.isna().sum()                               # nulls per column
df.dropna(subset=["email"])                   # drop rows with nulls in one column
df["city"] = df["city"].fillna("Unknown")      # fill nulls
df["age"] = df["age"].fillna(df["age"].median())   # impute with the median (robust to outliers)
df.duplicated().sum(); df.drop_duplicates()
df["price"] = pd.to_numeric(df["price"], errors="coerce")   # invalid → NaN
df["date"] = pd.to_datetime(df["date"], errors="coerce")
df["name"] = df["name"].str.strip().str.title()
df = df.rename(columns={"old": "new"})
df = df.drop(columns=["tmp"])
df["col"] = df["col"].astype("category")
```

**Outliers with the IQR** (interquartile range):

```python
q1, q3 = df["x"].quantile([0.25, 0.75])
iqr = q3 - q1
outliers = df[(df["x"] < q1 - 1.5 * iqr) | (df["x"] > q3 + 1.5 * iqr)]
```

## 5. New columns

```python
df["revenue"] = df["quantity"] * df["unit_price"]          # vectorized: fast
df["is_big"] = df["revenue"] > 1000
df["bucket"] = pd.cut(df["price"], bins=[0, 40, 300, float("inf")], labels=["Low", "Medium", "High"])
df["segment"] = df["revenue"].apply(lambda r: "VIP" if r > 2000 else "Regular")   # slower
df["month"] = df["date"].dt.to_period("M")                   # also .dt.year, .dt.month, .dt.day_name()
df["domain"] = df["email"].str.split("@").str[1]
```

> 💡 **Vectorize.** Operations on whole columns (`df["a"] * df["b"]`) are much faster than looping over rows with `for` or `iterrows()`. Saying this in the interview earns points.

## 6. Reshaping: pivot and melt

```python
# long → wide
pd.pivot_table(df, index="category", columns="status", values="revenue", aggfunc="sum", fill_value=0)
# wide → long
pd.melt(wide, id_vars=["category"], var_name="status", value_name="revenue")
pd.crosstab(df["segment"], df["country"])   # frequency table
```

## 7. Mini exercises (with solutions)

Use the DataFrames from `pandas_practica.py` (`customers`, `orders`, `items`, `products`, `employees`).

1. How many customers per segment are there in Colombia?
2. Total revenue per customer (name) on non-cancelled orders, from highest to lowest.
3. Add to `employees` a column with the average salary of their department and another with the difference from that average.
4. What percentage of orders is cancelled?

<details>
<summary>Solutions</summary>

```python
# 1
customers[customers["country"] == "Colombia"].groupby("segment").size()

# 2
sales = items.merge(orders, on="order_id").merge(customers[["customer_id", "name"]], on="customer_id")
sales["revenue"] = sales["quantity"] * sales["unit_price"]
(sales[sales["status"] != "cancelled"]
     .groupby("name")["revenue"].sum()
     .sort_values(ascending=False))

# 3  (transform returns one value PER ROW, like a window function)
employees["dept_avg"] = employees.groupby("department")["salary"].transform("mean")
employees["diff_vs_avg"] = employees["salary"] - employees["dept_avg"]

# 4
(orders["status"] == "cancelled").mean() * 100   # the mean of a boolean = share of True
```

</details>

---

**Next:** [04 · Algorithms and data structures](../04-algoritmos-y-estructuras/README.en.md)
