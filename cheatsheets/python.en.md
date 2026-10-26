# Cheat sheet: Python + pandas (1 page)

```python
# Strings
s[::-1]; s.lower(); s.split(); ",".join(lst); s.strip(); s.replace(a, b); f"{x:.2f}"
# Lists
lst.append(x); lst.pop(); lst.sort()  # in-place, returns None
sorted(lst, key=lambda v: (-v[1], v[0]))       # new list: value desc, name asc
lst[a:b]  # b excluded   lst[-1]  # last
# Dict / set
d.get(k, 0); d.items(); k in d   # O(1)
set(lst); a | b; a & b; a - b
# Comprehensions
[f(x) for x in xs if cond]; {k: v for k, v in pairs}; [x for row in m for x in row]
# collections
from collections import Counter, defaultdict, deque
Counter(xs).most_common(3); defaultdict(list); deque().popleft()
import heapq; heapq.nlargest(k, xs)
# Utilities
enumerate(xs); zip(a, b); any(...); all(...); sum(...); min/max(..., key=...)
```

| Trap | Remember |
|---|---|
| `7 / 2` → 3.5 · `7 // 2` → 3 · `-7 // 2` → −4 · `7 % 2` → 1 | |
| `b = a` (list) does **not copy** | `a.copy()`, `a[:]`, `copy.deepcopy` |
| `def f(x=[])` | The mutable default argument is shared between calls → use `None` |
| `[[0]*3]*3` | 3 references to the same row → `[[0]*3 for _ in range(3)]` |
| Falsy | `0, "", [], {}, set(), None, False` |
| `is` vs `==` | `is` = same object (use it only with `None`) |
| 1-element tuple | `(1,)` |
| `{}` | empty dict; empty set = `set()` |
| `"a" + 1` | `TypeError` · `int("x")` → `ValueError` · `d["no"]` → `KeyError` |

**pandas:**

```python
df[df["x"] > 5]                                   # WHERE
df[(df.a > 1) & (df.b == "X")]                    # AND (& | ~, with parentheses)
df.sort_values("x", ascending=False).head(5)      # ORDER BY ... LIMIT
df.groupby("g").agg(total=("x", "sum"), n=("x", "count")).reset_index()
a.merge(b, on="k", how="left")                    # LEFT JOIN
df["x"].fillna(0); df.dropna(subset=["c"]); df.drop_duplicates()
df.groupby("g")["x"].transform("mean")            # one value per row (like OVER)
df["x"].shift(1); df["x"].cumsum(); df["x"].pct_change()   # LAG, running total, % change
df.groupby("g")["x"].rank(method="dense", ascending=False)
pd.pivot_table(df, index="a", columns="b", values="x", aggfunc="sum", fill_value=0)
pd.to_datetime(df.d).dt.to_period("M"); pd.to_numeric(s, errors="coerce")
```
