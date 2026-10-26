# Laboratorios Prácticos

Laboratorios guiados para consolidar los conceptos del examen con práctica real en AWS. Cada laboratorio sigue la [plantilla estándar](template.md): objetivos, arquitectura, IAM mínimo viable, pasos, validación, troubleshooting, costos y limpieza.

| Lab | Título | Dominios | Nivel | Duración | Costo aprox.* |
|---|---|---|---|---|---|
| [01](lab-01-rag-bedrock-knowledge-bases/README.md) | Pipeline RAG con Bedrock Knowledge Bases, S3 y OpenSearch Serverless | D2, D3, D5 | Intermedio | 60–90 min | < USD 2 |
| 02 *(planificado)* | Bedrock Guardrails: content filters, denied topics, PII y grounding | D3, D4 | Básico | 45 min | < USD 1 |
| 03 *(planificado)* | Bedrock Agent con action group en Lambda y OpenAPI | D3 | Intermedio | 90 min | < USD 2 |
| 04 *(planificado)* | Detección de sesgo y explicabilidad con SageMaker Clarify | D1, D4 | Intermedio | 90 min | < USD 3 |
| 05 *(planificado)* | Invocación privada de Bedrock con PrivateLink, CloudTrail e invocation logging | D5 | Intermedio | 60 min | < USD 2 |

\* Siempre que se ejecute la limpieza al terminar. Verifica los precios en la [AWS Pricing Calculator](https://calculator.aws/).

## Reglas de seguridad para los laboratorios

1. Usa una **cuenta de AWS dedicada a formación** (idealmente bajo AWS Organizations con un presupuesto de AWS Budgets y alertas).
2. **Nunca** subas credenciales, IDs de cuenta reales ni archivos `build/` al repositorio (están en `.gitignore`).
3. Ejecuta **siempre** la sección de limpieza: algunos recursos (p. ej., colecciones de OpenSearch Serverless, endpoints de SageMaker) generan cargos por hora aunque no se usen.
4. Revisa cada política IAM antes de aplicarla: los laboratorios usan mínimo privilegio, y conviene que entiendas por qué.
