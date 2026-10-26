# Pares que se Confunden — El Origen de la Mayoría de los Fallos

> Las preguntas de D1, D3, D4 y D5 rara vez preguntan "¿qué es X?". Preguntan **"¿X o Y?"** con dos opciones casi correctas. Esta hoja enfrenta los pares que más se confunden y da **la pista que decide** cada uno.
>
> **Cómo estudiarla:** tapa la columna "Pista decisiva" y explica la diferencia en voz alta. Si dudas, ese par va a tu lista de repaso.

## 1. Dominio 3 — Servicios de IA y FMs (28 %)

| Par | Elige el primero cuando… | Elige el segundo cuando… | Pista decisiva |
|---|---|---|---|
| **Bedrock** vs. **SageMaker JumpStart** | Serverless, varios FMs, mínimo esfuerzo, pago por token | Control de instancia, red o contenedor, modelo open-source concreto, personalización profunda | "*sin gestionar infraestructura*" → Bedrock |
| **Bedrock Agents** vs. **Bedrock AgentCore** | Agente gestionado y configurable desde Bedrock (instrucciones + action groups + KB) | Agentes de **cualquier framework** (Strands, LangGraph…) en producción con runtime, memoria, identidad y observabilidad gestionados | "*framework open-source*" o "*a escala en producción*" → AgentCore |
| **Bedrock Agents** vs. **Bedrock Flows** | El modelo decide los pasos (razonamiento autónomo) | Flujo **predefinido y determinista** que encadena prompts, KB y Lambda | "*pasos fijos y predecibles*" → Flows |
| **Knowledge Bases** vs. **Fine-tuning** | Conocimiento privado o **cambiante**, citas | **Estilo, formato o tarea** con ejemplos etiquetados | "*se actualiza cada semana*" → KB |
| **Fine-tuning** vs. **Continued pre-training** | Pares prompt–respuesta **etiquetados** | Mucho texto de dominio **sin etiquetar** | "*sin etiquetar*" → continued pre-training |
| **Fine-tuning** vs. **Distillation** | Enseñar una tarea nueva al modelo | Hacer un modelo **más pequeño y barato** que imite a uno grande | "*reducir costo y latencia manteniendo calidad*" → distillation |
| **Comprehend** vs. **Textract** | Analizar el **significado** del texto (sentimiento, entidades, PII) | **Extraer** texto, formularios y tablas de documentos escaneados | "*PDF escaneado / formulario / factura*" → Textract |
| **Textract** vs. **Rekognition** | Documentos (texto estructurado) | Fotos y video (objetos, rostros, moderación) | "*imagen de una escena*" → Rekognition |
| **Transcribe** vs. **Polly** | Voz → texto | Texto → voz | Fíjate en la dirección de la flecha |
| **Lex** vs. **Q Business** | Chatbot de **intents y slots** (reservas, IVR, Connect) | Preguntas **abiertas** sobre documentos internos respetando permisos | "*respetando los permisos de SharePoint*" → Q Business |
| **Q Business** vs. **Bedrock + KB** | Asistente **listo para usar** para empleados | Aplicación **a medida** (p. ej., para clientes) con control total | "*menor esfuerzo para empleados*" → Q Business |
| **Q Business** vs. **Q Developer** | Empleados de cualquier área sobre datos corporativos | Desarrolladores (código, consola, CLI) | ¿Quién es el usuario? |
| **Q Developer** vs. **Kiro** | Asistente de código en tu IDE actual y en la consola de AWS | IDE agéntico **spec-driven** (requisitos → diseño → tareas) | "*especificaciones antes del código*" → Kiro |
| **Kiro** vs. **Strands Agents** | Herramienta para **escribir software** | SDK para **construir agentes** | ¿Se construye software o un agente? |
| **AWS Transform** vs. **Q Developer** | Migración y modernización **a gran escala** con agentes (mainframe, .NET, VMware) | Ayuda de código en el día a día | "*mainframe / VMware / portafolio de aplicaciones*" → Transform |
| **Amazon Quick** vs. **Q Business** | BI, dashboards, investigación y automatización para analistas | Asistente conversacional sobre documentos de la empresa | "*dashboards / métricas*" → Quick |
| **Kendra** vs. **Knowledge Bases** | **Búsqueda** empresarial (devuelve documentos o pasajes) | RAG que **genera** la respuesta con un FM | "*generar respuesta*" → KB |
| **Guardrails** vs. **Prompt engineering** | Política **aplicada y medible** sobre entrada y salida, para cualquier modelo | Instrucciones en el prompt (se pueden saltar) | "*garantizar / bloquear siempre*" → Guardrails |
| **Prompt Management** vs. **Flows** | Versionar y reutilizar **prompts** | Orquestar **pasos** | "*versión / rollback*" → Prompt Management |
| **Model Evaluation automática** vs. **humana** | Métricas objetivas a escala (exactitud, robustez, toxicidad) | Criterios subjetivos (tono de marca, utilidad) | "*tono / estilo / percepción*" → humana |
| **LLM-as-a-judge** vs. **ROUGE/BLEU** | Calidad semántica a escala (corrección, completitud) con explicaciones | Solapamiento con un texto de referencia | "*sin texto de referencia*" → LLM-as-a-judge |

