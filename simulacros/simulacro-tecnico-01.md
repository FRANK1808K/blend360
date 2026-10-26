# Mock technical exam #1: 90 minutes (simulacro técnico)

> **Instrucciones (como en el examen real):**
>
> - **Time: 90 minutes.** Part 1: 40 multiple-choice questions (~50 min). Part 2: 3 coding problems (~40 min).
> - Pon un cronómetro, **sin** buscar en internet y sin ejecutar código en la parte 1.
> - Escribe tus respuestas en un papel y revisa al final.
> - Todo está en **inglés**. Si una palabra te bloquea, sigue adelante y anótala para tus flashcards.

---

## Part 1: Multiple choice (40 questions)

### SQL

**1.** Which clause is used to filter groups AFTER an aggregation?
A) WHERE B) HAVING C) ORDER BY D) LIMIT

**2.** A table has 10 rows. The column `email` contains 3 NULL values. What does `SELECT COUNT(*), COUNT(email) FROM t;` return?
A) 10, 10 B) 7, 7 C) 10, 7 D) 7, 10

**3.** Table A has 4 rows and table B has 3 rows. How many rows does `SELECT * FROM A CROSS JOIN B;` return?
A) 3 B) 4 C) 7 D) 12

**4.** The salaries are 500, 400, 400 and 300. What is the `DENSE_RANK()` (ordered by salary descending) of the salary 300?
A) 2 B) 3 C) 4 D) 1

**5.** Which query returns the customers who have NEVER placed an order?
A) `SELECT c.* FROM customers c JOIN orders o ON o.customer_id = c.id;`
B) `SELECT c.* FROM customers c LEFT JOIN orders o ON o.customer_id = c.id WHERE o.id IS NULL;`
C) `SELECT c.* FROM customers c LEFT JOIN orders o ON o.customer_id = c.id WHERE o.id = NULL;`
D) `SELECT * FROM orders WHERE customer_id IS NULL;`

**6.** In PostgreSQL and SQL Server, what is the result of `SELECT 7 / 2;`?
A) 3.5 B) 3 C) 4 D) An error

**7.** Which operator combines the results of two queries and KEEPS the duplicate rows?
A) UNION B) UNION ALL C) INTERSECT D) EXCEPT

**8.** What is the correct LOGICAL order of execution of a SQL query?
A) SELECT → FROM → WHERE → GROUP BY
B) FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY
C) FROM → SELECT → WHERE → ORDER BY
D) WHERE → FROM → SELECT → HAVING

**9.** Which name matches the condition `WHERE name LIKE '_a%'`?
A) Ana B) Pedro C) Maria D) Andrea

**10.** What is wrong with this query? `SELECT department, COUNT(*) FROM employees;`
A) COUNT(*) cannot be used with other columns
B) It needs `GROUP BY department`
C) It needs a WHERE clause
D) Nothing, it is correct in all databases

### Python

**11.** What is the output? `print(len("Blend 360"))`
A) 8 B) 9 C) 10 D) 7

**12.** What is the output?

```python
x = [1, 2, 3]
print(x[-1] + x[0])
```

A) 3 B) 4 C) 5 D) An error

**13.** What is the output? `print(10 // 3, 10 % 3)`
A) 3.33 1 B) 3 1 C) 3 0 D) 1 3

**14.** What is the output?

```python
a = [1, 2]
b = a
b.append(3)
print(a)
```

A) [1, 2] B) [1, 2, 3] C) [3, 1, 2] D) An error

**15.** What is the output? `print({1, 2, 2, 3} == {3, 2, 1})`
A) True B) False C) An error D) None

**16.** What is the output?

```python
d = {"a": 1}
print(d.get("b", 0) + d["a"])
```

A) 0 B) 1 C) KeyError D) None

**17.** What is the output? `print([x for x in range(10) if x % 3 == 0])`
A) [3, 6, 9] B) [0, 3, 6, 9] C) [0, 3, 6] D) [1, 4, 7]

**18.** Which of the following Python types is IMMUTABLE?
A) list B) dict C) set D) tuple

**19.** What is the output?

```python
def f(n):
    return n if n <= 1 else n * f(n - 1)
print(f(4))
```

A) 4 B) 10 C) 24 D) 16

**20.** What is the output? `print("a,b,c".split(",")[1].upper())`
A) A B) B C) b D) ['B']

### Algorithms and data structures

**21.** What is the time complexity of binary search on a sorted array?
A) O(1) B) O(log n) C) O(n) D) O(n log n)

**22.** Which data structure follows the LIFO (Last In, First Out) principle?
A) Queue B) Stack C) Heap D) Linked list

**23.** What is the AVERAGE time complexity of looking up a key in a Python dictionary (hash table)?
A) O(1) B) O(log n) C) O(n) D) O(n²)

**24.** An algorithm has two nested loops, and each one iterates over n elements. What is its time complexity?
A) O(n) B) O(2n) C) O(n²) D) O(log n)

**25.** Which sorting algorithm has a WORST-CASE time complexity of O(n log n)?
A) Quick sort B) Bubble sort C) Merge sort D) Insertion sort

