# 06b · Análisis de datos en AWS

**Español** · [English](analisis-de-datos.en.md)

> Este es el corazón del trabajo de Blend360 con AWS: **construir plataformas de datos y analítica para clientes**. Blend tiene la competencia **AWS Data & Analytics** y es *delivery partner* de **Amazon EMR** y **Amazon QuickSight**, así que esos servicios merecen atención especial.

---

## 1. El ciclo de vida de los datos (y qué servicio va en cada etapa)

```text
 FUENTES           INGESTA              ALMACENAMIENTO         PROCESAMIENTO          ANÁLISIS / CONSULTA     VISUALIZACIÓN / ML
 ─────────         ─────────            ───────────────        ─────────────          ──────────────────      ──────────────────
 Bases de datos →  AWS DMS          →                          AWS Glue (ETL)     →   Amazon Athena       →   Amazon QuickSight
 Apps / logs   →   Amazon Data         Amazon S3              Amazon EMR (Spark)     Amazon Redshift         Amazon SageMaker AI
 IoT / clicks  →   Firehose,       →   (data lake)        →   AWS Lambda             Amazon OpenSearch       Amazon Bedrock
 SaaS          →   Kinesis Data        + Glue Data Catalog    Managed Service for
 Archivos      →   Streams, MSK,       + Lake Formation       Apache Flink
                   AppFlow, DataSync   (gobierno)

                         Orquestación: AWS Step Functions · Amazon MWAA (Airflow) · Glue Workflows · EventBridge
                         Monitoreo: CloudWatch · Auditoría: CloudTrail · Seguridad: IAM, KMS, Lake Formation
```

## 2. Servicios, uno por uno

### Almacenamiento: Amazon S3 como data lake

- Almacenamiento de **objetos**, barato, durable (11 nueves) y prácticamente ilimitado. Es la **base** de casi toda arquitectura de datos en AWS.
- Organización típica por **capas** (arquitectura *medallion*):

| Capa | También llamada | Contenido |
|---|---|---|
| **Raw** | Bronze / landing | Datos tal como llegan (CSV, JSON), sin tocar |
| **Clean / curated** | Silver | Limpios, tipados, deduplicados, en **Parquet** |
| **Analytics** | Gold / consumption | Agregados y modelados para el negocio (tablas listas para BI) |

- **Particiona** por fecha u otra columna muy filtrada: `s3://lake/silver/sales/year=2024/month=06/day=15/part-000.parquet`.

### Catálogo: AWS Glue Data Catalog

- **Metastore** central: guarda el **esquema** (tablas, columnas, tipos, particiones) de los datos que están en S3. Los datos se quedan en S3; el catálogo solo los describe.
- Lo usan **Athena, Redshift Spectrum, EMR y Glue ETL**.
- **Glue crawler:** recorre S3, **infiere el esquema** automáticamente y crea o actualiza las tablas del catálogo.

### Procesamiento / ETL

| Servicio | Qué es | Cuándo elegirlo |
|---|---|---|
| **AWS Glue (ETL jobs)** | ETL **serverless** basado en **Apache Spark** (PySpark/Scala) o Python Shell | ETL sin administrar clústeres; pagas por DPU-hora |
| **AWS Glue DataBrew** | Preparación visual de datos **sin código** (más de 250 transformaciones) | Analistas que limpian y perfilan datos sin programar |
| **Amazon EMR** | Clústeres gestionados de **Spark, Hadoop, Hive, Presto/Trino, HBase**. Hay EMR on EC2, **EMR Serverless** y EMR on EKS | Big data a gran escala, control fino del clúster, frameworks open source. Abarata costos con instancias **Spot** |
| **AWS Lambda** | Funciones cortas por eventos | Transformaciones pequeñas (por ejemplo, al llegar un archivo a S3) |
| **Amazon Managed Service for Apache Flink** (antes Kinesis Data Analytics) | Procesamiento de **streams** en tiempo real con SQL/Java/Python | Agregaciones en tiempo real, detección de anomalías |

> **Glue vs. EMR:** Glue es **serverless** y más simple: no hay que gestionar nada. EMR da **más control y flexibilidad** (versiones, frameworks, tipo de instancias) y suele ser más económico en cargas grandes y continuas.

### Ingesta

