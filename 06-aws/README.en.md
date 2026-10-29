# 06 · What is AWS? Cloud fundamentals

[Español](README.md) · **English**

> **Why it matters so much for Blend360:** Blend360 is an **AWS Premier Tier Services Partner** (the highest tier for services partners). It holds AWS competencies in **Data & Analytics**, **Generative AI**, Financial Services, DevOps and Migration, and it is a *delivery partner* for **Amazon EMR** and **Amazon QuickSight**. In other words, much of its client work is built on AWS. See [what Blend360 evaluates](../guides/que-evalua-blend360.en.md).
>
> **Your advantage:** since you take the **AWS Certified AI Practitioner on November 16**, you will be studying much of this anyway. The complete study material is integrated in the [AWS AI Practitioner (AIF-C01) module](../aws-ai-practitioner/README.en.md).

| File | Content |
|---|---|
| This README | What the cloud and AWS are, global infrastructure, shared responsibility, IAM, core services, pricing |
| [analisis-de-datos.en.md](analisis-de-datos.en.md) | ★ Data analytics on AWS: S3, Glue, Athena, Redshift, EMR, Kinesis, QuickSight, architectures |
| [preguntas.en.md](preguntas.en.md) | 30 practice questions with explanations |

---

## 1. What is cloud computing?

> **Cloud computing** is the **on-demand delivery** of IT resources over the Internet with **pay-as-you-go pricing**.

Instead of buying and maintaining your own servers (*on-premises*), you **rent** compute, storage and databases from a provider (AWS, Azure, Google Cloud) and pay only for what you use.

**AWS (Amazon Web Services)** is Amazon's cloud platform, launched in 2006. It offers more than 200 services and is the provider with the largest market share.

### The 6 advantages of the cloud (according to AWS, asked word for word!)

| # | In English | Meaning |
|---|---|---|
| 1 | **Trade fixed expense for variable expense** | You swap fixed investment (CapEx) for variable spending (OpEx): you pay for what you use |
| 2 | **Benefit from massive economies of scale** | AWS buys at huge scale, so the price per unit is lower |
| 3 | **Stop guessing capacity** | You scale up or down according to real demand |
| 4 | **Increase speed and agility** | New resources in minutes, not weeks |
| 5 | **Stop spending money running and maintaining data centers** | You focus on your business, not on infrastructure |
| 6 | **Go global in minutes** | You deploy to several regions of the world easily |

### Service models

| Model | You manage | The provider manages | AWS example | Analogy (pizza) |
|---|---|---|---|---|
| **IaaS** (Infrastructure as a Service) | OS, apps, data | Hardware, network, virtualization | **Amazon EC2** | You buy the ingredients and bake it at home |
| **PaaS** (Platform as a Service) | Apps and data | + OS, runtime | **AWS Elastic Beanstalk**, RDS | You order delivery |
| **SaaS** (Software as a Service) | You just use it | Everything | Gmail, Salesforce, Amazon QuickSight | You eat at the restaurant |

### Deployment models

- **Cloud (public):** everything in the cloud.
- **On-premises (private cloud):** in your own data center.
- **Hybrid:** a connected combination of both.

### Key characteristics

| Term | Meaning |
|---|---|
| **Elasticity** | Increasing or reducing resources **automatically** according to demand |
| **Scalability** | The ability to grow. **Vertical** = a bigger machine (*scale up*). **Horizontal** = more machines (*scale out*) |
| **High availability** | The system keeps working even if one component fails (several AZs) |
| **Fault tolerance** | Tolerates failures without interruption |
| **Serverless** | You do not manage servers; you pay per execution (Lambda, Athena, Glue) |
| **Managed service** | AWS takes care of patches, backups and scaling (RDS, Redshift) |

## 2. Global infrastructure

```text
Region (e.g., us-east-1, sa-east-1 São Paulo)
├── Availability Zone A  (1 or more data centers)
├── Availability Zone B
└── Availability Zone C
+ Edge locations / Points of presence (for CloudFront: cache close to users)
```

| Component | What it is | What for |
|---|---|---|
| **Region** | A geographic area with several isolated AZs. There are more than 30 regions | Choose by: **legal compliance** for data, **latency** (closeness to users), **available services** and **price** |
| **Availability Zone (AZ)** | One or more data centers with independent power and networking. Each region usually has 3 or more | High availability: deploy in **several AZs** |
| **Edge location** | A point of presence for caching and CDN | **CloudFront**, Route 53: low global latency |
| **Local Zones / Outposts** | AWS closer to cities / in your own data center | Ultra-low latency / hybrid |

