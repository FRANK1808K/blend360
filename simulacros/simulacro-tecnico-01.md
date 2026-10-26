# Simulacro técnico #1: 90 minutos

🌐 **Español** · [English](simulacro-tecnico-01.en.md)

> **Instrucciones (como en el examen real):**
>
> - **Tiempo: 90 minutos.** Parte 1: 40 preguntas de opción múltiple (~50 min). Parte 2: 3 problemas de código (~40 min).
> - Pon un cronómetro, **sin** buscar en internet y sin ejecutar código en la parte 1.
> - Las preguntas están en **inglés**, como en la prueba. **Primero intenta en inglés**; abre la traducción solo si te bloqueas (y anota esa pregunta: es vocabulario que debes repasar).
> - Escribe tus respuestas en un papel y revisa al final.
> - Versión 100 % en inglés (condiciones reales): [simulacro-tecnico-01.en.md](simulacro-tecnico-01.en.md).

---

## Parte 1: Opción múltiple (40 preguntas)

### SQL

**1.** Which clause is used to filter groups AFTER an aggregation?

- A) WHERE
- B) HAVING
- C) ORDER BY
- D) LIMIT

<details>
<summary>🇪🇸 Traducción</summary>

¿Qué cláusula se usa para filtrar grupos DESPUÉS de una agregación?

</details>

**2.** A table has 10 rows. The column `email` contains 3 NULL values. What does `SELECT COUNT(*), COUNT(email) FROM t;` return?

- A) 10, 10
- B) 7, 7
- C) 10, 7
- D) 7, 10

<details>
<summary>🇪🇸 Traducción</summary>

Una tabla tiene 10 filas. La columna `email` tiene 3 valores NULL. ¿Qué devuelve `SELECT COUNT(*), COUNT(email) FROM t;`?

</details>

**3.** Table A has 4 rows and table B has 3 rows. How many rows does `SELECT * FROM A CROSS JOIN B;` return?

- A) 3
- B) 4
- C) 7
- D) 12

<details>
<summary>🇪🇸 Traducción</summary>

La tabla A tiene 4 filas y la tabla B tiene 3. ¿Cuántas filas devuelve `SELECT * FROM A CROSS JOIN B;`?

</details>

**4.** The salaries are 500, 400, 400 and 300. What is the `DENSE_RANK()` (ordered by salary descending) of the salary 300?

- A) 2
- B) 3
- C) 4
- D) 1

<details>
<summary>🇪🇸 Traducción</summary>

Los salarios son 500, 400, 400 y 300. ¿Cuál es el `DENSE_RANK()` (ordenado por salario descendente) del salario 300?

</details>

**5.** Which query returns the customers who have NEVER placed an order?

- A) `SELECT c.* FROM customers c JOIN orders o ON o.customer_id = c.id;`
- B) `SELECT c.* FROM customers c LEFT JOIN orders o ON o.customer_id = c.id WHERE o.id IS NULL;`
- C) `SELECT c.* FROM customers c LEFT JOIN orders o ON o.customer_id = c.id WHERE o.id = NULL;`
- D) `SELECT * FROM orders WHERE customer_id IS NULL;`

<details>
<summary>🇪🇸 Traducción</summary>

¿Qué consulta devuelve los clientes que NUNCA han hecho un pedido?

</details>

**6.** In PostgreSQL and SQL Server, what is the result of `SELECT 7 / 2;`?

- A) 3.5
- B) 3
- C) 4
- D) An error

<details>
<summary>🇪🇸 Traducción</summary>

En PostgreSQL y SQL Server, ¿cuál es el resultado de `SELECT 7 / 2;`?

- A) 3.5
- B) 3
- C) 4
- D) Un error

</details>

**7.** Which operator combines the results of two queries and KEEPS the duplicate rows?

- A) UNION
- B) UNION ALL
- C) INTERSECT
- D) EXCEPT

<details>
<summary>🇪🇸 Traducción</summary>

