# Preguntas de Práctica — Dominio 1: Fundamentos de IA y ML

## Pregunta 1 — Opción múltiple

Un banco entrena un modelo para detectar transacciones fraudulentas. Solo el 0,3 % de las transacciones son fraude. El equipo de riesgos indica que **no detectar un fraude es mucho más costoso** que revisar manualmente una transacción legítima. ¿Qué métrica debe priorizarse?

- A. Exactitud (accuracy)
- B. Recall
- C. Precisión (precision)
- D. RMSE

<details>
<summary>▶ Ver respuesta</summary>

**Respuesta correcta:** B

- **B ✅** El recall mide la proporción de fraudes reales detectados; minimiza los falsos negativos, que son el error caro.
- **A ❌** Con clases tan desbalanceadas, un modelo que nunca predice fraude tendría 99,7 % de exactitud.
- **C ❌** La precisión minimiza los falsos positivos (revisiones innecesarias), que aquí son el error barato.
- **D ❌** RMSE es una métrica de regresión.

📚 [Dominio 1 — Métricas de clasificación](../domains/01-fundamentals-ai-ml/README.md#62-métricas-de-clasificación)
</details>

## Pregunta 2 — Opción múltiple

Un modelo obtiene un 98 % de exactitud en el conjunto de entrenamiento y un 71 % en el de validación. ¿Qué describe mejor la situación y qué acción es adecuada?

- A. Underfitting; aumentar la regularización.
- B. Overfitting; añadir más datos de entrenamiento o aplicar regularización.
- C. El modelo está bien ajustado; desplegarlo.
- D. Data drift; activar SageMaker Model Monitor.

<details>
<summary>▶ Ver respuesta</summary>

**Respuesta correcta:** B

- **B ✅** La gran diferencia entre train y validation indica alta varianza (overfitting). Más datos, regularización o early stopping ayudan a generalizar.
- **A ❌** El underfitting muestra bajo desempeño en ambos conjuntos; aumentar la regularización lo empeoraría.
- **C ❌** El modelo no generaliza.
- **D ❌** El drift ocurre en producción con el tiempo, no entre train y validation.

📚 [Dominio 1 — Bias vs. varianza](../domains/01-fundamentals-ai-ml/README.md#bias-vs-varianza-compromiso)
</details>

## Pregunta 3 — Opción múltiple

Una empresa de retail quiere agrupar a sus clientes en segmentos según su comportamiento de compra. No dispone de etiquetas de segmento. ¿Qué tipo de aprendizaje es adecuado?

- A. Aprendizaje supervisado — clasificación
- B. Aprendizaje supervisado — regresión
- C. Aprendizaje no supervisado — clustering
- D. Aprendizaje por refuerzo

<details>
<summary>▶ Ver respuesta</summary>

**Respuesta correcta:** C

- **C ✅** El clustering (p. ej., k-means) descubre grupos en datos sin etiquetar.
- **A ❌ / B ❌** Requieren etiquetas.
- **D ❌** El refuerzo aprende por recompensas en un entorno, no agrupa datos estáticos.

📚 [Dominio 1 — Tipos de aprendizaje](../domains/01-fundamentals-ai-ml/README.md#3-tipos-de-aprendizaje)
</details>

## Pregunta 4 — Ordenación

Ordena las fases del ciclo de vida de ML:

1. Despliegue
2. Recolección de datos
3. Monitoreo
4. Entrenamiento
5. Preparación de datos y feature engineering
6. Evaluación

<details>
<summary>▶ Ver respuesta</summary>

**Orden correcto:** 2 → 5 → 4 → 6 → 1 → 3

Recolección → Preparación → Entrenamiento → Evaluación → Despliegue → Monitoreo (con retroalimentación a la recolección cuando se detecta drift).

📚 [Dominio 1 — Ciclo de vida](../domains/01-fundamentals-ai-ml/README.md#5-ciclo-de-vida-de-ml)
</details>

## Pregunta 5 — Opción múltiple

Un equipo de analistas de negocio sin experiencia en programación quiere construir un modelo para predecir la demanda de productos a partir de un CSV histórico. ¿Qué servicio es el más adecuado?

- A. Amazon SageMaker Canvas
- B. Amazon SageMaker JumpStart
- C. Amazon Bedrock Agents
- D. Amazon SageMaker Ground Truth

<details>
<summary>▶ Ver respuesta</summary>

**Respuesta correcta:** A

- **A ✅** Canvas es la herramienta no-code de SageMaker para preparar datos, entrenar modelos y generar predicciones.
- **B ❌** JumpStart requiere conocimientos técnicos para desplegar y ajustar modelos.
- **C ❌** Los agentes orquestan acciones con FMs; no entrenan modelos de pronóstico.
- **D ❌** Ground Truth sirve para etiquetar datos.

📚 [Dominio 1 — Servicios clave](../domains/01-fundamentals-ai-ml/README.md#7-servicios-clave-del-dominio-resumen)
</details>

## Pregunta 6 — Respuesta múltiple (elige DOS)

¿En qué DOS situaciones una solución de ML **no** es la opción más adecuada?

- A. Calcular el IVA de una factura según la legislación vigente.
- B. Detectar productos defectuosos en imágenes de una línea de producción.
- C. Clasificar correos entrantes por intención del cliente.
- D. Determinar si un usuario es mayor de edad a partir de su fecha de nacimiento.
- E. Predecir la probabilidad de abandono de clientes.

<details>
<summary>▶ Ver respuesta</summary>

**Respuestas correctas:** A y D

- **A ✅ / D ✅** Son cálculos deterministas con reglas exactas; una fórmula es más barata, exacta y auditable que un modelo probabilístico.
- **B ❌, C ❌, E ❌** Son problemas de patrones complejos donde el ML aporta valor.

📚 [Dominio 1 — Cuándo NO usar ML](../domains/01-fundamentals-ai-ml/README.md#4-cuándo-no-usar-ml)
</details>
