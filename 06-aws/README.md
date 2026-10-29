# 06 · ¿Qué es AWS? Fundamentos de la nube

**Español** · [English](README.en.md)

> **Por qué importa tanto para Blend360:** Blend360 es **AWS Premier Tier Services Partner** (el nivel más alto de partners de servicios). Tiene competencias de AWS en **Data & Analytics**, **Generative AI**, Financial Services, DevOps y Migration, y es *delivery partner* de **Amazon EMR** y **Amazon QuickSight**. Es decir, gran parte de su trabajo con clientes se construye sobre AWS. Ver [qué evalúa Blend360](../guides/que-evalua-blend360.md).
>
> **Ventaja para ti:** como presentas el **AWS Certified AI Practitioner el 16 de noviembre**, mucho de esto ya lo estarás estudiando. Todo el material completo está integrado en el módulo [AWS AI Practitioner (AIF-C01)](../aws-ai-practitioner/README.md).

| Archivo | Contenido |
|---|---|
| Este README | Qué es la nube y AWS, infraestructura global, responsabilidad compartida, IAM, servicios principales, precios |
| [analisis-de-datos.md](analisis-de-datos.md) | ★ Análisis de datos en AWS: S3, Glue, Athena, Redshift, EMR, Kinesis, QuickSight, arquitecturas |
| [preguntas.md](preguntas.md) | 30 preguntas de práctica **en inglés** con explicación |

---

## 1. ¿Qué es la computación en la nube?

> **Cloud computing** is the **on-demand delivery** of IT resources over the Internet with **pay-as-you-go pricing**.

En lugar de comprar y mantener servidores propios (*on-premises*), **alquilas** capacidad de cómputo, almacenamiento y bases de datos a un proveedor (AWS, Azure, Google Cloud) y pagas solo por lo que usas.

**AWS (Amazon Web Services)** es la plataforma de nube de Amazon, lanzada en 2006. Ofrece más de 200 servicios y es el proveedor con mayor participación de mercado.

### Las 6 ventajas de la nube (según AWS, ¡las preguntan literalmente!)

| # | En inglés | Significado |
|---|---|---|
| 1 | **Trade fixed expense for variable expense** | Cambias inversión fija (CapEx) por gasto variable (OpEx): pagas lo que usas |
| 2 | **Benefit from massive economies of scale** | AWS compra a gran escala, así que el precio por unidad es menor |
| 3 | **Stop guessing capacity** | Escalas hacia arriba o hacia abajo según la demanda real |
| 4 | **Increase speed and agility** | Nuevos recursos en minutos, no en semanas |
| 5 | **Stop spending money running and maintaining data centers** | Te concentras en tu negocio, no en la infraestructura |
| 6 | **Go global in minutes** | Despliegas en varias regiones del mundo fácilmente |

### Modelos de servicio

| Modelo | Tú gestionas | El proveedor gestiona | Ejemplo AWS | Analogía (pizza) |
|---|---|---|---|---|
| **IaaS** (Infrastructure as a Service) | SO, apps, datos | Hardware, red, virtualización | **Amazon EC2** | Compras los ingredientes y la cocinas en tu casa |
| **PaaS** (Platform as a Service) | Apps y datos | + SO, runtime | **AWS Elastic Beanstalk**, RDS | Pides a domicilio |
| **SaaS** (Software as a Service) | Solo lo usas | Todo | Gmail, Salesforce, Amazon QuickSight | Vas a comer al restaurante |

### Modelos de despliegue

- **Cloud (pública):** todo en la nube.
- **On-premises (nube privada):** en tu propio centro de datos.
- **Hybrid (híbrida):** una combinación conectada de ambas.

### Características clave

