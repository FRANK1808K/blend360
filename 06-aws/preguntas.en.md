# 06c · AWS & data analytics: 30 practice questions

🌐 [Español](preguntas.md) · **English**

> Try to answer each question in **≤ 60 seconds**. If a word blocks you, look it up in the [technical vocabulary](../english/vocabulario-tecnico.en.md#aws-and-cloud). The answers and explanations are at the end.

---

## Part A: Cloud fundamentals

**1.** Which of the following is a benefit of cloud computing according to AWS?

- A) Trade variable expense for fixed expense
- B) Stop guessing capacity
- C) Increase hardware maintenance
- D) Pay upfront for all resources

**2.** Under the AWS shared responsibility model, which task is the customer's responsibility?

- A) Maintaining the physical security of data centers
- B) Patching the hypervisor
- C) Configuring security groups for EC2 instances
- D) Replacing failed hard drives

**3.** A company needs its application to remain available if one data center fails. What should it do?

- A) Deploy the application in multiple Availability Zones
- B) Use a larger EC2 instance type
- C) Enable AWS CloudTrail
- D) Store the data in S3 Glacier Deep Archive

**4.** Which AWS identity should be used to grant an AWS Glue job permission to read data from an S3 bucket?

- A) The root user
- B) An IAM user with long-term access keys
- C) An IAM role
- D) A security group

**5.** Which service records the API calls made in an AWS account, so you can see WHO deleted a resource?

- A) Amazon CloudWatch
- B) AWS CloudTrail
- C) AWS Config
- D) Amazon Inspector

**6.** A data processing job runs every night, can be stopped and restarted at any time, and the company wants the LOWEST cost. Which EC2 purchasing option is best?

- A) On-Demand Instances
- B) Dedicated Hosts
- C) Spot Instances
- D) Reserved Instances for 3 years

**7.** Which principle means giving users ONLY the permissions they need to do their job?

- A) Defense in depth
- B) Least privilege
- C) Elasticity
- D) High availability

**8.** Which S3 storage class is the MOST cost-effective for data that is kept for 7 years for compliance and is rarely, if ever, accessed?

- A) S3 Standard
- B) S3 Intelligent-Tiering
- C) S3 Standard-IA
- D) S3 Glacier Deep Archive

**9.** Which service lets you run code without provisioning or managing servers, paying only for the compute time you use?

- A) Amazon EC2
- B) AWS Lambda
- C) Amazon EBS
- D) Amazon VPC

**10.** Which of the following is NOT one of the six pillars of the AWS Well-Architected Framework?

- A) Reliability
- B) Cost Optimization
- C) Scalability
- D) Sustainability

## Part B: Data analytics on AWS

**11.** A data analyst wants to run standard SQL queries directly on CSV and Parquet files stored in Amazon S3 without managing any infrastructure. Which service should they use?

- A) Amazon Redshift
- B) Amazon Athena
- C) Amazon RDS
- D) Amazon DynamoDB

**12.** Which AWS Glue feature automatically scans data in S3, infers the schema and creates tables in the Data Catalog?

- A) Glue DataBrew
- B) Glue crawler
- C) Glue Studio
- D) Glue Data Quality

**13.** A company wants to reduce the cost and improve the performance of its Amazon Athena queries. Which actions should it take? (Choose TWO.)

- A) Convert the data from CSV to Apache Parquet
- B) Partition the data by date
- C) Use `SELECT *` in all queries
- D) Split the data into millions of very small files
- E) Store the data in S3 Glacier Deep Archive

**14.** Which service is a fully managed, petabyte-scale data warehouse that uses columnar storage and massively parallel processing?

- A) Amazon Redshift
- B) Amazon Aurora
- C) Amazon DynamoDB
- D) Amazon ElastiCache

**15.** A company needs to capture website clickstream data in real time and process it with custom consumer applications within milliseconds. Which service is the BEST fit?

- A) Amazon Data Firehose
- B) Amazon Kinesis Data Streams
- C) AWS DataSync
- D) Amazon S3 Glacier

**16.** A team wants to load streaming data into Amazon S3 in near real time, convert it to Parquet, and write NO code. Which service should it use?

- A) Amazon Data Firehose
- B) Amazon EMR
- C) AWS Lambda
- D) Amazon MSK

**17.** A company has an on-premises Oracle database and wants to continuously replicate its changes to Amazon S3 for analytics. Which service should it use?

- A) AWS DataSync
- B) AWS Database Migration Service (AWS DMS) with change data capture
- C) Amazon AppFlow
- D) AWS Snowball

**18.** A data science team needs full control over an Apache Spark and Hive cluster, wants to use open-source frameworks, and wants to reduce costs using Spot Instances. Which service fits best?

- A) AWS Glue
- B) Amazon Athena
- C) Amazon EMR
- D) Amazon QuickSight

**19.** Business users need interactive dashboards with an in-memory engine (SPICE) that they can also embed in a web application. Which service should be used?

- A) Amazon QuickSight
- B) Amazon OpenSearch Service
- C) AWS Glue DataBrew
- D) Amazon CloudWatch

**20.** A company wants to restrict access so that analysts can see only some COLUMNS of a table in its S3 data lake. Which service provides this fine-grained access control?

