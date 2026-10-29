# 02 · SQL — De cero a nivel prueba técnica

**Español** · [English](README.en.md)

> SQL es probablemente **el tema con más peso** en una prueba de una empresa de analítica como Blend360. Aquí cubres todo lo que suele preguntarse: desde `SELECT` hasta funciones de ventana.

**Cómo practicar:**

- **Sin instalar nada (recomendado):** el [laboratorio SQL del simulador](../simulator/README.md#laboratorio-de-código) tiene estos mismos 35 ejercicios. Escribes la consulta, la ejecutas y te dice si el resultado es correcto; funciona en el celular. Incluye un **reto de 5 consultas en 60 minutos**.
- **En tu computador:**

```bash
cd 02-sql
python3 setup_db.py --shell      # crea practice.db y abre una consola SQL
```

También puedes abrir `practice.db` con [DB Browser for SQLite](https://sqlitebrowser.org/) o DBeaver. Para practicar en línea están [sqliteonline.com](https://sqliteonline.com/), [LeetCode SQL 50](https://leetcode.com/studyplan/top-sql-50/), [HackerRank SQL](https://www.hackerrank.com/domains/sql) y [DataLemur](https://datalemur.com/).

Después de leer esta guía → [ejercicios.md](ejercicios.md) (35 ejercicios con solución).

---

## Índice

1. [El modelo de datos de práctica](#1-el-modelo-de-datos-de-práctica)
2. [Orden lógico de ejecución (¡clave!)](#2-orden-lógico-de-ejecución-clave)
3. [SELECT, WHERE, ORDER BY, LIMIT](#3-select-where-order-by-limit)
4. [NULL: la trampa favorita](#4-null-la-trampa-favorita)
5. [Agregaciones: GROUP BY y HAVING](#5-agregaciones-group-by-y-having)
6. [JOINs](#6-joins)
7. [Subconsultas y CTEs](#7-subconsultas-y-ctes)
8. [CASE WHEN](#8-case-when)
9. [Funciones de ventana](#9-funciones-de-ventana-window-functions)
10. [UNION, INTERSECT, EXCEPT](#10-union-intersect-except)
11. [Fechas y textos](#11-fechas-y-textos)
12. [DDL, DML y transacciones](#12-ddl-dml-y-transacciones)
13. [Patrones clásicos de entrevista](#13-patrones-clásicos-de-entrevista)
14. [Diferencias entre motores](#14-diferencias-entre-motores)

---

## 1. El modelo de datos de práctica

```text
customers (customer_id PK, name, email, city, country, segment, signup_date)
    │ 1
    │
    │ N
orders (order_id PK, customer_id FK, order_date, status)
    │ 1
    │
    │ N
order_items (order_id FK, product_id FK, quantity, unit_price)   PK = (order_id, product_id)
    │ N
    │
    │ 1
products (product_id PK, name, category, price)

employees (emp_id PK, name, department, salary, manager_id FK → employees.emp_id, hire_date)
```

Trampas que puse **a propósito** para que practiques:

- Carlos (customer 6) **nunca compró** → sirve para practicar `LEFT JOIN ... IS NULL`.
- El producto 9 (Desk Lamp) **nunca se vendió**.
- Carlos tiene `city = NULL` y Diego tiene `email = NULL`.
- Algunos pedidos están `cancelled`, y en esos casos casi nunca debes contar la venta.
- `unit_price` (precio real de la venta) a veces ≠ `products.price` (precio de lista), por descuentos.
- Camila y Julián ganan **lo mismo** (9000), lo que sirve para practicar empates con `RANK` y `DENSE_RANK`.

## 2. Orden lógico de ejecución (¡clave!)

Escribes en este orden:

```sql
SELECT ... FROM ... JOIN ... WHERE ... GROUP BY ... HAVING ... ORDER BY ... LIMIT ...
```

Pero el motor lo **evalúa** así:

| Paso | Cláusula | Qué hace |
|---|---|---|
| 1 | `FROM` / `JOIN` | Arma la tabla base combinando tablas |
| 2 | `WHERE` | Filtra **filas** (no puede usar agregados) |
| 3 | `GROUP BY` | Agrupa filas |
| 4 | `HAVING` | Filtra **grupos** (sí usa agregados) |
| 5 | `SELECT` | Calcula columnas, alias y funciones de ventana |
| 6 | `DISTINCT` | Elimina duplicados |
| 7 | `ORDER BY` | Ordena (aquí **sí** puedes usar alias del SELECT) |
| 8 | `LIMIT` / `OFFSET` | Recorta el resultado |

Consecuencias que preguntan mucho:

- ✗ `WHERE SUM(x) > 10` → error. ✓ Va en `HAVING`.
- ✗ `WHERE alias > 10` (alias definido en SELECT) → error en la mayoría de motores. ✓ Usa subconsulta/CTE.
- ✗ `WHERE ROW_NUMBER() OVER(...) = 1` → error. ✓ Calcula la ventana en una CTE y filtra afuera.
- ✓ `ORDER BY alias` funciona.

## 3. SELECT, WHERE, ORDER BY, LIMIT

```sql
SELECT name, price, price * 1.19 AS price_with_tax   -- columna calculada + alias
FROM products
WHERE category = 'Electronics'
  AND price BETWEEN 20 AND 500        -- BETWEEN es inclusivo en ambos extremos
ORDER BY price DESC                    -- DESC = mayor a menor; ASC (por defecto) = menor a mayor
LIMIT 3;                               -- SQL Server: SELECT TOP 3 ... ; Oracle/estándar: FETCH FIRST 3 ROWS ONLY
```

Operadores de filtro:

| Operador | Ejemplo | Nota |
|---|---|---|
| `=`, `<>` o `!=`, `<`, `>`, `<=`, `>=` | `price >= 100` | |
| `AND`, `OR`, `NOT` | `a AND (b OR c)` | `AND` tiene prioridad sobre `OR`. **Usa paréntesis.** |
| `IN (...)` | `country IN ('USA','Peru')` | Equivale a varios `OR` |
| `BETWEEN a AND b` | `order_date BETWEEN '2024-03-01' AND '2024-03-31'` | Inclusivo |
| `LIKE` | `name LIKE 'A%'` | `%` = cualquier cantidad de caracteres; `_` = exactamente uno |
| `IS NULL` / `IS NOT NULL` | `city IS NULL` | **Nunca** `= NULL` |
| `DISTINCT` | `SELECT DISTINCT country` | Quita filas repetidas del resultado |

## 4. NULL: la trampa favorita

`NULL` significa "desconocido" y **no es igual a nada, ni siquiera a otro NULL**.

| Expresión | Resultado |
|---|---|
| `NULL = NULL` | `NULL` (no TRUE) → la fila **no** pasa el WHERE |
| `NULL + 5` | `NULL` |
| `COUNT(*)` | Cuenta **todas** las filas |
| `COUNT(columna)` | Cuenta filas donde la columna **no** es NULL |
| `AVG(columna)` | Ignora los NULL (divide solo entre los no nulos) |
| `col NOT IN (1, 2, NULL)` | Nunca devuelve filas (si la subconsulta del `NOT IN` puede traer NULL, usa `NOT EXISTS`) |

```sql
SELECT COUNT(*) AS total, COUNT(city) AS con_ciudad FROM customers;  -- 10 y 9
SELECT name, COALESCE(city, 'Sin ciudad') AS city FROM customers;     -- reemplaza NULL
SELECT NULLIF(0, 0);                                                  -- NULL: útil para evitar dividir entre 0
```

## 5. Agregaciones: GROUP BY y HAVING

Funciones agregadas: `COUNT`, `SUM`, `AVG`, `MIN`, `MAX` (y `COUNT(DISTINCT col)`).

**Regla de oro:** toda columna del `SELECT` que **no** esté dentro de una función agregada **debe** estar en el `GROUP BY`.

```sql
-- Ingresos por categoría, solo pedidos no cancelados, solo categorías con más de 1000
SELECT p.category,
       COUNT(DISTINCT oi.order_id)        AS pedidos,
       SUM(oi.quantity * oi.unit_price)   AS ingresos
FROM order_items oi
JOIN products p ON p.product_id = oi.product_id
JOIN orders   o ON o.order_id   = oi.order_id
WHERE o.status <> 'cancelled'          -- filtro de FILAS (antes de agrupar)
GROUP BY p.category
HAVING SUM(oi.quantity * oi.unit_price) > 1000   -- filtro de GRUPOS
ORDER BY ingresos DESC;
```

## 6. JOINs

```text
INNER JOIN       LEFT JOIN         RIGHT JOIN        FULL OUTER JOIN     CROSS JOIN
  A ∩ B          todo A + match    match + todo B    todo A + todo B     A × B (todas las combinaciones)
```

| Tipo | Devuelve | Filas sin pareja |
|---|---|---|
| `INNER JOIN` (o solo `JOIN`) | Solo filas con coincidencia en ambas | Se descartan |
| `LEFT JOIN` | Todas las de la izquierda | Columnas de la derecha = `NULL` |
| `RIGHT JOIN` | Todas las de la derecha | Columnas de la izquierda = `NULL` |
| `FULL OUTER JOIN` | Todas las de ambas | `NULL` del lado que falte |
| `CROSS JOIN` | Producto cartesiano: filas(A) × filas(B) | — |
| **Self join** | Una tabla unida consigo misma (p. ej., empleado ↔ jefe) | — |

```sql
-- Anti-join: clientes que NUNCA compraron
SELECT c.name
FROM customers c
LEFT JOIN orders o ON o.customer_id = c.customer_id
WHERE o.order_id IS NULL;

-- Self join: cada empleado con su jefe
SELECT e.name AS empleado, m.name AS jefe
FROM employees e
LEFT JOIN employees m ON m.emp_id = e.manager_id;
```

**Trampa clásica:** si pones una condición sobre la tabla de la derecha en el `WHERE` de un `LEFT JOIN`, este se convierte en `INNER JOIN`. Ponla en el `ON`:

```sql
-- MAL: elimina a los clientes sin pedidos entregados (y a los que no tienen pedidos)
SELECT c.name, o.order_id FROM customers c
LEFT JOIN orders o ON o.customer_id = c.customer_id
WHERE o.status = 'delivered';

-- BIEN: conserva a todos los clientes
SELECT c.name, o.order_id FROM customers c
LEFT JOIN orders o ON o.customer_id = c.customer_id AND o.status = 'delivered';
```

**Cardinalidad:** si unes A con B y cada fila de A tiene 3 coincidencias en B, obtienes 3 filas por fila de A. Por eso un `SUM` después de un JOIN puede salir **inflado**. Pregúntate siempre: ¿cuántas filas por clave hay en cada lado?

## 7. Subconsultas y CTEs

```sql
-- Subconsulta escalar (devuelve un solo valor)
SELECT name, price FROM products
WHERE price > (SELECT AVG(price) FROM products);

-- Subconsulta con IN
SELECT name FROM customers
WHERE customer_id IN (SELECT customer_id FROM orders WHERE status = 'cancelled');

-- EXISTS / NOT EXISTS (seguro frente a NULLs)
SELECT p.name FROM products p
WHERE NOT EXISTS (SELECT 1 FROM order_items oi WHERE oi.product_id = p.product_id);

-- Subconsulta correlacionada: se evalúa por cada fila externa
SELECT e.name, e.department, e.salary
FROM employees e
WHERE e.salary > (SELECT AVG(salary) FROM employees x WHERE x.department = e.department);
```

**CTE** (`WITH`): es una "tabla temporal con nombre" que hace la consulta legible. **Úsala en la prueba**, porque se lee y se corrige mejor.

```sql
WITH order_totals AS (
    SELECT order_id, SUM(quantity * unit_price) AS total
    FROM order_items
    GROUP BY order_id
)
SELECT o.customer_id, AVG(t.total) AS ticket_promedio
FROM orders o
JOIN order_totals t ON t.order_id = o.order_id
WHERE o.status <> 'cancelled'
GROUP BY o.customer_id;
```

## 8. CASE WHEN

```sql
SELECT name, price,
       CASE
           WHEN price >= 300 THEN 'Alto'
           WHEN price >= 40  THEN 'Medio'
           ELSE 'Bajo'
       END AS rango_precio
FROM products;

-- "Pivot" manual / agregación condicional (MUY preguntado)
SELECT
    SUM(CASE WHEN status = 'delivered' THEN 1 ELSE 0 END) AS entregados,
    SUM(CASE WHEN status = 'cancelled' THEN 1 ELSE 0 END) AS cancelados,
    ROUND(100.0 * SUM(CASE WHEN status = 'cancelled' THEN 1 ELSE 0 END) / COUNT(*), 1) AS pct_cancelados
FROM orders;
```

> **Consejo:** `100.0 * x / y`: el `.0` evita la **división entera** (en SQLite, PostgreSQL y SQL Server `3/2 = 1`).

## 9. Funciones de ventana (window functions)

Calculan algo **sobre un conjunto de filas relacionadas sin colapsarlas** (a diferencia de `GROUP BY`).

```sql
funcion() OVER (PARTITION BY grupo ORDER BY orden [ROWS BETWEEN ...])
```

| Función | Para qué | Empates (9000, 9000, 7000) |
|---|---|---|
| `ROW_NUMBER()` | Numerar 1, 2, 3… sin repetir | 1, 2, 3 |
| `RANK()` | Ranking con saltos | 1, 1, 3 |
| `DENSE_RANK()` | Ranking sin saltos | 1, 1, 2 |
| `NTILE(n)` | Dividir en n cubetas (cuartiles, deciles) | — |
| `LAG(col, n)` / `LEAD(col, n)` | Valor de la fila anterior/siguiente | — |
| `SUM/AVG/COUNT(...) OVER (...)` | Totales, acumulados, promedios móviles | — |
| `FIRST_VALUE` / `LAST_VALUE` | Primer/último valor de la ventana | — |

```sql
-- Top 1 salario por departamento (patrón "top N por grupo")
WITH ranked AS (
    SELECT name, department, salary,
           DENSE_RANK() OVER (PARTITION BY department ORDER BY salary DESC) AS rk
    FROM employees
)
SELECT * FROM ranked WHERE rk = 1;

-- Acumulado de ventas por fecha (running total)
SELECT order_date, total,
       SUM(total) OVER (ORDER BY order_date) AS acumulado
FROM (SELECT o.order_date, SUM(oi.quantity * oi.unit_price) AS total
      FROM orders o JOIN order_items oi ON oi.order_id = o.order_id
      GROUP BY o.order_id, o.order_date) t;

-- Diferencia con el pedido anterior del mismo cliente
SELECT customer_id, order_date,
       LAG(order_date) OVER (PARTITION BY customer_id ORDER BY order_date) AS pedido_anterior
FROM orders;

-- Promedio móvil de 3 filas
SELECT order_id, AVG(order_id) OVER (ORDER BY order_id ROWS BETWEEN 2 PRECEDING AND CURRENT ROW) AS movil
FROM orders;
```

> **Atención:** `LAST_VALUE` con `ORDER BY` usa por defecto el marco `RANGE BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW`, así que devuelve la fila **actual**. Para el último de verdad, usa `ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING`.

## 10. UNION, INTERSECT, EXCEPT

| Operador | Resultado |
|---|---|
| `UNION` | Filas de ambas consultas **sin duplicados** (más lento: tiene que deduplicar) |
| `UNION ALL` | Filas de ambas **con duplicados** (más rápido) |
| `INTERSECT` | Filas presentes en ambas |
| `EXCEPT` (Oracle: `MINUS`) | Filas de la primera que no están en la segunda |

Regla: las consultas deben tener **el mismo número de columnas** con tipos compatibles.

## 11. Fechas y textos

| Necesidad | SQLite | PostgreSQL | SQL Server | MySQL |
|---|---|---|---|---|
| Año | `strftime('%Y', d)` | `EXTRACT(YEAR FROM d)` | `YEAR(d)` | `YEAR(d)` |
| Mes "2024-03" | `strftime('%Y-%m', d)` | `TO_CHAR(d,'YYYY-MM')` | `FORMAT(d,'yyyy-MM')` | `DATE_FORMAT(d,'%Y-%m')` |
| Truncar a mes | `date(d,'start of month')` | `DATE_TRUNC('month', d)` | `DATETRUNC(month, d)` | — |
| Días entre fechas | `julianday(b)-julianday(a)` | `b - a` | `DATEDIFF(day,a,b)` | `DATEDIFF(b,a)` |
| Hoy | `date('now')` | `CURRENT_DATE` | `GETDATE()` | `CURDATE()` |

Textos: `UPPER`, `LOWER`, `LENGTH` (SQL Server: `LEN`), `TRIM`, `SUBSTR`/`SUBSTRING`, `REPLACE`, concatenación con `||` (SQLite/PostgreSQL/Oracle) o `CONCAT()` (MySQL/SQL Server).

## 12. DDL, DML y transacciones

| Tipo | Significado | Comandos |
|---|---|---|
| **DDL** | Data Definition Language | `CREATE`, `ALTER`, `DROP`, `TRUNCATE` |
| **DML** | Data Manipulation Language | `SELECT`, `INSERT`, `UPDATE`, `DELETE` |
| **DCL** | Data Control Language | `GRANT`, `REVOKE` |
| **TCL** | Transaction Control Language | `BEGIN`, `COMMIT`, `ROLLBACK`, `SAVEPOINT` |

```sql
CREATE TABLE reviews (
    review_id  INTEGER PRIMARY KEY,
    product_id INTEGER NOT NULL REFERENCES products(product_id),
    rating     INTEGER CHECK (rating BETWEEN 1 AND 5),
    created_at DATE DEFAULT CURRENT_DATE
);
INSERT INTO reviews (review_id, product_id, rating) VALUES (1, 2, 5);
UPDATE products SET price = price * 1.10 WHERE category = 'Stationery';   -- sin WHERE actualiza TODO
DELETE FROM reviews WHERE rating < 2;
CREATE INDEX idx_orders_customer ON orders(customer_id);
CREATE VIEW v_delivered AS SELECT * FROM orders WHERE status = 'delivered';
```

**`DELETE` vs `TRUNCATE` vs `DROP`:**

| | `DELETE` | `TRUNCATE` | `DROP` |
|---|---|---|---|
| Qué borra | Filas (con `WHERE` opcional) | Todas las filas | La tabla completa (estructura + datos) |
| Tipo | DML | DDL | DDL |
| Se puede filtrar | Sí | No | No |
| Velocidad | Lento (fila por fila) | Rápido | Rápido |

## 13. Patrones clásicos de entrevista

| Pregunta típica | Patrón |
|---|---|
| "Segundo salario más alto" | `DENSE_RANK() ... = 2`, o `MAX(salary) WHERE salary < (SELECT MAX(salary) ...)` |
| "Top N por categoría" | `ROW_NUMBER()/DENSE_RANK() OVER (PARTITION BY ...)` + filtrar en CTE |
| "Registros duplicados" | `GROUP BY cols HAVING COUNT(*) > 1` |
| "Clientes sin compras" | `LEFT JOIN ... WHERE derecha.id IS NULL` o `NOT EXISTS` |
| "Acumulado / running total" | `SUM() OVER (ORDER BY fecha)` |
| "Crecimiento mes a mes (MoM)" | Agregar por mes + `LAG()` + `(actual - anterior) / anterior` |
| "% del total" | `x / SUM(x) OVER ()` |
| "Empleados que ganan más que su jefe" | Self join |
| "Primera compra de cada cliente" | `MIN(fecha)` por cliente, o `ROW_NUMBER() = 1` |
| "Pivot / conteos por estado" | `SUM(CASE WHEN ... THEN 1 ELSE 0 END)` |
| "Días consecutivos" | `fecha - ROW_NUMBER()` (gaps and islands) |

## 14. Diferencias entre motores

Si en la prueba no te dicen qué motor usan, lo más probable es que sea **PostgreSQL, MySQL o SQL Server**. En HackerRank puedes elegirlo. Lo que más cambia:

| Concepto | Estándar / PostgreSQL | MySQL | SQL Server |
|---|---|---|---|
| Limitar filas | `LIMIT 5` / `FETCH FIRST 5 ROWS ONLY` | `LIMIT 5` | `SELECT TOP 5` / `OFFSET 0 ROWS FETCH NEXT 5 ROWS ONLY` |
| Concatenar | `a \|\| b` | `CONCAT(a,b)` | `a + b` o `CONCAT(a,b)` |
| Si es nulo | `COALESCE(a,b)` | `IFNULL(a,b)` / `COALESCE` | `ISNULL(a,b)` / `COALESCE` |
| Autoincremento | `SERIAL` / `GENERATED AS IDENTITY` | `AUTO_INCREMENT` | `IDENTITY(1,1)` |

> **Consejo:** `COALESCE` funciona en **todos**. Úsalo y no te equivocas.

---

## Autoevaluación rápida (responde sin mirar)

1. ¿Qué diferencia hay entre `WHERE` y `HAVING`?
2. ¿Qué devuelve `COUNT(email)` en `customers`? (Pista: Diego tiene email NULL.)
3. ¿Por qué `WHERE salary = NULL` nunca devuelve filas?
4. Con salarios 9000, 9000, 7000, ¿qué devuelven `RANK` y `DENSE_RANK`?
5. ¿Cuándo un `LEFT JOIN` se comporta como `INNER JOIN` sin que lo notes?

<details>
<summary>Respuestas</summary>

1. `WHERE` filtra filas **antes** de agrupar; `HAVING` filtra grupos **después** y puede usar agregados.
2. 9: `COUNT(col)` ignora los NULL.
3. Porque `x = NULL` da NULL (desconocido), no TRUE. Se usa `IS NULL`.
4. `RANK`: 1, 1, 3. `DENSE_RANK`: 1, 1, 2.
5. Cuando filtras columnas de la tabla derecha en el `WHERE` (por ejemplo, `WHERE o.status = 'delivered'`): las filas sin pareja tienen NULL y se eliminan.

</details>
