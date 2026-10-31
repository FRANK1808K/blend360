# 05 · Bases de datos: teoría que preguntan

**Español** · [English](README.en.md)

> SQL es el *lenguaje*; este módulo es la *teoría*: modelado, llaves, normalización, ACID, índices, OLTP vs OLAP, NoSQL, data warehouse y data lake. Son preguntas típicas de opción múltiple y de entrevista técnica.

---

## 1. Conceptos básicos

| Término (EN) | Español | Definición |
|---|---|---|
| Database | Base de datos | Colección organizada de datos |
| DBMS / RDBMS | SGBD / SGBD relacional | Software que la gestiona (PostgreSQL, MySQL, SQL Server, Oracle, SQLite) |
| Table / relation | Tabla / relación | Conjunto de filas con las mismas columnas |
| Row / record / tuple | Fila / registro / tupla | Una entidad concreta |
| Column / field / attribute | Columna / campo / atributo | Una propiedad |
| Schema | Esquema | Estructura: tablas, columnas, tipos, relaciones |
| Query | Consulta | Pregunta a la base de datos |

## 2. Llaves (keys)

| Llave | Definición | Ejemplo |
|---|---|---|
| **Primary key (PK)** | Identifica de forma **única** cada fila. **No** admite NULL ni duplicados. Solo una por tabla (puede tener varias columnas) | `customer_id` |
| **Foreign key (FK)** | Columna que **referencia** la PK de otra tabla. Garantiza la **integridad referencial** | `orders.customer_id → customers.customer_id` |
| **Candidate key** | Cualquier columna (o grupo) que podría ser PK | `customer_id`, `email` |
| **Alternate key** | Llave candidata que no se eligió como PK | `email` |
| **Composite key** | PK formada por **varias columnas** | `(order_id, product_id)` en `order_items` |
| **Surrogate key** | PK artificial, sin significado de negocio (autoincremental, UUID) | `id SERIAL` |
| **Natural key** | PK con significado real | Número de cédula |
| **Unique** | Restricción: sin duplicados, pero **sí** admite NULL (según el motor) | `email UNIQUE` |

**Otras restricciones (constraints):** `NOT NULL`, `CHECK (precio > 0)`, `DEFAULT`.

**Acciones de la FK** al borrar el padre: `ON DELETE CASCADE` (borra también los hijos), `SET NULL`, `RESTRICT` / `NO ACTION` (impide el borrado).

## 3. Relaciones y modelo entidad-relación (ER)

| Cardinalidad | Ejemplo | Cómo se implementa |
|---|---|---|
| **1:1** | Persona ↔ pasaporte | FK con `UNIQUE` en una de las tablas |
| **1:N** | Cliente → pedidos | FK en la tabla del lado "N" (`orders.customer_id`) |
| **N:M** | Pedidos ↔ productos | **Tabla intermedia** (puente / asociativa): `order_items(order_id, product_id)` |

```text
CUSTOMER ||──o{ ORDER ||──|{ ORDER_ITEM }|──|| PRODUCT
  (1 cliente tiene 0..N pedidos; 1 pedido tiene 1..N líneas; cada línea es de 1 producto)
```

## 4. Normalización

Proceso para **eliminar redundancia** y **anomalías** (de inserción, actualización y borrado) dividiendo tablas.

**Tabla sin normalizar:**

| order_id | customer | customer_city | products |
|---|---|---|---|
| 101 | Ana | Bogotá | Laptop, Mouse |
| 103 | Ana | Bogotá | USB Hub |

| Forma normal | Regla | Qué arreglar en el ejemplo |
|---|---|---|
| **1NF** | Valores **atómicos** (una celda = un valor) y sin grupos repetidos | "Laptop, Mouse" → una fila por producto |
| **2NF** | 1NF + toda columna no clave depende de **toda** la PK (sin dependencias **parciales**; aplica con PK compuesta) | En `(order_id, product)`, `customer` depende solo de `order_id` → mover a una tabla `orders` |
| **3NF** | 2NF + sin dependencias **transitivas** (una columna no clave no depende de otra columna no clave) | `customer_city` depende de `customer`, no del pedido → tabla `customers` |
| **BCNF** | Versión más estricta de 3NF: todo determinante es llave candidata | — |

> Frase para memorizar (en inglés, como la preguntan): *"Every non-key attribute must depend on **the key** (1NF), **the whole key** (2NF), and **nothing but the key** (3NF)."*

**Desnormalización:** duplicar datos **a propósito** para que las lecturas sean más rápidas (menos JOINs). Es común en data warehouses y reportes.

## 5. Transacciones y ACID

Una **transacción** es un grupo de operaciones que se ejecutan como una **unidad**: o todas o ninguna. Ejemplo: una transferencia (restar de A y sumar a B).