¿Qué operador combina los resultados de dos consultas y CONSERVA las filas duplicadas?

</details>

**8.** What is the correct LOGICAL order of execution of a SQL query?

- A) SELECT → FROM → WHERE → GROUP BY
- B) FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY
- C) FROM → SELECT → WHERE → ORDER BY
- D) WHERE → FROM → SELECT → HAVING

<details>
<summary>🇪🇸 Traducción</summary>

¿Cuál es el orden LÓGICO correcto de ejecución de una consulta SQL?

</details>

**9.** Which name matches the condition `WHERE name LIKE '_a%'`?

- A) Ana
- B) Pedro
- C) Maria
- D) Andrea

<details>
<summary>🇪🇸 Traducción</summary>

¿Qué nombre cumple la condición `WHERE name LIKE '_a%'`?

</details>

**10.** What is wrong with this query? `SELECT department, COUNT(*) FROM employees;`

- A) COUNT(*) cannot be used with other columns
- B) It needs `GROUP BY department`
- C) It needs a WHERE clause
- D) Nothing, it is correct in all databases

<details>
<summary>🇪🇸 Traducción</summary>

¿Qué está mal en esta consulta? `SELECT department, COUNT(*) FROM employees;`

- A) COUNT(*) no se puede usar con otras columnas
- B) Le falta `GROUP BY department`
- C) Le falta una cláusula WHERE
- D) Nada, es correcta en todas las bases de datos

</details>

### Python

**11.** What is the output? `print(len("Blend 360"))`

- A) 8
- B) 9
- C) 10
- D) 7

<details>
<summary>🇪🇸 Traducción</summary>

¿Qué imprime? `print(len("Blend 360"))`

</details>

**12.** What is the output?

```python
x = [1, 2, 3]
print(x[-1] + x[0])
```

- A) 3
- B) 4
- C) 5
- D) An error

<details>
<summary>🇪🇸 Traducción</summary>

¿Qué imprime?

- A) 3
- B) 4
- C) 5
- D) Un error

</details>

**13.** What is the output? `print(10 // 3, 10 % 3)`

- A) 3.33 1
- B) 3 1
- C) 3 0
- D) 1 3

<details>
<summary>🇪🇸 Traducción</summary>

¿Qué imprime? `print(10 // 3, 10 % 3)`

</details>

**14.** What is the output?

```python
a = [1, 2]
b = a
b.append(3)
print(a)
```

- A) [1, 2]
- B) [1, 2, 3]
- C) [3, 1, 2]
- D) An error

<details>
<summary>🇪🇸 Traducción</summary>

¿Qué imprime?

- A) [1, 2]
- B) [1, 2, 3]
- C) [3, 1, 2]
- D) Un error

</details>

**15.** What is the output? `print({1, 2, 2, 3} == {3, 2, 1})`

- A) True
- B) False
- C) An error
- D) None

<details>
<summary>🇪🇸 Traducción</summary>

¿Qué imprime? `print({1, 2, 2, 3} == {3, 2, 1})`

- A) True
- B) False
- C) Un error
- D) None

</details>

**16.** What is the output?

```python
d = {"a": 1}
print(d.get("b", 0) + d["a"])
```

- A) 0
- B) 1
- C) KeyError
- D) None

<details>
<summary>🇪🇸 Traducción</summary>

¿Qué imprime?

</details>

**17.** What is the output? `print([x for x in range(10) if x % 3 == 0])`

- A) [3, 6, 9]
- B) [0, 3, 6, 9]
- C) [0, 3, 6]
- D) [1, 4, 7]

<details>
<summary>🇪🇸 Traducción</summary>

¿Qué imprime? `print([x for x in range(10) if x % 3 == 0])`

</details>

**18.** Which of the following Python types is IMMUTABLE?

- A) list
- B) dict
- C) set
- D) tuple

<details>
<summary>🇪🇸 Traducción</summary>

¿Cuál de estos tipos de Python es INMUTABLE?

</details>