| Servicio | Tipo | Detalle |
|---|---|---|
| **Amazon Kinesis Data Streams** | Streaming en **tiempo real** | Tú escribes los consumidores (Lambda, Flink, apps). Capacidad en *shards*. Retención configurable (24 h por defecto, ampliable) |
| **Amazon Data Firehose** (antes Kinesis Data Firehose) | Entrega **casi en tiempo real** (con *buffer*) | Totalmente gestionado: carga streams en **S3, Redshift, OpenSearch** o Splunk. Puede convertir a Parquet. Sin código |
| **Amazon MSK** | Apache **Kafka** gestionado | Si el cliente ya usa Kafka |
| **AWS DMS** (Database Migration Service) | Migración/replicación de **bases de datos** | Carga completa + **CDC** (*change data capture*: replica los cambios en curso) hacia S3, Redshift, etc. |
| **Amazon AppFlow** | Integración con **SaaS** | Salesforce, Google Analytics, Zendesk → S3/Redshift sin código |
| **AWS DataSync** | Transferencia de **archivos** | Servidores de archivos on-premises → S3/EFS |
| **AWS Snow Family** | Dispositivos físicos | Petabytes sin buena conexión |

> **Kinesis Data Streams vs. Firehose:** *Streams* = tiempo real, consumidores personalizados, tú gestionas la capacidad. *Firehose* = "manguera" totalmente gestionada que **entrega** datos a un destino en casi tiempo real (segundos o minutos de buffer), sin código.

### Consulta y data warehouse

| Servicio | Qué es | Cómo se paga | Cuándo |
|---|---|---|---|
| **Amazon Athena** | **SQL serverless** directamente sobre archivos en **S3** (motor Trino/Presto) usando el Glue Data Catalog | Por **datos escaneados** (TB) | Consultas ad hoc sobre el data lake, sin infraestructura |
| **Amazon Redshift** | **Data warehouse** columnar con procesamiento masivamente paralelo (**MPP**) | Por nodo/hora (aprovisionado) o por uso (**Redshift Serverless**) | BI con muchas consultas repetidas y complejas sobre datos estructurados, a gran escala |
| **Redshift Spectrum** | Consultar desde Redshift datos que están en S3 sin cargarlos | Por datos escaneados | Unir el warehouse con el lake |
| **Amazon OpenSearch Service** | Búsqueda y análisis de **logs** (Elasticsearch/OpenSearch + dashboards) | Por instancia / serverless | Búsqueda de texto, observabilidad, análisis de logs |

**Cómo optimizar costos y velocidad en Amazon Athena (pregunta fija):**

Athena cobra **$5 por cada TB de datos escaneado** en S3. La optimización consiste en escanear el mínimo de bytes posible:

| Estrategia | Efecto técnico | Reducción de datos escaneados |
|---|---|:---:|
| **Formato Columnar (Parquet/ORC)** | Lee solo las columnas requeridas por el `SELECT`, ignorando las demás columnas | 60% – 80% |
| **Compresión (Snappy / GZIP)** | Los datos columnares similares se comprimen con alta tasa | 70% – 85% |
| **Particionamiento (`year=2024/month=03/`)** | Omite por completo carpetas no coincidentes en el `WHERE` | 90% – 99% |
| **Tamaño óptimo de archivos (128 MB – 512 MB)** | Evita la sobrecarga de metadatos de millones de archivos pequeños | Mayor throughput |

> **Impacto real:** Una consulta sobre 1 TB de CSV sin particionar cuesta **$5.00**. La misma consulta sobre datos particionados en Parquet comprimido con Snappy escanea ~2 GB y cuesta **$0.01** (ahorro del 99.8%).

**Arquitectura profunda de Amazon Redshift (MPP):**