## 3. Shared responsibility model

| AWS is responsible for security **OF** the cloud | The customer is responsible for security **IN** the cloud |
|---|---|
| Hardware, physical data centers, global network | Customer **data** and its encryption |
| Virtualization software (hypervisor) | **IAM**: users, permissions, MFA |
| Infrastructure of the managed services | Configuration of **security groups** and firewalls |
| OS patches on managed services (RDS, Lambda) | OS patches **on EC2** and application patches |

> Rule: the more **managed** the service (Lambda, S3), the more responsibility AWS takes. With **EC2** (IaaS), the customer manages more.

## 4. Security and identity: IAM

**IAM (Identity and Access Management)** controls **who** can do **what** on **which** resources. It is a global, free service.

| Concept | What it is |
|---|---|
| **Root user** | The account created with the sign-up email. It has full access. **Do not** use it day to day; protect it with **MFA** |
| **User** | A person or application with long-term credentials |
| **Group** | A set of users who share permissions (e.g., "Analysts") |
| **Role** | An identity with **temporary credentials** that is *assumed*. It is the right way to give permissions to services (e.g., letting EC2 or Glue read from S3) |
| **Policy** | A **JSON** document that allows (`Allow`) or denies (`Deny`) actions. An explicit `Deny` **always wins** |
| **Least privilege** | Give **only** the minimum permissions needed |
| **MFA** | Multi-factor authentication |

```json
{
  "Version": "2012-10-17",
  "Statement": [{
    "Effect": "Allow",
    "Action": ["s3:GetObject", "s3:ListBucket"],
    "Resource": ["arn:aws:s3:::blend-datalake", "arn:aws:s3:::blend-datalake/*"]
  }]
}
```

Other security services: **KMS** (encryption keys), **Secrets Manager** (passwords, rotation), **AWS Shield** (DDoS), **AWS WAF** (web firewall), **GuardDuty** (threat detection), **Macie** (finds sensitive data/PII in S3), **Inspector** (vulnerabilities).

## 5. Core services

### Compute

| Service | What it is | When |
|---|---|---|
| **Amazon EC2** | Virtual machines (instances) | Full control of the server (IaaS) |
| **AWS Lambda** | **Serverless** functions that run on events; at most 15 minutes per run; you pay per ms | Short tasks: process a file when it lands in S3, APIs |
| **Amazon ECS / EKS** | Orchestration of Docker **containers** (EKS = Kubernetes) | Microservices |
| **AWS Fargate** | Containers without managing servers | Serverless containers |
| **Elastic Beanstalk** | PaaS: you upload the code and AWS deploys it | Quick web apps |
| **Auto Scaling** | Adds or removes EC2 instances according to demand | Elasticity |
| **Elastic Load Balancing (ELB)** | Distributes traffic across instances | High availability |

### Storage

| Service | Type | Detail |
|---|---|---|
| **Amazon S3** | **Objects** (files) in *buckets* | 99.999999999% durability (**11 nines**), practically unlimited capacity. The foundation of **data lakes** |
| **Amazon EBS** | **Block** storage (the hard drive of an EC2 instance) | Tied to one AZ |
| **Amazon EFS** | Shared **file** storage (NFS) | Several EC2 instances at once |
| **S3 Glacier** | Long-term archive | Very cheap; retrieval from minutes to hours |

**S3 storage classes** (from most expensive/fastest to cheapest):

| Class | Use |
|---|---|
| S3 Standard | Frequently accessed data |
| S3 Intelligent-Tiering | Unknown or changing access patterns (moves data automatically) |
| S3 Standard-IA / One Zone-IA | Infrequent access |
| S3 Glacier Instant / Flexible Retrieval | Archive |
| S3 Glacier Deep Archive | Archive for years; the cheapest; retrieval in hours |

> **Lifecycle policies:** move objects to cheaper classes automatically over time (e.g., to Glacier after 90 days).

### Databases