| Propiedad | Significado | Ejemplo |
|---|---|---|
| **A**tomicity | Todo o nada | Si falla la suma a B, también se deshace la resta a A (`ROLLBACK`) |
| **C**onsistency | La BD pasa de un estado válido a otro válido (se respetan las restricciones) | No puede quedar un saldo que viole un `CHECK` |
| **I**solation | Las transacciones concurrentes no se interfieren | Dos personas comprando el último producto |
| **D**urability | Lo confirmado (`COMMIT`) persiste aunque se caiga el servidor | Se escribe en el log en disco |

```sql
BEGIN TRANSACTION;
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
UPDATE accounts SET balance = balance + 100 WHERE id = 2;
COMMIT;      -- o ROLLBACK; si algo falló
```

### Concurrencia y niveles de aislamiento (pregunta fija de examen)

Cuando múltiples transacciones se ejecutan en paralelo, pueden ocurrir tres anomalías clásicas de concurrencia:

1. **Lectura sucia (Dirty Read):** La transacción A lee datos modificados por la transacción B que **aún no han sido confirmados** (`COMMIT`). Si B hace `ROLLBACK`, A leyó datos que nunca existieron formalmente.
2. **Lectura no repetible (Non-Repeatable Read):** La transacción A lee una fila. La transacción B modifica o borra esa misma fila y hace `COMMIT`. Si A vuelve a leer la fila, obtiene valores distintos.
3. **Lectura fantasma (Phantom Read):** La transacción A consulta un rango de filas (ej. `WHERE salario > 5000`). La transacción B inserta una fila nueva que cumple la condición y hace `COMMIT`. Si A repite la consulta, aparece una fila "fantasma" que antes no estaba.

| Nivel de aislamiento | Lectura sucia (*Dirty*) | Lectura no repetible | Lectura fantasma (*Phantom*) | Nivel de concurrencia |
|---|:---:|:---:|:---:|:---:|
| **Read Uncommitted** | Sí ocurre | Sí ocurre | Sí ocurre | Máxima (sin bloqueos de lectura) |
| **Read Committed** (por defecto en PostgreSQL/SQL Server) | **No** | Sí ocurre | Sí ocurre | Alta |
| **Repeatable Read** (por defecto en MySQL InnoDB) | **No** | **No** | Sí ocurre (mitigado con MVCC) | Media |
| **Serializable** | **No** | **No** | **No** | Baja (bloqueo estricto por rangos) |

> A mayor aislamiento, mayor consistencia de datos, pero menor concurrencia y mayor riesgo de bloqueos.

**Deadlock (interbloqueo):** Ocurre cuando la transacción 1 bloquea la fila A y espera la fila B, mientras la transacción 2 bloquea la fila B y espera la fila A. El motor detecta el ciclo automáticamente, cancela (*aborta*) una de las dos y lanza un error para que la aplicación reintente.

## 6. Índices

Un **índice** es una estructura auxiliar que permite encontrar filas sin recorrer toda la tabla, como el índice alfabético al final de un libro.

| ✓ Ventajas | ✗ Desventajas |
|---|---|
| Búsquedas, `JOIN`, `WHERE` y `ORDER BY` mucho más rápidos ($O(\log n)$ vs. $O(n)$ del *full table scan*) | Ocupan espacio adicional en disco y RAM |
| Garantizan unicidad (índice `UNIQUE`) | Hacen **más lentos** los `INSERT`, `UPDATE` y `DELETE` (el motor debe mantener el árbol) |

### B-Tree vs. Hash Index

| Característica | Índice B-Tree (predeterminado) | Índice Hash |
|---|---|---|
| **Estructura** | Árbol autobalanceado de búsqueda multinivel | Tabla hash con función hash y cubetas (*buckets*) |
| **Operaciones soportadas** | Igualdad (`=`), rangos (`<`, `>`, `BETWEEN`), ordenamiento (`ORDER BY`), prefijos (`LIKE 'abc%'`) | **Solo igualdad exacta (`=`)** |
| **Complejidad búsqueda** | $O(\log n)$ garantizado | $O(1)$ promedio |
| **Caso de uso** | Casi todas las tablas relacionales y analíticas | Búsquedas de clave-valor estricta en memoria |

- **Clustered index (Índice agrupado):** Define el ordenamiento **físico** de las filas en disco. Solo puede existir **uno por tabla** (generalmente la Primary Key).
- **Non-clustered index (Índice no agrupado):** Estructura separada cuyas hojas contienen punteros físicos (*RowID* o valor de PK) hacia los datos reales. Puede haber múltiples por tabla.
- **Cuándo indexar:** Columnas con **alta cardinalidad** (muchos valores distintos, ej. IDs, correos, fechas) muy consultadas en `WHERE` o `JOIN`.
- **Cuándo evitarlo:** Tablas con pocas filas, columnas con baja cardinalidad (ej. un booleano `activo` con 50/50), o tablas de ingesta masiva con miles de escrituras por segundo.