**19.** What is the output?

```python
def f(n):
    return n if n <= 1 else n * f(n - 1)
print(f(4))
```

- A) 4
- B) 10
- C) 24
- D) 16

<details>
<summary>🇪🇸 Traducción</summary>

¿Qué imprime?

</details>

**20.** What is the output? `print("a,b,c".split(",")[1].upper())`

- A) A
- B) B
- C) b
- D) ['B']

<details>
<summary>🇪🇸 Traducción</summary>

¿Qué imprime? `print("a,b,c".split(",")[1].upper())`

</details>

### Algoritmos y estructuras de datos

**21.** What is the time complexity of binary search on a sorted array?

- A) O(1)
- B) O(log n)
- C) O(n)
- D) O(n log n)

<details>
<summary>🇪🇸 Traducción</summary>

¿Cuál es la complejidad temporal de la búsqueda binaria en un arreglo ordenado?

</details>

**22.** Which data structure follows the LIFO (Last In, First Out) principle?

- A) Queue
- B) Stack
- C) Heap
- D) Linked list

<details>
<summary>🇪🇸 Traducción</summary>

¿Qué estructura de datos sigue el principio LIFO (el último en entrar es el primero en salir)?

- A) Cola
- B) Pila
- C) Heap (montículo)
- D) Lista enlazada

</details>

**23.** What is the AVERAGE time complexity of looking up a key in a Python dictionary (hash table)?

- A) O(1)
- B) O(log n)
- C) O(n)
- D) O(n²)

<details>
<summary>🇪🇸 Traducción</summary>

¿Cuál es la complejidad PROMEDIO de buscar una clave en un diccionario de Python (tabla hash)?

</details>

**24.** An algorithm has two nested loops, and each one iterates over n elements. What is its time complexity?

- A) O(n)
- B) O(2n)
- C) O(n²)
- D) O(log n)

<details>
<summary>🇪🇸 Traducción</summary>

Un algoritmo tiene dos bucles anidados y cada uno recorre n elementos. ¿Cuál es su complejidad temporal?

</details>

**25.** Which sorting algorithm has a WORST-CASE time complexity of O(n log n)?

- A) Quick sort
- B) Bubble sort
- C) Merge sort
- D) Insertion sort

<details>
<summary>🇪🇸 Traducción</summary>

¿Qué algoritmo de ordenamiento tiene complejidad O(n log n) en el PEOR caso?

</details>

**26.** Which data structure is used to implement Breadth-First Search (BFS)?

- A) Stack
- B) Queue
- C) Hash table
- D) Binary search tree

<details>
<summary>🇪🇸 Traducción</summary>

¿Qué estructura de datos se usa para implementar la búsqueda en anchura (BFS)?

- A) Pila
- B) Cola
- C) Tabla hash
- D) Árbol binario de búsqueda

</details>

**27.** Approximately how many steps does binary search need, in the worst case, to find an element in a sorted list of 1,000,000 elements?

- A) 20
- B) 1,000
- C) 500,000
- D) 1,000,000

<details>
<summary>🇪🇸 Traducción</summary>

¿Aproximadamente cuántos pasos necesita la búsqueda binaria, en el peor caso, para encontrar un elemento en una lista ordenada de 1.000.000 de elementos?

</details>

**28.** What is the value of `s` at the end?

```text
s ← 0
for i from 1 to 5:
    if i mod 2 = 1:
        s ← s + i
```

- A) 6
- B) 9
- C) 15
- D) 5

<details>
<summary>🇪🇸 Traducción</summary>

¿Cuál es el valor de `s` al final?

</details>

### Bases de datos

**29.** Which ACID property guarantees that ALL the operations of a transaction are completed, or NONE of them?

- A) Atomicity
- B) Consistency
- C) Isolation
- D) Durability

<details>
<summary>🇪🇸 Traducción</summary>

¿Qué propiedad ACID garantiza que se completen TODAS las operaciones de una transacción, o NINGUNA?

