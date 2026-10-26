# Cheat Sheet — Matriz de Decisión Rápida para el Examen AIF-C01

> **Cómo usarla:** identifica en el enunciado el **requisito clave** y la **restricción** (palabras como *menor esfuerzo operativo*, *más rentable*, *sin salir a Internet*, *sin re-entrenar*, *datos actualizados*). La combinación de ambos casi siempre señala una única respuesta.

## Escenarios frecuentes

Formato: **Si el escenario pide** [requisito] **Y** [restricción] → **la respuesta correcta de AWS es** [servicio/configuración], **PORQUE** [justificación].

| # | Si el escenario pide… | Y la restricción es… | → La respuesta de AWS es… | PORQUE… | Dom. |
|---|---|---|---|---|---|
| 1 | Respuestas de un chatbot basadas en documentación interna | Los documentos cambian con frecuencia y **no se quiere re-entrenar** | **Amazon Bedrock Knowledge Bases (RAG)** | Recupera el contexto en tiempo de consulta; actualizar la fuente solo exige re-sincronizar, no re-entrenar el modelo. | D2/D3 |
| 2 | Que el modelo adopte el **estilo/tono de marca** o una tarea muy específica | Ya existen miles de ejemplos **etiquetados** prompt–respuesta | **Fine-tuning en Bedrock (Custom Models)** | El fine-tuning modifica los pesos para aprender comportamiento y formato; RAG aporta conocimiento, no estilo. | D2/D3 |
| 3 | Que el modelo domine la **terminología** de un sector (legal, médico) | Solo hay grandes volúmenes de texto **sin etiquetar** | **Continued pre-training en Bedrock** | Adapta el modelo al dominio con datos no etiquetados; el fine-tuning requiere pares etiquetados. | D2/D3 |
| 4 | Mejorar el formato de las respuestas de un FM | **Menor costo y esfuerzo**, sin datos de entrenamiento | **Prompt engineering** (few-shot, instrucciones, plantillas) | No requiere entrenamiento ni infraestructura adicional; es la primera palanca a aplicar. | D2 |
| 5 | Usar FMs de varios proveedores para una app GenAI | **Sin gestionar infraestructura** (serverless) | **Amazon Bedrock** | API única y gestionada para FMs de Amazon, Anthropic, Meta, Mistral, etc., con pago por uso. | D3 |
| 6 | Desplegar un FM open-source y personalizarlo a fondo | Se requiere **control del tipo de instancia, red y contenedor** | **Amazon SageMaker JumpStart / SageMaker AI** | Despliega en endpoints de tu cuenta con control total de la infraestructura y del entrenamiento. | D3 |
| 7 | Bloquear contenido dañino, temas prohibidos y enmascarar PII en una app GenAI | Debe aplicarse **de forma consistente a varios modelos** | **Amazon Bedrock Guardrails** (y la API `ApplyGuardrail`) | Políticas centralizadas sobre entrada y salida, independientes del modelo, incluso fuera de Bedrock. | D3/D4 |
| 8 | Detectar alucinaciones en respuestas RAG | De forma **automática** en tiempo de ejecución | **Contextual grounding check de Bedrock Guardrails** | Puntúa si la respuesta está fundamentada en la fuente y es relevante, y bloquea por debajo del umbral. | D2/D4 |
| 9 | Un asistente que ejecute **acciones multi-paso** (consultar API, crear reservas) | Integración con sistemas existentes **sin orquestar a mano** | **Amazon Bedrock Agents** (action groups + Lambda + OpenAPI) | El agente razona, planifica e invoca APIs y Knowledge Bases de forma autónoma. | D3 |
| 10 | Procesar millones de documentos con un FM | **Sin requisito de tiempo real** y al **menor costo** | **Bedrock Batch Inference** | Procesamiento asíncrono desde/hacia S3 con descuento significativo frente a On-Demand. | D5 |
| 11 | Rendimiento **garantizado** para un modelo en producción o servir un modelo **fine-tuned** | Tráfico alto y predecible, sin *throttling* | **Bedrock Provisioned Throughput** | Reserva capacidad dedicada (Model Units) con throughput garantizado. | D5 |
| 12 | Prototipo o carga variable con FMs | **Sin compromiso** de capacidad | **Bedrock On-Demand** | Pago por token, sin costos fijos. | D5 |
| 13 | Invocar Bedrock desde una VPC | El tráfico **no debe salir a Internet** | **Interface VPC Endpoint (AWS PrivateLink)** para `bedrock-runtime` | Conecta en privado sobre la red de AWS; se combina con endpoint policies y `aws:SourceVpce`. | D5 |
| 14 | Saber **quién** invocó un modelo, **cuándo** y desde dónde | Auditoría de llamadas a la API | **AWS CloudTrail** | Registra la identidad, la acción, la hora y el origen de cada llamada a la API de Bedrock. | D5 |
| 15 | Auditar el **contenido** de prompts y respuestas | Retención para cumplimiento | **Bedrock Model Invocation Logging** (S3 / CloudWatch Logs) | CloudTrail no guarda prompts ni respuestas; el invocation logging sí. | D5 |
| 16 | Alertar cuando el consumo de tokens o la latencia se disparen | Monitoreo operativo en tiempo casi real | **Amazon CloudWatch Metrics + Alarms** (`AWS/Bedrock`) | Expone `InputTokenCount`, `OutputTokenCount`, `InvocationLatency`, `InvocationThrottles`, etc. | D5 |
| 17 | Detectar **sesgo** en los datos de entrenamiento y explicar predicciones | Modelo de ML en SageMaker | **Amazon SageMaker Clarify** | Métricas de sesgo pre/post-entrenamiento y explicabilidad con SHAP. | D4 |
| 18 | Detectar degradación o **drift** de un modelo en producción | Monitoreo continuo con alertas | **Amazon SageMaker Model Monitor** | Compara el tráfico con una línea base (calidad de datos, calidad del modelo, sesgo, atribución). | D1/D4 |
| 19 | **Documentar** el uso previsto, riesgos y métricas de un modelo | Transparencia y auditoría | **Amazon SageMaker Model Cards** | Registro estandarizado y versionado de la información de gobernanza del modelo. | D4 |
| 20 | **Revisión humana** de predicciones de baja confianza | Integrado con Textract/Rekognition o modelos propios | **Amazon Augmented AI (A2I)** | Flujos *human-in-the-loop* gestionados con umbrales de confianza. | D4 |
| 21 | Extraer **tablas y formularios** de documentos escaneados | **Sin experiencia en ML** | **Amazon Textract** | Va más allá del OCR: preserva la estructura clave-valor y las tablas. | D3 |
| 22 | Analizar **sentimiento** y entidades en reseñas de clientes | Servicio gestionado, sin entrenar modelos | **Amazon Comprehend** | NLP pre-entrenado vía API (sentimiento, entidades, frases clave, PII). | D3 |
| 23 | Moderar imágenes y videos subidos por usuarios | Escalable y sin construir modelos | **Amazon Rekognition (Content Moderation)** | Detección pre-entrenada de contenido inapropiado con etiquetas y confianza. | D3 |
| 24 | Transcribir llamadas del centro de contacto y **ocultar PII** | Servicio gestionado | **Amazon Transcribe** (redacción de PII / Call Analytics) | Speech-to-text con redacción automática de datos sensibles. | D3 |
| 25 | Convertir artículos en **audio** con voz natural | Control de pronunciación y pausas | **Amazon Polly** (voces neuronales/generativas + SSML) | Text-to-speech gestionado con soporte SSML. | D3 |
| 26 | Chatbot de voz/texto basado en **intents** para un IVR | Integración con Amazon Connect | **Amazon Lex** | Gestiona intents, slots y fulfillment con Lambda; integración nativa con Connect. | D3 |
| 27 | Asistente para empleados sobre datos corporativos (SharePoint, Confluence, S3) | **Respetar los permisos existentes**, mínima construcción | **Amazon Q Business** | Conectores gestionados que heredan las ACL de la fuente; listo para usar. | D3 |
| 28 | Acelerar el desarrollo: generación de código, escaneo de seguridad, actualización de Java | Integrado en el IDE | **Amazon Q Developer** | Asistente de código GenAI con transformación de código y escaneos de seguridad. | D3 |
| 29 | Preguntas en **lenguaje natural** sobre dashboards de BI | Usuarios de negocio sin SQL | **Amazon Q in QuickSight** | BI conversacional sobre los datasets de QuickSight. | D3 |
| 30 | Impedir que cualquier cuenta de la organización use modelos no aprobados | **Control centralizado** multi-cuenta | **SCP de AWS Organizations** (Deny `bedrock:InvokeModel` con `NotResource`) | Las SCP fijan el máximo de permisos en todas las cuentas, incluso para administradores. | D5 |
| 31 | Garantizar que **toda** invocación pase por un guardrail aprobado | Aplicación obligatoria, no opcional | **Política IAM con la condición `bedrock:GuardrailIdentifier`** | Deniega las invocaciones que no incluyan el guardrail especificado. | D5 |
| 32 | Que los datos de los servicios de IA **no se usen** para mejorar los servicios de AWS | Toda la organización | **AI services opt-out policy (AWS Organizations)** | Desactiva centralmente el almacenamiento/uso de contenido para la mejora de los servicios. | D4/D5 |
| 33 | Cifrar datos de entrenamiento, modelos personalizados y logs con control de rotación y revocación | Requisito regulatorio | **AWS KMS con customer managed keys** | Control total de la política de la clave y auditoría de su uso en CloudTrail. | D4/D5 |
| 34 | Detectar **PII** en los buckets S3 usados para entrenamiento o RAG | Descubrimiento automático | **Amazon Macie** | Clasificación de datos sensibles en S3 con ML. | D5 |
| 35 | Descargar informes de cumplimiento (SOC, ISO) de AWS para un auditor | — | **AWS Artifact** | Portal de autoservicio de los informes de cumplimiento de AWS. | D5 |
| 36 | Comparar la calidad de varios FMs para **tu** caso de uso | Con métricas automáticas y evaluación humana | **Amazon Bedrock Model Evaluation** | Evaluaciones automáticas, humanas y LLM-as-a-judge sobre tus propios datasets. | D3 |
| 37 | Construir un modelo de ML **sin escribir código** | Analistas de negocio | **Amazon SageMaker Canvas** | Interfaz visual no-code para preparar datos, entrenar y predecir. | D1 |
| 38 | Etiquetar un gran dataset de imágenes con calidad | Combinar humanos y etiquetado automático | **Amazon SageMaker Ground Truth** | Flujos de etiquetado humano con aprendizaje activo para reducir costos. | D1 |
| 39 | Reducir el costo de un FM grande manteniendo calidad similar | Alto volumen de inferencia | **Bedrock Model Distillation** (o un modelo más pequeño) | Un modelo "estudiante" aprende del "maestro" y es más barato y rápido. | D3/D5 |
| 40 | Residencia de datos estricta en una región | Usando Bedrock | **Invocación en la región requerida sin cross-region inference** (+ SCP con `aws:RequestedRegion`) | Los *inference profiles* pueden procesar en otras regiones de la geografía. | D4/D5 |

