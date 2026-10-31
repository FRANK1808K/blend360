# 05 · Databases: the theory that gets asked

[Español](README.md) · **English**

> SQL is the *language*; this module is the *theory*: modeling, keys, normalization, ACID, indexes, OLTP vs OLAP, NoSQL, data warehouse and data lake. These are typical multiple-choice and technical-interview questions.

---

## 1. Basic concepts

| Term | Spanish | Definition |
|---|---|---|
| Database | Base de datos | An organized collection of data |
| DBMS / RDBMS | SGBD / SGBD relacional | The software that manages it (PostgreSQL, MySQL, SQL Server, Oracle, SQLite) |
| Table / relation | Tabla / relación | A set of rows with the same columns |
| Row / record / tuple | Fila / registro / tupla | One specific entity |
| Column / field / attribute | Columna / campo / atributo | One property |
| Schema | Esquema | The structure: tables, columns, types, relationships |
| Query | Consulta | A question asked to the database |

## 2. Keys

| Key | Definition | Example |
|---|---|---|
| **Primary key (PK)** | **Uniquely** identifies each row. Does **not** allow NULLs or duplicates. Only one per table (it can have several columns) | `customer_id` |
| **Foreign key (FK)** | A column that **references** the PK of another table. Guarantees **referential integrity** | `orders.customer_id → customers.customer_id` |
| **Candidate key** | Any column (or group of columns) that could be the PK | `customer_id`, `email` |
| **Alternate key** | A candidate key that was not chosen as the PK | `email` |
| **Composite key** | A PK made of **several columns** | `(order_id, product_id)` in `order_items` |
| **Surrogate key** | An artificial PK with no business meaning (auto-increment, UUID) | `id SERIAL` |
| **Natural key** | A PK with real-world meaning | National ID number |
| **Unique** | A constraint: no duplicates, but it **does** allow NULLs (depending on the engine) | `email UNIQUE` |

**Other constraints:** `NOT NULL`, `CHECK (price > 0)`, `DEFAULT`.

**FK actions** when the parent row is deleted: `ON DELETE CASCADE` (also deletes the children), `SET NULL`, `RESTRICT` / `NO ACTION` (blocks the delete).

## 3. Relationships and the entity-relationship (ER) model

| Cardinality | Example | How it is implemented |
|---|---|---|
| **1:1** | Person ↔ passport | An FK with `UNIQUE` in one of the tables |
| **1:N** | Customer → orders | An FK in the "N" side table (`orders.customer_id`) |
| **N:M** | Orders ↔ products | A **junction table** (bridge / associative): `order_items(order_id, product_id)` |

```text
CUSTOMER ||──o{ ORDER ||──|{ ORDER_ITEM }|──|| PRODUCT
  (1 customer has 0..N orders; 1 order has 1..N lines; each line is for 1 product)
```

## 4. Normalization

The process of **removing redundancy** and **anomalies** (insert, update and delete anomalies) by splitting tables.

**Unnormalized table:**

| order_id | customer | customer_city | products |
|---|---|---|---|
| 101 | Ana | Bogotá | Laptop, Mouse |
| 103 | Ana | Bogotá | USB Hub |

| Normal form | Rule | What to fix in the example |
|---|---|---|
| **1NF** | **Atomic** values (one cell = one value) and no repeating groups | "Laptop, Mouse" → one row per product |
| **2NF** | 1NF + every non-key column depends on the **whole** PK (no **partial** dependencies; applies with a composite PK) | In `(order_id, product)`, `customer` depends only on `order_id` → move it to an `orders` table |
| **3NF** | 2NF + no **transitive** dependencies (a non-key column does not depend on another non-key column) | `customer_city` depends on `customer`, not on the order → a `customers` table |
| **BCNF** | A stricter version of 3NF: every determinant is a candidate key | — |

> Phrase to memorize: *"Every non-key attribute must depend on **the key** (1NF), **the whole key** (2NF), and **nothing but the key** (3NF)."*