- A) Atomicidad
- B) Consistencia
- C) Aislamiento
- D) Durabilidad

</details>

**30.** What is the main purpose of a foreign key?

- A) To make queries faster
- B) To guarantee referential integrity between tables
- C) To encrypt a column
- D) To allow NULL values in a primary key

<details>
<summary>🇪🇸 Traducción</summary>

¿Cuál es el propósito principal de una llave foránea?

- A) Hacer las consultas más rápidas
- B) Garantizar la integridad referencial entre tablas
- C) Cifrar una columna
- D) Permitir valores NULL en una llave primaria

</details>

**31.** Which normal form removes TRANSITIVE dependencies?

- A) 1NF
- B) 2NF
- C) 3NF
- D) None

<details>
<summary>🇪🇸 Traducción</summary>

¿Qué forma normal elimina las dependencias TRANSITIVAS?

- A) 1NF
- B) 2NF
- C) 3NF
- D) Ninguna

</details>

**32.** What is a disadvantage of adding many indexes to a table?

- A) SELECT queries become slower
- B) INSERT, UPDATE and DELETE operations become slower
- C) The table cannot have a primary key
- D) The data is deleted

<details>
<summary>🇪🇸 Traducción</summary>

¿Qué desventaja tiene agregar muchos índices a una tabla?

- A) Las consultas SELECT se vuelven más lentas
- B) Las operaciones INSERT, UPDATE y DELETE se vuelven más lentas
- C) La tabla no puede tener llave primaria
- D) Se borran los datos

</details>

**33.** Which of the following is typical of an OLAP system?

- A) Many short transactions that update few rows
- B) Complex queries that aggregate millions of rows, often with columnar storage
- C) Strictly normalized tables to process payments
- D) It is used to process credit card payments in real time

<details>
<summary>🇪🇸 Traducción</summary>

¿Cuál de las siguientes es típica de un sistema OLAP?

- A) Muchas transacciones cortas que actualizan pocas filas
- B) Consultas complejas que agregan millones de filas, a menudo con almacenamiento columnar
- C) Tablas estrictamente normalizadas para procesar pagos
- D) Se usa para procesar pagos con tarjeta en tiempo real

</details>

**34.** In a star schema, which table contains the numeric measures (for example, revenue and quantity)?

- A) Dimension table
- B) Fact table
- C) Lookup table
- D) Staging table

<details>
<summary>🇪🇸 Traducción</summary>

En un esquema estrella, ¿qué tabla contiene las medidas numéricas (por ejemplo, ingresos y cantidad)?

- A) Tabla de dimensión
- B) Tabla de hechos
- C) Tabla de consulta (lookup)
- D) Tabla de staging

</details>

### AWS y análisis de datos

**35.** Which AWS service lets you run SQL queries directly on data stored in Amazon S3 without managing any servers?

- A) Amazon RDS
- B) Amazon Athena
- C) Amazon EC2
- D) Amazon DynamoDB

<details>
<summary>🇪🇸 Traducción</summary>

¿Qué servicio de AWS permite ejecutar consultas SQL directamente sobre datos guardados en Amazon S3 sin administrar servidores?

</details>

**36.** Under the AWS shared responsibility model, which of the following is the CUSTOMER's responsibility?

- A) The physical security of data centers
- B) The hardware of the servers
- C) Managing IAM users and permissions
- D) The global network infrastructure

<details>
<summary>🇪🇸 Traducción</summary>

Según el modelo de responsabilidad compartida de AWS, ¿cuál de las siguientes es responsabilidad del CLIENTE?

- A) La seguridad física de los centros de datos
- B) El hardware de los servidores
- C) Administrar usuarios y permisos de IAM
- D) La infraestructura de red global

</details>

**37.** Which AWS service is a petabyte-scale, columnar data warehouse?

- A) Amazon Redshift
- B) Amazon S3
- C) AWS Lambda
- D) Amazon Aurora

<details>
<summary>🇪🇸 Traducción</summary>

