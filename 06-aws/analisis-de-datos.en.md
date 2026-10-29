# 06b · Data analytics on AWS

[Español](analisis-de-datos.md) · **English**

> This is the core of Blend360's work with AWS: **building data and analytics platforms for clients**. Blend holds the **AWS Data & Analytics** competency and is a *delivery partner* for **Amazon EMR** and **Amazon QuickSight**, so those services deserve special attention.

---

## 1. The data lifecycle (and which service fits each stage)

```text
 SOURCES           INGESTION            STORAGE                PROCESSING             ANALYSIS / QUERY        VISUALIZATION / ML
 ───────           ─────────            ───────                ──────────             ────────────────        ──────────────────
 Databases     →   AWS DMS          →                          AWS Glue (ETL)     →   Amazon Athena       →   Amazon QuickSight
 Apps / logs   →   Amazon Data         Amazon S3              Amazon EMR (Spark)     Amazon Redshift         Amazon SageMaker AI
 IoT / clicks  →   Firehose,       →   (data lake)        →   AWS Lambda             Amazon OpenSearch       Amazon Bedrock
 SaaS          →   Kinesis Data        + Glue Data Catalog    Managed Service for
 Files         →   Streams, MSK,       + Lake Formation       Apache Flink
                   AppFlow, DataSync   (governance)

                         Orchestration: AWS Step Functions · Amazon MWAA (Airflow) · Glue Workflows · EventBridge
                         Monitoring: CloudWatch · Audit: CloudTrail · Security: IAM, KMS, Lake Formation
```

## 2. The services, one by one

### Storage: Amazon S3 as a data lake

- Cheap, durable (11 nines), practically unlimited **object** storage. It is the **foundation** of almost every data architecture on AWS.
- Typical organization in **layers** (*medallion* architecture):

| Layer | Also called | Content |
|---|---|---|
| **Raw** | Bronze / landing | Data exactly as it arrives (CSV, JSON), untouched |
| **Clean / curated** | Silver | Cleaned, typed, deduplicated, in **Parquet** |
| **Analytics** | Gold / consumption | Aggregated and modeled for the business (tables ready for BI) |

- **Partition** by date or another frequently filtered column: `s3://lake/silver/sales/year=2024/month=06/day=15/part-000.parquet`.

### Catalog: AWS Glue Data Catalog

- A central **metastore**: it stores the **schema** (tables, columns, types, partitions) of the data in S3. The data stays in S3; the catalog only describes it.
- Used by **Athena, Redshift Spectrum, EMR and Glue ETL**.
- **Glue crawler:** scans S3, **infers the schema** automatically and creates or updates the tables in the catalog.

### Processing / ETL

| Service | What it is | When to choose it |
|---|---|---|
| **AWS Glue (ETL jobs)** | **Serverless** ETL based on **Apache Spark** (PySpark/Scala) or Python Shell | ETL without managing clusters; you pay per DPU-hour |
| **AWS Glue DataBrew** | **No-code** visual data preparation (more than 250 transformations) | Analysts who clean and profile data without programming |
| **Amazon EMR** | Managed clusters for **Spark, Hadoop, Hive, Presto/Trino, HBase**. Available as EMR on EC2, **EMR Serverless** and EMR on EKS | Large-scale big data, fine-grained cluster control, open-source frameworks. Cut costs with **Spot** instances |
| **AWS Lambda** | Short event-driven functions | Small transformations (e.g., when a file lands in S3) |
| **Amazon Managed Service for Apache Flink** (formerly Kinesis Data Analytics) | Real-time **stream** processing with SQL/Java/Python | Real-time aggregations, anomaly detection |

> **Glue vs. EMR:** Glue is **serverless** and simpler: nothing to manage. EMR gives **more control and flexibility** (versions, frameworks, instance types) and is usually cheaper for large, continuous workloads.

### Ingestion

| Service | Type | Detail |
|---|---|---|
| **Amazon Kinesis Data Streams** | **Real-time** streaming | You write the consumers (Lambda, Flink, apps). Capacity in *shards*. Configurable retention (24 h by default, extendable) |
| **Amazon Data Firehose** (formerly Kinesis Data Firehose) | **Near real-time** delivery (with a *buffer*) | Fully managed: loads streams into **S3, Redshift, OpenSearch** or Splunk. Can convert to Parquet. No code |
| **Amazon MSK** | Managed Apache **Kafka** | When the client already uses Kafka |
| **AWS DMS** (Database Migration Service) | **Database** migration/replication | Full load + **CDC** (*change data capture*: replicates ongoing changes) into S3, Redshift, etc. |
| **Amazon AppFlow** | **SaaS** integration | Salesforce, Google Analytics, Zendesk → S3/Redshift without code |
| **AWS DataSync** | **File** transfer | On-premises file servers → S3/EFS |
| **AWS Snow Family** | Physical devices | Petabytes without a good connection |