**Denormalization:** duplicating data **on purpose** to make reads faster (fewer JOINs). Common in data warehouses and reports.

## 5. Transactions and ACID

A **transaction** is a group of operations executed as a **unit**: all or nothing. Example: a transfer (subtract from A and add to B).

| Property | Meaning | Example |
|---|---|---|
| **A**tomicity | All or nothing | If adding to B fails, the subtraction from A is also undone (`ROLLBACK`) |
| **C**onsistency | The DB goes from one valid state to another valid state (constraints are respected) | A balance cannot end up violating a `CHECK` |
| **I**solation | Concurrent transactions do not interfere with each other | Two people buying the last product |
| **D**urability | What was committed (`COMMIT`) persists even if the server crashes | It is written to the log on disk |

```sql
BEGIN TRANSACTION;
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
UPDATE accounts SET balance = balance + 100 WHERE id = 2;
COMMIT;      -- or ROLLBACK; if something failed
```

### Concurrency and isolation levels (frequent exam question)

When multiple transactions execute concurrently, three classic concurrency anomalies can occur:

1. **Dirty Read:** Transaction A reads data modified by Transaction B that has **not yet been committed** (`COMMIT`). If B rolls back (`ROLLBACK`), A read data that never formally existed.
2. **Non-Repeatable Read:** Transaction A reads a row. Transaction B modifies or deletes that row and commits. If A rereads the row, it sees different values.
3. **Phantom Read:** Transaction A queries a range of rows (e.g. `WHERE salary > 5000`). Transaction B inserts a new row satisfying the condition and commits. If A repeats the query, a "phantom" row appears.

| Isolation level | Dirty read | Non-repeatable read | Phantom read | Concurrency level |
|---|:---:|:---:|:---:|:---:|
| **Read Uncommitted** | Occurs | Occurs | Occurs | Maximum (no read locks) |
| **Read Committed** (default in PostgreSQL/SQL Server) | **No** | Occurs | Occurs | High |
| **Repeatable Read** (default in MySQL InnoDB) | **No** | **No** | Occurs (mitigated by MVCC) | Medium |
| **Serializable** | **No** | **No** | **No** | Lowest (strict range locking) |

> Higher isolation yields greater consistency, but lower concurrency and higher lock contention.

**Deadlock:** Occurs when Transaction 1 holds a lock on row A and requests row B, while Transaction 2 holds a lock on row B and requests row A. The database engine detects the cycle automatically, aborts one transaction, and raises an error so the application can retry.

## 6. Indexes

An **index** is an auxiliary data structure that finds rows without scanning the whole table, like an index at the back of a book.

| ✓ Advantages | ✗ Disadvantages |
|---|---|
| Searches, `JOIN`s, `WHERE` and `ORDER BY` are much faster ($O(\log n)$ vs. $O(n)$ *full table scan*) | Consumes additional disk space and buffer memory |
| Guarantees uniqueness (`UNIQUE` index) | Makes `INSERT`, `UPDATE` and `DELETE` **slower** (the engine must update the index tree) |

### B-Tree vs. Hash Index

| Feature | B-Tree Index (default) | Hash Index |
|---|---|---|
| **Structure** | Multi-level self-balancing search tree | Hash table with hash function and buckets |
| **Supported operators** | Equality (`=`), ranges (`<`, `>`, `BETWEEN`), ordering (`ORDER BY`), prefix search (`LIKE 'abc%'`) | **Strict equality only (`=`)** |
| **Lookup complexity** | Guaranteed $O(\log n)$ | Average $O(1)$ |
| **Typical use** | Relational and analytical tables | In-memory key-value lookups |

