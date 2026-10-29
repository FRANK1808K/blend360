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

**Cómo bajar costos y acelerar Athena (pregunta clásica):**

1. Convertir los datos a formato **columnar** (**Parquet** u ORC).
2. **Comprimir** (Snappy, GZIP).
3. **Particionar** por las columnas que más se filtran (por ejemplo, fecha) y filtrar por partición en el `WHERE`.
4. Seleccionar solo las columnas necesarias (evita `SELECT *`).
5. Evitar muchos archivos pequeños (mejor archivos de 128 MB a 1 GB).

**Conceptos de Redshift que conviene reconocer:**

- Arquitectura: **leader node** (planifica las consultas) + **compute nodes** (ejecutan en paralelo).
- **Distribution style** (cómo se reparten las filas entre nodos): `AUTO`, `EVEN`, `KEY` (las filas con la misma clave van al mismo nodo, lo que acelera JOINs), `ALL` (copia completa en cada nodo; para dimensiones pequeñas).
- **Sort key:** orden físico que acelera los filtros por rango (por ejemplo, por fecha).
- **`COPY`:** la forma eficiente de cargar datos masivos desde S3 (en paralelo). Evita los `INSERT` fila por fila.
- **Zero-ETL integrations:** replican datos de Aurora/RDS/DynamoDB a Redshift sin construir pipelines.

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