| Término | Significado |
|---|---|
| **Elasticity** (elasticidad) | Aumentar o reducir recursos **automáticamente** según la demanda |
| **Scalability** (escalabilidad) | Capacidad de crecer. **Vertical** = máquina más grande (*scale up*). **Horizontal** = más máquinas (*scale out*) |
| **High availability** | El sistema sigue funcionando aunque falle un componente (varias AZ) |
| **Fault tolerance** | Tolera fallos sin interrupción |
| **Serverless** | No administras servidores; pagas por ejecución (Lambda, Athena, Glue) |
| **Managed service** | AWS se encarga de parches, backups y escalado (RDS, Redshift) |

## 2. Infraestructura global

```text
Región (p. ej., us-east-1, sa-east-1 São Paulo)
├── Zona de disponibilidad A  (1 o más centros de datos)
├── Zona de disponibilidad B
└── Zona de disponibilidad C
+ Edge locations / Puntos de presencia (para CloudFront: caché cerca de los usuarios)
```

| Componente | Qué es | Para qué |
|---|---|---|
| **Region** | Área geográfica con varias AZ aisladas entre sí. Hay más de 30 regiones | Elegir por: **cumplimiento legal** de datos, **latencia** (cercanía a los usuarios), **servicios disponibles** y **precio** |
| **Availability Zone (AZ)** | Uno o más centros de datos con energía y red independientes. Cada región tiene normalmente 3 o más | Alta disponibilidad: despliega en **varias AZ** |
| **Edge location** | Punto de presencia para caché y CDN | **CloudFront**, Route 53: baja latencia global |
| **Local Zones / Outposts** | AWS más cerca de ciudades / en tu propio centro de datos | Latencia ultrabaja / híbrido |

## 3. Modelo de responsabilidad compartida

| AWS es responsable de la seguridad **DE** la nube (*security **of** the cloud*) | El cliente es responsable de la seguridad **EN** la nube (*security **in** the cloud*) |
|---|---|
| Hardware, centros de datos físicos, red global | **Datos** del cliente y su cifrado |
| Software de virtualización (hipervisor) | **IAM**: usuarios, permisos, MFA |
| Infraestructura de los servicios gestionados | Configuración de **security groups** y firewall |
| Parches del SO en servicios gestionados (RDS, Lambda) | Parches del SO **en EC2** y de las aplicaciones |

> Regla: cuanto más **gestionado** es el servicio (Lambda, S3), más responsabilidad asume AWS. Con **EC2** (IaaS), el cliente gestiona más cosas.

## 4. Seguridad e identidad: IAM

**IAM (Identity and Access Management)** controla **quién** puede hacer **qué** sobre **cuáles** recursos. Es un servicio global y gratuito.

| Concepto | Qué es |
|---|---|
| **Root user** | La cuenta creada con el email de registro. Tiene acceso total. **No** lo uses en el día a día; protégelo con **MFA** |
| **User** | Una persona o aplicación con credenciales de largo plazo |
| **Group** | Conjunto de usuarios que comparten permisos (por ejemplo, "Analysts") |
| **Role** | Identidad con **credenciales temporales** que se *asume*. Es la forma correcta de dar permisos a servicios (por ejemplo, que EC2 o Glue lean de S3) |
| **Policy** | Documento **JSON** que permite (`Allow`) o deniega (`Deny`) acciones. Un `Deny` explícito **siempre gana** |
| **Least privilege** | Dar **solo** los permisos mínimos necesarios |
| **MFA** | Autenticación multifactor |

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

Otros servicios de seguridad: **KMS** (llaves de cifrado), **Secrets Manager** (contraseñas, rotación), **AWS Shield** (DDoS), **AWS WAF** (firewall web), **GuardDuty** (detección de amenazas), **Macie** (descubre datos sensibles/PII en S3), **Inspector** (vulnerabilidades).

## 5. Servicios principales

### Cómputo

