# 02 · SQL — 35 ejercicios con solución

🌐 **Español** · [English](ejercicios.en.md)

> **Cómo usar este archivo:**
>
> 1. Ejecuta `python3 setup_db.py --shell` (o abre `practice.db` en DB Browser).
> 2. Lee el enunciado **en inglés** (así viene en la prueba). Si no lo entiendes, lee la traducción.
> 3. Escribe tu consulta **antes** de abrir la solución. Compara tu resultado con el "Resultado esperado".
> 4. Marca ✅ los que te salgan a la primera y repite los ❌ dos días después.
>
> Las soluciones están verificadas automáticamente con `python3 check_solutions.py`.
> Modelo de datos: ver [README.md](README.md#1-el-modelo-de-datos-de-práctica).

| Nivel | Ejercicios | Tiempo objetivo por ejercicio |
|---|---|---|
| 🟢 Básico | 1–10 | 2–3 min |
| 🟡 JOINs y subconsultas | 11–21 | 4–5 min |
| 🟠 CASE y ventanas | 22–32 | 5–7 min |
| 🔴 Retos de entrevista | 33–35 | 8–10 min |

---

## 🟢 Nivel básico

### 1. Filtrar y ordenar

**Write a query that returns the name and price of all products in the `Electronics` category, sorted from the most expensive to the cheapest.**

*Escribe una consulta que devuelva el nombre y el precio de todos los productos de la categoría `Electronics`, ordenados del más caro al más barato.*

<details>
<summary>Solución</summary>

```sql
SELECT name, price
FROM products
WHERE category = 'Electronics'
ORDER BY price DESC;
```

Resultado esperado:

```text
name           | price
---------------+--------
Laptop Pro 14  | 1200.00
Monitor 27"    | 300.00
USB-C Hub      | 45.00
Wireless Mouse | 25.00
(4 filas)
```

</details>

### 2. Varias condiciones

**List the name, city and signup date of customers from Colombia who signed up on or after March 1st, 2024.**

*Lista el nombre, la ciudad y la fecha de registro de los clientes de Colombia que se registraron el 1 de marzo de 2024 o después.*

<details>
<summary>Solución</summary>

```sql
SELECT name, city, signup_date
FROM customers
WHERE country = 'Colombia'
  AND signup_date >= '2024-03-01'
ORDER BY signup_date;
```

Resultado esperado:

```text
name         | city         | signup_date
-------------+--------------+------------
Sofía Torres | Bogotá       | 2024-03-25
Carlos Díaz  | NULL         | 2024-04-02
Pedro Castro | Barranquilla | 2024-05-07
Diego Vargas | Medellín     | 2024-06-12
(4 filas)
```

> Las fechas en formato ISO (`YYYY-MM-DD`) se pueden comparar como texto.

</details>

### 3. Valores faltantes

**Return the customers whose city is unknown (missing).**

*Devuelve los clientes cuya ciudad es desconocida (falta el dato).*

<details>
<summary>Solución</summary>

```sql
SELECT customer_id, name
FROM customers
WHERE city IS NULL;
```

Resultado esperado:

```text
customer_id | name
------------+------------
6           | Carlos Díaz
(1 fila)
```

> ❌ `WHERE city = NULL` devuelve 0 filas.

</details>

### 4. Contar por grupo

**How many customers are there in each country? Show the country with the most customers first.**

*¿Cuántos clientes hay en cada país? Muestra primero el país con más clientes.*

<details>
<summary>Solución</summary>

```sql
SELECT country, COUNT(*) AS customers
FROM customers
GROUP BY country
ORDER BY customers DESC;
```

Resultado esperado:

```text
country  | customers
---------+----------
Colombia | 7
USA      | 2
Peru     | 1
(3 filas)
```

</details>

### 5. Búsqueda por patrón

**Find all the products whose name contains the word "Desk".**

*Encuentra todos los productos cuyo nombre contiene la palabra "Desk".*

<details>
<summary>Solución</summary>

```sql
SELECT product_id, name
FROM products
WHERE name LIKE '%Desk%';
```

Resultado esperado:

```text
product_id | name
-----------+--------------
5          | Standing Desk
9          | Desk Lamp
(2 filas)
```

</details>

### 6. Valores únicos

**Return the list of distinct order statuses, in alphabetical order.**

*Devuelve la lista de estados de pedido distintos (sin repetir), en orden alfabético.*

<details>
<summary>Solución</summary>

```sql
SELECT DISTINCT status
FROM orders
ORDER BY status;
```

Resultado esperado:

```text
status
---------
cancelled
delivered
shipped
(3 filas)
```

</details>

### 7. Ingreso total

**Calculate the total revenue (quantity × unit price) of all orders that were NOT cancelled.**

*Calcula el ingreso total (cantidad × precio unitario) de todos los pedidos que NO fueron cancelados.*

<details>
<summary>Solución</summary>

```sql
SELECT SUM(oi.quantity * oi.unit_price) AS total_revenue
FROM order_items oi
JOIN orders o ON o.order_id = oi.order_id
WHERE o.status <> 'cancelled';
```

Resultado esperado:

```text
total_revenue
-------------
8489.50
(1 fila)
```

> El ingreso se calcula con `unit_price` (lo que realmente se cobró), no con `products.price`.

</details>

### 8. Conteo por estado

**Count how many orders there are for each status.**

*Cuenta cuántos pedidos hay en cada estado.*

<details>
<summary>Solución</summary>

```sql
SELECT status, COUNT(*) AS orders
FROM orders
GROUP BY status
ORDER BY orders DESC;
```

Resultado esperado:

```text
status    | orders
----------+-------
delivered | 11
shipped   | 2
cancelled | 2
(3 filas)
```

</details>

### 9. HAVING

**Show the average salary of each department, rounded to 2 decimals, but only for departments whose average salary is greater than 8,000.**

*Muestra el salario promedio de cada departamento, redondeado a 2 decimales, pero solo de los departamentos cuyo salario promedio es mayor que 8.000.*

<details>
<summary>Solución</summary>

```sql
SELECT department, ROUND(AVG(salary), 2) AS avg_salary
FROM employees
GROUP BY department
HAVING AVG(salary) > 8000
ORDER BY avg_salary DESC;
```

Resultado esperado:

```text
department  | avg_salary
------------+-----------
Executive   | 25000.00
Engineering | 10500.00
Data        | 9750.00
(3 filas)
```

</details>

### 10. Ingreso por categoría

**Calculate the revenue of each product category (excluding cancelled orders), from highest to lowest.**

*Calcula el ingreso de cada categoría de producto (sin contar los pedidos cancelados), de mayor a menor.*

<details>
<summary>Solución</summary>

```sql
SELECT p.category, SUM(oi.quantity * oi.unit_price) AS revenue
FROM order_items oi
JOIN products p ON p.product_id = oi.product_id
JOIN orders   o ON o.order_id   = oi.order_id
WHERE o.status <> 'cancelled'
GROUP BY p.category
ORDER BY revenue DESC;
```

Resultado esperado:

```text
category    | revenue
------------+--------
Electronics | 6515.00
Furniture   | 1770.00
Stationery  | 204.50
(3 filas)
```

</details>

---

## 🟡 JOINs y subconsultas

### 11. INNER JOIN

**List every order with its id, date, status and the name of the customer who placed it. Sort by date.**

*Lista cada pedido con su id, fecha, estado y el nombre del cliente que lo hizo. Ordena por fecha.*

<details>
<summary>Solución</summary>

```sql
SELECT o.order_id, o.order_date, o.status, c.name
FROM orders o
JOIN customers c ON c.customer_id = o.customer_id
ORDER BY o.order_date;
```

Resultado esperado:

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
(15 filas)
```

</details>

### 12. Clientes sin pedidos

**Find the customers who have never placed an order.**

*Encuentra los clientes que nunca han hecho un pedido.*

<details>
<summary>Solución</summary>

```sql
SELECT c.customer_id, c.name
FROM customers c
LEFT JOIN orders o ON o.customer_id = c.customer_id
WHERE o.order_id IS NULL;
```

Resultado esperado:

```text
customer_id | name
------------+------------
6           | Carlos Díaz
(1 fila)
```

> Patrón **anti-join**. Alternativa: `WHERE NOT EXISTS (SELECT 1 FROM orders o WHERE o.customer_id = c.customer_id)`.

</details>

### 13. Productos nunca vendidos

**Which products have never been sold? Use `NOT EXISTS`.**

*¿Qué productos nunca se han vendido? Usa `NOT EXISTS`.*

<details>
<summary>Solución</summary>

```sql
SELECT p.product_id, p.name
FROM products p
WHERE NOT EXISTS (
    SELECT 1 FROM order_items oi WHERE oi.product_id = p.product_id
);
```

Resultado esperado:

```text
product_id | name
-----------+----------
9          | Desk Lamp
(1 fila)
```

</details>

### 14. Self join

**Show each employee's name together with their manager's name. Employees without a manager must also appear.**

*Muestra el nombre de cada empleado junto con el nombre de su jefe. Los empleados sin jefe también deben aparecer.*

<details>
<summary>Solución</summary>

```sql
SELECT e.name AS employee, m.name AS manager
FROM employees e
LEFT JOIN employees m ON m.emp_id = e.manager_id
ORDER BY e.emp_id;
```

Resultado esperado:

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
(11 filas)
```

> Con `INNER JOIN` desaparecería la CEO (su `manager_id` es NULL).

</details>

### 15. Ganar más que el jefe

**Find the employees who earn more than their direct manager.**

*Encuentra los empleados que ganan más que su jefe directo.*

<details>
<summary>Solución</summary>

```sql
SELECT e.name AS employee, e.salary, m.name AS manager, m.salary AS manager_salary
FROM employees e
JOIN employees m ON m.emp_id = e.manager_id
WHERE e.salary > m.salary;
```

Resultado esperado:

```text
employee     | salary | manager      | manager_salary
-------------+--------+--------------+---------------
Daniel Pardo | 11000  | Natalia Cruz | 10000
(1 fila)
```

</details>

### 16. Gasto por cliente (incluido el cero)

**For every customer, show the total amount spent on non-cancelled orders. Customers with no purchases must appear with 0.**

*Para cada cliente, muestra el monto total gastado en pedidos no cancelados. Los clientes sin compras deben aparecer con 0.*

<details>
<summary>Solución</summary>

```sql
SELECT c.name,
       COALESCE(SUM(oi.quantity * oi.unit_price), 0) AS total_spent
FROM customers c
LEFT JOIN orders o
       ON o.customer_id = c.customer_id
      AND o.status <> 'cancelled'          -- el filtro va en el ON para no perder clientes
LEFT JOIN order_items oi ON oi.order_id = o.order_id
GROUP BY c.customer_id, c.name
ORDER BY total_spent DESC, c.name;
```

Resultado esperado:

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
(10 filas)
```

> María y Laura solo tienen pedidos cancelados → salen con 0, igual que Carlos.

</details>

### 17. Mayor que el promedio

**List the products whose price is greater than the average price of all products.**

*Lista los productos cuyo precio es mayor que el precio promedio de todos los productos.*

<details>
<summary>Solución</summary>

```sql
SELECT name, price
FROM products
WHERE price > (SELECT AVG(price) FROM products)
ORDER BY price DESC;
```

Resultado esperado:

```text
name          | price
--------------+--------
Laptop Pro 14 | 1200.00
Standing Desk | 350.00
Monitor 27"   | 300.00
(3 filas)
```

</details>

### 18. Subconsulta correlacionada

**Find the employees who earn more than the average salary of their own department.**

*Encuentra los empleados que ganan más que el salario promedio de su propio departamento.*

<details>
<summary>Solución</summary>

```sql
SELECT e.name, e.department, e.salary
FROM employees e
WHERE e.salary > (
    SELECT AVG(x.salary) FROM employees x WHERE x.department = e.department
)
ORDER BY e.department, e.salary DESC;
```

Resultado esperado:

```text
name          | department  | salary
--------------+-------------+-------
Andrés López  | Data        | 14000
Felipe Rojas  | Engineering | 13000
Daniel Pardo  | Engineering | 11000
Isabel Suárez | Marketing   | 9500
(4 filas)
```

</details>

### 19. Segundo salario más alto

**Return the second highest distinct salary in the company.**

*Devuelve el segundo salario distinto más alto de la empresa.*

<details>
<summary>Solución</summary>

```sql
SELECT MAX(salary) AS second_highest
FROM employees
WHERE salary < (SELECT MAX(salary) FROM employees);
```

Resultado esperado:

```text
second_highest
--------------
14000
(1 fila)
```

> Alternativas: `SELECT DISTINCT salary FROM employees ORDER BY salary DESC LIMIT 1 OFFSET 1;` o `DENSE_RANK() = 2`. Para el "N-ésimo", la de `DENSE_RANK` es la más general.

</details>

### 20. Mejor cliente (CTE)

**Using a CTE, find the customer who spent the most on non-cancelled orders.**

*Usando una CTE, encuentra el cliente que más gastó en pedidos no cancelados.*

<details>
<summary>Solución</summary>

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

Resultado esperado:

```text
name         | total
-------------+--------
Sofía Torres | 2750.00
(1 fila)
```

> Con `WHERE total = MAX` (y no con `ORDER BY ... LIMIT 1`) devuelves **todos** los empatados.

</details>

### 21. Ticket promedio

**What is the average order value (AOV) of non-cancelled orders? Round to 2 decimals.**

*¿Cuál es el valor promedio por pedido (AOV, «average order value») de los pedidos no cancelados? Redondea a 2 decimales.*

<details>
<summary>Solución</summary>

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

Resultado esperado:

```text
orders | avg_order_value
-------+----------------
13     | 653.04
(1 fila)
```

> ⚠️ `AVG(quantity * unit_price)` directamente sobre `order_items` da el promedio **por línea**, no por pedido. Primero se suma por pedido y después se promedia.

</details>

---

## 🟠 CASE y funciones de ventana

### 22. Rangos de precio

**Classify each product as `High` (price ≥ 300), `Medium` (40 ≤ price < 300) or `Low` (price < 40).**

*Clasifica cada producto como `High` (precio ≥ 300), `Medium` (40 ≤ precio < 300) o `Low` (precio < 40).*

<details>
<summary>Solución</summary>

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

Resultado esperado:

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
(9 filas)
```

> El `CASE` se evalúa en orden y se detiene en el **primer** `WHEN` verdadero.

</details>

### 23. Agregación condicional

**In a single row, show the number of delivered, shipped and cancelled orders, and the cancellation rate as a percentage (1 decimal).**

*En una sola fila, muestra el número de pedidos entregados (delivered), enviados (shipped) y cancelados (cancelled), y la tasa de cancelación en porcentaje (1 decimal).*

<details>
<summary>Solución</summary>

```sql
SELECT
    SUM(CASE WHEN status = 'delivered' THEN 1 ELSE 0 END) AS delivered,
    SUM(CASE WHEN status = 'shipped'   THEN 1 ELSE 0 END) AS shipped,
    SUM(CASE WHEN status = 'cancelled' THEN 1 ELSE 0 END) AS cancelled,
    ROUND(100.0 * SUM(CASE WHEN status = 'cancelled' THEN 1 ELSE 0 END) / COUNT(*), 1) AS cancel_rate_pct
FROM orders;
```

Resultado esperado:

```text
delivered | shipped | cancelled | cancel_rate_pct
----------+---------+-----------+----------------
11        | 2       | 2         | 13.30
(1 fila)
```

</details>

### 24. Segmentación de clientes

**Label each customer according to their number of orders (any status): 0 → `No orders`, 1 → `New`, 2 or more → `Returning`.**

*Etiqueta a cada cliente según su número de pedidos (en cualquier estado): 0 → `No orders`, 1 → `New`, 2 o más → `Returning`.*

<details>
<summary>Solución</summary>

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

Resultado esperado:

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
(10 filas)
```

> `COUNT(o.order_id)` (y no `COUNT(*)`) para que el cliente sin pedidos cuente 0 y no 1.

</details>

### 25. Funciones de ranking

**Rank employees by salary (highest first) within each department using `ROW_NUMBER`, `RANK` and `DENSE_RANK`.**

*Ordena a los empleados por salario (el más alto primero) dentro de cada departamento usando `ROW_NUMBER`, `RANK` y `DENSE_RANK`.*

<details>
<summary>Solución</summary>

```sql
SELECT department, name, salary,
       ROW_NUMBER() OVER (PARTITION BY department ORDER BY salary DESC, name) AS row_num,
       RANK()       OVER (PARTITION BY department ORDER BY salary DESC)       AS rnk,
       DENSE_RANK() OVER (PARTITION BY department ORDER BY salary DESC)       AS dense_rnk
FROM employees
ORDER BY department, salary DESC, name;
```

Resultado esperado:

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
(11 filas)
```

> Fíjate en Data: Camila y Julián empatan con 9000 → `RANK` salta al 4 y `DENSE_RANK` sigue con el 3.

</details>

### 26. Mejor pagado por departamento

**Return the highest-paid employee(s) of each department.**

*Devuelve el empleado (o los empleados) mejor pagado(s) de cada departamento.*

<details>
<summary>Solución</summary>

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

Resultado esperado:

```text
department  | name           | salary
------------+----------------+-------
Data        | Andrés López   | 14000
Engineering | Felipe Rojas   | 13000
Executive   | Valentina Ríos | 25000
Marketing   | Isabel Suárez  | 9500
(4 filas)
```

</details>

### 27. Total acumulado

**For each non-cancelled order, show its date, its total and the running (cumulative) revenue ordered by date.**

*Para cada pedido no cancelado, muestra su fecha, su total y el ingreso acumulado ordenado por fecha.*

<details>
<summary>Solución</summary>

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

Resultado esperado:

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
(13 filas)
```

</details>

### 28. Crecimiento mes a mes

**Calculate the revenue of each month (non-cancelled orders), the previous month's revenue and the month-over-month growth percentage (1 decimal).**

*Calcula el ingreso de cada mes (pedidos no cancelados), el ingreso del mes anterior y el porcentaje de crecimiento mes a mes (1 decimal).*

<details>
<summary>Solución</summary>

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

Resultado esperado:

```text
month   | revenue | prev_revenue | mom_growth_pct
--------+---------+--------------+---------------
2024-02 | 1835.00 | NULL         | NULL
2024-03 | 45.00   | 1835.00      | -97.50
2024-04 | 3340.00 | 45.00        | 7322.20
2024-05 | 599.50  | 3340.00      | -82.10
2024-06 | 800.00  | 599.50       | 33.40
2024-07 | 1870.00 | 800.00       | 133.80
(6 filas)
```

> En PostgreSQL: `DATE_TRUNC('month', order_date)`. El primer mes tiene `NULL` porque no hay mes anterior.

</details>

### 29. Participación sobre el total

**For each category, show its revenue (non-cancelled orders) and its percentage of the total revenue (1 decimal).**

*Para cada categoría, muestra su ingreso (pedidos no cancelados) y su porcentaje del ingreso total (1 decimal).*

<details>
<summary>Solución</summary>

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

Resultado esperado:

```text
category    | revenue | pct_of_total
------------+---------+-------------
Electronics | 6515.00 | 76.70
Furniture   | 1770.00 | 20.80
Stationery  | 204.50  | 2.40
(3 filas)
```

> `OVER ()` vacío = la ventana es **todo** el resultado.

</details>

### 30. Días entre pedidos

**For each order, show the customer, the order date, the date of that customer's previous order and the number of days between them.**

*Para cada pedido, muestra el cliente, la fecha del pedido, la fecha del pedido anterior de ese mismo cliente y el número de días entre los dos.*

<details>
<summary>Solución</summary>

```sql
SELECT customer_id, order_id, order_date,
       LAG(order_date) OVER w AS prev_order_date,
       CAST(julianday(order_date) - julianday(LAG(order_date) OVER w) AS INTEGER) AS days_since_prev
FROM orders
WINDOW w AS (PARTITION BY customer_id ORDER BY order_date)
ORDER BY customer_id, order_date;
```

Resultado esperado:

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
(15 filas)
```

> `WINDOW w AS (...)` define la ventana una sola vez (SQLite, PostgreSQL y MySQL 8 lo soportan).

</details>

### 31. Primer pedido de cada cliente

**Return the first order (id and date) of every customer who has ordered.**

*Devuelve el primer pedido (id y fecha) de cada cliente que ha hecho pedidos.*

<details>
<summary>Solución</summary>

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

Resultado esperado:

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
(9 filas)
```

</details>

### 32. Top 2 productos por categoría

**For each category, return the 2 products with the most units sold (non-cancelled orders).**

*Para cada categoría, devuelve los 2 productos con más unidades vendidas (pedidos no cancelados).*

<details>
<summary>Solución</summary>

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

Resultado esperado:

```text
category    | name           | units_sold
------------+----------------+-----------
Electronics | Wireless Mouse | 8
Electronics | Monitor 27"    | 5
Furniture   | Office Chair   | 4
Furniture   | Standing Desk  | 3
Stationery  | Notebook A5    | 33
Stationery  | Gel Pens (x10) | 7
(6 filas)
```

</details>

---

## 🔴 Retos tipo entrevista

### 33. Duplicados

**Find the salary values that are shared by more than one employee, and how many employees have each one.**

*Encuentra los valores de salario que comparten varios empleados, y cuántos empleados tienen cada uno.*

<details>
<summary>Solución</summary>

```sql
SELECT salary, COUNT(*) AS employees
FROM employees
GROUP BY salary
HAVING COUNT(*) > 1;
```

Resultado esperado:

```text
salary | employees
-------+----------
9000   | 2
(1 fila)
```

> El mismo patrón sirve para encontrar emails o registros duplicados: `GROUP BY <columnas> HAVING COUNT(*) > 1`.

</details>

### 34. Compradores de dos categorías

**Find the customers who bought products from BOTH the `Electronics` and the `Furniture` categories (non-cancelled orders).**

*Encuentra los clientes que compraron productos de AMBAS categorías, `Electronics` y `Furniture` (pedidos no cancelados).*

<details>
<summary>Solución</summary>

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

Resultado esperado:

```text
name
------------
John Smith
Luis Pérez
Pedro Castro
Sofía Torres
(4 filas)
```

> ❌ `WHERE category = 'Electronics' AND category = 'Furniture'` nunca es verdadero: una **fila** no puede tener dos categorías. La condición "ambas" se evalúa por **grupo** con `HAVING`. Alternativa: `INTERSECT`.

</details>

### 35. Conversión de registro a compra

**For each customer, compute the number of days between signup and their first order (any status). Then, in a second query, calculate what percentage of ALL customers placed their first order within 30 days of signing up.**

*Para cada cliente, calcula el número de días entre su registro y su primer pedido (en cualquier estado). Luego, en una segunda consulta, calcula qué porcentaje de TODOS los clientes hizo su primer pedido dentro de los 30 días siguientes a su registro.*

<details>
<summary>Solución</summary>

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

Resultado esperado:

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
(10 filas)
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

Resultado esperado:

```text
customers | converted_30d | conversion_pct
----------+---------------+---------------
10        | 8             | 80.00
(1 fila)
```

> El denominador es **todos** los clientes (por eso `LEFT JOIN`). Carlos tiene `NULL`; la comparación con NULL no es verdadera, así que cae en el `ELSE 0`.

</details>

---

## ¿Terminaste? Siguiente paso

- Rehaz en limpio los ejercicios 16, 21, 26, 28, 32 y 34: son los patrones que más se repiten en las pruebas.
- Practica con los planes [LeetCode SQL 50](https://leetcode.com/studyplan/top-sql-50/) y [HackerRank SQL (Basic → Intermediate)](https://www.hackerrank.com/domains/sql).
- Repasa el [cheatsheet de SQL](../cheatsheets/sql.md) el día anterior al examen.
