# 02 · SQL — from zero to technical-test level

🌐 [Español](README.md) · **English**

> SQL is probably **the heaviest topic** in a test from an analytics company like Blend360. This module covers everything that is usually asked, from `SELECT` to window functions.

**How to practice:**

- **Nothing to install (recommended):** the [simulator's SQL lab](../simulator/README.en.md#code-lab) has these same 35 exercises. You write the query, run it, and it tells you whether the result is right; it works on your phone. It includes a **challenge of 5 queries in 60 minutes**.
- **On your computer:**

```bash
cd 02-sql
python3 setup_db.py --shell      # creates practice.db and opens a SQL console
```

You can also open `practice.db` with [DB Browser for SQLite](https://sqlitebrowser.org/) or DBeaver. To practice online: [sqliteonline.com](https://sqliteonline.com/), [LeetCode SQL 50](https://leetcode.com/studyplan/top-sql-50/), [HackerRank SQL](https://www.hackerrank.com/domains/sql) and [DataLemur](https://datalemur.com/).

After this guide → [ejercicios.en.md](ejercicios.en.md) (35 exercises with solutions).

---

## Contents

1. [The practice data model](#1-the-practice-data-model)
2. [Logical order of execution (key!)](#2-logical-order-of-execution-key)
3. [SELECT, WHERE, ORDER BY, LIMIT](#3-select-where-order-by-limit)
4. [NULL: the favorite trap](#4-null-the-favorite-trap)
5. [Aggregations: GROUP BY and HAVING](#5-aggregations-group-by-and-having)
6. [JOINs](#6-joins)
7. [Subqueries and CTEs](#7-subqueries-and-ctes)
8. [CASE WHEN](#8-case-when)
9. [Window functions](#9-window-functions)
10. [UNION, INTERSECT, EXCEPT](#10-union-intersect-except)
11. [Dates and text](#11-dates-and-text)
12. [DDL, DML and transactions](#12-ddl-dml-and-transactions)
13. [Classic interview patterns](#13-classic-interview-patterns)
14. [Differences between engines](#14-differences-between-engines)

---

## 1. The practice data model

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

Traps I added **on purpose** so you can practice:

- Carlos (customer 6) **never bought anything** → practice for `LEFT JOIN ... IS NULL`.
- Product 9 (Desk Lamp) **was never sold**.
- Carlos has `city = NULL` and Diego has `email = NULL`.
- Some orders are `cancelled`; in those cases you almost never count the sale.
- `unit_price` (the real sale price) is sometimes ≠ `products.price` (list price), because of discounts.
- Camila and Julián earn **the same** (9000), to practice ties with `RANK` and `DENSE_RANK`.

## 2. Logical order of execution (key!)

You write it in this order:

```sql
SELECT ... FROM ... JOIN ... WHERE ... GROUP BY ... HAVING ... ORDER BY ... LIMIT ...
```

But the engine **evaluates** it like this:

| Step | Clause | What it does |
|---|---|---|
| 1 | `FROM` / `JOIN` | Builds the base table by combining tables |
| 2 | `WHERE` | Filters **rows** (cannot use aggregates) |
| 3 | `GROUP BY` | Groups rows |
| 4 | `HAVING` | Filters **groups** (can use aggregates) |
| 5 | `SELECT` | Computes columns, aliases and window functions |
| 6 | `DISTINCT` | Removes duplicates |
| 7 | `ORDER BY` | Sorts (here you **can** use aliases from the SELECT) |
| 8 | `LIMIT` / `OFFSET` | Cuts the result |

Consequences that are asked a lot:

- ❌ `WHERE SUM(x) > 10` → error. ✅ It goes in `HAVING`.
- ❌ `WHERE alias > 10` (alias defined in the SELECT) → error in most engines. ✅ Use a subquery/CTE.
- ❌ `WHERE ROW_NUMBER() OVER(...) = 1` → error. ✅ Compute the window in a CTE and filter outside.
- ✅ `ORDER BY alias` works.

## 3. SELECT, WHERE, ORDER BY, LIMIT

```sql
SELECT name, price, price * 1.19 AS price_with_tax   -- computed column + alias
FROM products
WHERE category = 'Electronics'
  AND price BETWEEN 20 AND 500        -- BETWEEN is inclusive on both ends
ORDER BY price DESC                    -- DESC = highest to lowest; ASC (default) = lowest to highest
LIMIT 3;                               -- SQL Server: SELECT TOP 3 ... ; Oracle/standard: FETCH FIRST 3 ROWS ONLY
```

Filter operators:

| Operator | Example | Note |
|---|---|---|
| `=`, `<>` or `!=`, `<`, `>`, `<=`, `>=` | `price >= 100` | |
| `AND`, `OR`, `NOT` | `a AND (b OR c)` | `AND` has priority over `OR`. **Use parentheses.** |
| `IN (...)` | `country IN ('USA','Peru')` | Same as several `OR`s |
| `BETWEEN a AND b` | `order_date BETWEEN '2024-03-01' AND '2024-03-31'` | Inclusive |
| `LIKE` | `name LIKE 'A%'` | `%` = any number of characters; `_` = exactly one |
| `IS NULL` / `IS NOT NULL` | `city IS NULL` | **Never** `= NULL` |
| `DISTINCT` | `SELECT DISTINCT country` | Removes repeated rows from the result |

## 4. NULL: the favorite trap

`NULL` means "unknown" and it is **not equal to anything, not even another NULL**.

| Expression | Result |
|---|---|
| `NULL = NULL` | `NULL` (not TRUE) → the row does **not** pass the WHERE |
| `NULL + 5` | `NULL` |
| `COUNT(*)` | Counts **all** rows |
| `COUNT(column)` | Counts rows where the column is **not** NULL |
| `AVG(column)` | Ignores NULLs (divides only by the non-null values) |
| `col NOT IN (1, 2, NULL)` | Never returns rows ⚠️ (if the `NOT IN` subquery can return NULL, use `NOT EXISTS`) |

```sql
SELECT COUNT(*) AS total, COUNT(city) AS with_city FROM customers;  -- 10 and 9
SELECT name, COALESCE(city, 'No city') AS city FROM customers;      -- replaces NULL
SELECT NULLIF(0, 0);                                                -- NULL: useful to avoid dividing by 0
```

## 5. Aggregations: GROUP BY and HAVING

Aggregate functions: `COUNT`, `SUM`, `AVG`, `MIN`, `MAX` (and `COUNT(DISTINCT col)`).

**Golden rule:** every column in the `SELECT` that is **not** inside an aggregate function **must** be in the `GROUP BY`.

```sql
-- Revenue per category, only non-cancelled orders, only categories above 1000
SELECT p.category,
       COUNT(DISTINCT oi.order_id)        AS orders,
       SUM(oi.quantity * oi.unit_price)   AS revenue
FROM order_items oi
JOIN products p ON p.product_id = oi.product_id
JOIN orders   o ON o.order_id   = oi.order_id
WHERE o.status <> 'cancelled'          -- ROW filter (before grouping)
GROUP BY p.category
HAVING SUM(oi.quantity * oi.unit_price) > 1000   -- GROUP filter
ORDER BY revenue DESC;
```

## 6. JOINs

```text
INNER JOIN       LEFT JOIN          RIGHT JOIN          FULL OUTER JOIN     CROSS JOIN
  A ∩ B          all of A + match   match + all of B    all of A + all of B A × B (every combination)
```

| Type | Returns | Rows without a match |
|---|---|---|
| `INNER JOIN` (or just `JOIN`) | Only rows that match in both | Discarded |
| `LEFT JOIN` | All rows from the left table | Right-table columns = `NULL` |
| `RIGHT JOIN` | All rows from the right table | Left-table columns = `NULL` |
| `FULL OUTER JOIN` | All rows from both | `NULL` on the missing side |
| `CROSS JOIN` | Cartesian product: rows(A) × rows(B) | — |
| **Self join** | A table joined with itself (e.g., employee ↔ manager) | — |

```sql
-- Anti-join: customers who NEVER bought
SELECT c.name
FROM customers c
LEFT JOIN orders o ON o.customer_id = c.customer_id
WHERE o.order_id IS NULL;

-- Self join: each employee with their manager
SELECT e.name AS employee, m.name AS manager
FROM employees e
LEFT JOIN employees m ON m.emp_id = e.manager_id;
```

⚠️ **Classic trap:** if you put a condition on the right table in the `WHERE` of a `LEFT JOIN`, it turns into an `INNER JOIN`. Put it in the `ON`:

```sql
-- WRONG: removes customers without delivered orders (and those without orders)
SELECT c.name, o.order_id FROM customers c
LEFT JOIN orders o ON o.customer_id = c.customer_id
WHERE o.status = 'delivered';

-- RIGHT: keeps every customer
SELECT c.name, o.order_id FROM customers c
LEFT JOIN orders o ON o.customer_id = c.customer_id AND o.status = 'delivered';
```

⚠️ **Cardinality:** if you join A with B and each row of A has 3 matches in B, you get 3 rows per row of A. That is why a `SUM` after a JOIN can come out **inflated**. Always ask yourself: how many rows per key are there on each side?

## 7. Subqueries and CTEs

```sql
-- Scalar subquery (returns a single value)
SELECT name, price FROM products
WHERE price > (SELECT AVG(price) FROM products);

-- Subquery with IN
SELECT name FROM customers
WHERE customer_id IN (SELECT customer_id FROM orders WHERE status = 'cancelled');

-- EXISTS / NOT EXISTS (safe with NULLs)
SELECT p.name FROM products p
WHERE NOT EXISTS (SELECT 1 FROM order_items oi WHERE oi.product_id = p.product_id);

-- Correlated subquery: evaluated for each outer row
SELECT e.name, e.department, e.salary
FROM employees e
WHERE e.salary > (SELECT AVG(salary) FROM employees x WHERE x.department = e.department);
```

A **CTE** (`WITH`) is a "named temporary table" that makes the query readable. **Use it in the test**: it is easier to read and to fix.

```sql
WITH order_totals AS (
    SELECT order_id, SUM(quantity * unit_price) AS total
    FROM order_items
    GROUP BY order_id
)
SELECT o.customer_id, AVG(t.total) AS average_ticket
FROM orders o
JOIN order_totals t ON t.order_id = o.order_id
WHERE o.status <> 'cancelled'
GROUP BY o.customer_id;
```

## 8. CASE WHEN

```sql
SELECT name, price,
       CASE
           WHEN price >= 300 THEN 'High'
           WHEN price >= 40  THEN 'Medium'
           ELSE 'Low'
       END AS price_range
FROM products;

-- Manual "pivot" / conditional aggregation (asked A LOT)
SELECT
    SUM(CASE WHEN status = 'delivered' THEN 1 ELSE 0 END) AS delivered,
    SUM(CASE WHEN status = 'cancelled' THEN 1 ELSE 0 END) AS cancelled,
    ROUND(100.0 * SUM(CASE WHEN status = 'cancelled' THEN 1 ELSE 0 END) / COUNT(*), 1) AS pct_cancelled
FROM orders;
```

> 💡 `100.0 * x / y`: the `.0` avoids **integer division** (in SQLite, PostgreSQL and SQL Server `3/2 = 1`).

## 9. Window functions

They compute something **over a set of related rows without collapsing them** (unlike `GROUP BY`).

```sql
function() OVER (PARTITION BY group ORDER BY order [ROWS BETWEEN ...])
```

| Function | Use | Ties (9000, 9000, 7000) |
|---|---|---|
| `ROW_NUMBER()` | Number 1, 2, 3… without repeats | 1, 2, 3 |
| `RANK()` | Ranking with gaps | 1, 1, 3 |
| `DENSE_RANK()` | Ranking without gaps | 1, 1, 2 |
| `NTILE(n)` | Split into n buckets (quartiles, deciles) | — |
| `LAG(col, n)` / `LEAD(col, n)` | Value of the previous/next row | — |
| `SUM/AVG/COUNT(...) OVER (...)` | Totals, running totals, moving averages | — |
| `FIRST_VALUE` / `LAST_VALUE` | First/last value of the window | — |

```sql
-- Top 1 salary per department ("top N per group" pattern)
WITH ranked AS (
    SELECT name, department, salary,
           DENSE_RANK() OVER (PARTITION BY department ORDER BY salary DESC) AS rk
    FROM employees
)
SELECT * FROM ranked WHERE rk = 1;

-- Running total of sales by date
SELECT order_date, total,
       SUM(total) OVER (ORDER BY order_date) AS running_total
FROM (SELECT o.order_date, SUM(oi.quantity * oi.unit_price) AS total
      FROM orders o JOIN order_items oi ON oi.order_id = o.order_id
      GROUP BY o.order_id, o.order_date) t;

-- Previous order of the same customer
SELECT customer_id, order_date,
       LAG(order_date) OVER (PARTITION BY customer_id ORDER BY order_date) AS previous_order
FROM orders;

-- 3-row moving average
SELECT order_id, AVG(order_id) OVER (ORDER BY order_id ROWS BETWEEN 2 PRECEDING AND CURRENT ROW) AS moving_avg
FROM orders;
```

> ⚠️ `LAST_VALUE` with `ORDER BY` uses the default frame `RANGE BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW`, so it returns the **current** row. For the real last value use `ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING`.

## 10. UNION, INTERSECT, EXCEPT

| Operator | Result |
|---|---|
| `UNION` | Rows from both queries **without duplicates** (slower: it has to deduplicate) |
| `UNION ALL` | Rows from both **with duplicates** (faster) |
| `INTERSECT` | Rows present in both |
| `EXCEPT` (Oracle: `MINUS`) | Rows from the first query that are not in the second |

Rule: the queries must have **the same number of columns**, with compatible types.

## 11. Dates and text

| Need | SQLite | PostgreSQL | SQL Server | MySQL |
|---|---|---|---|---|
| Year | `strftime('%Y', d)` | `EXTRACT(YEAR FROM d)` | `YEAR(d)` | `YEAR(d)` |
| Month "2024-03" | `strftime('%Y-%m', d)` | `TO_CHAR(d,'YYYY-MM')` | `FORMAT(d,'yyyy-MM')` | `DATE_FORMAT(d,'%Y-%m')` |
| Truncate to month | `date(d,'start of month')` | `DATE_TRUNC('month', d)` | `DATETRUNC(month, d)` | — |
| Days between dates | `julianday(b)-julianday(a)` | `b - a` | `DATEDIFF(day,a,b)` | `DATEDIFF(b,a)` |
| Today | `date('now')` | `CURRENT_DATE` | `GETDATE()` | `CURDATE()` |

Text: `UPPER`, `LOWER`, `LENGTH` (SQL Server: `LEN`), `TRIM`, `SUBSTR`/`SUBSTRING`, `REPLACE`, concatenation with `||` (SQLite/PostgreSQL/Oracle) or `CONCAT()` (MySQL/SQL Server).

## 12. DDL, DML and transactions

| Type | Meaning | Commands |
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
UPDATE products SET price = price * 1.10 WHERE category = 'Stationery';   -- ⚠️ without WHERE it updates EVERYTHING
DELETE FROM reviews WHERE rating < 2;
CREATE INDEX idx_orders_customer ON orders(customer_id);
CREATE VIEW v_delivered AS SELECT * FROM orders WHERE status = 'delivered';
```

**`DELETE` vs `TRUNCATE` vs `DROP`:**

| | `DELETE` | `TRUNCATE` | `DROP` |
|---|---|---|---|
| What it removes | Rows (optional `WHERE`) | All rows | The whole table (structure + data) |
| Type | DML | DDL | DDL |
| Can filter | Yes | No | No |
| Speed | Slow (row by row) | Fast | Fast |

## 13. Classic interview patterns

| Typical question | Pattern |
|---|---|
| "Second highest salary" | `DENSE_RANK() ... = 2`, or `MAX(salary) WHERE salary < (SELECT MAX(salary) ...)` |
| "Top N per category" | `ROW_NUMBER()/DENSE_RANK() OVER (PARTITION BY ...)` + filter in a CTE |
| "Duplicate records" | `GROUP BY cols HAVING COUNT(*) > 1` |
| "Customers without purchases" | `LEFT JOIN ... WHERE right.id IS NULL` or `NOT EXISTS` |
| "Running total" | `SUM() OVER (ORDER BY date)` |
| "Month-over-month (MoM) growth" | Aggregate by month + `LAG()` + `(current - previous) / previous` |
| "% of total" | `x / SUM(x) OVER ()` |
| "Employees who earn more than their manager" | Self join |
| "First purchase of each customer" | `MIN(date)` per customer, or `ROW_NUMBER() = 1` |
| "Pivot / counts per status" | `SUM(CASE WHEN ... THEN 1 ELSE 0 END)` |
| "Consecutive days" | `date - ROW_NUMBER()` (gaps and islands) |

## 14. Differences between engines

If the test does not say which engine it uses, it is most likely **PostgreSQL, MySQL or SQL Server** (on HackerRank you can choose). What changes the most:

| Concept | Standard / PostgreSQL | MySQL | SQL Server |
|---|---|---|---|
| Limit rows | `LIMIT 5` / `FETCH FIRST 5 ROWS ONLY` | `LIMIT 5` | `SELECT TOP 5` / `OFFSET 0 ROWS FETCH NEXT 5 ROWS ONLY` |
| Concatenate | `a \|\| b` | `CONCAT(a,b)` | `a + b` or `CONCAT(a,b)` |
| If null | `COALESCE(a,b)` | `IFNULL(a,b)` / `COALESCE` | `ISNULL(a,b)` / `COALESCE` |
| Auto-increment | `SERIAL` / `GENERATED AS IDENTITY` | `AUTO_INCREMENT` | `IDENTITY(1,1)` |

> 💡 `COALESCE` works **everywhere**. Use it and you cannot go wrong.

---

## Quick self-assessment (answer without looking)

1. What is the difference between `WHERE` and `HAVING`?
2. What does `COUNT(email)` return on `customers`? (Hint: Diego's email is NULL.)
3. Why does `WHERE salary = NULL` never return rows?
4. With salaries 9000, 9000, 7000, what do `RANK` and `DENSE_RANK` return?
5. When does a `LEFT JOIN` behave like an `INNER JOIN` without you noticing?

<details>
<summary>Answers</summary>

1. `WHERE` filters rows **before** grouping; `HAVING` filters groups **after** and can use aggregates.
2. 9: `COUNT(col)` ignores NULLs.
3. Because `x = NULL` gives NULL (unknown), not TRUE. Use `IS NULL`.
4. `RANK`: 1, 1, 3. `DENSE_RANK`: 1, 1, 2.
5. When you filter columns of the right table in the `WHERE` (for example, `WHERE o.status = 'delivered'`): unmatched rows have NULL and are removed.

</details>
