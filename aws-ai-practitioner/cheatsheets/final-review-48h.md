# Repaso Final 48 h — Lo que tienes que saber sí o sí

> Léelo dos veces: el día anterior y la mañana del examen. **Nada nuevo** en las últimas 48 h.

## 1. Las 12 decisiones que más se preguntan

| Si ves… | Responde |
|---|---|
| Datos privados o cambiantes + citas + sin re-entrenar | **RAG → Bedrock Knowledge Bases** |
| Estilo/formato/tarea + datos etiquetados | **Fine-tuning** |
| Dominio especializado + texto sin etiquetar | **Continued pre-training** |
| Lo más barato y rápido para mejorar respuestas | **Prompt engineering** |
| Serverless, varios FMs, mínimo esfuerzo | **Amazon Bedrock** |
| Control de instancias / open-source / personalización profunda | **SageMaker JumpStart** |
| Acciones multi-paso con APIs | **Bedrock Agents** (o **AgentCore** si es cualquier framework y producción a escala) |
| Bloquear temas, toxicidad, PII o alucinaciones | **Bedrock Guardrails** |
| Masivo y no urgente | **Batch inference** |
| Throughput garantizado o modelo fine-tuned | **Provisioned Throughput** |
| Quién llamó a la API / qué decía el prompt | **CloudTrail** / **Model Invocation Logging** |
| Sin Internet | **VPC endpoint (PrivateLink)** |

## 2. Métricas (D1/D2)

```text
Precisión = TP/(TP+FP)  → FP caro (spam)          Recall = TP/(TP+FN) → FN caro (cáncer, fraude)
F1 = equilibrio en clases desbalanceadas          Accuracy → solo con clases balanceadas
RMSE → penaliza errores grandes (regresión)       MAE → robusta a outliers
ROUGE → resumen    BLEU → traducción    BERTScore → similitud semántica    LLM-as-a-judge → a escala
```

## 3. SageMaker: una línea por servicio

| Servicio | Para |
|---|---|
| Ground Truth | Etiquetar datos |
| Data Wrangler | Preparar datos |
| Feature Store | Guardar y reutilizar features |
| Canvas | ML sin código |
| Autopilot | AutoML |
| JumpStart | Hub de modelos pre-entrenados |
| Pipelines | CI/CD de ML |
| Model Registry | Versionar y aprobar modelos |
| Clarify | Sesgo + explicabilidad (SHAP) |
| Model Monitor | Drift en producción |
| Model Cards | Documentar el modelo |
| Serverless / Async / Batch Transform / Real-time | Intermitente / grande y lento / offline / baja latencia |

## 4. Servicios de IA aplicada

**Comprehend** texto (sentimiento, entidades, PII) · **Textract** documentos (formularios, tablas) · **Rekognition** imágenes y video · **Transcribe** voz→texto · **Polly** texto→voz · **Translate** traducción · **Lex** chatbots con intents · **Kendra** búsqueda empresarial · **Personalize** recomendaciones · **A2I** revisión humana · **Q Business** asistente de empresa con permisos · **Q Developer** asistente de código · **Amazon Quick** BI, investigación y automatización con IA.

## 5. Temas nuevos de la v1.1 (no los olvides)

| Concepto | En una línea |
|---|---|
| IA agéntica | FM que planifica, usa herramientas y actúa hacia un objetivo |
| MCP | Protocolo abierto agente ↔ herramientas/datos |
| Context engineering | Qué entra en el contexto: instrucciones, ejemplos, herramientas, memoria, RAG |
| Precio por tokens | Entrada + salida; la salida es más cara; menos tokens = menos costo y latencia |
| ML tradicional vs. FM | Tabular + regulado + explicable → ML tradicional |
| AgentCore | Operar agentes de cualquier framework en producción (Runtime, Memory, Gateway, Identity, Policy, Observability…) |
| AgentCore Identity / Policy | Credenciales OAuth del agente / autorización determinista (Cedar) fuera del LLM |
| Strands Agents | SDK open source de agentes model-driven |
| Kiro | IDE agéntico spec-driven |
| AWS Transform | Modernización con agentes (mainframe, .NET, VMware) |
| Prompt Management | Versionar prompts y hacer rollback |
| Métricas de negocio | Tareas completadas, satisfacción, costo por interacción |
| Alucinaciones | Grounding RAG + contextual grounding check + validación de la salida + confianza + A2I |

## 6. IA responsable y seguridad

- **Bedrock no usa tus datos** para entrenar modelos base ni los comparte con los proveedores.
- **El cliente es responsable de:** IAM, datos, cifrado (KMS), red, logging y guardrails. **AWS es responsable de:** infraestructura y operación del servicio.
- **Scoping Matrix:** 1 consumo · 2 empresarial · 3 pre-entrenado · 4 fine-tuned · 5 entrenado por ti.
- **Macie** = PII en S3 · **Artifact** = informes de cumplimiento de AWS · **SCP** = límite para toda la organización · **`bedrock:GuardrailIdentifier`** = forzar un guardrail.

## 7. En el examen

1. Lee la **última frase** primero y busca la **restricción**.
2. Descarta lo que no cumple el requisito, lo que viola la restricción y lo que sobra.
3. Entre dos opciones válidas: la **más gestionada y específica**.
4. Marca y avanza si dudas más de 90 segundos. **Nunca dejes nada en blanco.**