## Palabras clave → servicio

| Palabra clave del enunciado | Piensa en… |
|---|---|
| "serverless", "menor esfuerzo operativo", "API para FMs" | Amazon Bedrock |
| "control de instancias", "open-source", "despliegue en mi VPC con mi contenedor" | SageMaker AI / JumpStart |
| "documentos internos", "datos actualizados", "citas", "reducir alucinaciones" | RAG → Bedrock Knowledge Bases |
| "embeddings", "búsqueda semántica", "vector" | Titan Embeddings + OpenSearch Serverless / Aurora pgvector / S3 Vectors |
| "tareas multi-paso", "llamar APIs", "orquestar" | Bedrock Agents |
| "contenido dañino", "temas prohibidos", "PII en respuestas" | Bedrock Guardrails |
| "sesgo", "explicabilidad", "SHAP" | SageMaker Clarify |
| "drift", "degradación en producción" | SageMaker Model Monitor |
| "documentar el modelo" | SageMaker Model Cards |
| "revisión humana" | Amazon A2I |
| "quién llamó a la API" | CloudTrail |
| "contenido de prompts" | Model Invocation Logging |
| "tráfico privado" | VPC Endpoint / PrivateLink |
| "throughput garantizado", "modelo fine-tuned" | Provisioned Throughput |
| "procesamiento masivo, no urgente" | Batch Inference |

## Trampas frecuentes

1. **Accuracy con clases desbalanceadas** → casi nunca es la respuesta; busca F1, recall o precisión.
2. **Fine-tuning para datos que cambian** → incorrecto; es RAG.
3. **CloudTrail para ver prompts** → incorrecto; es Model Invocation Logging.
4. **Comprehend para extraer texto de PDFs escaneados** → incorrecto; primero Textract.
5. **"Bedrock usa mis datos para entrenar"** → falso: no se usan para entrenar modelos base ni se comparten con los proveedores.
6. **Temperatura alta para respuestas factuales** → incorrecto; usa temperatura baja.
7. **SageMaker cuando el enunciado dice "sin gestionar infraestructura"** → suele ser Bedrock o un servicio de IA gestionado.
8. **Provisioned Throughput para cargas esporádicas** → sobrecosto; usa On-Demand.