## 7. Vistas, procedimientos y triggers

| Objeto | Qué es |
|---|---|
| **View (vista)** | Consulta guardada que se usa como una tabla virtual. No guarda datos |
| **Materialized view** | Vista que **sí** guarda el resultado; se refresca periódicamente. Es muy usada en analítica |
| **Stored procedure** | Bloque de código SQL guardado en la BD que se ejecuta con `CALL` |
| **Function** | Como un procedimiento, pero devuelve un valor y se usa dentro de consultas |
| **Trigger** | Código que se ejecuta **automáticamente** ante un `INSERT`, `UPDATE` o `DELETE` |

## 8. OLTP vs OLAP

| | **OLTP** (Online Transaction Processing) | **OLAP** (Online Analytical Processing) |
|---|---|---|
| Propósito | Operación diaria: ventas, pagos, registros | Análisis, reportes, BI |
| Consultas | Muchas, cortas, leen/escriben pocas filas | Pocas, complejas, leen **millones** de filas y agregan |
| Diseño | Normalizado (3NF) | Desnormalizado (esquema estrella) |
| Almacenamiento | Por **filas** | Por **columnas** (columnar) |
| Ejemplos | PostgreSQL, MySQL, Amazon RDS / Aurora | Amazon Redshift, Snowflake, BigQuery |

**¿Por qué el almacenamiento columnar es mejor para analítica?** Una consulta como `SUM(revenue)` solo necesita leer **una** columna, no la fila completa. Además, los datos de una columna se parecen entre sí y se **comprimen** mucho mejor.

## 9. Modelado dimensional (data warehouse)

**Esquema estrella (star schema):** una **tabla de hechos** en el centro rodeada de **tablas de dimensiones**.

```text
                 dim_date
                    │
dim_customer ── fact_sales ── dim_product
                    │
                 dim_store
```

| Tipo de tabla | Contiene | Ejemplo |
|---|---|---|
| **Fact (hechos)** | Métricas numéricas (*measures*) + FKs a las dimensiones. Muchas filas | `fact_sales(date_key, product_key, customer_key, quantity, revenue)` |
| **Dimension** | Atributos descriptivos para filtrar y agrupar (*quién, qué, dónde, cuándo*) | `dim_product(product_key, name, category, brand)` |

- **Snowflake schema:** las dimensiones se normalizan en subtablas (por ejemplo, `dim_product → dim_category`). Ahorra espacio, pero requiere más JOINs.
- **Granularidad (grain):** qué representa **una fila** de la tabla de hechos (por ejemplo, "una línea de pedido").

### Dimensiones de cambio lento (Slowly Changing Dimensions - SCD)

En analítica de datos es vital saber cómo evoluciona la información descriptiva en el tiempo (por ejemplo, si un cliente se muda de ciudad):

| Tipo SCD | Estrategia | Ventaja | Desventaja | Ejemplo (Cliente cambia de Bogotá a Medellín) |
|---|---|---|---|---|
| **SCD Tipo 1** | **Sobrescribir** el valor actual | Fácil de implementar, no aumenta el tamaño de la tabla | Se pierde todo el historial previo (las ventas pasadas parecerán de Medellín) | `ciudad = 'Medellín'` sobre la fila existente |
| **SCD Tipo 2** | **Nueva fila** con control de fechas | **Conserva el historial completo** de auditoría y análisis temporal | Aumenta el número de filas en la dimensión; requiere llaves subrogadas | Fila 1: `ciudad='Bogotá'`, `fin='2024-03-01'`, `is_current=False`.<br>Fila 2: `ciudad='Medellín'`, `inicio='2024-03-01'`, `is_current=True` |
| **SCD Tipo 3** | **Nueva columna** (`previous_city`) | Permite comparar el valor anterior sin duplicar filas | Solo guarda el estado anterior inmediato; no sirve para múltiples cambios | Columnas: `ciudad_actual = 'Medellín'`, `ciudad_anterior = 'Bogotá'` |

## 10. Data warehouse vs. data lake vs. lakehouse