## 2. Dominio 1 — Fundamentos de ML (20 %)

| Par | Primero | Segundo | Pista decisiva |
|---|---|---|---|
| **Precisión** vs. **Recall** | El **falso positivo** es caro (spam, alarmas que cuestan dinero) | El **falso negativo** es caro (cáncer, fraude, intrusiones) | Pregúntate qué error duele más |
| **Accuracy** vs. **F1** | Clases balanceadas | Clases **desbalanceadas** | "*0,5 % de casos positivos*" → F1 |
| **RMSE** vs. **MAE** | Penalizar errores **grandes** | Robustez frente a outliers, fácil de explicar | "*errores grandes muy costosos*" → RMSE |
| **Clasificación** vs. **Regresión** | Salida **categórica** (sí/no, clase) | Salida **numérica** continua | ¿Categoría o número? |
| **Supervisado** vs. **No supervisado** | Hay **etiquetas** | **No** hay etiquetas (agrupar, anomalías) | "*sin etiquetas*" → no supervisado |
| **Overfitting** vs. **Underfitting** | Train ≫ validación | Ambos bajos | Compara las dos cifras |
| **Parámetro** vs. **Hiperparámetro** | Aprendido (pesos) | Fijado antes (learning rate, epochs) | ¿Lo aprende el modelo? |
| **Canvas** vs. **Autopilot** | Analistas **sin código** | AutoML con **visibilidad** para equipos técnicos | "*analistas de negocio*" → Canvas |
| **Ground Truth** vs. **A2I** | Etiquetar datos **para entrenar** | Revisión humana de **predicciones en producción** | ¿Antes o después de entrenar? |
| **Data Wrangler** vs. **Feature Store** | **Preparar** datos | **Almacenar y compartir** features | ¿Transformar o reutilizar? |
| **Model Registry** vs. **Model Cards** | **Versionar y aprobar** modelos para desplegar | **Documentar** el uso previsto y los riesgos | "*aprobación del despliegue*" → Registry |
| **Serverless** vs. **Asynchronous** inference | Tráfico **intermitente**, payload pequeño | Payload **grande**, procesos **largos**, cola | "*1 GB / 1 hora*" → Async |
| **Asynchronous** vs. **Batch Transform** | Peticiones individuales encoladas cerca del tiempo real | Dataset **completo** offline, sin endpoint | "*todo el dataset de una vez*" → Batch Transform |
| **ML tradicional** vs. **FM** 🆕 | Tabular, regulado, explicable, barato | Lenguaje, generación, datos no estructurados | "*explicar cada decisión al regulador*" → ML tradicional |

## 3. Dominio 4 — IA responsable (14 %)

| Par | Primero | Segundo | Pista decisiva |
|---|---|---|---|
| **Clarify** vs. **Model Monitor** | Sesgo y explicabilidad (antes y después de entrenar) | **Drift** en producción a lo largo del tiempo | "*con el tiempo / en producción*" → Model Monitor |
| **Clarify** vs. **Guardrails** | Modelos de **ML** (sesgo, SHAP) | Contenido de **FMs** (toxicidad, temas, PII) | ¿ML clásico o GenAI? |
| **Model Cards** vs. **AI Service Cards** | Documentan **tus** modelos | Documentación de **AWS** sobre **sus** servicios de IA | ¿De quién es el modelo? |
| **Explicabilidad** vs. **Transparencia** | Explicar **una salida concreta** (SHAP) | Comunicar **cómo** se construyó el sistema y sus límites | "*por qué esta predicción*" → explicabilidad |
| **Interpretabilidad** vs. **Explicabilidad** | Entender el **funcionamiento interno** (árbol, regresión) | Explicar salidas de una caja negra | "*modelo intrínsecamente comprensible*" → interpretabilidad |
| **Sesgo de muestreo** vs. **sesgo histórico** | El dataset **no representa** a la población | Los datos reflejan **desigualdades pasadas** | "*pocos datos de un grupo*" → muestreo |
| **A2I** vs. **Ground Truth** | Revisión humana de predicciones | Etiquetado de datos de entrenamiento | Ver D1 |

