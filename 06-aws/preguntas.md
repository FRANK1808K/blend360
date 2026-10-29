# 06c · AWS y análisis de datos: 30 preguntas de práctica

**Español** · [English](preguntas.en.md)

> Las preguntas están **en inglés**, como en la prueba. Intenta responder en **≤ 60 segundos** cada una. **Primero intenta en inglés**; abre la traducción solo si te bloqueas y anota las palabras nuevas en tus [flashcards](../flashcards/README.md). Las respuestas y explicaciones están al final.

---

## Parte A: Fundamentos de la nube

**1.** Which of the following is a benefit of cloud computing according to AWS?

- A) Trade variable expense for fixed expense
- B) Stop guessing capacity
- C) Increase hardware maintenance
- D) Pay upfront for all resources

<details>
<summary>Traducción al español</summary>

¿Cuál de las siguientes es una ventaja de la computación en la nube según AWS?

- A) Cambiar gasto variable por gasto fijo
- B) Dejar de adivinar la capacidad
- C) Aumentar el mantenimiento del hardware
- D) Pagar por adelantado todos los recursos

</details>

**2.** Under the AWS shared responsibility model, which task is the customer's responsibility?

- A) Maintaining the physical security of data centers
- B) Patching the hypervisor
- C) Configuring security groups for EC2 instances
- D) Replacing failed hard drives

<details>
<summary>Traducción al español</summary>

Según el modelo de responsabilidad compartida de AWS, ¿qué tarea es responsabilidad del cliente?

- A) Mantener la seguridad física de los centros de datos
- B) Parchear el hipervisor
- C) Configurar los security groups de las instancias EC2
- D) Reemplazar discos duros dañados

</details>

**3.** A company needs its application to remain available if one data center fails. What should it do?

- A) Deploy the application in multiple Availability Zones
- B) Use a larger EC2 instance type
- C) Enable AWS CloudTrail
- D) Store the data in S3 Glacier Deep Archive

<details>
<summary>Traducción al español</summary>

Una empresa necesita que su aplicación siga disponible si falla un centro de datos. ¿Qué debe hacer?

- A) Desplegar la aplicación en varias zonas de disponibilidad
- B) Usar un tipo de instancia EC2 más grande
- C) Activar AWS CloudTrail
- D) Guardar los datos en S3 Glacier Deep Archive

</details>

**4.** Which AWS identity should be used to grant an AWS Glue job permission to read data from an S3 bucket?

- A) The root user
- B) An IAM user with long-term access keys
- C) An IAM role
- D) A security group

<details>
<summary>Traducción al español</summary>

¿Qué identidad de AWS se debe usar para que un job de AWS Glue pueda leer datos de un bucket de S3?

- A) El usuario root
- B) Un usuario IAM con claves de acceso de largo plazo
- C) Un rol de IAM
- D) Un security group

</details>

**5.** Which service records the API calls made in an AWS account, so you can see WHO deleted a resource?

- A) Amazon CloudWatch
- B) AWS CloudTrail
- C) AWS Config
- D) Amazon Inspector

<details>
<summary>Traducción al español</summary>

¿Qué servicio registra las llamadas a la API de una cuenta de AWS, para ver QUIÉN borró un recurso?

</details>

**6.** A data processing job runs every night, can be stopped and restarted at any time, and the company wants the LOWEST cost. Which EC2 purchasing option is best?

- A) On-Demand Instances
- B) Dedicated Hosts
- C) Spot Instances
- D) Reserved Instances for 3 years

<details>
<summary>Traducción al español</summary>

Un trabajo de procesamiento se ejecuta cada noche, puede detenerse y reiniciarse en cualquier momento, y la empresa quiere el MENOR costo. ¿Qué opción de compra de EC2 es la mejor?

- A) Instancias On-Demand
- B) Hosts dedicados
- C) Instancias Spot
- D) Instancias reservadas por 3 años

</details>

**7.** Which principle means giving users ONLY the permissions they need to do their job?

- A) Defense in depth
- B) Least privilege
- C) Elasticity
- D) High availability

<details>
<summary>Traducción al español</summary>

¿Qué principio significa dar a los usuarios SOLO los permisos que necesitan para su trabajo?

- A) Defensa en profundidad
- B) Mínimo privilegio
- C) Elasticidad
- D) Alta disponibilidad

</details>

**8.** Which S3 storage class is the MOST cost-effective for data that is kept for 7 years for compliance and is rarely, if ever, accessed?

- A) S3 Standard
- B) S3 Intelligent-Tiering
- C) S3 Standard-IA
- D) S3 Glacier Deep Archive

<details>
<summary>Traducción al español</summary>

¿Qué clase de almacenamiento de S3 es la MÁS económica para datos que se guardan 7 años por cumplimiento normativo y casi nunca se consultan?