¿Qué servicio de AWS es un data warehouse columnar a escala de petabytes?

</details>

**38.** A company needs to ingest clickstream events in real time and process them with custom applications. Which service is the BEST fit?

- A) AWS Glue DataBrew
- B) Amazon Kinesis Data Streams
- C) Amazon S3 Glacier
- D) AWS Snowball

<details>
<summary>🇪🇸 Traducción</summary>

Una empresa necesita ingerir eventos de clics en tiempo real y procesarlos con aplicaciones propias. ¿Qué servicio es el MÁS adecuado?

</details>

**39.** What does an AWS Glue crawler do?

- A) It deletes old data from S3
- B) It scans data sources, infers the schema and creates tables in the Data Catalog
- C) It creates dashboards
- D) It monitors EC2 instances

<details>
<summary>🇪🇸 Traducción</summary>

¿Qué hace un crawler de AWS Glue?

- A) Borra datos antiguos de S3
- B) Escanea fuentes de datos, infiere el esquema y crea tablas en el Data Catalog
- C) Crea dashboards
- D) Monitorea instancias EC2

</details>

**40.** Which AWS service is used to build interactive BI dashboards?

- A) Amazon QuickSight
- B) AWS CloudTrail
- C) Amazon SQS
- D) AWS IAM

<details>
<summary>🇪🇸 Traducción</summary>

¿Qué servicio de AWS se usa para crear dashboards de BI interactivos?

</details>

---

## Parte 2: Problemas de código (~40 minutos)

### Problem 1 (SQL, 12 min)

Table `orders(order_id, customer_id, order_date, amount)`.

**a)** Return the `customer_id`, the number of orders and the total amount of each customer, **only** for customers whose total amount is **greater than 500**. Sort by total amount, from highest to lowest.

**b)** For each month (`YYYY-MM`), return the customer with the **highest total amount** in that month. In case of ties, return all of them.

<details>
<summary>🇪🇸 Traducción</summary>

Tabla `orders(order_id, customer_id, order_date, amount)`.

**a)** Devuelve el `customer_id`, el número de pedidos y el monto total de cada cliente, **solo** para los clientes cuyo monto total sea **mayor que 500**. Ordena por monto total, de mayor a menor.

**b)** Para cada mes (`YYYY-MM`), devuelve el cliente con el **mayor monto total** de ese mes. En caso de empate, devuélvelos todos.

</details>

### Problem 2 (Python, 12 min)

You receive a list of strings with the format `"user,amount"`. Some lines are **invalid** (missing fields, empty values or an amount that is not a number). Write a function `total_by_user(lines)` that returns a dictionary `{user: total_amount}` that **ignores the invalid lines**. User names must be in lowercase and without surrounding spaces.

```python
lines = ["ana,10.5", "Luis, 20", "ana,4.5", "bad line", "pedro,abc", ",5", " LUIS ,1"]
total_by_user(lines)  # {'ana': 15.0, 'luis': 21.0}
```

<details>
<summary>🇪🇸 Traducción</summary>

Recibes una lista de textos con el formato `"usuario,monto"`. Algunas líneas son **inválidas** (campos faltantes, valores vacíos o un monto que no es número). Escribe una función `total_by_user(lines)` que devuelva un diccionario `{usuario: monto_total}` **ignorando las líneas inválidas**. Los nombres de usuario deben quedar en minúsculas y sin espacios alrededor.

</details>

### Problem 3 (Algorithm, 15 min)

Given an unsorted list of integers, return the length of the **longest sequence of consecutive integers**. Your solution should run in **O(n)** time.

```python
longest_consecutive([100, 4, 200, 1, 3, 2])   # 4  → the sequence is 1, 2, 3, 4
longest_consecutive([])                       # 0
```

<details>
<summary>🇪🇸 Traducción</summary>

Dada una lista desordenada de enteros, devuelve la longitud de la **secuencia más larga de enteros consecutivos**. Tu solución debe ejecutarse en tiempo **O(n)**.

