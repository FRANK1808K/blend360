# Cheat sheet: SQL (1 page)

```sql
-- WRITING order                            -- LOGICAL order of execution
SELECT DISTINCT col, AGG(x) AS a            -- 5 SELECT  6 DISTINCT
FROM t1 JOIN t2 ON t1.k = t2.k              -- 1 FROM / JOIN
WHERE row_condition                         -- 2 WHERE  (no aggregates)
GROUP BY col                                -- 3 GROUP BY
HAVING group_condition                      -- 4 HAVING (with aggregates)
ORDER BY a DESC                             -- 7 ORDER BY (accepts aliases)
LIMIT 10 OFFSET 0;                          -- 8 LIMIT
```

| I need… | Use |
|---|---|
| Nulls | `IS NULL`, `COALESCE(x, 0)`, `NULLIF(y, 0)` · `COUNT(col)` ignores NULLs |
| Text | `LIKE 'A%'` (`%` = many, `_` = one) · `UPPER`, `TRIM`, `SUBSTR`, `\|\|` / `CONCAT` |
| Range | `BETWEEN a AND b` (inclusive) · `IN (...)` |
| Avoid integer division | `100.0 * a / b` |
| Conditional | `CASE WHEN ... THEN ... ELSE ... END` |
| Count by condition | `SUM(CASE WHEN cond THEN 1 ELSE 0 END)` |
| No match (anti-join) | `LEFT JOIN b ... WHERE b.id IS NULL` / `NOT EXISTS (...)` |
| "Both conditions per group" | `HAVING COUNT(DISTINCT cat) = 2` |
| Duplicates | `GROUP BY cols HAVING COUNT(*) > 1` |
| Nth value | `DENSE_RANK() OVER (ORDER BY x DESC) = N` (in a CTE) |
| Top N per group | `ROW_NUMBER() OVER (PARTITION BY g ORDER BY x DESC) <= N` (in a CTE) |
| Running total | `SUM(x) OVER (ORDER BY date)` |
| % of total | `x * 100.0 / SUM(x) OVER ()` |
| Previous / next row | `LAG(x) OVER (...)` / `LEAD(x) OVER (...)` |
| Month over month | `(x - LAG(x) OVER (ORDER BY month)) * 100.0 / LAG(x) OVER (ORDER BY month)` |
| 3-row moving average | `AVG(x) OVER (ORDER BY d ROWS BETWEEN 2 PRECEDING AND CURRENT ROW)` |
| Consecutive streaks | `date - ROW_NUMBER() OVER (ORDER BY date)` → group by it |

**Ties (9000, 9000, 7000):** `ROW_NUMBER` 1, 2, 3 · `RANK` 1, 1, 3 · `DENSE_RANK` 1, 1, 2.

**JOINs:** `INNER` = matches only · `LEFT` = all of the left + NULL · `FULL` = everything · `CROSS` = A × B · Self join = a table with itself.
⚠️ A filter on the right table in the `WHERE` turns a `LEFT` into an `INNER` → put it in the `ON`.

**UNION** (no duplicates) vs. **UNION ALL** (with duplicates, faster). **DELETE** (DML, filters) vs. **TRUNCATE** (DDL, everything) vs. **DROP** (removes the table).

**Engines:** limit `LIMIT` / `TOP` (SQL Server) · month `strftime('%Y-%m', d)` (SQLite), `DATE_TRUNC('month', d)` (PostgreSQL), `FORMAT(d, 'yyyy-MM')` (SQL Server).