> **Kinesis Data Streams vs. Firehose:** *Streams* = real time, custom consumers, you manage the capacity. *Firehose* = a fully managed "hose" that **delivers** data to a destination in near real time (seconds to minutes of buffering), without code.

### Query and data warehouse

| Service | What it is | How you pay | When |
|---|---|---|---|
| **Amazon Athena** | **Serverless SQL** directly on files in **S3** (Trino/Presto engine) using the Glue Data Catalog | Per **data scanned** (TB) | Ad hoc queries on the data lake, without infrastructure |
| **Amazon Redshift** | Columnar **data warehouse** with massively parallel processing (**MPP**) | Per node/hour (provisioned) or per use (**Redshift Serverless**) | BI with many repeated, complex queries on structured data, at large scale |
| **Redshift Spectrum** | Query data in S3 from Redshift without loading it | Per data scanned | Join the warehouse with the lake |
| **Amazon OpenSearch Service** | Search and **log** analytics (Elasticsearch/OpenSearch + dashboards) | Per instance / serverless | Text search, observability, log analysis |

**How to cut costs and speed up Athena (classic question):**

1. Convert the data to a **columnar** format (**Parquet** or ORC).
2. **Compress** it (Snappy, GZIP).
3. **Partition** by the most filtered columns (e.g., date) and filter by partition in the `WHERE`.
4. Select only the columns you need (avoid `SELECT *`).
5. Avoid many small files (128 MB to 1 GB files are better).

**Redshift concepts worth recognizing:**

- Architecture: **leader node** (plans the queries) + **compute nodes** (execute in parallel).
- **Distribution style** (how rows are spread across nodes): `AUTO`, `EVEN`, `KEY` (rows with the same key go to the same node, which speeds up JOINs), `ALL` (a full copy on each node; for small dimensions).
- **Sort key:** a physical order that speeds up range filters (e.g., by date).
- **`COPY`:** the efficient way to load bulk data from S3 (in parallel). Avoid row-by-row `INSERT`s.
- **Zero-ETL integrations:** replicate data from Aurora/RDS/DynamoDB into Redshift without building pipelines.

### Data governance and security

| Service | What for |
|---|---|
| **AWS Lake Formation** | Build and **govern** the data lake: fine-grained permissions by database, table, **column** and row on the data in S3/Glue Catalog |
| **IAM** | Who can use which service or resource |
| **AWS KMS** | Encryption of data at rest (S3, Redshift, Glue) |
| **Amazon Macie** | Discover **sensitive data (PII)** in S3 |
| **Amazon DataZone / SageMaker Unified Studio** | Business catalog, data discovery and governance across teams |

### Visualization: Amazon QuickSight

- A **serverless BI** service in the cloud: interactive dashboards, reports and *embedded analytics* (embedding dashboards in applications).
- **SPICE:** an **in-memory** engine that speeds up dashboards (you import the data into SPICE instead of querying the source on every click).
- Sources: Athena, Redshift, RDS/Aurora, S3, Snowflake, Salesforce, files…
- **ML Insights** (anomaly detection, forecasting) and **natural-language** questions with generative AI (Amazon Q in QuickSight).
- Priced per user (authors and readers).
- In 2025, AWS brought QuickSight into **Amazon Quick Suite** (as "Quick Sight"). If you see either name, it is AWS's BI service.

### Machine learning and AI (just enough)

- **Amazon SageMaker AI:** prepare data, train, tune and **deploy** ML models.
- **Amazon Bedrock:** generative AI through an API (foundation models), RAG with *Knowledge Bases*, agents. Blend holds the **AWS Generative AI** competency.
- Pre-trained AI services: **Comprehend** (NLP: sentiment, entities), **Rekognition** (images/video), **Textract** (extract text and tables from documents), **Forecast**, **Personalize** (recommendations), **Transcribe** (speech → text), **Translate**, **Polly** (text → speech).

### Orchestration