- **Nodo Líder (Leader Node):** Punto de enlace SQL. Recibe la consulta del cliente, la parsea, compila código C++ optimizado y coordina la ejecución en paralelo. No almacena datos de usuario.
- **Nodos de Cómputo (Compute Nodes):** Ejecutan las porciones de código en paralelo. Cada nodo se divide en **slices** (porciones de memoria y disco) que procesan su segmento de datos.
- **Estilos de Distribución (`DISTSTYLE`):**
  - **`KEY`:** Reparte las filas según el valor hash de una columna. Si dos tablas grandes hacen `JOIN` por esa misma columna, las filas correspondientes quedan en el **mismo slice físico**, evitando el costosísimo movimiento de datos por la red (*data redistribution/broadcast*).
  - **`EVEN`:** Distribución Round-Robin uniforme. Se usa cuando la tabla no tiene un `JOIN` claro o para tablas de hechos intermedias.
  - **`ALL`:** Almacena una copia idéntica de la tabla en el primer slice de cada nodo. **Ideal para tablas dimensionales pequeñas** (< 2–3 millones de filas) como `dim_date` o `dim_category`, garantizando JOINs locales instantáneos.
  - **`AUTO`:** Redshift decide automáticamente (asigna `ALL` mientras sea pequeña y migra a `EVEN` al crecer).
- **Claves de Ordenamiento (`SORTKEY`):**
  - **`COMPOUND`:** Ordenamiento jerárquico clásico (columna A, luego B). Óptimo para filtros de prefijo estricto.
  - **`INTERLEAVED`:** Asigna el mismo peso a varias columnas. Ideal cuando las consultas filtran distintas combinaciones de columnas de forma impredecible.
- **Comando `COPY` masivo:** Carga datos en paralelo directamente desde múltiples archivos de S3 a los slices de cómputo. Es entre 100x y 1000x más rápido que ejecutar sentencias `INSERT` individuales.
- **Integraciones Zero-ETL:** Replicación gestionada y continua de bases transaccionales (Aurora PostgreSQL/MySQL, DynamoDB) hacia Redshift en segundos sin pipelines de Glue.

### Gobierno y seguridad de datos

| Servicio | Para qué |
|---|---|
| **AWS Lake Formation** | Construir y **gobernar** el data lake: permisos finos por base de datos, tabla, **columna** y fila, sobre los datos de S3/Glue Catalog |
| **IAM** | Quién puede usar qué servicio o recurso |
| **AWS KMS** | Cifrado de datos en reposo (S3, Redshift, Glue) |
| **Amazon Macie** | Descubrir **datos sensibles (PII)** en S3 |
| **Amazon DataZone / SageMaker Unified Studio** | Catálogo de negocio, descubrimiento y gobierno de datos entre equipos |

### Visualización: Amazon QuickSight

- Servicio de **BI serverless** en la nube: dashboards interactivos, reportes y *embedded analytics* (incrustar dashboards en aplicaciones).
- **SPICE:** motor **en memoria** que acelera los dashboards (importas los datos a SPICE en lugar de consultar la fuente en cada clic).
- Fuentes: Athena, Redshift, RDS/Aurora, S3, Snowflake, Salesforce, archivos…
- **ML Insights** (detección de anomalías, pronósticos) y consultas en **lenguaje natural** con IA generativa (Amazon Q en QuickSight).
- Pago por usuario (autores y lectores).
- En 2025, AWS integró QuickSight dentro de **Amazon Quick Suite** (como "Quick Sight"). Si ves cualquiera de los dos nombres, es el servicio de BI de AWS.

### Machine learning e IA (lo justo)

- **Amazon SageMaker AI:** preparar datos, entrenar, ajustar y **desplegar** modelos de ML.
- **Amazon Bedrock:** IA generativa por API (modelos fundacionales), RAG con *Knowledge Bases*, agentes. Blend tiene la competencia **AWS Generative AI**.
- Servicios de IA preentrenados: **Comprehend** (NLP: sentimiento, entidades), **Rekognition** (imágenes/video), **Textract** (extraer texto y tablas de documentos), **Forecast**, **Personalize** (recomendaciones), **Transcribe** (voz → texto), **Translate**, **Polly** (texto → voz).

### Orquestación

| Servicio | Cuándo |
|---|---|
| **AWS Step Functions** | Flujos con pasos, reintentos y ramas entre servicios AWS (serverless, visual) |
| **Amazon MWAA** (Managed Workflows for Apache Airflow) | El cliente ya usa **Airflow** o necesita DAGs complejos en Python |
| **AWS Glue Workflows / Triggers** | Encadenar crawlers y jobs de Glue |
| **Amazon EventBridge** | Disparar procesos por eventos o por horario (*cron*) |

## 3. Arquitecturas de referencia (dibújalas de memoria)

### A) Data lake batch (la más común)