## 4. Dominio 5 — Seguridad, cumplimiento y gobernanza (14 %)

| Par | Primero | Segundo | Pista decisiva |
|---|---|---|---|
| **CloudTrail** vs. **Model Invocation Logging** | **Quién, cuándo y desde dónde** se llamó a la API | **Contenido** de prompts y respuestas | "*texto del prompt*" → invocation logging |
| **CloudTrail** vs. **CloudWatch** | Auditoría de **acciones** | **Métricas**, logs y **alarmas** operativas | "*alertar si sube la latencia*" → CloudWatch |
| **CloudTrail** vs. **AWS Config** | Llamadas a la API | **Configuración** de recursos y cumplimiento de reglas | "*¿el recurso cumple la regla?*" → Config |
| **Macie** vs. **Inspector** vs. **GuardDuty** | Macie: **PII** en S3 | Inspector: **vulnerabilidades** en EC2, contenedores y Lambda · GuardDuty: **amenazas** y actividad sospechosa en la cuenta | Datos / software / comportamiento |
| **Artifact** vs. **Audit Manager** | Descargar los informes de cumplimiento **de AWS** | Recopilar **tu** evidencia para auditorías | ¿De quién es el informe? |
| **IAM policy** vs. **SCP** | Permisos de una identidad en **una cuenta** | **Límite máximo** para **todas** las cuentas de la organización | "*ninguna cuenta de la organización*" → SCP |
| **IAM** vs. **Guardrails** | Quién puede **invocar** qué modelo | Qué **contenido** puede entrar o salir | ¿Acceso o contenido? |
| **VPC endpoint** vs. **Direct Connect** | Acceso privado **desde la VPC** a Bedrock | Enlace privado **desde on-premises** a AWS | "*subred privada sin Internet*" → VPC endpoint |
| **On-Demand** vs. **Provisioned Throughput** | Tráfico variable, sin compromiso | Throughput **garantizado**, tráfico alto y estable, modelo personalizado | "*garantizado / sin throttling*" → PT |
| **On-Demand** vs. **Batch** | Tiempo real | Masivo, **no urgente**, ≈ 50 % más barato | "*no requiere tiempo real*" → Batch |
| **KMS AWS managed key** vs. **customer managed key** | Cifrado sin gestionar nada | **Control** de la política, rotación y revocación | "*control / auditar el uso de la clave*" → CMK |
| **AgentCore Identity** vs. **Policy** 🆕 | **Quién** invoca al agente y **qué credenciales** usa el agente | **Qué acciones** puede ejecutar el agente (Cedar, determinista) | "*nunca permitir la acción X*" → Policy |
| **Responsabilidad de AWS** vs. **del cliente** | Infraestructura, operación del servicio, aislamiento de modelos | IAM, datos, cifrado, red, logging, guardrails, uso responsable | En servicios gestionados, los **datos y la configuración** son siempre del cliente |

## 5. Dominio 2 — Para mantener tu fortaleza (24 %)

| Par | Primero | Segundo | Pista decisiva |
|---|---|---|---|
| **Temperatura baja** vs. **alta** | Factual, consistente | Creativo, variado | "*extracción / clasificación*" → baja |
| **Top-P** vs. **Top-K** | Umbral de probabilidad **acumulada** | Número **fijo** de candidatos | ¿Porcentaje o cantidad? |
| **ROUGE** vs. **BLEU** | Resumen | Traducción | R de "resumen" |
| **Prompt engineering** vs. **Context engineering** 🆕 | Redactar la instrucción | Gestionar **todo** lo que entra en la ventana de contexto | "*memoria, herramientas, datos recuperados*" → context engineering |
| **MCP** vs. **action group** 🆕 | Estándar abierto para conectar agentes con herramientas | Mecanismo propio de Bedrock Agents (OpenAPI + Lambda) | "*estándar abierto / interoperable*" → MCP |