| Service | Type | When |
|---|---|---|
| **Amazon RDS** | Managed relational (PostgreSQL, MySQL, MariaDB, Oracle, SQL Server) | Transactional applications (OLTP) |
| **Amazon Aurora** | AWS relational DB, compatible with MySQL/PostgreSQL; higher performance | High-performance OLTP |
| **Amazon DynamoDB** | **Key-value**/document NoSQL, serverless, millisecond latency | Massive scale, low latency |
| **Amazon Redshift** | Columnar **data warehouse** (OLAP) | Analytics and BI |
| **Amazon ElastiCache** | In-memory cache (Redis/Memcached) | Speed up reads |
| **Amazon Neptune** | Graphs | Relationships, fraud, recommendations |
| **Amazon DocumentDB** | Documents (MongoDB-compatible) | JSON |

### Networking

| Service | What it is |
|---|---|
| **Amazon VPC** | Your private virtual network on AWS. Divided into public **subnets** (with Internet access through an *Internet Gateway*) and private subnets |
| **Security group** | Firewall at the **instance** level; *stateful*; allow rules only |
| **Network ACL** | Firewall at the **subnet** level; *stateless*; allow and deny |
| **Route 53** | DNS |
| **CloudFront** | CDN (cache at edge locations) |
| **API Gateway** | Create and publish APIs |

### Monitoring and governance

| Service | Question it answers |
|---|---|
| **Amazon CloudWatch** | How is it performing? Metrics, logs, alarms, dashboards |
| **AWS CloudTrail** | **Who** did **what** and **when**? Audit of API calls |
| **AWS Config** | How was a resource configured, and does it comply with the rules? |
| **AWS Trusted Advisor** | Recommendations on cost, security, performance and limits |

## 6. Pricing

| Purchase model | Approx. discount | When |
|---|---|---|
| **On-Demand** | — | Unpredictable, short workloads, tests |
| **Savings Plans / Reserved Instances** | Up to ~72 % | **Steady** usage with a 1- or 3-year commitment |
| **Spot Instances** | Up to ~90 % | **Interruption-tolerant** jobs (batch, data processing, ML training). AWS can reclaim them with a 2-minute warning |
| **Dedicated Hosts** | — | Licenses or regulations that require dedicated hardware |

**Principles:** pay for what you use; pay less the more you use (volume discounts); pay less when you reserve. In general, **data transfer into AWS (ingress) is free** and data transfer out to the Internet (egress) is charged.

**Tools:** AWS Pricing Calculator (estimate beforehand), AWS Budgets (budget alerts), Cost Explorer (analyze spending), Free Tier, *tags* to allocate costs.

## 7. AWS Well-Architected Framework: 6 pillars

| Pillar | Key idea |
|---|---|
| **Operational Excellence** | Automate, infrastructure as code, learn from failures |
| **Security** | Least privilege, encryption, traceability |
| **Reliability** | Recover from failures: several AZs, backups, auto scaling |
| **Performance Efficiency** | Use the right resource; serverless; experiment |
| **Cost Optimization** | Pay only for what is needed: right sizing, Spot, Savings Plans |
| **Sustainability** | Minimize environmental impact |

## 8. Other services worth recognizing

| Service | In one sentence |
|---|---|
| **AWS CloudFormation** | Infrastructure as code (YAML/JSON templates) |
| **Amazon SNS** | *Pub/sub* notifications (email, SMS, to many subscribers) |
| **Amazon SQS** | Message queues to decouple components |
| **Amazon EventBridge** | Event bus and scheduled tasks (*cron*) |
| **AWS Step Functions** | Orchestrate steps (workflows) with states |
| **Amazon SageMaker AI** | Build, train and deploy machine learning models |
| **Amazon Bedrock** | API access to generative AI foundation models (Claude, Llama, Amazon Nova…) |
| **AWS Snow Family** | Physical devices to move petabytes into AWS without a network |

---

## Self-assessment

1. A company wants to stop buying servers every 3 years "just in case". Which cloud advantage applies?
2. Who is responsible for patching the operating system of an EC2 instance?
3. Which IAM identity should a Glue job use to read from S3?
4. A nightly processing job can be restarted if it is interrupted. Which pricing model is cheapest?
5. Which service tells you who deleted an S3 bucket?
6. What is the difference between a region and an AZ?

<details>
<summary>Answers</summary>

1. *Stop guessing capacity* (and also *trade fixed expense for variable expense*).
2. The **customer** (on EC2, the OS is "in the cloud").
3. An **IAM role**: temporary credentials, no fixed keys.
4. **Spot Instances**.
5. **AWS CloudTrail**.
6. A **region** is a geographic area that contains several **AZs**; each AZ is one or more isolated data centers inside the region.

</details>

---

**Next:** [Data analytics on AWS](analisis-de-datos.en.md)
