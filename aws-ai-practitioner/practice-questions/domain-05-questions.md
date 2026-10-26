# Preguntas de Práctica — Dominio 5: Seguridad, Cumplimiento y Gobernanza

## Pregunta 1 — Opción múltiple

Una aplicación en subredes privadas sin acceso a Internet necesita invocar modelos de Amazon Bedrock. ¿Qué solución es la adecuada?

- A. Añadir un Internet Gateway a la VPC.
- B. Crear un interface VPC endpoint (AWS PrivateLink) para `bedrock-runtime`.
- C. Crear un gateway VPC endpoint para Amazon S3.
- D. Usar AWS Direct Connect.

<details>
<summary>▶ Ver respuesta</summary>

**Respuesta correcta:** B

- **B ✅** PrivateLink permite invocar Bedrock de forma privada a través de la red de AWS.
- **A ❌** Expone la carga de trabajo a Internet.
- **C ❌** Solo cubre S3.
- **D ❌** Conecta redes on-premises con AWS; no resuelve el acceso privado desde la VPC.

📚 [Dominio 5 — Aislamiento de red](../domains/05-security-compliance-governance/README.md#3-aislamiento-de-red-vpc-endpoints-aws-privatelink)
</details>

## Pregunta 2 — Opción múltiple

El equipo de seguridad necesita conservar el **texto de los prompts y de las respuestas** de un modelo de Bedrock para auditorías de cumplimiento. ¿Qué debe habilitar?

- A. AWS CloudTrail
- B. Bedrock Model Invocation Logging
- C. Amazon CloudWatch Metrics
- D. AWS Config

<details>
<summary>▶ Ver respuesta</summary>

**Respuesta correcta:** B

- **B ✅** El invocation logging entrega el contenido de las peticiones y respuestas a S3 y/o CloudWatch Logs.
- **A ❌** CloudTrail registra metadatos de las llamadas (quién, cuándo), no el contenido.
- **C ❌** Las métricas son agregadas (tokens, latencia).
- **D ❌** Config registra la configuración de los recursos.

📚 [Dominio 5 — Auditoría y monitoreo](../domains/05-security-compliance-governance/README.md#4-auditoría-y-monitoreo)
</details>

## Pregunta 3 — Opción múltiple

Una empresa debe generar resúmenes de 2 millones de documentos históricos durante el próximo mes. No hay requisito de tiempo real y el objetivo es **minimizar el costo**. ¿Qué opción de Bedrock es la adecuada?

- A. On-Demand
- B. Provisioned Throughput con compromiso de 6 meses
- C. Batch Inference
- D. Cross-region inference

<details>
<summary>▶ Ver respuesta</summary>

**Respuesta correcta:** C

- **C ✅** Batch Inference procesa grandes volúmenes de forma asíncrona desde S3 con un descuento significativo frente a On-Demand.
- **A ❌** Más caro por token para este volumen.
- **B ❌** Compromiso de capacidad innecesario para una carga puntual.
- **D ❌** Mejora la disponibilidad y el throughput, no el precio.

📚 [Dominio 5 — Optimización de costos](../domains/05-security-compliance-governance/README.md#5-optimización-de-costos-en-bedrock)
</details>

## Pregunta 4 — Opción múltiple

Según el modelo de responsabilidad compartida, ¿cuál de estas tareas es responsabilidad **del cliente** al usar Amazon Bedrock?

- A. Parchear el sistema operativo de los servidores de inferencia.
- B. Mantener la disponibilidad física de los centros de datos.
- C. Configurar los permisos IAM que controlan quién puede invocar cada modelo.
- D. Aislar los modelos de los proveedores en cuentas de despliegue.

<details>
<summary>▶ Ver respuesta</summary>

**Respuesta correcta:** C

La identidad y el acceso, los datos y la configuración (guardrails, cifrado, red, logging) son siempre responsabilidad del cliente. Las opciones A, B y D corresponden a AWS en un servicio gestionado.

📚 [Dominio 5 — Responsabilidad compartida](../domains/05-security-compliance-governance/README.md#1-modelo-de-responsabilidad-compartida-aplicado-a-genai)
</details>

## Pregunta 5 — Opción múltiple

Una organización con 40 cuentas de AWS quiere garantizar que **ninguna** cuenta pueda invocar modelos de Bedrock distintos de los aprobados por el comité de IA, incluso si un administrador local lo intenta. ¿Qué mecanismo es el adecuado?

- A. Una política IAM en cada usuario.
- B. Una Service Control Policy (SCP) en AWS Organizations.
- C. Un guardrail de Bedrock.
- D. Una regla de AWS Config.

<details>
<summary>▶ Ver respuesta</summary>

**Respuesta correcta:** B

- **B ✅** Las SCPs establecen el máximo de permisos para todas las cuentas de la organización y no pueden ser anuladas por administradores locales.
- **A ❌** No escala y un administrador local podría modificarla.
- **C ❌** Filtra contenido; no controla qué modelo se invoca.
- **D ❌** Detecta configuraciones; no impide llamadas a la API.

📚 [Dominio 5 — SCP organizacional](../domains/05-security-compliance-governance/README.md#23-scp-organizacional-restringir-modelos-y-regiones)
</details>

## Pregunta 6 — Respuesta múltiple (elige DOS)

Un equipo usa buckets S3 como fuente de datos para una Knowledge Base de Bedrock y para fine-tuning. Quiere **detectar PII** en esos datos y **cifrarlos con claves que controle**. ¿Qué DOS servicios debe usar?

- A. Amazon Macie
- B. AWS KMS con customer managed keys
- C. Amazon Inspector
- D. AWS Artifact
- E. Amazon Polly

<details>
<summary>▶ Ver respuesta</summary>

**Respuestas correctas:** A y B

- **A ✅** Macie descubre y clasifica datos sensibles en S3.
- **B ✅** KMS con claves gestionadas por el cliente da control sobre la política, la rotación y la revocación.
- **C ❌** Inspector busca vulnerabilidades en cargas de cómputo.
- **D ❌** Proporciona informes de cumplimiento de AWS.
- **E ❌** Es text-to-speech.

📚 [Dominio 5 — Gobernanza de datos](../domains/05-security-compliance-governance/README.md#6-gobernanza-de-datos-y-servicios-de-cumplimiento)
</details>
