# Preguntas de Práctica — Dominio 4: Directrices de IA Responsable

## Pregunta 1 — Opción múltiple

Antes de entrenar un modelo de aprobación de créditos, un equipo quiere comprobar si el dataset está desbalanceado respecto a la edad de los solicitantes. ¿Qué servicio deben usar?

- A. Amazon SageMaker Model Monitor
- B. Amazon SageMaker Clarify
- C. Amazon Bedrock Guardrails
- D. AWS CloudTrail

<details>
<summary>▶ Ver respuesta</summary>

**Respuesta correcta:** B

- **B ✅** Clarify calcula métricas de sesgo **pre-entrenamiento** (p. ej., Class Imbalance) sobre el dataset.
- **A ❌** Model Monitor observa modelos ya desplegados.
- **C ❌** Guardrails filtra entradas/salidas de FMs.
- **D ❌** CloudTrail audita llamadas a APIs.

📚 [Dominio 4 — SageMaker Clarify](../domains/04-responsible-ai/README.md#31-amazon-sagemaker-clarify)
</details>

## Pregunta 2 — Opción múltiple

Un regulador exige documentar, para cada modelo en producción, su uso previsto, nivel de riesgo, datos de entrenamiento y métricas de evaluación. ¿Qué herramienta de AWS está diseñada para esto?

- A. Amazon SageMaker Model Cards
- B. AWS Artifact
- C. Amazon SageMaker Feature Store
- D. AWS Config

<details>
<summary>▶ Ver respuesta</summary>

**Respuesta correcta:** A

- **A ✅** Las Model Cards documentan de forma estandarizada la información de gobernanza de un modelo.
- **B ❌** Artifact proporciona informes de cumplimiento **de AWS**, no de tus modelos.
- **C ❌** Feature Store almacena features.
- **D ❌** Config evalúa la configuración de recursos de AWS.

📚 [Dominio 4 — Model Cards](../domains/04-responsible-ai/README.md#32-amazon-sagemaker-model-cards)
</details>

## Pregunta 3 — Opción múltiple

Una empresa usa Amazon Textract para procesar formularios de solicitud. Cuando la confianza de la extracción es baja, una persona debe revisar el resultado antes de continuar. ¿Qué servicio cubre este requisito?

- A. Amazon SageMaker Ground Truth
- B. Amazon Augmented AI (A2I)
- C. Amazon Comprehend
- D. Amazon Bedrock Model Evaluation

<details>
<summary>▶ Ver respuesta</summary>

**Respuesta correcta:** B

- **B ✅** A2I crea flujos de revisión humana activados por umbrales de confianza, con integración nativa con Textract.
- **A ❌** Ground Truth se orienta al etiquetado de datos de entrenamiento.
- **C ❌** Es un servicio de NLP.
- **D ❌** Evalúa modelos, no revisa predicciones individuales en producción.

📚 [Dominio 4 — Otras herramientas](../domains/04-responsible-ai/README.md#34-otras-herramientas-de-ia-responsable)
</details>

## Pregunta 4 — Opción múltiple

Una aseguradora debe poder explicar a cada cliente qué factores influyeron en el precio de su póliza calculado por un modelo XGBoost. ¿Qué pilar de la IA responsable aborda este requisito y con qué técnica?

- A. Privacidad — cifrado con KMS
- B. Explicabilidad — valores SHAP con SageMaker Clarify
- C. Robustez — Bedrock Guardrails
- D. Gobernanza — SCPs

<details>
<summary>▶ Ver respuesta</summary>

**Respuesta correcta:** B

- **B ✅** La explicabilidad local (por predicción) se obtiene con SHAP, disponible en SageMaker Clarify.
- **A ❌, C ❌, D ❌** Abordan otros pilares.

📚 [Dominio 4 — Transparencia y explicabilidad](../domains/04-responsible-ai/README.md#4-transparencia-explicabilidad-e-interpretabilidad)
</details>

## Pregunta 5 — Opción múltiple

Un cliente pregunta si los prompts que su aplicación envía a Amazon Bedrock se usarán para entrenar los modelos base. ¿Cuál es la respuesta correcta?

- A. Sí, salvo que se active una opción de exclusión en cada petición.
- B. Sí, pero solo los modelos de Amazon.
- C. No: los prompts y respuestas no se usan para entrenar los modelos base ni se comparten con los proveedores de modelos.
- D. Solo si se usa Provisioned Throughput.

<details>
<summary>▶ Ver respuesta</summary>

**Respuesta correcta:** C

Amazon Bedrock no usa el contenido del cliente para entrenar los modelos base ni lo comparte con terceros proveedores.

📚 [Dominio 4 — Garantías de privacidad](../domains/04-responsible-ai/README.md#51-garantías-de-privacidad-en-servicios-gestionados)
</details>

## Pregunta 6 — Respuesta múltiple (elige DOS)

Un modelo de selección de personal recomienda sistemáticamente menos candidatas mujeres. ¿Qué DOS acciones son más adecuadas?

- A. Aumentar el tamaño del modelo.
- B. Analizar el sesgo de los datos y de las predicciones con SageMaker Clarify.
- C. Reequilibrar el dataset para que sea representativo y diverso.
- D. Aumentar la temperatura del modelo.
- E. Desactivar los logs de CloudTrail.

<details>
<summary>▶ Ver respuesta</summary>

**Respuestas correctas:** B y C

- **B ✅** Permite medir el sesgo pre y post-entrenamiento y localizar su origen.
- **C ✅** Los datos inclusivos y balanceados son la principal palanca para reducir el sesgo.
- **A ❌, D ❌** No abordan la causa del sesgo.
- **E ❌** Reduce la auditabilidad.

📚 [Dominio 4 — Sesgo y calidad de datos](../domains/04-responsible-ai/README.md#2-sesgo-equidad-y-calidad-de-datos)
</details>
