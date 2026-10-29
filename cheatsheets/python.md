# Cheatsheet: Python + pandas (1 página)

**Español** · [English](python.en.md)

```python
# Strings
s[::-1]; s.lower(); s.split(); ",".join(lst); s.strip(); s.replace(a, b); f"{x:.2f}"
# Listas
lst.append(x); lst.pop(); lst.sort()  # in-place, devuelve None
sorted(lst, key=lambda v: (-v[1], v[0]))       # nueva lista: valor desc, nombre asc
lst[a:b]  # b excluido   lst[-1]  # último
# Dict / set
d.get(k, 0); d.items(); k in d   # O(1)
set(lst); a | b; a & b; a - b
# Comprensiones
[f(x) for x in xs if cond]; {k: v for k, v in pares}; [x for fila in m for x in fila]
# collections
from collections import Counter, defaultdict, deque
Counter(xs).most_common(3); defaultdict(list); deque().popleft()
import heapq; heapq.nlargest(k, xs)
# Utilidades
enumerate(xs); zip(a, b); any(...); all(...); sum(...); min/max(..., key=...)
```

| Trampa | Recuerda |
|---|---|
| `7 / 2` → 3.5 · `7 // 2` → 3 · `-7 // 2` → −4 · `7 % 2` → 1 | |
| `b = a` (lista) **no copia** | `a.copy()`, `a[:]`, `copy.deepcopy` |
| `def f(x=[])` | El argumento por defecto mutable se comparte entre llamadas → usa `None` |
| `[[0]*3]*3` | 3 referencias a la misma fila → `[[0]*3 for _ in range(3)]` |
| Falsy | `0, "", [], {}, set(), None, False` |
| `is` vs `==` | `is` = mismo objeto (úsalo solo con `None`) |
| Tupla con 1 elemento | `(1,)` |
| `{}` | dict vacío; set vacío = `set()` |
| `"a" + 1` | `TypeError` · `int("x")` → `ValueError` · `d["no"]` → `KeyError` |

**pandas:**

```python
df[df["x"] > 5]                                   # WHERE
df[(df.a > 1) & (df.b == "X")]                    # AND (& | ~, con paréntesis)
df.sort_values("x", ascending=False).head(5)      # ORDER BY ... LIMIT
df.groupby("g").agg(total=("x", "sum"), n=("x", "count")).reset_index()
a.merge(b, on="k", how="left")                    # LEFT JOIN
df["x"].fillna(0); df.dropna(subset=["c"]); df.drop_duplicates()
df.groupby("g")["x"].transform("mean")            # valor por fila (como OVER)
df["x"].shift(1); df["x"].cumsum(); df["x"].pct_change()   # LAG, acumulado, % de cambio
df.groupby("g")["x"].rank(method="dense", ascending=False)
pd.pivot_table(df, index="a", columns="b", values="x", aggfunc="sum", fill_value=0)
pd.to_datetime(df.d).dt.to_period("M"); pd.to_numeric(s, errors="coerce")
```
