# 02 · SQL — 35 exercises with solutions

> **How to use this file:**
>
> 1. Run `python3 setup_db.py --shell` (or open `practice.db` in DB Browser).
> 2. Read the statement. If you get stuck on the English, the Spanish version is in [ejercicios.md](ejercicios.md).
> 3. Write your query **before** opening the solution. Compare your result with the "Expected result".
> 4. Mark ✅ the ones you solve on the first try and redo the ❌ ones two days later.
>
> The solutions are verified automatically with `python3 check_solutions.py`.
> Data model: see [README.en.md](README.en.md#1-the-practice-data-model).

| Level | Exercises | Target time per exercise |
|---|---|---|
| 🟢 Basic | 1–10 | 2–3 min |
| 🟡 JOINs and subqueries | 11–21 | 4–5 min |
| 🟠 CASE and window functions | 22–32 | 5–7 min |
| 🔴 Interview challenges | 33–35 | 8–10 min |

---

## 🟢 Basic level

### 1. Filter and sort

**Write a query that returns the name and price of all products in the `Electronics` category, sorted from the most expensive to the cheapest.**

<details>
<summary>Solution</summary>

```sql
SELECT name, price
FROM products
WHERE category = 'Electronics'
ORDER BY price DESC;
```

Expected result:

```text
name           | price
---------------+--------
Laptop Pro 14  | 1200.00
Monitor 27"    | 300.00
USB-C Hub      | 45.00
Wireless Mouse | 25.00
(4 rows)
```

</details>

### 2. Multiple conditions

**List the name, city and signup date of customers from Colombia who signed up on or after March 1st, 2024.**

<details>
<summary>Solution</summary>

```sql
SELECT name, city, signup_date
FROM customers
WHERE country = 'Colombia'
  AND signup_date >= '2024-03-01'
ORDER BY signup_date;
```

Expected result:

```text
name         | city         | signup_date
-------------+--------------+------------
Sofía Torres | Bogotá       | 2024-03-25
Carlos Díaz  | NULL         | 2024-04-02
Pedro Castro | Barranquilla | 2024-05-07
Diego Vargas | Medellín     | 2024-06-12
(4 rows)
```

> Dates in ISO format (`YYYY-MM-DD`) can be compared as text.

</details>

### 3. Missing values

**Return the customers whose city is unknown (missing).**

<details>
<summary>Solution</summary>

```sql
SELECT customer_id, name
FROM customers
WHERE city IS NULL;
```

Expected result:

```text
customer_id | name
------------+------------
6           | Carlos Díaz
(1 row)
```

> ❌ `WHERE city = NULL` returns 0 rows.

</details>

### 4. Count per group

**How many customers are there in each country? Show the country with the most customers first.**

<details>
<summary>Solution</summary>

```sql
SELECT country, COUNT(*) AS customers
FROM customers
GROUP BY country
ORDER BY customers DESC;
```

Expected result:

```text
country  | customers
---------+----------
Colombia | 7
USA      | 2
Peru     | 1
(3 rows)
```

</details>

### 5. Pattern matching

**Find all the products whose name contains the word "Desk".**

<details>
<summary>Solution</summary>

```sql
SELECT product_id, name
FROM products
WHERE name LIKE '%Desk%';
```

Expected result:

```text
product_id | name
-----------+--------------
5          | Standing Desk
9          | Desk Lamp
(2 rows)
```

</details>

### 6. Unique values

**Return the list of distinct order statuses, in alphabetical order.**

<details>
<summary>Solution</summary>

```sql
SELECT DISTINCT status
FROM orders
ORDER BY status;
```

Expected result:

```text
status
---------
cancelled
delivered
shipped
(3 rows)
```

</details>

### 7. Total revenue

**Calculate the total revenue (quantity × unit price) of all orders that were NOT cancelled.**

<details>
<summary>Solution</summary>

```sql
SELECT SUM(oi.quantity * oi.unit_price) AS total_revenue
FROM order_items oi
JOIN orders o ON o.order_id = oi.order_id
WHERE o.status <> 'cancelled';
```

Expected result:

```text
total_revenue
-------------
8489.50
(1 row)
```

> Revenue is calculated with `unit_price` (what was actually charged), not with `products.price`.

</details>

### 8. Count by status

**Count how many orders there are for each status.**

<details>
<summary>Solution</summary>

```sql
SELECT status, COUNT(*) AS orders
FROM orders
GROUP BY status
ORDER BY orders DESC;
```

Expected result:

```text
status    | orders
----------+-------
delivered | 11
shipped   | 2
cancelled | 2
(3 rows)
```

</details>

### 9. HAVING

**Show the average salary of each department, rounded to 2 decimals, but only for departments whose average salary is greater than 8,000.**

<details>
<summary>Solution</summary>

```sql
SELECT department, ROUND(AVG(salary), 2) AS avg_salary
FROM employees
GROUP BY department
HAVING AVG(salary) > 8000
ORDER BY avg_salary DESC;
```

Expected result:

```text
department  | avg_salary
------------+-----------
Executive   | 25000.00
Engineering | 10500.00
Data        | 9750.00
(3 rows)
```

</details>

### 10. Revenue by category

**Calculate the revenue of each product category (excluding cancelled orders), from highest to lowest.**

<details>
<summary>Solution</summary>

```sql
SELECT p.category, SUM(oi.quantity * oi.unit_price) AS revenue
FROM order_items oi
JOIN products p ON p.product_id = oi.product_id
JOIN orders   o ON o.order_id   = oi.order_id
WHERE o.status <> 'cancelled'
GROUP BY p.category
ORDER BY revenue DESC;
```

Expected result:

```text
category    | revenue
------------+--------
Electronics | 6515.00
Furniture   | 1770.00
Stationery  | 204.50
(3 rows)
```

</details>

---

## 🟡 JOINs and subqueries

### 11. INNER JOIN

**List every order with its id, date, status and the name of the customer who placed it. Sort by date.**

<details>
<summary>Solution</summary>

```sql
SELECT o.order_id, o.order_date, o.status, c.name
FROM orders o
JOIN customers c ON c.customer_id = o.customer_id
ORDER BY o.order_date;
```

Expected result:

```text
order_id | order_date | status    | name
---------+------------+-----------+-------------
101      | 2024-02-01 | delivered | Ana Gómez
102      | 2024-02-14 | delivered | Luis Pérez
103      | 2024-03-05 | delivered | Ana Gómez
104      | 2024-03-18 | cancelled | María Ruiz
105      | 2024-04-02 | delivered | John Smith
106      | 2024-04-10 | delivered | Sofía Torres
107      | 2024-04-22 | shipped   | Luis Pérez
108      | 2024-05-01 | delivered | Emily Brown
109      | 2024-05-15 | delivered | Ana Gómez
110      | 2024-05-20 | delivered | Pedro Castro
111      | 2024-06-03 | delivered | Sofía Torres
112      | 2024-06-15 | cancelled | Laura Moreno
113      | 2024-06-28 | delivered | John Smith
114      | 2024-07-04 | delivered | Luis Pérez
115      | 2024-07-19 | shipped   | Diego Vargas
(15 rows)
```

</details>

### 12. Customers without orders

**Find the customers who have never placed an order.**

<details>
<summary>Solution</summary>

```sql
SELECT c.customer_id, c.name
FROM customers c
LEFT JOIN orders o ON o.customer_id = c.customer_id
WHERE o.order_id IS NULL;
```

Expected result:

```text
customer_id | name
------------+------------
6           | Carlos Díaz
(1 row)
```

> **Anti-join** pattern. Alternative: `WHERE NOT EXISTS (SELECT 1 FROM orders o WHERE o.customer_id = c.customer_id)`.

</details>

### 13. Products never sold

**Which products have never been sold? Use `NOT EXISTS`.**

<details>
<summary>Solution</summary>

```sql
SELECT p.product_id, p.name
FROM products p
WHERE NOT EXISTS (
    SELECT 1 FROM order_items oi WHERE oi.product_id = p.product_id
);
```

Expected result:

```text
product_id | name
-----------+----------
9          | Desk Lamp
(1 row)
```

</details>

### 14. Self join

**Show each employee's name together with their manager's name. Employees without a manager must also appear.**

<details>
<summary>Solution</summary>

```sql
SELECT e.name AS employee, m.name AS manager
FROM employees e
LEFT JOIN employees m ON m.emp_id = e.manager_id
ORDER BY e.emp_id;
```

Expected result:

```text
employee       | manager
---------------+---------------
Valentina Ríos | NULL
Andrés López   | Valentina Ríos
Camila Herrera | Andrés López
Julián Mejía   | Andrés López
Paula Ortiz    | Andrés López
Felipe Rojas   | Valentina Ríos
Natalia Cruz   | Felipe Rojas
Santiago Gil   | Felipe Rojas
Isabel Suárez  | Valentina Ríos
Mateo Ramírez  | Isabel Suárez
Daniel Pardo   | Natalia Cruz
(11 rows)
```

> With an `INNER JOIN` the CEO would disappear (her `manager_id` is NULL).

</details>

### 15. Earning more than the manager

**Find the employees who earn more than their direct manager.**

<details>
<summary>Solution</summary>

```sql
SELECT e.name AS employee, e.salary, m.name AS manager, m.salary AS manager_salary
FROM employees e
JOIN employees m ON m.emp_id = e.manager_id
WHERE e.salary > m.salary;
```

Expected result:

```text
employee     | salary | manager      | manager_salary
-------------+--------+--------------+---------------
Daniel Pardo | 11000  | Natalia Cruz | 10000
(1 row)
```

</details>

### 16. Spend per customer (including zero)

**For every customer, show the total amount spent on non-cancelled orders. Customers with no purchases must appear with 0.**

<details>
<summary>Solution</summary>

```sql
SELECT c.name,
       COALESCE(SUM(oi.quantity * oi.unit_price), 0) AS total_spent
FROM customers c
LEFT JOIN orders o
       ON o.customer_id = c.customer_id
      AND o.status <> 'cancelled'          -- the filter goes in the ON so no customer is lost
LEFT JOIN order_items oi ON oi.order_id = o.order_id
GROUP BY c.customer_id, c.name
ORDER BY total_spent DESC, c.name;
```

Expected result:

```text
name         | total_spent
-------------+------------
Sofía Torres | 2750.00
Luis Pérez   | 2405.00
Ana Gómez    | 1595.00
John Smith   | 1350.00
Pedro Castro | 270.00
Diego Vargas | 90.00
Emily Brown  | 29.50
Carlos Díaz  | 0
Laura Moreno | 0
María Ruiz   | 0
(10 rows)
```

> María and Laura only have cancelled orders → they show 0, just like Carlos.

</details>

### 17. Above the average

**List the products whose price is greater than the average price of all products.**

<details>
<summary>Solution</summary>

```sql
SELECT name, price
FROM products
WHERE price > (SELECT AVG(price) FROM products)
ORDER BY price DESC;
```

Expected result:

```text
name          | price
--------------+--------
Laptop Pro 14 | 1200.00
Standing Desk | 350.00
Monitor 27"   | 300.00
(3 rows)
```

</details>

### 18. Correlated subquery

**Find the employees who earn more than the average salary of their own department.**

<details>
<summary>Solution</summary>

```sql
SELECT e.name, e.department, e.salary
FROM employees e
WHERE e.salary > (
    SELECT AVG(x.salary) FROM employees x WHERE x.department = e.department
)
ORDER BY e.department, e.salary DESC;
```

Expected result:

```text
name          | department  | salary
--------------+-------------+-------
Andrés López  | Data        | 14000
Felipe Rojas  | Engineering | 13000
Daniel Pardo  | Engineering | 11000
Isabel Suárez | Marketing   | 9500
(4 rows)
```

</details>

### 19. Second highest salary

**Return the second highest distinct salary in the company.**

<details>
<summary>Solution</summary>

```sql
SELECT MAX(salary) AS second_highest
FROM employees
WHERE salary < (SELECT MAX(salary) FROM employees);
```

Expected result:

```text
second_highest
--------------
14000
(1 row)
```

> Alternatives: `SELECT DISTINCT salary FROM employees ORDER BY salary DESC LIMIT 1 OFFSET 1;` or `DENSE_RANK() = 2`. For the "Nth" value, the `DENSE_RANK` version is the most general.

</details>

### 20. Best customer (CTE)

**Using a CTE, find the customer who spent the most on non-cancelled orders.**

<details>
<summary>Solution</summary>

```sql
WITH spend AS (
    SELECT o.customer_id, SUM(oi.quantity * oi.unit_price) AS total
    FROM orders o
    JOIN order_items oi ON oi.order_id = o.order_id
    WHERE o.status <> 'cancelled'
    GROUP BY o.customer_id
)
SELECT c.name, s.total
FROM spend s
JOIN customers c ON c.customer_id = s.customer_id
WHERE s.total = (SELECT MAX(total) FROM spend);
```

Expected result:

```text
name         | total
-------------+--------
Sofía Torres | 2750.00
(1 row)
```

> With `WHERE total = MAX` (instead of `ORDER BY ... LIMIT 1`) you return **all** tied customers.

</details>

### 21. Average order value

**What is the average order value (AOV) of non-cancelled orders? Round to 2 decimals.**

<details>
<summary>Solution</summary>

```sql
WITH order_totals AS (
    SELECT o.order_id, SUM(oi.quantity * oi.unit_price) AS total
    FROM orders o
    JOIN order_items oi ON oi.order_id = o.order_id
    WHERE o.status <> 'cancelled'
    GROUP BY o.order_id
)
SELECT COUNT(*) AS orders, ROUND(AVG(total), 2) AS avg_order_value
FROM order_totals;
```

Expected result:

```text
orders | avg_order_value
-------+----------------
13     | 653.04
(1 row)
```

> ⚠️ `AVG(quantity * unit_price)` directly on `order_items` gives the average **per line**, not per order. First sum per order, then average.

</details>

---

## 🟠 CASE and window functions

### 22. Price buckets

**Classify each product as `High` (price ≥ 300), `Medium` (40 ≤ price < 300) or `Low` (price < 40).**

<details>
<summary>Solution</summary>

```sql
SELECT name, price,
       CASE
           WHEN price >= 300 THEN 'High'
           WHEN price >= 40  THEN 'Medium'
           ELSE 'Low'
       END AS price_bucket
FROM products
ORDER BY price DESC;
```

Expected result:

```text
name           | price   | price_bucket
---------------+---------+-------------
Laptop Pro 14  | 1200.00 | High
Standing Desk  | 350.00  | High
Monitor 27"    | 300.00  | High
Office Chair   | 180.00  | Medium
USB-C Hub      | 45.00   | Medium
Desk Lamp      | 40.00   | Medium
Wireless Mouse | 25.00   | Low
Gel Pens (x10) | 8.00    | Low
Notebook A5    | 4.50    | Low
(9 rows)
```

> `CASE` is evaluated in order and stops at the **first** true `WHEN`.

</details>

### 23. Conditional aggregation

**In a single row, show the number of delivered, shipped and cancelled orders, and the cancellation rate as a percentage (1 decimal).**

<details>
<summary>Solution</summary>

```sql
SELECT
    SUM(CASE WHEN status = 'delivered' THEN 1 ELSE 0 END) AS delivered,
    SUM(CASE WHEN status = 'shipped'   THEN 1 ELSE 0 END) AS shipped,
    SUM(CASE WHEN status = 'cancelled' THEN 1 ELSE 0 END) AS cancelled,
    ROUND(100.0 * SUM(CASE WHEN status = 'cancelled' THEN 1 ELSE 0 END) / COUNT(*), 1) AS cancel_rate_pct
FROM orders;
```

Expected result:

```text
delivered | shipped | cancelled | cancel_rate_pct
----------+---------+-----------+----------------
11        | 2       | 2         | 13.30
(1 row)
```

</details>

### 24. Customer segmentation

**Label each customer according to their number of orders (any status): 0 → `No orders`, 1 → `New`, 2 or more → `Returning`.**

<details>
<summary>Solution</summary>

```sql
SELECT c.name,
       COUNT(o.order_id) AS orders,
       CASE
           WHEN COUNT(o.order_id) = 0 THEN 'No orders'
           WHEN COUNT(o.order_id) = 1 THEN 'New'
           ELSE 'Returning'
       END AS label
FROM customers c
LEFT JOIN orders o ON o.customer_id = c.customer_id
GROUP BY c.customer_id, c.name
ORDER BY orders DESC, c.name;
```

Expected result:

```text
name         | orders | label
-------------+--------+----------
Ana Gómez    | 3      | Returning
Luis Pérez   | 3      | Returning
John Smith   | 2      | Returning
Sofía Torres | 2      | Returning
Diego Vargas | 1      | New
Emily Brown  | 1      | New
Laura Moreno | 1      | New
María Ruiz   | 1      | New
Pedro Castro | 1      | New
Carlos Díaz  | 0      | No orders
(10 rows)
```

> `COUNT(o.order_id)` (not `COUNT(*)`) so the customer without orders counts as 0, not 1.

</details>

### 25. Ranking functions

**Rank employees by salary (highest first) within each department using `ROW_NUMBER`, `RANK` and `DENSE_RANK`.**

<details>
<summary>Solution</summary>

```sql
SELECT department, name, salary,
       ROW_NUMBER() OVER (PARTITION BY department ORDER BY salary DESC, name) AS row_num,
       RANK()       OVER (PARTITION BY department ORDER BY salary DESC)       AS rnk,
       DENSE_RANK() OVER (PARTITION BY department ORDER BY salary DESC)       AS dense_rnk
FROM employees
ORDER BY department, salary DESC, name;
```

Expected result:

```text
department  | name           | salary | row_num | rnk | dense_rnk
------------+----------------+--------+---------+-----+----------
Data        | Andrés López   | 14000  | 1       | 1   | 1
Data        | Camila Herrera | 9000   | 2       | 2   | 2
Data        | Julián Mejía   | 9000   | 3       | 2   | 2
Data        | Paula Ortiz    | 7000   | 4       | 4   | 3
Engineering | Felipe Rojas   | 13000  | 1       | 1   | 1
Engineering | Daniel Pardo   | 11000  | 2       | 2   | 2
Engineering | Natalia Cruz   | 10000  | 3       | 3   | 3
Engineering | Santiago Gil   | 8000   | 4       | 4   | 4
Executive   | Valentina Ríos | 25000  | 1       | 1   | 1
Marketing   | Isabel Suárez  | 9500   | 1       | 1   | 1
Marketing   | Mateo Ramírez  | 6000   | 2       | 2   | 2
(11 rows)
```

> Look at Data: Camila and Julián tie at 9000 → `RANK` jumps to 4 and `DENSE_RANK` continues with 3.

</details>

### 26. Top earner per department

**Return the highest-paid employee(s) of each department.**

<details>
<summary>Solution</summary>

```sql
WITH ranked AS (
    SELECT department, name, salary,
           DENSE_RANK() OVER (PARTITION BY department ORDER BY salary DESC) AS rk
    FROM employees
)
SELECT department, name, salary
FROM ranked
WHERE rk = 1
ORDER BY department;
```

Expected result:

```text
department  | name           | salary
------------+----------------+-------
Data        | Andrés López   | 14000
Engineering | Felipe Rojas   | 13000
Executive   | Valentina Ríos | 25000
Marketing   | Isabel Suárez  | 9500
(4 rows)
```

</details>

### 27. Running total

**For each non-cancelled order, show its date, its total and the running (cumulative) revenue ordered by date.**

<details>
<summary>Solution</summary>

```sql
WITH order_totals AS (
    SELECT o.order_id, o.order_date, SUM(oi.quantity * oi.unit_price) AS total
    FROM orders o
    JOIN order_items oi ON oi.order_id = o.order_id
    WHERE o.status <> 'cancelled'
    GROUP BY o.order_id, o.order_date
)
SELECT order_id, order_date, total,
       SUM(total) OVER (ORDER BY order_date, order_id) AS running_revenue
FROM order_totals
ORDER BY order_date, order_id;
```

Expected result:

```text
order_id | order_date | total   | running_revenue
---------+------------+---------+----------------
101      | 2024-02-01 | 1250.00 | 1250.00
102      | 2024-02-14 | 585.00  | 1835.00
103      | 2024-03-05 | 45.00   | 1880.00
105      | 2024-04-02 | 650.00  | 2530.00
106      | 2024-04-10 | 2650.00 | 5180.00
107      | 2024-04-22 | 40.00   | 5220.00
108      | 2024-05-01 | 29.50   | 5249.50
109      | 2024-05-15 | 300.00  | 5549.50
110      | 2024-05-20 | 270.00  | 5819.50
111      | 2024-06-03 | 100.00  | 5919.50
113      | 2024-06-28 | 700.00  | 6619.50
114      | 2024-07-04 | 1780.00 | 8399.50
115      | 2024-07-19 | 90.00   | 8489.50
(13 rows)
```

</details>

### 28. Month-over-month growth

**Calculate the revenue of each month (non-cancelled orders), the previous month's revenue and the month-over-month growth percentage (1 decimal).**

<details>
<summary>Solution</summary>

```sql
WITH monthly AS (
    SELECT strftime('%Y-%m', o.order_date) AS month,
           SUM(oi.quantity * oi.unit_price) AS revenue
    FROM orders o
    JOIN order_items oi ON oi.order_id = o.order_id
    WHERE o.status <> 'cancelled'
    GROUP BY month
)
SELECT month, revenue,
       LAG(revenue) OVER (ORDER BY month) AS prev_revenue,
       ROUND(100.0 * (revenue - LAG(revenue) OVER (ORDER BY month))
             / LAG(revenue) OVER (ORDER BY month), 1) AS mom_growth_pct
FROM monthly
ORDER BY month;
```

Expected result:

```text
month   | revenue | prev_revenue | mom_growth_pct
--------+---------+--------------+---------------
2024-02 | 1835.00 | NULL         | NULL
2024-03 | 45.00   | 1835.00      | -97.50
2024-04 | 3340.00 | 45.00        | 7322.20
2024-05 | 599.50  | 3340.00      | -82.10
2024-06 | 800.00  | 599.50       | 33.40
2024-07 | 1870.00 | 800.00       | 133.80
(6 rows)
```

> In PostgreSQL: `DATE_TRUNC('month', order_date)`. The first month is `NULL` because there is no previous month.

</details>

### 29. Share of total

**For each category, show its revenue (non-cancelled orders) and its percentage of the total revenue (1 decimal).**

<details>
<summary>Solution</summary>

```sql
WITH cat AS (
    SELECT p.category, SUM(oi.quantity * oi.unit_price) AS revenue
    FROM order_items oi
    JOIN products p ON p.product_id = oi.product_id
    JOIN orders   o ON o.order_id   = oi.order_id
    WHERE o.status <> 'cancelled'
    GROUP BY p.category
)
SELECT category, revenue,
       ROUND(100.0 * revenue / SUM(revenue) OVER (), 1) AS pct_of_total
FROM cat
ORDER BY revenue DESC;
```

Expected result:

```text
category    | revenue | pct_of_total
------------+---------+-------------
Electronics | 6515.00 | 76.70
Furniture   | 1770.00 | 20.80
Stationery  | 204.50  | 2.40
(3 rows)
```

> An empty `OVER ()` = the window is the **whole** result.

</details>

### 30. Days between orders

**For each order, show the customer, the order date, the date of that customer's previous order and the number of days between them.**

<details>
<summary>Solution</summary>

```sql
SELECT customer_id, order_id, order_date,
       LAG(order_date) OVER w AS prev_order_date,
       CAST(julianday(order_date) - julianday(LAG(order_date) OVER w) AS INTEGER) AS days_since_prev
FROM orders
WINDOW w AS (PARTITION BY customer_id ORDER BY order_date)
ORDER BY customer_id, order_date;
```

Expected result:

```text
customer_id | order_id | order_date | prev_order_date | days_since_prev
------------+----------+------------+-----------------+----------------
1           | 101      | 2024-02-01 | NULL            | NULL
1           | 103      | 2024-03-05 | 2024-02-01      | 33
1           | 109      | 2024-05-15 | 2024-03-05      | 71
2           | 102      | 2024-02-14 | NULL            | NULL
2           | 107      | 2024-04-22 | 2024-02-14      | 68
2           | 114      | 2024-07-04 | 2024-04-22      | 73
3           | 104      | 2024-03-18 | NULL            | NULL
4           | 105      | 2024-04-02 | NULL            | NULL
4           | 113      | 2024-06-28 | 2024-04-02      | 87
5           | 106      | 2024-04-10 | NULL            | NULL
5           | 111      | 2024-06-03 | 2024-04-10      | 54
7           | 108      | 2024-05-01 | NULL            | NULL
8           | 110      | 2024-05-20 | NULL            | NULL
9           | 112      | 2024-06-15 | NULL            | NULL
10          | 115      | 2024-07-19 | NULL            | NULL
(15 rows)
```

> `WINDOW w AS (...)` defines the window only once (SQLite, PostgreSQL and MySQL 8 support it).

</details>

### 31. First order per customer

**Return the first order (id and date) of every customer who has ordered.**

<details>
<summary>Solution</summary>

```sql
WITH numbered AS (
    SELECT customer_id, order_id, order_date,
           ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY order_date) AS rn
    FROM orders
)
SELECT customer_id, order_id, order_date
FROM numbered
WHERE rn = 1
ORDER BY customer_id;
```

Expected result:

```text
customer_id | order_id | order_date
------------+----------+-----------
1           | 101      | 2024-02-01
2           | 102      | 2024-02-14
3           | 104      | 2024-03-18
4           | 105      | 2024-04-02
5           | 106      | 2024-04-10
7           | 108      | 2024-05-01
8           | 110      | 2024-05-20
9           | 112      | 2024-06-15
10          | 115      | 2024-07-19
(9 rows)
```

</details>

### 32. Top 2 products per category

**For each category, return the 2 products with the most units sold (non-cancelled orders).**

<details>
<summary>Solution</summary>

```sql
WITH units AS (
    SELECT p.category, p.name, SUM(oi.quantity) AS units_sold
    FROM order_items oi
    JOIN products p ON p.product_id = oi.product_id
    JOIN orders   o ON o.order_id   = oi.order_id
    WHERE o.status <> 'cancelled'
    GROUP BY p.category, p.name
),
ranked AS (
    SELECT *, ROW_NUMBER() OVER (PARTITION BY category ORDER BY units_sold DESC, name) AS rn
    FROM units
)
SELECT category, name, units_sold
FROM ranked
WHERE rn <= 2
ORDER BY category, rn;
```

Expected result:

```text
category    | name           | units_sold
------------+----------------+-----------
Electronics | Wireless Mouse | 8
Electronics | Monitor 27"    | 5
Furniture   | Office Chair   | 4
Furniture   | Standing Desk  | 3
Stationery  | Notebook A5    | 33
Stationery  | Gel Pens (x10) | 7
(6 rows)
```

</details>

---

## 🔴 Interview challenges

### 33. Duplicates

**Find the salary values that are shared by more than one employee, and how many employees have each one.**

<details>
<summary>Solution</summary>

```sql
SELECT salary, COUNT(*) AS employees
FROM employees
GROUP BY salary
HAVING COUNT(*) > 1;
```

Expected result:

```text
salary | employees
-------+----------
9000   | 2
(1 row)
```

> The same pattern finds duplicated emails or records: `GROUP BY <columns> HAVING COUNT(*) > 1`.

</details>

### 34. Cross-category buyers

**Find the customers who bought products from BOTH the `Electronics` and the `Furniture` categories (non-cancelled orders).**

<details>
<summary>Solution</summary>

```sql
SELECT c.name
FROM customers c
JOIN orders o       ON o.customer_id = c.customer_id
JOIN order_items oi ON oi.order_id   = o.order_id
JOIN products p     ON p.product_id  = oi.product_id
WHERE o.status <> 'cancelled'
  AND p.category IN ('Electronics', 'Furniture')
GROUP BY c.customer_id, c.name
HAVING COUNT(DISTINCT p.category) = 2
ORDER BY c.name;
```

Expected result:

```text
name
------------
John Smith
Luis Pérez
Pedro Castro
Sofía Torres
(4 rows)
```

> ❌ `WHERE category = 'Electronics' AND category = 'Furniture'` is never true: a **row** cannot have two categories. The "both" condition is evaluated per **group** with `HAVING`. Alternative: `INTERSECT`.

</details>

### 35. Signup-to-purchase conversion

**For each customer, compute the number of days between signup and their first order (any status). Then, in a second query, calculate what percentage of ALL customers placed their first order within 30 days of signing up.**

<details>
<summary>Solution</summary>

```sql
WITH first_order AS (
    SELECT customer_id, MIN(order_date) AS first_order_date
    FROM orders
    GROUP BY customer_id
)
SELECT c.name, c.signup_date, f.first_order_date,
       CAST(julianday(f.first_order_date) - julianday(c.signup_date) AS INTEGER) AS days_to_first_order
FROM customers c
LEFT JOIN first_order f ON f.customer_id = c.customer_id
ORDER BY c.customer_id;
```

Expected result:

```text
name         | signup_date | first_order_date | days_to_first_order
-------------+-------------+------------------+--------------------
Ana Gómez    | 2024-01-15  | 2024-02-01       | 17
Luis Pérez   | 2024-02-03  | 2024-02-14       | 11
María Ruiz   | 2024-02-20  | 2024-03-18       | 27
John Smith   | 2024-03-11  | 2024-04-02       | 22
Sofía Torres | 2024-03-25  | 2024-04-10       | 16
Carlos Díaz  | 2024-04-02  | NULL             | NULL
Emily Brown  | 2024-04-18  | 2024-05-01       | 13
Pedro Castro | 2024-05-07  | 2024-05-20       | 13
Laura Moreno | 2024-05-30  | 2024-06-15       | 16
Diego Vargas | 2024-06-12  | 2024-07-19       | 37
(10 rows)
```

```sql
WITH first_order AS (
    SELECT customer_id, MIN(order_date) AS first_order_date
    FROM orders
    GROUP BY customer_id
)
SELECT COUNT(*) AS customers,
       SUM(CASE WHEN julianday(f.first_order_date) - julianday(c.signup_date) <= 30
                THEN 1 ELSE 0 END) AS converted_30d,
       ROUND(100.0 * SUM(CASE WHEN julianday(f.first_order_date) - julianday(c.signup_date) <= 30
                              THEN 1 ELSE 0 END) / COUNT(*), 1) AS conversion_pct
FROM customers c
LEFT JOIN first_order f ON f.customer_id = c.customer_id;
```

Expected result:

```text
customers | converted_30d | conversion_pct
----------+---------------+---------------
10        | 8             | 80.00
(1 row)
```

> The denominator is **all** customers (that is why it is a `LEFT JOIN`). Carlos has `NULL`; a comparison with NULL is not true, so he falls into the `ELSE 0`.

</details>

---

## Done? Next step

- Redo exercises 16, 21, 26, 28, 32 and 34 from scratch: they are the patterns that repeat most in tests.
- Practice with [LeetCode SQL 50](https://leetcode.com/studyplan/top-sql-50/) and [HackerRank SQL (Basic → Intermediate)](https://www.hackerrank.com/domains/sql).
- Review the [SQL cheat sheet](../cheatsheets/sql.en.md) the day before the exam.
