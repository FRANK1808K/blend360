# Cheat sheet: AWS + databases (1 page)

[Español](aws-y-bases-de-datos.md) · **English**

**Cloud:** pay-as-you-go, on demand. **6 advantages:** variable instead of fixed expense · economies of scale · stop guessing capacity · speed and agility · stop maintaining data centers · go global in minutes.
**IaaS** (EC2) · **PaaS** (Elastic Beanstalk) · **SaaS** (QuickSight, Gmail). **Region** > **AZ** (1+ data centers) · **edge location** (CloudFront).
**Shared responsibility:** AWS = security **OF** the cloud (hardware, facilities). Customer = security **IN** the cloud (data, IAM, EC2 OS, security groups).
**IAM:** user · group · **role** (temporary credentials, for services) · JSON policy (`Deny` wins) · **least privilege** · MFA on root.
**Pricing:** On-Demand · Savings Plans/Reserved (≈ −72 %, 1–3-year commitment) · **Spot** (≈ −90 %, interruptible).
**Monitoring:** CloudWatch = metrics/logs · **CloudTrail = who did what** (API) · Config = configuration.
**Well-Architected (6):** Operational Excellence, Security, Reliability, Performance Efficiency, Cost Optimization, Sustainability.

| Data need | Service |
|---|---|
| Data lake / objects | **S3** (11 nines; classes Standard → IA → Glacier → Deep Archive) |
| Automatic schema + catalog | **Glue crawler + Data Catalog** |
| Serverless ETL (Spark) | **Glue** · no code: **DataBrew** |
| Spark/Hadoop with control, Spot | **EMR** (Blend is a delivery partner) |
| Serverless SQL on S3 | **Athena** (pay per TB scanned → Parquet + partitions) |
| Data warehouse | **Redshift** (columnar, MPP, `COPY` from S3, Spectrum) |
| Real-time streaming | **Kinesis Data Streams** · delivery to S3/Redshift without code: **Data Firehose** · Kafka: **MSK** |
| Replicate a DB (CDC) | **DMS** · SaaS → S3: **AppFlow** |
| Column/row permissions in the lake | **Lake Formation** · PII in S3: **Macie** · encryption: **KMS** |
| BI dashboards | **QuickSight** (in-memory SPICE) |
| Logs / text search | **OpenSearch** |
| Orchestrate | **Step Functions** · Airflow: **MWAA** |
| ML / generative AI | **SageMaker AI** / **Bedrock** |
| Relational OLTP / NoSQL | **RDS, Aurora** / **DynamoDB** |

**Databases:** PK (unique, not null) · FK (referential integrity) · 1:N (FK on the N side) · N:M (bridge table).
**1NF** atomic values · **2NF** no partial dependencies on a composite PK · **3NF** no transitive dependencies.
**ACID:** Atomicity (all or nothing) · Consistency · Isolation · Durability.
**Index:** speeds up reads (B-tree) and slows down writes. **OLTP** (rows, normalized, transactions) vs. **OLAP** (columnar, star schema, aggregations).
**Star:** **fact** table (metrics + FKs) + **dimensions** (attributes). **Warehouse** (schema-on-write) vs. **Lake** (schema-on-read). **ETL** vs. **ELT**.
**NoSQL:** key-value (DynamoDB) · document (DocumentDB) · wide-column (Keyspaces) · graph (Neptune). **CAP:** during a partition, choose C or A.