```text
RDS / ERP ──(AWS DMS)──┐
Salesforce ─(AppFlow)──┼──> S3 raw ──(Glue crawler)──> Glue Data Catalog
Archivos CSV ──────────┘        │
                                └──(Glue ETL / EMR Spark: limpiar, Parquet, particionar)──> S3 curated
                                                                                              │
                                     ┌────────────────────────────────────────────────────────┤
                                     ▼                                                        ▼
                               Amazon Athena (ad hoc)                           Amazon Redshift (COPY / Spectrum)
                                     └──────────────────> Amazon QuickSight <─────────────────┘
Orquestado con Step Functions o MWAA · Gobernado con Lake Formation · Cifrado con KMS
```

### B) Streaming en tiempo real (por ejemplo, clics de un e-commerce)

```text
Web/App ──> Kinesis Data Streams ──> Managed Service for Apache Flink (métricas por minuto) ──> Redshift / OpenSearch ──> Dashboard
                    │
                    └──> Amazon Data Firehose ──(Parquet)──> S3 (histórico para Athena/ML)
```

### C) Analítica de marketing (típico de Blend360)

```text
Google Analytics / CRM / redes ──(AppFlow)──> S3 ──(Glue)──> Redshift (modelo estrella: fact_campaign_performance)
   ──> QuickSight (ROI por campaña) + SageMaker AI (propensión de compra, segmentación) ──> resultados de vuelta al CRM
```

## 4. Tabla de decisión rápida

| Si el enunciado dice… | Respuesta probable |
|---|---|
| "SQL sobre datos en S3 **sin servidores**", "ad hoc", "pagar por consulta" | **Athena** |
| "Data warehouse", "BI complejo", "petabytes estructurados", "columnar MPP" | **Redshift** |
| "Descubrir el esquema automáticamente", "catálogo de metadatos" | **Glue crawler + Data Catalog** |
| "ETL serverless", "Spark sin administrar clúster" | **AWS Glue** |
| "Hadoop/Spark/Hive", "control del clúster", "frameworks open source", "Spot" | **Amazon EMR** |
| "Limpiar datos visualmente sin código" | **Glue DataBrew** |
| "Tiempo real", "consumidores personalizados", "milisegundos" | **Kinesis Data Streams** |
| "Cargar streams en S3/Redshift sin código", "casi en tiempo real" | **Amazon Data Firehose** |
| "Kafka" | **Amazon MSK** |
| "Migrar o replicar una base de datos", "CDC" | **AWS DMS** |
| "Datos de Salesforce/SaaS a S3" | **Amazon AppFlow** |
| "Permisos a nivel de columna en el data lake" | **Lake Formation** |
| "Dashboards", "BI", "SPICE", "embedded analytics" | **QuickSight** |
| "Buscar en logs", "texto completo" | **OpenSearch** |
| "Encontrar PII en S3" | **Macie** |
| "Entrenar y desplegar un modelo de ML" | **SageMaker AI** |
| "IA generativa / LLM por API" | **Bedrock** |
| "Orquestar un pipeline con reintentos" | **Step Functions** (o **MWAA** si dice Airflow) |
| "Reducir el costo de Athena" | **Parquet + particiones + compresión** |
| "Cargar datos masivos en Redshift" | **Comando `COPY` desde S3** |

## 5. Conceptos de análisis de datos (más allá de AWS)

| Tipo de analítica | Pregunta | Ejemplo |
|---|---|---|
| **Descriptiva** | ¿Qué pasó? | Ventas del mes pasado por región |
| **Diagnóstica** | ¿Por qué pasó? | Bajaron las ventas porque falló una campaña |
| **Predictiva** | ¿Qué pasará? | Pronóstico de demanda |
| **Prescriptiva** | ¿Qué debo hacer? | Precio óptimo, presupuesto óptimo por canal |

- **KPI:** indicador clave (por ejemplo, conversión, ticket promedio, retención, churn, CAC, LTV, ROI/ROAS).
- **Batch vs. streaming:** por lotes cada cierto tiempo vs. continuo en tiempo real.
- **Calidad de datos** (*data quality*): completitud, exactitud, consistencia, oportunidad y unicidad. En AWS existe **Glue Data Quality**.
- **Data pipeline:** secuencia automatizada de ingesta → transformación → carga → consumo.

---

**Practica:** [preguntas.md](preguntas.md) (30 preguntas en inglés).