- **Clustered index:** Defines the **physical** storage order of rows on disk. Only **one per table** can exist (typically the Primary Key).
- **Non-clustered index:** A separate structure whose leaf nodes point (*RowID* or PK value) to data rows. Multiple non-clustered indexes can exist per table.
- **When to index:** Columns with **high cardinality** (many unique values, e.g. IDs, emails, dates) frequently filtered in `WHERE` or joined in `JOIN`.
- **When to avoid:** Small lookup tables, low-cardinality flags (e.g. boolean `active` with 50/50 distribution), or write-heavy ingestion staging tables.

## 7. Views, procedures and triggers

| Object | What it is |
|---|---|
| **View** | A saved query used like a virtual table. It does not store data |
| **Materialized view** | A view that **does** store the result; refreshed periodically. Widely used in analytics |
| **Stored procedure** | A block of SQL code saved in the DB and executed with `CALL` |
| **Function** | Like a procedure, but it returns a value and is used inside queries |
| **Trigger** | Code that runs **automatically** on an `INSERT`, `UPDATE` or `DELETE` |

## 8. OLTP vs OLAP

| | **OLTP** (Online Transaction Processing) | **OLAP** (Online Analytical Processing) |
|---|---|---|
| Purpose | Daily operations: sales, payments, records | Analysis, reports, BI |
| Queries | Many, short, read/write few rows | Few, complex, read **millions** of rows and aggregate |
| Design | Normalized (3NF) | Denormalized (star schema) |
| Storage | **Row**-based | **Column**-based (columnar) |
| Examples | PostgreSQL, MySQL, Amazon RDS / Aurora | Amazon Redshift, Snowflake, BigQuery |

**Why is columnar storage better for analytics?** A query like `SUM(revenue)` only needs to read **one** column, not the whole row. Also, the values in one column are similar to each other, so they **compress** much better.

## 9. Dimensional modeling (data warehouse)

**Star schema:** a **fact table** in the center surrounded by **dimension tables**.

```text
                 dim_date
                    │
dim_customer ── fact_sales ── dim_product
                    │
                 dim_store
```

| Table type | Contains | Example |
|---|---|---|
| **Fact** | Numeric metrics (*measures*) + FKs to the dimensions. Many rows | `fact_sales(date_key, product_key, customer_key, quantity, revenue)` |
| **Dimension** | Descriptive attributes to filter and group by (*who, what, where, when*) | `dim_product(product_key, name, category, brand)` |

- **Snowflake schema:** the dimensions are normalized into sub-tables (e.g., `dim_product → dim_category`). Saves space but requires more JOINs.
- **Grain:** what **one row** of the fact table represents (e.g., "one order line").

### Slowly Changing Dimensions (SCD)

In data analytics, tracking how descriptive attributes change over time is essential (e.g., when a customer moves cities):

| SCD Type | Strategy | Advantage | Disadvantage | Example (Customer moves from Bogotá to Medellín) |
|---|---|---|---|---|
| **SCD Type 1** | **Overwrite** the existing value | Simple, does not increase table size | Loses all historical context (past sales appear attributed to Medellín) | `city = 'Medellín'` updated on existing row |
| **SCD Type 2** | **New row** with versioning dates | **Preserves complete audit history** for point-in-time reporting | Table row count grows; requires surrogate keys | Row 1: `city='Bogotá'`, `end='2024-03-01'`, `is_current=False`.<br>Row 2: `city='Medellín'`, `start='2024-03-01'`, `is_current=True` |
| **SCD Type 3** | **New column** (`previous_city`) | Compares old vs current without duplicating rows | Only stores one previous state; cannot handle multi-step transitions | Columns: `current_city = 'Medellín'`, `previous_city = 'Bogotá'` |

## 10. Data warehouse vs. data lake vs. lakehouse

| | **Data warehouse** | **Data lake** | **Lakehouse** |
|---|---|---|---|
| Data | Structured, clean | Anything: structured, semi-structured (JSON) and unstructured (images, logs) | Anything |
| Schema | **Schema-on-write** (defined when loading) | **Schema-on-read** (defined when querying) | Both |
| Users | Business analysts, BI | Data scientists, engineers | Everyone |
| Storage cost | Higher | Low (object storage) | Low |
| On AWS | **Amazon Redshift** | **Amazon S3** (+ Glue Data Catalog + Athena) | S3 + open table formats (Apache Iceberg) + Redshift/Athena |

