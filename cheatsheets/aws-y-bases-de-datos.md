# Cheatsheet: AWS + bases de datos (1 página)

**Español** · [English](aws-y-bases-de-datos.en.md)

**Nube:** pago por uso, bajo demanda. **6 ventajas:** gasto variable en vez de fijo · economías de escala · dejar de adivinar la capacidad · velocidad y agilidad · no mantener centros de datos · global en minutos.
**IaaS** (EC2) · **PaaS** (Elastic Beanstalk) · **SaaS** (QuickSight, Gmail). **Región** > **AZ** (1+ centros de datos) · **edge location** (CloudFront).
**Responsabilidad compartida:** AWS = seguridad **DE** la nube (hardware, instalaciones). Cliente = seguridad **EN** la nube (datos, IAM, SO de EC2, security groups).
**IAM:** user · group · **role** (credenciales temporales, para servicios) · policy JSON (el `Deny` gana) · **mínimo privilegio** · MFA en root.
**Precios:** On-Demand · Savings Plans/Reserved (≈ −72 %, compromiso de 1–3 años) · **Spot** (≈ −90 %, interrumpible).
**Monitoreo:** CloudWatch = métricas/logs · **CloudTrail = quién hizo qué** (API) · Config = configuración.
**Well-Architected (6):** Operational Excellence, Security, Reliability, Performance Efficiency, Cost Optimization, Sustainability.

| Necesidad de datos | Servicio |
|---|---|
| Data lake / objetos | **S3** (11 nueves; clases Standard → IA → Glacier → Deep Archive) |
| Esquema automático + catálogo | **Glue crawler + Data Catalog** |
| ETL serverless (Spark) | **Glue** · sin código: **DataBrew** |
| Spark/Hadoop con control, Spot | **EMR** (Blend es delivery partner) |
| SQL serverless sobre S3 | **Athena** (pago por TB escaneado → Parquet + particiones) |
| Data warehouse | **Redshift** (columnar, MPP, `COPY` desde S3, Spectrum) |
| Streaming en tiempo real | **Kinesis Data Streams** · entrega a S3/Redshift sin código: **Data Firehose** · Kafka: **MSK** |
| Replicar una BD (CDC) | **DMS** · SaaS → S3: **AppFlow** |
| Permisos por columna/fila en el lake | **Lake Formation** · PII en S3: **Macie** · cifrado: **KMS** |
| Dashboards BI | **QuickSight** (SPICE en memoria) |
| Logs / búsqueda de texto | **OpenSearch** |
| Orquestar | **Step Functions** · Airflow: **MWAA** |
| ML / IA generativa | **SageMaker AI** / **Bedrock** |
| OLTP relacional / NoSQL | **RDS, Aurora** / **DynamoDB** |

**Bases de datos:** PK (única, no nula) · FK (integridad referencial) · 1:N (FK en el lado N) · N:M (tabla puente).
**1NF** valores atómicos · **2NF** sin dependencias parciales de la PK compuesta · **3NF** sin dependencias transitivas.
**ACID:** Atomicidad (todo o nada) · Consistencia · Aislamiento · Durabilidad.
**Índice:** acelera lecturas (B-tree) y hace más lentas las escrituras. **OLTP** (filas, normalizado, transacciones) vs. **OLAP** (columnar, estrella, agregaciones).
**Estrella:** tabla de **hechos** (métricas + FKs) + **dimensiones** (atributos). **Warehouse** (schema-on-write) vs. **Lake** (schema-on-read). **ETL** vs. **ELT**.
**NoSQL:** key-value (DynamoDB) · documentos (DocumentDB) · columnas anchas (Keyspaces) · grafos (Neptune). **CAP:** ante una partición, elegir C o A.
