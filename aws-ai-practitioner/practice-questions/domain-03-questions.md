# Preguntas de Práctica — Dominio 3: Aplicaciones de Modelos Fundacionales

## Pregunta 1 — Opción múltiple

Una startup quiere añadir un asistente GenAI a su producto lo antes posible, probando modelos de varios proveedores y **sin gestionar servidores ni GPUs**. ¿Qué servicio debe usar?

- A. Amazon EC2 con instancias P5
- B. Amazon SageMaker JumpStart
- C. Amazon Bedrock
- D. Amazon Comprehend

<details>
<summary>▶ Ver respuesta</summary>

**Respuesta correcta:** C

- **C ✅** Bedrock es serverless y ofrece FMs de múltiples proveedores mediante una API unificada.
- **A ❌** Exige gestionar toda la infraestructura.
- **B ❌** Despliega modelos en endpoints que el cliente dimensiona y gestiona.
- **D ❌** Es un servicio de NLP, no una plataforma de FMs.

📚 [Dominio 3 — Bedrock vs. JumpStart](../domains/03-applications-foundation-models/README.md#21-bedrock-vs-sagemaker-jumpstart)
</details>

## Pregunta 2 — Opción múltiple

Una aerolínea quiere un asistente que, a partir de la petición del cliente, consulte la política de cambios, verifique la disponibilidad en su sistema de reservas mediante una API y modifique la reserva. ¿Qué capacidad de Amazon Bedrock es la más adecuada?

- A. Bedrock Knowledge Bases
- B. Bedrock Agents
- C. Bedrock Guardrails
- D. Bedrock Model Evaluation

<details>
<summary>▶ Ver respuesta</summary>

**Respuesta correcta:** B

- **B ✅** Los agentes planifican tareas multi-paso, invocan APIs mediante action groups (Lambda + OpenAPI) y pueden consultar Knowledge Bases.
- **A ❌** Solo recupera información; no ejecuta acciones.
- **C ❌** Aplica políticas de seguridad.
- **D ❌** Compara la calidad de los modelos.

📚 [Dominio 3 — Bedrock Agents](../domains/03-applications-foundation-models/README.md#15-amazon-bedrock-agents)
</details>

## Pregunta 3 — Opción múltiple

Una empresa necesita extraer automáticamente los importes, fechas y líneas de detalle de miles de facturas escaneadas en PDF. ¿Qué servicio es el más adecuado con el menor esfuerzo?

- A. Amazon Rekognition
- B. Amazon Comprehend
- C. Amazon Textract
- D. Amazon Polly

<details>
<summary>▶ Ver respuesta</summary>

**Respuesta correcta:** C

- **C ✅** Textract extrae texto, formularios y tablas, y ofrece una API especializada para facturas y recibos (AnalyzeExpense).
- **A ❌** Rekognition analiza imágenes/video (objetos, rostros), no la estructura de documentos.
- **B ❌** Comprehend analiza texto ya extraído; no hace OCR.
- **D ❌** Polly convierte texto en voz.

📚 [Dominio 3 — NLP y Visión](../domains/03-applications-foundation-models/README.md#31-nlp-y-visión)
</details>

## Pregunta 4 — Opción múltiple

Un banco usa Bedrock para un chatbot público. Debe impedir que el asistente ofrezca **asesoría de inversión** y que muestre números de tarjeta de crédito en sus respuestas. ¿Qué solución cumple ambos requisitos con el menor esfuerzo?

- A. Fine-tuning del modelo con ejemplos de rechazo.
- B. Amazon Bedrock Guardrails con un *denied topic* y un filtro de información sensible (PII).
- C. Amazon Macie sobre las respuestas del modelo.
- D. Una política IAM que deniegue `bedrock:InvokeModel`.

<details>
<summary>▶ Ver respuesta</summary>

**Respuesta correcta:** B

- **B ✅** Los *denied topics* bloquean temas definidos en lenguaje natural y los filtros PII bloquean o enmascaran datos como tarjetas de crédito.
- **A ❌** Costoso y sin garantías.
- **C ❌** Macie analiza datos en S3, no filtra respuestas en tiempo real.
- **D ❌** Bloquearía el chatbot por completo.

📚 [Dominio 3 — Guardrails](../domains/03-applications-foundation-models/README.md#16-amazon-bedrock-guardrails)
</details>

## Pregunta 5 — Opción múltiple

Un equipo de data science necesita desplegar un modelo open-source específico, elegir el tipo de instancia GPU, ejecutarlo dentro de su VPC con aislamiento de red y modificar el script de entrenamiento. ¿Qué opción es la más adecuada?

- A. Amazon Bedrock On-Demand
- B. Amazon SageMaker JumpStart
- C. Amazon Q Business
- D. Amazon Bedrock Knowledge Bases

<details>
<summary>▶ Ver respuesta</summary>

**Respuesta correcta:** B

- **B ✅** JumpStart despliega modelos en endpoints de SageMaker con control de la instancia, de la red y de la personalización.
- **A ❌** No permite elegir infraestructura ni modificar el entrenamiento.
- **C ❌** Es un asistente empresarial listo para usar.
- **D ❌** Es una funcionalidad de RAG.

📚 [Dominio 3 — Criterios de decisión](../domains/03-applications-foundation-models/README.md#2-amazon-sagemaker-jumpstart-y-criterios-de-decisión)
</details>

## Pregunta 6 — Emparejamiento

Relaciona cada necesidad con el servicio:

| Necesidad | Servicio |
|---|---|
| 1. Asistente para empleados sobre SharePoint y Confluence respetando permisos | a. Amazon Q Developer |
| 2. Actualizar una aplicación de Java 8 a Java 17 | b. Amazon Transcribe |
| 3. Transcribir llamadas y redactar PII | c. Amazon Q Business |
| 4. Chatbot de IVR basado en intents | d. Amazon Lex |

<details>
<summary>▶ Ver respuesta</summary>

**Solución:** 1 → c, 2 → a, 3 → b, 4 → d

📚 [Dominio 3 — Tabla resumen](../domains/03-applications-foundation-models/README.md#35-tabla-resumen-servicio--caso-de-uso-principal--cuándo-no-usarlo)
</details>
