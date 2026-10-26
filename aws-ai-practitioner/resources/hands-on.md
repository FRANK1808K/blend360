# Práctica en AWS (Laboratorios y Workshops)

[⬅️ Centro de recursos](README.md)

> El AIF-C01 es un examen **fundamental**: no exige construir soluciones, pero haber **usado** Bedrock, Knowledge Bases y Guardrails al menos una vez hace que las preguntas de escenario sean mucho más fáciles. Usa una cuenta de formación con **AWS Budgets** y alertas de costo.

## 1. Sin código y sin costo de AWS

| Recurso | Qué practicas | Tiempo |
|---|---|---|
| ⭐ [PartyRock](https://partyrock.aws/) | Crear apps de GenAI con prompts, sin código y sin cuenta de AWS. Ideal para entender prompts, temperatura y encadenamiento. | 30 min |
| Playground de Amazon Bedrock (consola) | Comparar modelos y ajustar temperatura, Top-P y longitud. Se paga por token, pero el costo es mínimo. | 30 min |

## 2. Laboratorios guiados

| Recurso | Qué practicas | Costo aprox. |
|---|---|---|
| ⭐ [Lab 01 de este repo — RAG con Bedrock Knowledge Bases](../labs/lab-01-rag-bedrock-knowledge-bases/README.md) | Knowledge Base, S3, OpenSearch Serverless, IAM de mínimo privilegio, citas. | < USD 2 con limpieza |
| ⭐ [aws-samples/amazon-bedrock-workshop](https://github.com/aws-samples/amazon-bedrock-workshop) | Notebooks oficiales: generación de texto, Knowledge Bases y RAG, personalización de modelos, imágenes, agentes. Se ejecuta en **tu** cuenta (pagas los tokens). | Bajo |
| [Workshop "Building with Generative AI Apps on AWS"](https://catalog.workshops.aws/building-gen-ai-apps/en-US) | PartyRock (sin código) y Bedrock (low-code). | Bajo |
| AWS Builder Labs y Escape Room (Skill Builder) | Laboratorios en entornos temporales de AWS, sin usar tu cuenta. | 💲 suscripción |

## 3. Temas nuevos de la v1.1 (opcional, para entenderlos mejor)

| Recurso | Qué practicas |
|---|---|
| [Strands Agents](https://strandsagents.com/) | Crear un agente con modelo + system prompt + herramientas en pocas líneas de Python. |
| [Kiro](https://kiro.dev/) | Ver en la práctica el desarrollo *spec-driven* (requisitos → diseño → tareas), *steering* y *hooks*. |
| Amazon Bedrock Prompt Management (consola) | Crear un prompt con variables, generar versiones y compararlas. |
| Amazon Bedrock Guardrails (consola) | Probar content filters, denied topics, filtros PII y contextual grounding check. |

## 4. Mini-retos de 15 minutos (consola)

1. En el playground, pide la misma respuesta con temperatura 0 y 1 cinco veces. ¿Qué cambia?
2. Crea un guardrail con el tema prohibido "asesoría de inversión" y pruébalo con `ApplyGuardrail` desde la consola.
3. Crea una Knowledge Base con *Quick create* y pregunta algo que no esté en los documentos. ¿Alucina?
4. En Prompt Management, crea dos versiones de un prompt de resumen y compáralas.
5. Revisa en CloudWatch las métricas `InputTokenCount` y `OutputTokenCount` de tus pruebas y calcula su costo.

> ⚠️ Al terminar, **borra** Knowledge Bases, colecciones de OpenSearch Serverless y cualquier endpoint de SageMaker: generan cargos por hora.
