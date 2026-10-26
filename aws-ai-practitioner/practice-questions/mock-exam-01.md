# Simulacro 01 — 65 preguntas (alineado con la guía v1.1)

> **Instrucciones:** 90 minutos (120 si usas ESL +30), sin consultar material. Anota tus respuestas en papel y corrige con la [clave de respuestas](#clave-de-respuestas) al final.
>
> - Distribución por pesos oficiales: **D1 13 · D2 16 · D3 18 · D4 9 · D5 9** preguntas.
> - Las preguntas marcadas con 🆕 cubren temas añadidos en la **guía v1.1** (abril 2026).
> - Preguntas originales, no extraídas del examen real. Están ordenadas por dominio para que puedas calcular tu puntuación por dominio, a diferencia del examen real, donde aparecen mezcladas.
> - **Objetivo:** ≥ 85 % (56/65) en el primer intento.

---

## Dominio 1 — Fundamentos de IA y ML

**1.** Una tienda online quiere agrupar a sus clientes por comportamiento de compra. No tiene etiquetas de segmento. ¿Qué enfoque es el adecuado?

- A. Clasificación supervisada
- B. Regresión lineal
- C. Clustering (aprendizaje no supervisado)
- D. Aprendizaje por refuerzo

**2.** 🆕 ¿Qué describe mejor un sistema de **IA agéntica**?

- A. Un sistema que usa un FM para planificar, invocar herramientas y ejecutar acciones de varios pasos hacia un objetivo.
- B. Un modelo de difusión que genera imágenes a partir de texto.
- C. Un sistema experto basado únicamente en reglas `if/else`.
- D. Un modelo de regresión que predice ventas.

**3.** ¿Cuál de los siguientes es un **hiperparámetro**?

- A. Los pesos de la red neuronal tras el entrenamiento
- B. Las predicciones del modelo
- C. Las features del dataset
- D. La tasa de aprendizaje (*learning rate*)

**4.** Un hospital entrena un modelo para detectar una enfermedad grave. **No detectar** a un paciente enfermo es mucho más grave que hacer una prueba adicional a un paciente sano. ¿Qué métrica debe priorizar?

- A. Exactitud (accuracy)
- B. Precisión (precision)
- C. Recall
- D. R²

**5.** En un filtro de spam, enviar a la carpeta de spam un correo **legítimo** importante es el error más costoso. ¿Qué métrica debe priorizarse?

- A. Precisión (precision)
- B. Recall
- C. RMSE
- D. MAE

**6.** 🆕 Un banco necesita un modelo para aprobar o rechazar préstamos a partir de datos **tabulares**. El regulador exige **explicar cada decisión** individual. ¿Qué enfoque es el más adecuado?

- A. Un LLM de Amazon Bedrock con un prompt que decida la aprobación
- B. Un modelo de ML tradicional (p. ej., XGBoost) con explicaciones de SageMaker Clarify
- C. Un modelo de difusión
- D. Un agente de Bedrock con acceso a la base de datos de clientes

**7.** Un modelo de pronóstico de demanda debe penalizar especialmente los **errores grandes**. ¿Qué métrica es la más adecuada?

- A. F1-score
- B. Precisión
- C. RMSE
- D. AUC-ROC

**8.** Un modelo obtiene 99 % de exactitud en entrenamiento y 65 % en validación. ¿Qué acción es la adecuada?

- A. Aumentar la complejidad del modelo
- B. Entrenar durante más epochs
- C. Eliminar el conjunto de validación
- D. Aplicar regularización y conseguir más datos de entrenamiento

**9.** Una empresa necesita **etiquetar** 200 000 imágenes con ayuda de personas y reducir costos mediante etiquetado automático. ¿Qué servicio debe usar?

- A. Amazon SageMaker Ground Truth
- B. Amazon SageMaker Clarify
- C. Amazon SageMaker Model Monitor
- D. Amazon SageMaker Data Wrangler

**10.** Un modelo recibe tráfico **intermitente e impredecible**, con horas sin peticiones. El equipo quiere minimizar costos y tolera arranques en frío. ¿Qué opción de inferencia de SageMaker debe usar?

- A. Endpoint en tiempo real
- B. Serverless Inference
- C. Batch Transform
- D. Instancias EC2 reservadas

**11.** Un modelo procesa archivos de **500 MB** que tardan unos **20 minutos** cada uno. Las peticiones pueden encolarse. ¿Qué opción de inferencia es la adecuada?

- A. Real-time inference
- B. Serverless Inference
- C. Asynchronous Inference
- D. Amazon Bedrock On-Demand

**12.** Un equipo quiere automatizar el flujo de ML (preparación, entrenamiento, evaluación y registro del modelo) como un pipeline de **CI/CD**. ¿Qué servicio debe usar?

- A. Amazon SageMaker Canvas
- B. Amazon SageMaker Ground Truth
- C. Amazon SageMaker JumpStart
- D. Amazon SageMaker Pipelines

**13.** Un modelo obtiene resultados excelentes en el conjunto de prueba, pero malos en producción. Se descubre que una feature se calculaba con información del propio valor objetivo. ¿Qué problema es?

- A. Underfitting
- B. Data leakage (fuga de datos)
- C. Desbalanceo de clases
- D. Drift de concepto

## Dominio 2 — Fundamentos de IA Generativa

**14.** Un equipo de marketing quiere que un LLM genere eslóganes **creativos y variados**. ¿Qué ajuste es el adecuado?

- A. Temperatura 0
- B. Top-K = 1
- C. Temperatura alta (p. ej., 0,9)
- D. Reducir el máximo de tokens a 10

**15.** Un chatbot empieza a fallar en conversaciones largas con un error de "entrada demasiado larga". ¿Cuál es la mejor solución?

- A. Resumir o recortar el historial antiguo para no superar la ventana de contexto
- B. Aumentar la temperatura
- C. Cambiar a un modelo de generación de imágenes
- D. Aumentar Top-P

**16.** 🆕 Una aplicación envía un manual de 200 páginas completo en **cada** petición al modelo y los costos son muy altos. ¿Qué cambio reduce más el costo sin perder calidad?

- A. Aumentar `maxTokens`
- B. Contratar Provisioned Throughput aunque el tráfico sea bajo
- C. Aumentar la temperatura
- D. Usar RAG para enviar solo los fragmentos relevantes del manual

**17.** 🆕 ¿Qué afirmación sobre el **precio por tokens** de los FMs en Bedrock On-Demand es correcta?

- A. Solo se facturan los tokens de salida.
- B. Se facturan tokens de entrada y de salida, y los de salida suelen ser más caros por token.
- C. Se factura un precio fijo por petición independientemente de su tamaño.
- D. Se factura por hora de instancia.

**18.** 🆕 ¿Qué es el **context engineering**?

- A. Ajustar los pesos del modelo con datos etiquetados
- B. Cifrar los prompts con AWS KMS
- C. Decidir y estructurar qué información (instrucciones, datos recuperados, herramientas, memoria) entra en el contexto del modelo
- D. Elegir el tipo de instancia GPU para el entrenamiento

**19.** 🆕 ¿Qué es el **Model Context Protocol (MCP)**?

- A. Un protocolo abierto que estandariza cómo los agentes y aplicaciones de IA se conectan con herramientas y fuentes de datos externas
- B. Un protocolo propietario de facturación de AWS
- C. Una técnica de compresión de modelos
- D. Una métrica de evaluación de LLMs

**20.** 🆕 Un asistente de viajes tiene un agente coordinador que delega en agentes especialistas de vuelos, hoteles y pagos, y combina sus resultados. ¿Qué patrón es?

- A. RLHF
- B. Supervisor (orquestador) multi-agente
- C. Inferencia por lotes
- D. Few-shot prompting

**21.** 🆕 Un asistente debe **recordar las preferencias del usuario entre sesiones distintas** (p. ej., asiento de pasillo). ¿Qué capacidad necesita?

- A. Una temperatura más baja
- B. Stop sequences
- C. Memoria a largo plazo del agente (p. ej., AgentCore Memory)
- D. Un Top-K mayor

**22.** Una empresa quiere un asistente que responda sobre sus políticas internas, que **cambian cada semana**, sin re-entrenar modelos. ¿Qué técnica debe usar?

- A. RAG con una base de conocimiento
- B. Fine-tuning semanal
- C. Pre-entrenamiento desde cero
- D. Incluir todas las políticas como ejemplos few-shot

**23.** ¿Qué datos se necesitan para hacer **fine-tuning** de un FM con instrucciones?

- A. Un corpus sin etiquetar
- B. Ningún dato
- C. Solo imágenes
- D. Pares prompt–respuesta etiquetados

**24.** ¿Qué es una **alucinación** de un LLM?

- A. Una respuesta plausible pero incorrecta o no respaldada por los datos
- B. Una negativa del modelo a responder
- C. Una respuesta lenta
- D. Un error de autenticación

**25.** Para buscar documentos **semánticamente similares** a una consulta, ¿qué debe generarse para la consulta y los documentos?

- A. Stop sequences
- B. Embeddings (vectores)
- C. Hiperparámetros
- D. Model Units

**26.** Un equipo quiere evaluar automáticamente **resúmenes** generados comparándolos con resúmenes de referencia. ¿Qué métrica debe usar?

- A. BLEU
- B. RMSE
- C. ROUGE
- D. F1-score

**27.** ¿Qué tipo de modelo genera imágenes **eliminando ruido de forma iterativa**?

- A. Modelo de difusión
- B. Transformer encoder-only
- C. Regresión lineal
- D. K-means

**28.** Un desarrollador quiere que el modelo devuelva siempre un formato JSON concreto **sin entrenar el modelo**. ¿Qué técnica debe usar primero?

- A. Continued pre-training
- B. RLHF
- C. Fine-tuning
- D. Few-shot prompting con ejemplos del formato esperado

**29.** Elige **DOS** limitaciones de la IA generativa.

- A. Salidas no deterministas
- B. Exactitud factual garantizada
- C. Alucinaciones
- D. Explicabilidad total de cada salida
- E. Costo de inferencia nulo

## Dominio 3 — Aplicaciones de Modelos Fundacionales

**30.** Una startup quiere usar FMs de varios proveedores mediante una API, con **el menor esfuerzo operativo** y pago por uso. ¿Qué servicio debe elegir?

- A. Amazon EC2 con GPU
- B. Amazon SageMaker JumpStart
- C. Amazon Bedrock
- D. Amazon Comprehend

**31.** Un equipo de data science necesita desplegar un modelo open-source concreto **eligiendo el tipo de instancia GPU** y modificando el script de fine-tuning. ¿Qué opción es la adecuada?

- A. Amazon SageMaker JumpStart
- B. Amazon Bedrock On-Demand
- C. Amazon Q Business
- D. Amazon Bedrock Guardrails

**32.** Al crear una Knowledge Base de Bedrock con la opción *Quick create*, ¿qué vector store se aprovisiona por defecto?

- A. Amazon DynamoDB
- B. Amazon MemoryDB
- C. Amazon RDS for MySQL
- D. Amazon OpenSearch Serverless

**33.** 🆕 Una empresa ya usa **Amazon Aurora PostgreSQL** y quiere guardar los embeddings de su Knowledge Base junto a sus datos relacionales. ¿Qué opción es la adecuada?

- A. Aurora PostgreSQL con la extensión pgvector
- B. Amazon S3 Glacier
- C. Amazon ElastiCache
- D. Amazon Redshift sin extensiones

**34.** En Amazon Bedrock Agents, ¿qué componente define las **APIs que el agente puede invocar**, normalmente ejecutadas por AWS Lambda y descritas con un esquema OpenAPI?

- A. Knowledge Base
- B. Guardrail
- C. Action group
- D. Provisioned Throughput

**35.** 🆕 Un equipo ha construido agentes con un framework open-source (LangGraph) y quiere ejecutarlos en producción con **runtime serverless, memoria, identidad y observabilidad gestionadas**. ¿Qué servicio debe usar?

- A. Amazon Lex
- B. Amazon Bedrock AgentCore
- C. Amazon SageMaker Canvas
- D. Amazon Kendra

**36.** 🆕 ¿Qué es **Strands Agents**?

- A. Un IDE agéntico de AWS
- B. Un servicio de modernización de mainframes
- C. Un SDK open source de AWS para construir agentes "model-driven" con poco código
- D. Un vector store gestionado

**37.** 🆕 Un equipo de desarrollo quiere un IDE que, antes de generar código, convierta la petición en **requisitos, diseño y lista de tareas** (desarrollo guiado por especificaciones). ¿Qué herramienta encaja?

- A. Kiro
- B. Amazon Q Business
- C. AWS CodeCommit
- D. Amazon SageMaker Canvas

**38.** 🆕 Una aseguradora quiere modernizar aplicaciones **COBOL de mainframe** y migrar aplicaciones **.NET** de Windows a Linux con ayuda de agentes de IA. ¿Qué servicio debe usar?

- A. Amazon Textract
- B. Amazon Translate
- C. AWS Glue
- D. AWS Transform

**39.** Un chatbot público construido con Bedrock no debe mostrar **números de tarjeta de crédito** en sus respuestas. ¿Qué solución es la más sencilla?

- A. Fine-tuning con ejemplos de enmascarado
- B. Un filtro de información sensible (PII) de Amazon Bedrock Guardrails con acción MASK
- C. Amazon Macie sobre las respuestas
- D. Una política IAM que deniegue `bedrock:InvokeModel`

**40.** 🆕 El equipo necesita **versionar** los prompts de producción, compararlos entre modelos y **volver a una versión anterior** si la calidad empeora. ¿Qué debe usar?

- A. AWS CloudTrail
- B. Amazon S3 Lifecycle
- C. Amazon Bedrock Prompt Management
- D. Amazon CloudWatch Logs Insights

**41.** Una empresa necesita extraer importes, fechas y tablas de **facturas escaneadas**. ¿Qué servicio debe usar?

- A. Amazon Textract
- B. Amazon Rekognition
- C. Amazon Comprehend
- D. Amazon Polly

**42.** Una empresa quiere analizar el **sentimiento de llamadas grabadas** del centro de contacto. ¿Qué combinación de servicios es la adecuada?

- A. Amazon Polly → Amazon Comprehend
- B. Amazon Rekognition → Amazon Lex
- C. Amazon Translate → Amazon Polly
- D. Amazon Transcribe → Amazon Comprehend

**43.** Los empleados quieren hacer preguntas sobre documentos de RR. HH. guardados en SharePoint. Cada empleado solo debe ver lo que ya tiene permiso para ver, y la empresa quiere una solución **lista para usar**. ¿Qué servicio debe usar?

- A. Amazon Q Developer
- B. Amazon Q Business
- C. Amazon Lex
- D. Amazon Personalize

**44.** 🆕 Los analistas de negocio quieren hacer **preguntas en lenguaje natural** sobre sus dashboards, generar investigaciones con fuentes citadas y crear **automatizaciones sin código**. ¿Qué servicio encaja mejor?

- A. Amazon EMR
- B. AWS Glue DataBrew
- C. Amazon Quick (Quick Sight, Quick Research, Quick Flows)
- D. Amazon Athena

**45.** Una empresa quiere comparar tres FMs según si sus respuestas respetan el **tono de la marca**, con la valoración de su propio equipo. ¿Qué debe usar?

- A. Amazon Bedrock Model Evaluation con trabajadores humanos
- B. Amazon CloudWatch
- C. SageMaker Clarify (sesgo pre-entrenamiento)
- D. AWS Trusted Advisor

**46.** 🆕 Un equipo necesita evaluar la **corrección y completitud** de miles de respuestas de un FM a escala, sin revisores humanos y con explicaciones. ¿Qué método es el adecuado?

- A. Solo la métrica BLEU
- B. RMSE
- C. Revisión manual de todas las respuestas
- D. LLM-as-a-judge en Amazon Bedrock Model Evaluation

**47.** 🆕 ¿Qué métrica muestra mejor si un asistente de soporte aporta **valor de negocio**?

- A. Perplexity
- B. Tasa de tareas completadas sin escalar a un humano
- C. Número de parámetros del modelo
- D. Dimensión de los embeddings

## Dominio 4 — IA Responsable

**48.** Antes de entrenar un modelo de contratación, un equipo quiere comprobar si el dataset está **desbalanceado por género**. ¿Qué servicio debe usar?

- A. Amazon SageMaker Model Monitor
- B. AWS CloudTrail
- C. Amazon SageMaker Clarify
- D. Amazon Bedrock Guardrails

**49.** Un modelo en producción empieza a recibir datos con una distribución distinta a la del entrenamiento. ¿Qué servicio detecta este **drift** y emite alertas?

- A. Amazon SageMaker Model Monitor
- B. Amazon SageMaker Ground Truth
- C. AWS Artifact
- D. Amazon Macie

**50.** ¿Qué herramienta documenta de forma estandarizada el **uso previsto, el nivel de riesgo y las métricas** de un modelo?

- A. AWS Config
- B. Amazon SageMaker Feature Store
- C. AWS Artifact
- D. Amazon SageMaker Model Cards

**51.** Cuando Amazon Textract extrae datos con **baja confianza**, una persona debe revisarlos antes de continuar. ¿Qué servicio implementa este flujo?

- A. Amazon Comprehend
- B. Amazon Augmented AI (A2I)
- C. Amazon Bedrock Model Evaluation
- D. AWS Step Functions sin revisión

**52.** Una aseguradora debe explicar a cada cliente **qué factores influyeron** en el precio calculado por su modelo. ¿Qué técnica es la adecuada?

- A. Valores SHAP con SageMaker Clarify
- B. Aumentar la temperatura
- C. Cifrado con KMS
- D. Batch Transform

**53.** 🆕 Elige **DOS** herramientas de AWS que la guía cita para la **explicabilidad y transparencia** de soluciones de IA.

- A. AWS Shield
- B. Amazon SageMaker Clarify
- C. Amazon Bedrock Model Evaluations
- D. Amazon Route 53
- E. AWS Snowball

**54.** Un cliente pregunta si los prompts enviados a Amazon Bedrock se usan para **entrenar los modelos base**. ¿Qué respuesta es correcta?

- A. Sí, salvo que lo desactives en cada petición.
- B. Solo en los modelos de Amazon.
- C. No: no se usan para entrenar los modelos base ni se comparten con los proveedores.
- D. Solo si usas Provisioned Throughput.

**55.** Un modelo de reconocimiento de voz funciona mal con personas mayores porque el dataset tenía muy pocas grabaciones de ese grupo. ¿Qué problema es y cómo se corrige?

- A. Overfitting; reducir los epochs
- B. Sesgo de muestreo; ampliar el dataset para que sea representativo
- C. Alucinación; bajar la temperatura
- D. Latencia; usar Provisioned Throughput

**56.** ¿Qué afirmación describe el **compromiso entre interpretabilidad y desempeño**?

- A. Los modelos simples siempre son más precisos.
- B. El deep learning es totalmente interpretable.
- C. Los modelos más complejos suelen ser más precisos pero menos interpretables.
- D. La interpretabilidad no importa en sectores regulados.

## Dominio 5 — Seguridad, Cumplimiento y Gobernanza

**57.** Al usar Amazon Bedrock, ¿cuál de estas tareas es responsabilidad **del cliente**?

- A. Parchear los servidores de inferencia
- B. Configurar los permisos IAM sobre quién puede invocar cada modelo
- C. Mantener la seguridad física de los centros de datos
- D. Aislar los modelos de los proveedores

**58.** Una aplicación en subredes privadas **sin acceso a Internet** debe invocar Bedrock. ¿Qué solución es la adecuada?

- A. Interface VPC endpoint (AWS PrivateLink) para `bedrock-runtime`
- B. Internet Gateway
- C. Gateway endpoint de Amazon S3
- D. AWS Direct Connect

**59.** El equipo de auditoría necesita saber **qué identidad** invocó un modelo de Bedrock, cuándo y desde qué IP. ¿Qué servicio lo registra?

- A. Amazon CloudWatch Metrics
- B. AWS Config
- C. AWS CloudTrail
- D. Amazon Inspector

**60.** Por cumplimiento normativo, hay que conservar el **texto de los prompts y de las respuestas** del modelo. ¿Qué se debe habilitar?

- A. AWS CloudTrail
- B. Amazon Bedrock Model Invocation Logging
- C. AWS Trusted Advisor
- D. VPC Flow Logs

**61.** Hay que clasificar **5 millones de documentos históricos** con un FM durante el próximo mes, sin requisito de tiempo real y al **menor costo**. ¿Qué opción es la adecuada?

- A. On-Demand
- B. Provisioned Throughput con compromiso de 6 meses
- C. Cross-region inference
- D. Batch inference

**62.** Una empresa necesita **rendimiento garantizado y sin throttling** para un modelo ajustado (fine-tuned) en Bedrock con tráfico alto y estable. ¿Qué opción debe contratar?

- A. Provisioned Throughput
- B. On-Demand
- C. Batch inference
- D. Prompt caching

**63.** 🆕 Un agente de atención al cliente puede emitir reembolsos. La empresa debe garantizar que el agente **nunca** pueda ejecutar reembolsos superiores a 500 USD, **aunque sufra un ataque de prompt injection**. ¿Qué solución es la adecuada?

- A. Añadir la regla al system prompt del agente
- B. Aumentar la temperatura
- C. Policy in AgentCore con políticas deterministas (Cedar) aplicadas a las llamadas a herramientas en AgentCore Gateway
- D. Una alarma de CloudWatch

**64.** 🆕 Un agente debe acceder al calendario y al CRM del usuario **en su nombre** mediante OAuth, sin guardar secretos en el código. ¿Qué servicio gestiona estas credenciales?

- A. Amazon Bedrock AgentCore Identity
- B. Amazon Inspector
- C. Un bucket S3 con las claves
- D. AWS Shield

**65.** 🆕 Elige **DOS** técnicas para **detectar alucinaciones** en una aplicación RAG.

- A. El *contextual grounding check* de Amazon Bedrock Guardrails
- B. Aumentar la temperatura
- C. Validar la salida contra un esquema JSON y reglas de negocio
- D. Desactivar el logging
- E. Eliminar las citas de las respuestas

---

## Clave de respuestas

<details>
<summary>▶ Mostrar clave (corrige solo al terminar)</summary>

| # | Resp. | Dom. | Justificación breve |
|---|---|---|---|
| 1 | C | D1 | Sin etiquetas + agrupar = clustering. |
| 2 | A | D1 🆕 | Agente = FM que planifica, usa herramientas y actúa hacia un objetivo. |
| 3 | D | D1 | El learning rate se fija antes de entrenar; los pesos son parámetros. |
| 4 | C | D1 | El falso negativo es caro → recall. |
| 5 | A | D1 | El falso positivo es caro → precisión. |
| 6 | B | D1 🆕 | Decisión regulada sobre datos tabulares que debe explicarse → ML tradicional + Clarify (1.2.6). |
| 7 | C | D1 | RMSE eleva al cuadrado los errores y penaliza los grandes. |
| 8 | D | D1 | Overfitting → regularización y más datos. |
| 9 | A | D1 | Etiquetado humano + automático → Ground Truth. |
| 10 | B | D1 | Tráfico intermitente, escala a cero, tolera cold starts → Serverless Inference. |
| 11 | C | D1 | Payloads grandes, procesos largos, cola → Asynchronous Inference. |
| 12 | D | D1 | CI/CD de ML → SageMaker Pipelines. |
| 13 | B | D1 | Información del objetivo filtrada a las features → data leakage. |
| 14 | C | D2 | Más creatividad → temperatura alta. |
| 15 | A | D2 | Se supera la ventana de contexto → resumir o recortar el historial (context engineering). |
| 16 | D | D2 🆕 | Menos tokens de entrada con RAG → menos costo (2.1.4). |
| 17 | B | D2 🆕 | Se pagan entrada y salida; la salida es más cara. |
| 18 | C | D2 🆕 | Definición de context engineering (2.1.5). |
| 19 | A | D2 🆕 | MCP = protocolo abierto agente ↔ herramientas/datos (2.1.6). |
| 20 | B | D2 🆕 | Coordinador que delega en especialistas → patrón supervisor. |
| 21 | C | D2 🆕 | Recordar entre sesiones → memoria a largo plazo. |
| 22 | A | D2 | Datos cambiantes sin re-entrenar → RAG. |
| 23 | D | D2 | El fine-tuning con instrucciones necesita pares etiquetados. |
| 24 | A | D2 | Definición de alucinación. |
| 25 | B | D2 | La búsqueda semántica compara embeddings. |
| 26 | C | D2 | Resumen → ROUGE (BLEU es para traducción). |
| 27 | A | D2 | Los modelos de difusión eliminan ruido iterativamente. |
| 28 | D | D2 | Formato sin entrenar → few-shot prompting. |
| 29 | A, C | D2 | No determinismo y alucinaciones; las demás opciones son falsas. |
| 30 | C | D3 | Serverless, varios proveedores, menor esfuerzo → Bedrock. |
| 31 | A | D3 | Control de la instancia y del entrenamiento → JumpStart. |
| 32 | D | D3 | *Quick create* usa OpenSearch Serverless. MemoryDB salió del alcance en la v1.1. |
| 33 | A | D3 🆕 | Aurora (añadido en la v1.1) admite vectores con pgvector y es un vector store soportado por las KB. |
| 34 | C | D3 | Action groups = APIs (OpenAPI) + Lambda. |
| 35 | B | D3 🆕 | Cualquier framework + runtime/memoria/identidad/observabilidad gestionados → AgentCore. |
| 36 | C | D3 🆕 | Strands Agents = SDK open source model-driven. |
| 37 | A | D3 🆕 | Kiro = IDE agéntico spec-driven. |
| 38 | D | D3 🆕 | Modernización de mainframe/.NET con agentes → AWS Transform. |
| 39 | B | D3 | Filtro de información sensible de Guardrails con MASK. |
| 40 | C | D3 🆕 | Versionado y rollback de prompts → Prompt Management (3.2.5). |
| 41 | A | D3 | Formularios y tablas en documentos → Textract. |
| 42 | D | D3 | Voz → texto (Transcribe) → sentimiento (Comprehend). |
| 43 | B | D3 | Datos corporativos + permisos + listo para usar → Q Business. |
| 44 | C | D3 🆕 | BI en lenguaje natural, investigación y automatización → Amazon Quick. |
| 45 | A | D3 | Criterios subjetivos (tono) → evaluación humana. |
| 46 | D | D3 🆕 | Evaluación a escala con explicaciones → LLM-as-a-judge (3.4.2). |
| 47 | B | D3 🆕 | Métrica de negocio → tasa de tareas completadas (3.4.5). |
| 48 | C | D4 | Sesgo pre-entrenamiento → Clarify. |
| 49 | A | D4 | Drift en producción → Model Monitor. |
| 50 | D | D4 | Documentación del modelo → Model Cards. |
| 51 | B | D4 | Revisión humana por baja confianza → A2I. |
| 52 | A | D4 | Explicación por predicción → SHAP (Clarify). |
| 53 | B, C | D4 🆕 | La guía cita Clarify y Bedrock Model Evaluations (4.2.2). |
| 54 | C | D4 | Bedrock no usa tus datos para entrenar modelos base. |
| 55 | B | D4 | Grupo infrarrepresentado → sesgo de muestreo → datos representativos. |
| 56 | C | D4 | Más complejidad suele implicar menos interpretabilidad. |
| 57 | B | D5 | IAM, datos y configuración son siempre responsabilidad del cliente. |
| 58 | A | D5 | Acceso privado → PrivateLink. |
| 59 | C | D5 | Quién/cuándo/desde dónde → CloudTrail. |
| 60 | B | D5 | Contenido de prompts y respuestas → Model Invocation Logging. |
| 61 | D | D5 | Masivo, no urgente, barato → Batch inference. |
| 62 | A | D5 | Rendimiento garantizado / modelo personalizado → Provisioned Throughput. |
| 63 | C | D5 🆕 | La autorización determinista fuera del LLM no se puede saltar con prompt injection (5.1.1). |
| 64 | A | D5 🆕 | Credenciales OAuth del agente → AgentCore Identity. |
| 65 | A, C | D5 🆕 | Grounding check + validación de la salida (5.1.5). |

</details>

## Calcula tu resultado

| Dominio | Preguntas | Aciertos | % |
|---|---|---|---|
| D1 | 1–13 (13) | | |
| D2 | 14–29 (16) | | |
| D3 | 30–47 (18) | | |
| D4 | 48–56 (9) | | |
| D5 | 57–65 (9) | | |
| **Total** | **65** | | |

- **≥ 56 (85 %)**: buen nivel. Pasa a los simulacros de terceros.
- **46–55 (70–84 %)**: repasa los dominios con menor porcentaje y vuelve a la [matriz de decisión](../cheatsheets/exam-decision-matrix.md).
- **< 46**: vuelve al [plan de reintento](../guides/retake-plan.md) desde la semana del dominio más bajo.