**26.** Which data structure is used to implement Breadth-First Search (BFS)?
A) Stack B) Queue C) Hash table D) Binary search tree

**27.** Approximately how many steps does binary search need, in the worst case, to find an element in a sorted list of 1,000,000 elements?
A) 20 B) 1,000 C) 500,000 D) 1,000,000

**28.** What is the value of `s` at the end?

```text
s ← 0
for i from 1 to 5:
    if i mod 2 = 1:
        s ← s + i
```

A) 6 B) 9 C) 15 D) 5

### Databases

**29.** Which ACID property guarantees that ALL the operations of a transaction are completed, or NONE of them?
A) Atomicity B) Consistency C) Isolation D) Durability

**30.** What is the main purpose of a foreign key?
A) To make queries faster
B) To guarantee referential integrity between tables
C) To encrypt a column
D) To allow NULL values in a primary key

**31.** Which normal form removes TRANSITIVE dependencies?
A) 1NF B) 2NF C) 3NF D) None

**32.** What is a disadvantage of adding many indexes to a table?
A) SELECT queries become slower
B) INSERT, UPDATE and DELETE operations become slower
C) The table cannot have a primary key
D) The data is deleted

**33.** Which of the following is typical of an OLAP system?
A) Many short transactions that update few rows
B) Complex queries that aggregate millions of rows, often with columnar storage
C) Strictly normalized tables to process payments
D) It is used to process credit card payments in real time

**34.** In a star schema, which table contains the numeric measures (for example, revenue and quantity)?
A) Dimension table B) Fact table C) Lookup table D) Staging table

### AWS and data analytics

**35.** Which AWS service lets you run SQL queries directly on data stored in Amazon S3 without managing any servers?
A) Amazon RDS B) Amazon Athena C) Amazon EC2 D) Amazon DynamoDB

**36.** Under the AWS shared responsibility model, which of the following is the CUSTOMER's responsibility?
A) The physical security of data centers
B) The hardware of the servers
C) Managing IAM users and permissions
D) The global network infrastructure

**37.** Which AWS service is a petabyte-scale, columnar data warehouse?
A) Amazon Redshift B) Amazon S3 C) AWS Lambda D) Amazon Aurora

**38.** A company needs to ingest clickstream events in real time and process them with custom applications. Which service is the BEST fit?
A) AWS Glue DataBrew B) Amazon Kinesis Data Streams C) Amazon S3 Glacier D) AWS Snowball

**39.** What does an AWS Glue crawler do?
A) It deletes old data from S3
B) It scans data sources, infers the schema and creates tables in the Data Catalog
C) It creates dashboards
D) It monitors EC2 instances

**40.** Which AWS service is used to build interactive BI dashboards?
A) Amazon QuickSight B) AWS CloudTrail C) Amazon SQS D) AWS IAM

---

## Part 2: Coding problems (~40 minutes)

### Problem 1 (SQL, 12 min)

Table `orders(order_id, customer_id, order_date, amount)`.

**a)** Return the `customer_id`, the number of orders and the total amount of each customer, **only** for customers whose total amount is **greater than 500**. Sort by total amount, from highest to lowest.

**b)** For each month (`YYYY-MM`), return the customer with the **highest total amount** in that month. In case of ties, return all of them.

### Problem 2 (Python, 12 min)

You receive a list of strings with the format `"user,amount"`. Some lines are **invalid** (missing fields, empty values or an amount that is not a number). Write a function `total_by_user(lines)` that returns a dictionary `{user: total_amount}` that **ignores the invalid lines**. User names must be in lowercase and without surrounding spaces.

```python
lines = ["ana,10.5", "Luis, 20", "ana,4.5", "bad line", "pedro,abc", ",5", " LUIS ,1"]
total_by_user(lines)  # {'ana': 15.0, 'luis': 21.0}
```

### Problem 3 (Algorithm, 15 min)

Given an unsorted list of integers, return the length of the **longest sequence of consecutive integers**. Your solution should run in **O(n)** time.

```python
longest_consecutive([100, 4, 200, 1, 3, 2])   # 4  → the sequence is 1, 2, 3, 4
longest_consecutive([])                       # 0
```

---

<details>
<summary><b>Answer key: Part 1 (clave de respuestas)</b></summary>

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
- **5:** la C usa `= NULL`, que nunca es verdadero. Se usa `IS NULL`.
- **6:** división **entera** entre enteros. Para obtener 3.5: `7.0 / 2` o `CAST(7 AS DECIMAL) / 2`.
- **9:** `_` = exactamente un carácter cualquiera y después una "a". "M**a**ria" ✅; "Ana" tiene "n" en la 2.ª posición.
- **11:** "Blend 360" tiene 9 caracteres: el **espacio cuenta**.
- **14:** `b = a` no copia: las dos variables apuntan a la misma lista.
- **25:** quick sort es O(n²) en el peor caso; merge sort siempre es O(n log n).
- **27:** log₂(1.000.000) ≈ 20.
- **28:** suma de los impares 1 + 3 + 5 = 9.

**Puntaje:** 36–40 excelente · 30–35 bien · < 30 repasa los módulos de los temas que fallaste.

</details>

<details>
<summary><b>Solutions: Part 2</b></summary>

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