</details>

---

<details>
<summary><b>Clave de respuestas: Parte 1</b></summary>

| # | Resp. | # | Resp. | # | Resp. | # | Resp. |
|---|---|---|---|---|---|---|---|
| 1 | B | 11 | B | 21 | B | 31 | C |
| 2 | C | 12 | B | 22 | B | 32 | B |
| 3 | D | 13 | B | 23 | A | 33 | B |
| 4 | B | 14 | B | 24 | C | 34 | B |
| 5 | B | 15 | A | 25 | C | 35 | B |
| 6 | B | 16 | B | 26 | B | 36 | C |
| 7 | B | 17 | B | 27 | A | 37 | A |
| 8 | B | 18 | D | 28 | B | 38 | B |
| 9 | C | 19 | C | 29 | A | 39 | B |
| 10 | B | 20 | B | 30 | B | 40 | A |

**Explicaciones de las más traicioneras:**

- **4:** DENSE_RANK → 500 = 1, 400 = 2, 400 = 2, 300 = **3** (sin saltos; con `RANK` sería 4).
- **5:** La C usa `= NULL`, que nunca es verdadero. Se usa `IS NULL`.
- **6:** División **entera** entre enteros. Para obtener 3.5: `7.0 / 2` o `CAST(7 AS DECIMAL) / 2`.
- **9:** `_` = exactamente un carácter cualquiera y después una "a". "M**a**ria" ✅; "Ana" tiene "n" en la 2.ª posición.
- **11:** "Blend 360" tiene 9 caracteres: el **espacio cuenta**.
- **14:** `b = a` no copia: las dos variables apuntan a la misma lista.
- **25:** Quick sort es O(n²) en el peor caso; merge sort siempre es O(n log n).
- **27:** log₂(1.000.000) ≈ 20.
- **28:** Suma de los impares 1 + 3 + 5 = 9.

**Puntaje:** 36–40 excelente · 30–35 bien · < 30 repasa los módulos de los temas que fallaste.

</details>

<details>
<summary><b>Soluciones: Parte 2</b></summary>

**Problem 1a**

```sql
SELECT customer_id,
       COUNT(*)    AS num_orders,
       SUM(amount) AS total_amount
FROM orders
GROUP BY customer_id
HAVING SUM(amount) > 500
ORDER BY total_amount DESC;
```

**Problem 1b**

```sql
WITH monthly AS (
    SELECT strftime('%Y-%m', order_date) AS month,      -- PostgreSQL: TO_CHAR(order_date, 'YYYY-MM')
           customer_id,
           SUM(amount) AS total
    FROM orders
    GROUP BY month, customer_id
),
ranked AS (
    SELECT *, RANK() OVER (PARTITION BY month ORDER BY total DESC) AS rk
    FROM monthly
)
SELECT month, customer_id, total
FROM ranked
WHERE rk = 1          -- RANK (no ROW_NUMBER) para devolver todos los empatados
ORDER BY month;
```

**Problem 2**

```python
def total_by_user(lines):
    totals = {}
    for line in lines:
        parts = line.split(",")
        if len(parts) != 2:
            continue
        user, raw_amount = parts[0].strip().lower(), parts[1].strip()
        if not user:
            continue
        try:
            amount = float(raw_amount)
        except ValueError:
            continue
        totals[user] = totals.get(user, 0) + amount
    return totals
```

**Problem 3**: set + empezar a contar solo desde el inicio de cada secuencia. O(n).

```python
def longest_consecutive(nums):
    values = set(nums)
    best = 0
    for x in values:
        if x - 1 not in values:          # x es el INICIO de una secuencia
            length = 1
            while x + length in values:
                length += 1
            best = max(best, length)
    return best
```

> ¿Por qué es O(n) si hay un `while` dentro del `for`? Porque el `while` solo arranca desde el inicio de cada secuencia, así que cada número se visita como máximo dos veces en total.

</details>