- A) AWS Lake Formation
- B) Amazon Macie
- C) AWS Shield
- D) Amazon Route 53

**21.** Which is the MOST efficient way to load a large amount of data from Amazon S3 into Amazon Redshift?

- A) Many single-row `INSERT` statements
- B) The `COPY` command
- C) Exporting to Excel first
- D) Using AWS CloudTrail

**22.** A marketing analyst who does not know how to code needs to clean and normalize a dataset visually before analysis. Which service should they use?

- A) AWS Glue DataBrew
- B) Amazon EMR
- C) Amazon Kinesis Data Streams
- D) AWS Step Functions

**23.** Which service can discover and classify sensitive data such as personally identifiable information (PII) stored in Amazon S3?

- A) Amazon Inspector
- B) Amazon Macie
- C) AWS Config
- D) Amazon GuardDuty

**24.** A company needs to orchestrate a data pipeline with several steps (crawler → ETL job → quality check → notification), including retries and error handling, using a serverless visual workflow. Which service fits best?

- A) AWS Step Functions
- B) Amazon SQS
- C) Amazon CloudFront
- D) AWS Snowball

**25.** In a data lake, which layer usually stores the data exactly as it arrived from the source, without transformations?

- A) Gold / analytics layer
- B) Silver / curated layer
- C) Raw / bronze layer
- D) Presentation layer

**26.** Which file format is columnar, compressed, and generally recommended for analytics in Athena and Redshift Spectrum?

- A) CSV
- B) JSON
- C) Apache Parquet
- D) TXT

**27.** A company wants to import data from Salesforce into Amazon S3 on a schedule without writing code. Which service should it use?

- A) Amazon AppFlow
- B) AWS DMS
- C) Amazon Kinesis Data Streams
- D) AWS Direct Connect

**28.** Which type of analytics answers the question "What is likely to happen next month?"

- A) Descriptive
- B) Diagnostic
- C) Predictive
- D) Prescriptive

**29.** A company needs to search and analyze large volumes of application logs with full-text search and dashboards. Which service is the BEST fit?

- A) Amazon OpenSearch Service
- B) Amazon RDS
- C) Amazon Redshift
- D) AWS Glue Data Catalog

**30.** Which AWS service allows developers to build generative AI applications using foundation models through an API?

- A) Amazon Bedrock
- B) Amazon Rekognition
- C) Amazon Redshift
- D) AWS Glue

---

<details>
<summary><b>Answer key and explanations</b></summary>

| # | Ans. | Explanation |
|---|---|---|
| 1 | **B** | It is one of the 6 advantages. A is backwards: you trade **fixed** expense for **variable** expense. |
| 2 | **C** | The customer configures its security groups (security **in** the cloud). Everything else belongs to AWS. |
| 3 | **A** | Multiple AZs provide high availability: each AZ is made of independent data centers. |
| 4 | **C** | Services use **roles** (temporary credentials). Never use the root user or long-term keys. |
| 5 | **B** | CloudTrail audits API calls (who, what, when). CloudWatch is for performance metrics and logs. |
| 6 | **C** | Spot is up to ~90% cheaper and fits interruption-tolerant jobs. |
| 7 | **B** | That is *least privilege*. |
| 8 | **D** | Deep Archive is the cheapest option for long-term archives that are almost never accessed. |
| 9 | **B** | Lambda is serverless and you pay per execution. |
| 10 | **C** | The 6 pillars are: Operational Excellence, Security, Reliability, Performance Efficiency, Cost Optimization and Sustainability. "Scalability" is not a pillar. |
| 11 | **B** | Athena = serverless SQL on S3. |
| 12 | **B** | The crawler infers the schema and creates the tables in the catalog. |
| 13 | **A, B** | Parquet (columnar) and partitions reduce the data scanned; Athena charges per data scanned. |
| 14 | **A** | Redshift = columnar MPP data warehouse. |
| 15 | **B** | Real time with custom consumers → Kinesis Data Streams. |
| 16 | **A** | Firehose delivers to S3 in near real time, converts to Parquet and requires no code. |
| 17 | **B** | DMS with **CDC** replicates the changes continuously. |
| 18 | **C** | EMR = managed Spark/Hive cluster with full control and Spot support. |
| 19 | **A** | QuickSight (SPICE, embedded analytics). |
| 20 | **A** | Lake Formation provides fine-grained permissions (table/column/row) on the data lake. |
| 21 | **B** | `COPY` loads in parallel from S3. |
| 22 | **A** | DataBrew = visual, no-code data preparation. |
| 23 | **B** | Macie detects PII in S3. |
| 24 | **A** | Step Functions orchestrates steps with retries, visually and serverless. |
| 25 | **C** | Raw/bronze stores the data exactly as it arrives. |
| 26 | **C** | Parquet is columnar and compressed. |
| 27 | **A** | AppFlow integrates SaaS applications (Salesforce, etc.) without code. |
| 28 | **C** | Predictive = what will happen? |
| 29 | **A** | OpenSearch = full-text search and log analytics. |
| 30 | **A** | Bedrock = generative AI through an API. |

**Score:** 27–30 excellent · 22–26 good (review your mistakes) · < 22 re-read [analisis-de-datos.en.md](analisis-de-datos.en.md).

</details>
