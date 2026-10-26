# Preguntas de Práctica — Dominio 2: Fundamentos de IA Generativa

## Pregunta 1 — Opción múltiple

Una aplicación usa un LLM para extraer campos de facturas en formato JSON. Las respuestas varían entre ejecuciones y a veces incluyen texto adicional. ¿Qué ajuste de inferencia ayuda más a obtener salidas consistentes?

- A. Aumentar la temperatura a 1,0.
- B. Reducir la temperatura a un valor cercano a 0.
- C. Aumentar Top-K a 500.
- D. Aumentar el número máximo de tokens.

<details>
<summary>▶ Ver respuesta</summary>

**Respuesta correcta:** B

- **B ✅** Una temperatura baja hace el muestreo más determinista, ideal para extracción estructurada.
- **A ❌ / C ❌** Aumentan la diversidad y la variabilidad.
- **D ❌** Solo permite respuestas más largas; no mejora la consistencia.

📚 [Dominio 2 — Parámetros de inferencia](../domains/02-fundamentals-generative-ai/README.md#22-parámetros-de-inferencia)
</details>

## Pregunta 2 — Opción múltiple

Una aseguradora quiere que su asistente responda preguntas sobre las condiciones de sus pólizas, que se actualizan cada mes. Necesita incluir la fuente en cada respuesta y minimizar costos. ¿Qué enfoque es el más adecuado?

- A. Pre-entrenar un LLM desde cero con las pólizas.
- B. Hacer fine-tuning de un FM cada mes con las pólizas.
- C. Retrieval-Augmented Generation (RAG) sobre las pólizas.
- D. Aumentar la ventana de contexto e incluir todas las pólizas en cada prompt.

<details>
<summary>▶ Ver respuesta</summary>

**Respuesta correcta:** C

- **C ✅** RAG recupera los fragmentos relevantes en tiempo de consulta, permite citar fuentes y solo requiere re-sincronizar al cambiar los documentos.
- **A ❌** Costo y complejidad extremos.
- **B ❌** Costoso de repetir cada mes y no aporta citas.
- **D ❌** Incrementa el costo por token en cada petición y no escala con muchos documentos.

📚 [Dominio 2 — Técnicas de adaptación](../domains/02-fundamentals-generative-ai/README.md#3-técnicas-de-adaptación)
</details>

## Pregunta 3 — Emparejamiento

Relaciona cada métrica con su uso más habitual:

| Métrica | Uso |
|---|---|
| 1. ROUGE | a. Traducción automática |
| 2. BLEU | b. Similitud semántica entre textos |
| 3. BERTScore | c. Resumen de textos |

<details>
<summary>▶ Ver respuesta</summary>

**Solución:** 1 → c, 2 → a, 3 → b

ROUGE mide el solapamiento con resúmenes de referencia; BLEU, la precisión de n-gramas frente a traducciones de referencia; BERTScore compara significado usando embeddings.

📚 [Dominio 2 — Métricas](../domains/02-fundamentals-generative-ai/README.md#52-métricas-de-evaluación-de-modelos-generativos)
</details>

## Pregunta 4 — Opción múltiple

¿Qué describe mejor un **embedding**?

- A. Un fragmento de texto de tamaño fijo usado en RAG.
- B. Un vector numérico que representa el significado semántico de un contenido.
- C. El número máximo de tokens que puede procesar un modelo.
- D. Un parámetro que controla la aleatoriedad de la salida.

<details>
<summary>▶ Ver respuesta</summary>

**Respuesta correcta:** B

- **B ✅** Los embeddings permiten medir similitud semántica entre textos (base de la búsqueda vectorial).
- **A ❌** Eso es un *chunk*.
- **C ❌** Eso es la ventana de contexto.
- **D ❌** Eso es la temperatura.

📚 [Dominio 2 — Definiciones](../domains/02-fundamentals-generative-ai/README.md#11-definiciones)
</details>

## Pregunta 5 — Opción múltiple

Una empresa farmacéutica quiere que un FM comprenda mejor la terminología de su sector. Dispone de millones de documentos científicos **sin etiquetar**. ¿Qué técnica es la más adecuada?

- A. Fine-tuning con instrucciones
- B. Continued pre-training
- C. Few-shot prompting
- D. Reducir el Top-P

<details>
<summary>▶ Ver respuesta</summary>

**Respuesta correcta:** B

- **B ✅** El continued pre-training adapta el modelo a un dominio usando grandes volúmenes de texto sin etiquetar.
- **A ❌** El fine-tuning con instrucciones necesita pares prompt–respuesta etiquetados.
- **C ❌** Unos pocos ejemplos en el prompt no transfieren el conocimiento de millones de documentos.
- **D ❌** Es un parámetro de inferencia; no añade conocimiento.

📚 [Dominio 2 — Tabla comparativa](../domains/02-fundamentals-generative-ai/README.md#31-tabla-comparativa)
</details>

## Pregunta 6 — Respuesta múltiple (elige DOS)

Un chatbot de atención al cliente a veces inventa políticas de devolución que no existen. ¿Qué DOS medidas reducen este problema?

- A. Aumentar la temperatura.
- B. Implementar RAG con la documentación oficial de políticas.
- C. Activar el *contextual grounding check* de Amazon Bedrock Guardrails.
- D. Aumentar el número máximo de tokens de salida.
- E. Cambiar a un modelo de generación de imágenes.

<details>
<summary>▶ Ver respuesta</summary>

**Respuestas correctas:** B y C

- **B ✅** Ancla las respuestas en la documentación real.
- **C ✅** Bloquea respuestas no fundamentadas en la fuente.
- **A ❌** Aumenta la aleatoriedad y el riesgo de alucinación.
- **D ❌** No afecta a la veracidad.
- **E ❌** No tiene sentido para el caso de uso.

📚 [Dominio 2 — Desafíos](../domains/02-fundamentals-generative-ai/README.md#4-desafíos-y-limitaciones)
</details>