| Service | When |
|---|---|
| **AWS Step Functions** | Workflows with steps, retries and branches across AWS services (serverless, visual) |
| **Amazon MWAA** (Managed Workflows for Apache Airflow) | The client already uses **Airflow** or needs complex DAGs in Python |
| **AWS Glue Workflows / Triggers** | Chain Glue crawlers and jobs |
| **Amazon EventBridge** | Trigger processes on events or on a schedule (*cron*) |

## 3. Reference architectures (draw them from memory)

### A) Batch data lake (the most common)

```text
RDS / ERP ──(AWS DMS)──┐
Salesforce ─(AppFlow)──┼──> S3 raw ──(Glue crawler)──> Glue Data Catalog
CSV files ─────────────┘        │
                                └──(Glue ETL / EMR Spark: clean, Parquet, partition)──> S3 curated
                                                                                          │
                                     ┌────────────────────────────────────────────────────┤
                                     ▼                                                    ▼
                               Amazon Athena (ad hoc)                       Amazon Redshift (COPY / Spectrum)
                                     └──────────────────> Amazon QuickSight <─────────────┘
Orchestrated with Step Functions or MWAA · Governed with Lake Formation · Encrypted with KMS
```

### B) Real-time streaming (e.g., e-commerce clicks)

```text
Web/App ──> Kinesis Data Streams ──> Managed Service for Apache Flink (per-minute metrics) ──> Redshift / OpenSearch ──> Dashboard
                    │
                    └──> Amazon Data Firehose ──(Parquet)──> S3 (history for Athena/ML)
```

### C) Marketing analytics (typical for Blend360)

```text
Google Analytics / CRM / social media ──(AppFlow)──> S3 ──(Glue)──> Redshift (star schema: fact_campaign_performance)
   ──> QuickSight (ROI per campaign) + SageMaker AI (purchase propensity, segmentation) ──> results back to the CRM
```

## 4. Quick decision table

| If the question says… | Likely answer |
|---|---|
| "SQL on data in S3 **without servers**", "ad hoc", "pay per query" | **Athena** |
| "Data warehouse", "complex BI", "structured petabytes", "columnar MPP" | **Redshift** |
| "Discover the schema automatically", "metadata catalog" | **Glue crawler + Data Catalog** |
| "Serverless ETL", "Spark without managing a cluster" | **AWS Glue** |
| "Hadoop/Spark/Hive", "cluster control", "open-source frameworks", "Spot" | **Amazon EMR** |
| "Clean data visually without code" | **Glue DataBrew** |
| "Real time", "custom consumers", "milliseconds" | **Kinesis Data Streams** |
| "Load streams into S3/Redshift without code", "near real time" | **Amazon Data Firehose** |
| "Kafka" | **Amazon MSK** |
| "Migrate or replicate a database", "CDC" | **AWS DMS** |
| "Data from Salesforce/SaaS into S3" | **Amazon AppFlow** |
| "Column-level permissions in the data lake" | **Lake Formation** |
| "Dashboards", "BI", "SPICE", "embedded analytics" | **QuickSight** |
| "Search logs", "full text" | **OpenSearch** |
| "Find PII in S3" | **Macie** |
| "Train and deploy an ML model" | **SageMaker AI** |
| "Generative AI / LLM through an API" | **Bedrock** |
| "Orchestrate a pipeline with retries" | **Step Functions** (or **MWAA** if it says Airflow) |
| "Reduce the cost of Athena" | **Parquet + partitions + compression** |
| "Load bulk data into Redshift" | **The `COPY` command from S3** |

## 5. Data analytics concepts (beyond AWS)

| Type of analytics | Question | Example |
|---|---|---|
| **Descriptive** | What happened? | Last month's sales by region |
| **Diagnostic** | Why did it happen? | Sales dropped because a campaign failed |
| **Predictive** | What will happen? | Demand forecast |
| **Prescriptive** | What should I do? | Optimal price, optimal budget per channel |

- **KPI:** a key performance indicator (e.g., conversion, average order value, retention, churn, CAC, LTV, ROI/ROAS).
- **Batch vs. streaming:** in batches every so often vs. continuously in real time.
- **Data quality:** completeness, accuracy, consistency, timeliness and uniqueness. On AWS there is **Glue Data Quality**.
- **Data pipeline:** an automated sequence of ingestion → transformation → loading → consumption.

---

**Practice:** [preguntas.en.md](preguntas.en.md) (30 questions).