| | **Data warehouse** | **Data lake** | **Lakehouse** |
|---|---|---|---|
| Datos | Estructurados, limpios | Cualquiera: estructurados, semiestructurados (JSON) y no estructurados (imágenes, logs) | Cualquiera |
| Esquema | **Schema-on-write** (se define al cargar) | **Schema-on-read** (se define al consultar) | Ambos |
| Usuarios | Analistas de negocio, BI | Data scientists, ingenieros | Todos |
| Costo de almacenamiento | Mayor | Bajo (almacenamiento de objetos) | Bajo |
| En AWS | **Amazon Redshift** | **Amazon S3** (+ Glue Data Catalog + Athena) | S3 + formatos de tabla abiertos (Apache Iceberg) + Redshift/Athena |

**Data mart:** subconjunto del data warehouse dedicado a un área (por ejemplo, el data mart de Marketing).

## 11. ETL vs. ELT

| | **ETL** (Extract → Transform → Load) | **ELT** (Extract → Load → Transform) |
|---|---|---|
| Dónde se transforma | En un servidor/motor intermedio **antes** de cargar | **Dentro** del warehouse/lake después de cargar |
| Cuándo conviene | Datos sensibles que hay que limpiar antes; destinos con poca capacidad | Warehouses modernos en la nube con mucha capacidad de cómputo |
| Herramientas | AWS Glue, Informatica | dbt + Redshift/Snowflake |

## 12. SQL vs. NoSQL

| Tipo NoSQL | Modelo | Ejemplos | Caso de uso |
|---|---|---|---|
| **Key-value** | Clave → valor | Amazon **DynamoDB**, Redis (ElastiCache) | Sesiones, carritos, caché |
| **Document** | Documentos JSON | MongoDB, Amazon DocumentDB | Catálogos, perfiles con estructura variable |
| **Wide-column** | Filas con columnas flexibles | Apache Cassandra, Amazon Keyspaces | Series de tiempo, IoT, escritura masiva |
| **Graph** | Nodos y aristas | Neo4j, Amazon **Neptune** | Redes sociales, recomendaciones, fraude |

| | SQL (relacional) | NoSQL |
|---|---|---|
| Esquema | Fijo, definido antes | Flexible |
| Escalado | Principalmente **vertical** (máquina más grande) | **Horizontal** (más máquinas) |
| Consistencia | Fuerte (ACID) | A menudo **eventual** (modelo BASE), configurable |
| Ideal para | Relaciones complejas, transacciones, reportes | Gran volumen, baja latencia, datos semiestructurados |

**Teorema CAP:** un sistema distribuido, ante una **partición** de red (P), debe elegir entre **consistencia** (C) y **disponibilidad** (A). No puede garantizar las tres a la vez.

## 13. Big data: las 5 V y formatos de archivo

**5 V:** Volumen, Velocidad, Variedad, Veracidad y Valor.

| Formato | Tipo | Comentario |
|---|---|---|
| CSV | Texto, por filas | Simple, sin tipos, pesado |
| JSON | Texto, semiestructurado | Flexible, pesado |
| **Parquet** | Binario, **columnar**, comprimido | ★ El estándar para analítica (Athena, Redshift Spectrum, Spark) |
| ORC | Binario, columnar | Similar a Parquet (ecosistema Hive) |
| Avro | Binario, por filas, con esquema | Streaming / Kafka |

**Particionamiento:** organizar los archivos en carpetas por una columna (por ejemplo, `s3://bucket/ventas/year=2024/month=05/`). Así las consultas que filtran por fecha leen **solo** las carpetas necesarias (*partition pruning*), y en Athena eso es más rápido y **más barato**.

---

## Autoevaluación

1. ¿Por qué una PK no puede ser NULL?
2. En `order_items(order_id, product_id, quantity, product_name)`, ¿qué forma normal se viola y por qué?
3. ¿Qué propiedad ACID garantiza que una transferencia no quede "a medias"?
4. Si una tabla recibe 10.000 inserciones por segundo y casi nunca se consulta, ¿le agregarías muchos índices?
5. ¿Qué usarías para guardar logs JSON crudos a bajo costo y después consultarlos con SQL en AWS?
6. ¿Qué es la "granularidad" de una tabla de hechos?

<details>
<summary>Respuestas</summary>

1. Porque la PK debe identificar de forma única cada fila, y NULL significa "desconocido": no identifica nada.
2. **2NF**: `product_name` depende solo de `product_id` (una parte de la PK compuesta). Es una dependencia parcial, así que debe ir en la tabla `products`.
3. **Atomicidad**.
4. No: cada índice hace más lentas las escrituras, y como casi no se lee, no se aprovechan.
5. **Amazon S3** (data lake) + **AWS Glue Data Catalog** (esquema) + **Amazon Athena** (SQL serverless). Mejor todavía si los conviertes a Parquet y los particionas.
6. Qué representa una fila: el nivel de detalle (por ejemplo, una venta por producto por día).

</details>

---

**Siguiente:** [06 · AWS y análisis de datos](../06-aws/README.md)