</details>

**9.** Which service lets you run code without provisioning or managing servers, paying only for the compute time you use?

- A) Amazon EC2
- B) AWS Lambda
- C) Amazon EBS
- D) Amazon VPC

<details>
<summary>Traducción al español</summary>

¿Qué servicio permite ejecutar código sin aprovisionar ni administrar servidores, pagando solo por el tiempo de cómputo usado?

</details>

**10.** Which of the following is NOT one of the six pillars of the AWS Well-Architected Framework?

- A) Reliability
- B) Cost Optimization
- C) Scalability
- D) Sustainability

<details>
<summary>Traducción al español</summary>

¿Cuál de los siguientes NO es uno de los seis pilares del AWS Well-Architected Framework?

- A) Confiabilidad (Reliability)
- B) Optimización de costos
- C) Escalabilidad
- D) Sostenibilidad

</details>

## Parte B: Análisis de datos en AWS

**11.** A data analyst wants to run standard SQL queries directly on CSV and Parquet files stored in Amazon S3 without managing any infrastructure. Which service should they use?

- A) Amazon Redshift
- B) Amazon Athena
- C) Amazon RDS
- D) Amazon DynamoDB

<details>
<summary>Traducción al español</summary>

Un analista quiere ejecutar consultas SQL estándar directamente sobre archivos CSV y Parquet guardados en Amazon S3, sin administrar infraestructura. ¿Qué servicio debe usar?

</details>

**12.** Which AWS Glue feature automatically scans data in S3, infers the schema and creates tables in the Data Catalog?

- A) Glue DataBrew
- B) Glue crawler
- C) Glue Studio
- D) Glue Data Quality

<details>
<summary>Traducción al español</summary>

¿Qué función de AWS Glue escanea automáticamente los datos en S3, infiere el esquema y crea tablas en el Data Catalog?

</details>

**13.** A company wants to reduce the cost and improve the performance of its Amazon Athena queries. Which actions should it take? (Choose TWO.)

- A) Convert the data from CSV to Apache Parquet
- B) Partition the data by date
- C) Use `SELECT *` in all queries
- D) Split the data into millions of very small files
- E) Store the data in S3 Glacier Deep Archive

<details>
<summary>Traducción al español</summary>

Una empresa quiere reducir el costo y mejorar el rendimiento de sus consultas en Amazon Athena. ¿Qué acciones debe tomar? (Elige DOS.)

- A) Convertir los datos de CSV a Apache Parquet
- B) Particionar los datos por fecha
- C) Usar `SELECT *` en todas las consultas
- D) Dividir los datos en millones de archivos muy pequeños
- E) Guardar los datos en S3 Glacier Deep Archive

</details>

**14.** Which service is a fully managed, petabyte-scale data warehouse that uses columnar storage and massively parallel processing?

- A) Amazon Redshift
- B) Amazon Aurora
- C) Amazon DynamoDB
- D) Amazon ElastiCache

<details>
<summary>Traducción al español</summary>

¿Qué servicio es un data warehouse totalmente gestionado, a escala de petabytes, con almacenamiento columnar y procesamiento masivamente paralelo?

</details>

**15.** A company needs to capture website clickstream data in real time and process it with custom consumer applications within milliseconds. Which service is the BEST fit?

- A) Amazon Data Firehose
- B) Amazon Kinesis Data Streams
- C) AWS DataSync
- D) Amazon S3 Glacier

<details>
<summary>Traducción al español</summary>

Una empresa necesita capturar los clics de su sitio web en tiempo real y procesarlos con aplicaciones consumidoras propias en milisegundos. ¿Qué servicio es el MÁS adecuado?

</details>

**16.** A team wants to load streaming data into Amazon S3 in near real time, convert it to Parquet, and write NO code. Which service should it use?

- A) Amazon Data Firehose
- B) Amazon EMR
- C) AWS Lambda
- D) Amazon MSK

<details>
<summary>Traducción al español</summary>

Un equipo quiere cargar datos en streaming en Amazon S3 casi en tiempo real, convertirlos a Parquet y NO escribir código. ¿Qué servicio debe usar?

</details>

**17.** A company has an on-premises Oracle database and wants to continuously replicate its changes to Amazon S3 for analytics. Which service should it use?

- A) AWS DataSync
- B) AWS Database Migration Service (AWS DMS) with change data capture
- C) Amazon AppFlow
- D) AWS Snowball

<details>
<summary>Traducción al español</summary>

Una empresa tiene una base de datos Oracle en sus instalaciones y quiere replicar continuamente sus cambios a Amazon S3 para analítica. ¿Qué servicio debe usar?