| Servicio | Qué es | Cuándo |
|---|---|---|
| **Amazon EC2** | Máquinas virtuales (instancias) | Control total del servidor (IaaS) |
| **AWS Lambda** | Funciones **serverless** que se ejecutan ante eventos; máximo 15 minutos por ejecución; pagas por ms | Tareas cortas: procesar un archivo al llegar a S3, APIs |
| **Amazon ECS / EKS** | Orquestación de **contenedores** Docker (EKS = Kubernetes) | Microservicios |
| **AWS Fargate** | Contenedores sin gestionar servidores | Contenedores serverless |
| **Elastic Beanstalk** | PaaS: subes el código y AWS despliega | Apps web rápidas |
| **Auto Scaling** | Agrega o quita instancias EC2 según la demanda | Elasticidad |
| **Elastic Load Balancing (ELB)** | Distribuye el tráfico entre instancias | Alta disponibilidad |

### Almacenamiento

| Servicio | Tipo | Detalle |
|---|---|---|
| **Amazon S3** | **Objetos** (archivos) en *buckets* | Durabilidad de 99,999999999 % (**11 nueves**), capacidad prácticamente ilimitada. Es la base de los **data lakes** |
| **Amazon EBS** | **Bloques** (disco duro de una EC2) | Atado a una AZ |
| **Amazon EFS** | **Archivos** (NFS) compartidos | Varias EC2 a la vez |
| **S3 Glacier** | Archivo a largo plazo | Muy barato; recuperación de minutos a horas |

**Clases de almacenamiento de S3** (de más cara/rápida a más barata):

| Clase | Uso |
|---|---|
| S3 Standard | Datos de acceso frecuente |
| S3 Intelligent-Tiering | Patrón de acceso desconocido o cambiante (mueve los datos automáticamente) |
| S3 Standard-IA / One Zone-IA | Acceso infrecuente (*Infrequent Access*) |
| S3 Glacier Instant / Flexible Retrieval | Archivo |
| S3 Glacier Deep Archive | Archivo de años; lo más barato; recuperación en horas |

> **Lifecycle policies:** mueven objetos automáticamente a clases más baratas con el tiempo (por ejemplo, a Glacier después de 90 días).

### Bases de datos

| Servicio | Tipo | Cuándo |
|---|---|---|
| **Amazon RDS** | Relacional gestionada (PostgreSQL, MySQL, MariaDB, Oracle, SQL Server) | Aplicaciones transaccionales (OLTP) |
| **Amazon Aurora** | Relacional de AWS, compatible con MySQL/PostgreSQL; más rendimiento | OLTP de alto rendimiento |
| **Amazon DynamoDB** | NoSQL **key-value**/documentos, serverless, latencia de milisegundos | Escala masiva, baja latencia |
| **Amazon Redshift** | **Data warehouse** columnar (OLAP) | Analítica y BI |
| **Amazon ElastiCache** | Caché en memoria (Redis/Memcached) | Acelerar lecturas |
| **Amazon Neptune** | Grafos | Relaciones, fraude, recomendaciones |
| **Amazon DocumentDB** | Documentos (compatible con MongoDB) | JSON |

### Redes

| Servicio | Qué es |
|---|---|
| **Amazon VPC** | Tu red privada virtual en AWS. Se divide en **subnets** públicas (con salida a Internet por un *Internet Gateway*) y privadas |
| **Security group** | Firewall a nivel de **instancia**; *stateful*; solo reglas de permitir |
| **Network ACL** | Firewall a nivel de **subnet**; *stateless*; permite y deniega |
| **Route 53** | DNS |
| **CloudFront** | CDN (caché en edge locations) |
| **API Gateway** | Crear y publicar APIs |

### Monitoreo y gobierno

| Servicio | Pregunta que responde |
|---|---|
| **Amazon CloudWatch** | ¿Cómo está funcionando? Métricas, logs, alarmas, dashboards |
| **AWS CloudTrail** | ¿**Quién** hizo **qué** y **cuándo**? Auditoría de llamadas a la API |
| **AWS Config** | ¿Cómo estaba configurado un recurso y cumple las reglas? |
| **AWS Trusted Advisor** | Recomendaciones de costo, seguridad, rendimiento y límites |