**Data mart:** a subset of the data warehouse dedicated to one area (e.g., the Marketing data mart).

## 11. ETL vs. ELT

| | **ETL** (Extract → Transform → Load) | **ELT** (Extract → Load → Transform) |
|---|---|---|
| Where it transforms | In an intermediate server/engine **before** loading | **Inside** the warehouse/lake after loading |
| When it makes sense | Sensitive data that must be cleaned first; destinations with little capacity | Modern cloud warehouses with plenty of compute |
| Tools | AWS Glue, Informatica | dbt + Redshift/Snowflake |

## 12. SQL vs. NoSQL

| NoSQL type | Model | Examples | Use case |
|---|---|---|---|
| **Key-value** | Key → value | Amazon **DynamoDB**, Redis (ElastiCache) | Sessions, shopping carts, cache |
| **Document** | JSON documents | MongoDB, Amazon DocumentDB | Catalogs, profiles with a variable structure |
| **Wide-column** | Rows with flexible columns | Apache Cassandra, Amazon Keyspaces | Time series, IoT, massive writes |
| **Graph** | Nodes and edges | Neo4j, Amazon **Neptune** | Social networks, recommendations, fraud |

| | SQL (relational) | NoSQL |
|---|---|---|
| Schema | Fixed, defined upfront | Flexible |
| Scaling | Mainly **vertical** (bigger machine) | **Horizontal** (more machines) |
| Consistency | Strong (ACID) | Often **eventual** (BASE model), configurable |
| Ideal for | Complex relationships, transactions, reports | High volume, low latency, semi-structured data |

**CAP theorem:** when there is a network **partition** (P), a distributed system must choose between **consistency** (C) and **availability** (A). It cannot guarantee all three at the same time.

## 13. Big data: the 5 Vs and file formats

**5 Vs:** Volume, Velocity, Variety, Veracity and Value.

| Format | Type | Comment |
|---|---|---|
| CSV | Text, row-based | Simple, untyped, heavy |
| JSON | Text, semi-structured | Flexible, heavy |
| **Parquet** | Binary, **columnar**, compressed | ★ The standard for analytics (Athena, Redshift Spectrum, Spark) |
| ORC | Binary, columnar | Similar to Parquet (Hive ecosystem) |
| Avro | Binary, row-based, with a schema | Streaming / Kafka |

**Partitioning:** organizing files into folders by a column (e.g., `s3://bucket/sales/year=2024/month=05/`). That way, queries that filter by date read **only** the folders they need (*partition pruning*). On Athena, that is faster and **cheaper**.

---

## Self-assessment

1. Why can't a PK be NULL?
2. In `order_items(order_id, product_id, quantity, product_name)`, which normal form is violated and why?
3. Which ACID property guarantees that a transfer is not left "half done"?
4. If a table receives 10,000 inserts per second and is almost never queried, would you add many indexes?
5. What would you use on AWS to store raw JSON logs at low cost and then query them with SQL?
6. What is the "grain" of a fact table?

<details>
<summary>Answers</summary>

1. Because the PK must uniquely identify each row, and NULL means "unknown": it does not identify anything.
2. **2NF**: `product_name` depends only on `product_id` (part of the composite PK). That is a partial dependency, so it belongs in the `products` table.
3. **Atomicity**.
4. No: each index slows down writes, and since it is rarely read, they are not used.
5. **Amazon S3** (data lake) + **AWS Glue Data Catalog** (schema) + **Amazon Athena** (serverless SQL). Even better if you convert them to Parquet and partition them.
6. What one row represents: the level of detail (e.g., one sale per product per day).

</details>

---

**Next:** [06 · AWS and data analytics](../06-aws/README.en.md)