- A) AWS DataSync
- B) AWS Database Migration Service (AWS DMS) con captura de cambios (CDC)
- C) Amazon AppFlow
- D) AWS Snowball

</details>

**18.** A data science team needs full control over an Apache Spark and Hive cluster, wants to use open-source frameworks, and wants to reduce costs using Spot Instances. Which service fits best?

- A) AWS Glue
- B) Amazon Athena
- C) Amazon EMR
- D) Amazon QuickSight

<details>
<summary>Traducción al español</summary>

Un equipo de ciencia de datos necesita control total de un clúster de Apache Spark y Hive, quiere usar frameworks open source y reducir costos con instancias Spot. ¿Qué servicio encaja mejor?

</details>

**19.** Business users need interactive dashboards with an in-memory engine (SPICE) that they can also embed in a web application. Which service should be used?

- A) Amazon QuickSight
- B) Amazon OpenSearch Service
- C) AWS Glue DataBrew
- D) Amazon CloudWatch

<details>
<summary>Traducción al español</summary>

Los usuarios de negocio necesitan dashboards interactivos con un motor en memoria (SPICE) que también puedan incrustar en una aplicación web. ¿Qué servicio se debe usar?

</details>

**20.** A company wants to restrict access so that analysts can see only some COLUMNS of a table in its S3 data lake. Which service provides this fine-grained access control?

- A) AWS Lake Formation
- B) Amazon Macie
- C) AWS Shield
- D) Amazon Route 53

<details>
<summary>Traducción al español</summary>

Una empresa quiere restringir el acceso para que los analistas vean solo algunas COLUMNAS de una tabla de su data lake en S3. ¿Qué servicio ofrece este control de acceso detallado?

</details>

**21.** Which is the MOST efficient way to load a large amount of data from Amazon S3 into Amazon Redshift?

- A) Many single-row `INSERT` statements
- B) The `COPY` command
- C) Exporting to Excel first
- D) Using AWS CloudTrail

<details>
<summary>Traducción al español</summary>

¿Cuál es la forma MÁS eficiente de cargar una gran cantidad de datos de Amazon S3 en Amazon Redshift?

- A) Muchas sentencias `INSERT` de una fila
- B) El comando `COPY`
- C) Exportar primero a Excel
- D) Usar AWS CloudTrail

</details>

**22.** A marketing analyst who does not know how to code needs to clean and normalize a dataset visually before analysis. Which service should they use?

- A) AWS Glue DataBrew
- B) Amazon EMR
- C) Amazon Kinesis Data Streams
- D) AWS Step Functions

<details>
<summary>Traducción al español</summary>

Un analista de marketing que no sabe programar necesita limpiar y normalizar un conjunto de datos de forma visual antes del análisis. ¿Qué servicio debe usar?

</details>

**23.** Which service can discover and classify sensitive data such as personally identifiable information (PII) stored in Amazon S3?

- A) Amazon Inspector
- B) Amazon Macie
- C) AWS Config
- D) Amazon GuardDuty

<details>
<summary>Traducción al español</summary>

¿Qué servicio puede descubrir y clasificar datos sensibles, como información de identificación personal (PII), guardados en Amazon S3?

</details>

**24.** A company needs to orchestrate a data pipeline with several steps (crawler → ETL job → quality check → notification), including retries and error handling, using a serverless visual workflow. Which service fits best?

- A) AWS Step Functions
- B) Amazon SQS
- C) Amazon CloudFront
- D) AWS Snowball

<details>
<summary>Traducción al español</summary>

Una empresa necesita orquestar un pipeline de datos con varios pasos (crawler → job ETL → control de calidad → notificación), con reintentos y manejo de errores, usando un flujo visual serverless. ¿Qué servicio encaja mejor?

</details>

**25.** In a data lake, which layer usually stores the data exactly as it arrived from the source, without transformations?

- A) Gold / analytics layer
- B) Silver / curated layer
- C) Raw / bronze layer
- D) Presentation layer

<details>
<summary>Traducción al español</summary>

En un data lake, ¿qué capa suele guardar los datos exactamente como llegaron de la fuente, sin transformaciones?

- A) Capa gold / analítica
- B) Capa silver / curada
- C) Capa raw / bronze
- D) Capa de presentación

</details>

**26.** Which file format is columnar, compressed, and generally recommended for analytics in Athena and Redshift Spectrum?

- A) CSV
- B) JSON
- C) Apache Parquet
- D) TXT

<details>
<summary>Traducción al español</summary>

¿Qué formato de archivo es columnar, comprimido y generalmente recomendado para analítica en Athena y Redshift Spectrum?

</details>

**27.** A company wants to import data from Salesforce into Amazon S3 on a schedule without writing code. Which service should it use?