## 6. Precios

| Modelo de compra | Descuento aprox. | Cuándo |
|---|---|---|
| **On-Demand** | — | Cargas impredecibles, cortas, pruebas |
| **Savings Plans / Reserved Instances** | Hasta ~72 % | Uso **constante** con compromiso de 1 o 3 años |
| **Spot Instances** | Hasta ~90 % | Trabajos **tolerantes a interrupciones** (batch, procesamiento de datos, entrenamiento ML). AWS puede reclamarlas con 2 minutos de aviso |
| **Dedicated Hosts** | — | Licencias o cumplimiento normativo que exigen hardware dedicado |

**Principios:** pagas por uso; pagas menos cuanto más usas (descuentos por volumen); pagas menos si reservas. En general, **la transferencia de datos de entrada (ingress) es gratis** y la de salida a Internet (egress) se cobra.

**Herramientas:** AWS Pricing Calculator (estimar antes), AWS Budgets (alertas de presupuesto), Cost Explorer (analizar el gasto), Free Tier (capa gratuita), etiquetas (*tags*) para asignar costos.

## 7. AWS Well-Architected Framework: 6 pilares

| Pilar | Idea clave |
|---|---|
| **Operational Excellence** | Automatizar, infraestructura como código, aprender de los fallos |
| **Security** | Mínimo privilegio, cifrado, trazabilidad |
| **Reliability** | Recuperarse de fallos: varias AZ, backups, autoescalado |
| **Performance Efficiency** | Usar el recurso adecuado; serverless; experimentar |
| **Cost Optimization** | Pagar solo lo necesario: tamaño correcto, Spot, Savings Plans |
| **Sustainability** | Minimizar el impacto ambiental |

## 8. Otros servicios que conviene reconocer

| Servicio | En una frase |
|---|---|
| **AWS CloudFormation** | Infraestructura como código (plantillas YAML/JSON) |
| **Amazon SNS** | Notificaciones *pub/sub* (email, SMS, a muchos suscriptores) |
| **Amazon SQS** | Colas de mensajes para desacoplar componentes |
| **Amazon EventBridge** | Bus de eventos y tareas programadas (*cron*) |
| **AWS Step Functions** | Orquestar pasos (flujos de trabajo) con estados |
| **Amazon SageMaker AI** | Construir, entrenar y desplegar modelos de machine learning |
| **Amazon Bedrock** | Acceso por API a modelos fundacionales de IA generativa (Claude, Llama, Amazon Nova…) |
| **AWS Snow Family** | Dispositivos físicos para mover petabytes a AWS sin red |

---

## Autoevaluación

1. Una empresa quiere dejar de comprar servidores cada 3 años "por si acaso". ¿Qué ventaja de la nube aplica?
2. ¿Quién es responsable de parchear el sistema operativo de una instancia EC2?
3. ¿Qué identidad de IAM debe usar una función Glue para leer de S3?
4. Un trabajo de procesamiento nocturno puede reiniciarse si se interrumpe. ¿Qué modelo de precio es el más barato?
5. ¿Qué servicio te dice quién borró un bucket de S3?
6. ¿Qué diferencia hay entre una región y una AZ?

<details>
<summary>Respuestas</summary>

1. *Stop guessing capacity* (y también *trade fixed expense for variable expense*).
2. El **cliente** (en EC2, el SO está "en la nube").
3. Un **IAM role**: credenciales temporales, sin claves fijas.
4. **Spot Instances**.
5. **AWS CloudTrail**.
6. Una **región** es un área geográfica que contiene varias **AZ**; cada AZ es uno o más centros de datos aislados dentro de la región.

</details>

---

**Siguiente:** [Análisis de datos en AWS](analisis-de-datos.md)
