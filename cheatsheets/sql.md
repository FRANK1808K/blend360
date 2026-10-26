# Cheatsheet: SQL (1 página)

🌐 **Español** · [English](sql.en.md)

```sql
-- Orden de ESCRITURA                       -- Orden LÓGICO de ejecución
SELECT DISTINCT col, AGG(x) AS a            -- 5 SELECT  6 DISTINCT
FROM t1 JOIN t2 ON t1.k = t2.k              -- 1 FROM / JOIN
WHERE condición_de_filas                    -- 2 WHERE  (sin agregados)
GROUP BY col                                -- 3 GROUP BY
HAVING condición_de_grupos                  -- 4 HAVING (con agregados)
ORDER BY a DESC                             -- 7 ORDER BY (acepta alias)
LIMIT 10 OFFSET 0;                          -- 8 LIMIT
```

| Necesito… | Uso |
|---|---|
| Nulos | `IS NULL`, `COALESCE(x, 0)`, `NULLIF(y, 0)` · `COUNT(col)` ignora NULL |
| Texto | `LIKE 'A%'` (`%` = varios, `_` = uno) · `UPPER`, `TRIM`, `SUBSTR`, `\|\|` / `CONCAT` |
| Rango | `BETWEEN a AND b` (inclusivo) · `IN (...)` |
| Evitar división entera | `100.0 * a / b` |
| Condicional | `CASE WHEN ... THEN ... ELSE ... END` |
| Contar por condición | `SUM(CASE WHEN cond THEN 1 ELSE 0 END)` |
| Sin coincidencia (anti-join) | `LEFT JOIN b ... WHERE b.id IS NULL` / `NOT EXISTS (...)` |
| "Ambas condiciones por grupo" | `HAVING COUNT(DISTINCT cat) = 2` |
| Duplicados | `GROUP BY cols HAVING COUNT(*) > 1` |
| N-ésimo valor | `DENSE_RANK() OVER (ORDER BY x DESC) = N` (en CTE) |
| Top N por grupo | `ROW_NUMBER() OVER (PARTITION BY g ORDER BY x DESC) <= N` (en CTE) |
| Acumulado | `SUM(x) OVER (ORDER BY fecha)` |
| % del total | `x * 100.0 / SUM(x) OVER ()` |
| Fila anterior / siguiente | `LAG(x) OVER (...)` / `LEAD(x) OVER (...)` |
| Mes contra mes | `(x - LAG(x) OVER (ORDER BY mes)) * 100.0 / LAG(x) OVER (ORDER BY mes)` |
| Promedio móvil 3 | `AVG(x) OVER (ORDER BY f ROWS BETWEEN 2 PRECEDING AND CURRENT ROW)` |
| Rachas consecutivas | `fecha - ROW_NUMBER() OVER (ORDER BY fecha)` → agrupar |

**Empates (9000, 9000, 7000):** `ROW_NUMBER` 1, 2, 3 · `RANK` 1, 1, 3 · `DENSE_RANK` 1, 1, 2.

**JOINs:** `INNER` = solo coincidencias · `LEFT` = toda la izquierda + NULL · `FULL` = todo · `CROSS` = A × B · Self join = la tabla consigo misma.
⚠️ Un filtro sobre la tabla derecha en el `WHERE` convierte el `LEFT` en `INNER` → ponlo en el `ON`.

**UNION** (sin duplicados) vs. **UNION ALL** (con duplicados, más rápido). **DELETE** (DML, filtra) vs. **TRUNCATE** (DDL, todo) vs. **DROP** (borra la tabla).

**Motores:** límite `LIMIT` / `TOP` (SQL Server) · mes `strftime('%Y-%m', d)` (SQLite), `DATE_TRUNC('month', d)` (PostgreSQL), `FORMAT(d, 'yyyy-MM')` (SQL Server).