- A) Amazon AppFlow
- B) AWS DMS
- C) Amazon Kinesis Data Streams
- D) AWS Direct Connect

<details>
<summary>Traducción al español</summary>

Una empresa quiere importar datos de Salesforce a Amazon S3 de forma programada y sin escribir código. ¿Qué servicio debe usar?

</details>

**28.** Which type of analytics answers the question "What is likely to happen next month?"

- A) Descriptive
- B) Diagnostic
- C) Predictive
- D) Prescriptive

<details>
<summary>Traducción al español</summary>

¿Qué tipo de analítica responde la pregunta "¿Qué es probable que pase el próximo mes?"

- A) Descriptiva
- B) Diagnóstica
- C) Predictiva
- D) Prescriptiva

</details>

**29.** A company needs to search and analyze large volumes of application logs with full-text search and dashboards. Which service is the BEST fit?

- A) Amazon OpenSearch Service
- B) Amazon RDS
- C) Amazon Redshift
- D) AWS Glue Data Catalog

<details>
<summary>Traducción al español</summary>

Una empresa necesita buscar y analizar grandes volúmenes de logs de aplicaciones con búsqueda de texto completo y dashboards. ¿Qué servicio es el MÁS adecuado?

</details>

**30.** Which AWS service allows developers to build generative AI applications using foundation models through an API?

- A) Amazon Bedrock
- B) Amazon Rekognition
- C) Amazon Redshift
- D) AWS Glue

<details>
<summary>Traducción al español</summary>

¿Qué servicio de AWS permite a los desarrolladores crear aplicaciones de IA generativa usando modelos fundacionales a través de una API?

</details>

---

<details>
<summary><b>Respuestas y explicaciones</b></summary>

| # | Resp. | Explicación |
|---|---|---|
| 1 | **B** | Es una de las 6 ventajas. A está al revés: se cambia gasto **fijo** por **variable**. |
| 2 | **C** | El cliente configura sus security groups (seguridad **en** la nube). Lo demás es de AWS. |
| 3 | **A** | Varias AZ dan alta disponibilidad: cada AZ son centros de datos independientes. |
| 4 | **C** | Los servicios usan **roles** (credenciales temporales). Nunca uses root ni claves fijas. |
| 5 | **B** | CloudTrail audita las llamadas a la API (quién, qué, cuándo). CloudWatch es para métricas y logs de rendimiento. |
| 6 | **C** | Spot es hasta ~90 % más barato y sirve para trabajos tolerantes a interrupciones. |
| 7 | **B** | *Least privilege* = mínimo privilegio. |
| 8 | **D** | Deep Archive es lo más barato para archivo a largo plazo con acceso rarísimo. |
| 9 | **B** | Lambda es serverless y se paga por ejecución. |
| 10 | **C** | Los 6 pilares son: Operational Excellence, Security, Reliability, Performance Efficiency, Cost Optimization y Sustainability. "Scalability" no es un pilar. |
| 11 | **B** | Athena = SQL serverless sobre S3. |
| 12 | **B** | El crawler infiere el esquema y crea las tablas en el catálogo. |
| 13 | **A, B** | Parquet (columnar) y las particiones reducen los datos escaneados; Athena cobra por datos escaneados. |
| 14 | **A** | Redshift = data warehouse columnar MPP. |
| 15 | **B** | Tiempo real con consumidores personalizados → Kinesis Data Streams. |
| 16 | **A** | Firehose entrega a S3 casi en tiempo real, convierte a Parquet y no requiere código. |
| 17 | **B** | DMS con **CDC** replica los cambios continuamente. |
| 18 | **C** | EMR = clúster gestionado de Spark/Hive con control total y soporte para Spot. |
| 19 | **A** | QuickSight (SPICE, embedded analytics). |
| 20 | **A** | Lake Formation da permisos finos (tabla/columna/fila) en el data lake. |
| 21 | **B** | `COPY` carga en paralelo desde S3. |
| 22 | **A** | DataBrew = preparación visual sin código. |
| 23 | **B** | Macie detecta PII en S3. |
| 24 | **A** | Step Functions orquesta pasos con reintentos, de forma visual y serverless. |
| 25 | **C** | Raw/bronze guarda los datos tal como llegan. |
| 26 | **C** | Parquet es columnar y comprimido. |
| 27 | **A** | AppFlow integra aplicaciones SaaS (Salesforce, etc.) sin código. |
| 28 | **C** | Predictiva = ¿qué pasará? |
| 29 | **A** | OpenSearch = búsqueda de texto completo y análisis de logs. |
| 30 | **A** | Bedrock = IA generativa por API. |

**Puntaje:** 27–30 excelente · 22–26 bien (repasa los fallos) · < 22 vuelve a leer [analisis-de-datos.md](analisis-de-datos.md).

</details>
