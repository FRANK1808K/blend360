# Plan de Reintento — de 630 a 700+ en 4 semanas

> **Diagnóstico de partida (examen del 28-sep-2026):** puntuación escalada **630 / 1000** (aprobado: **700**).
>
> | Dominio | Peso | Resultado |
> |---|---|---|
> | D1 — Fundamentos de IA y ML | 20 % | 🟧 Necesita mejora |
> | D2 — Fundamentos de IA generativa | 24 % | ✅ Cumple con las competencias |
> | D3 — Aplicaciones de modelos fundacionales | 28 % | 🟧 Necesita mejora |
> | D4 — IA responsable | 14 % | 🟧 Necesita mejora |
> | D5 — Seguridad, cumplimiento y gobernanza | 14 % | 🟧 Necesita mejora |
>
> **Reintento posible desde el 12-oct-2026** (14 días de espera tras un suspenso).

---

## 1. Lectura del resultado

1. **Estás cerca.** 630 está a 70 puntos del aprobado. La puntuación es **compensatoria**: no hace falta "aprobar" cada dominio, basta con subir el total. Con unas pocas preguntas más acertadas en D3 y D1 se aprueba.
2. **El 76 % del examen está en "necesita mejora"** (D1 + D3 + D4 + D5). D2 (conceptos de GenAI) va bien: **entiendes la teoría de GenAI, pero fallas al aplicarla a servicios concretos de AWS** (D3, D5), en los fundamentos de ML clásico (D1) y en las herramientas de IA responsable (D4).
3. **Prioridad por impacto** (peso × margen de mejora):

| Prioridad | Dominio | Por qué |
|---|---|---|
| 🥇 1 | **D3 (28 %)** | El mayor peso. Selección de servicios: Bedrock (KB, Agents, Guardrails), JumpStart, servicios de IA, Amazon Q/Quick, servicios agénticos nuevos. |
| 🥈 2 | **D1 (20 %)** | Métricas (precisión/recall/F1/RMSE), tipos de aprendizaje, ciclo de vida de ML y servicios de SageMaker. Son preguntas "memorizables": mucho retorno por hora de estudio. |
| 🥉 3 | **D5 (14 %)** | Responsabilidad compartida, IAM, PrivateLink, CloudTrail frente a invocation logging, modelos de precios. Muy de "palabra clave → servicio". |
| 4 | **D4 (14 %)** | Clarify, Model Cards, Model Monitor, A2I y Guardrails: pocas herramientas, fáciles de asociar. |
| Mantener | D2 (24 %) | Repaso ligero para no perder el nivel. |

**4. La guía v1.1 ya estaba vigente en tu examen.** Desde junio de 2026 el examen incluye IA agéntica, MCP, AgentCore, Kiro, Strands Agents, AWS Transform, context engineering y detección de alucinaciones. Si estudiaste con material anterior a mayo de 2026, parte de las preguntas de D1, D3 y D5 trataban temas que no habías visto. **Estúdialo primero:** [novedades v1.1](../domains/00-exam-guide-v1.1-changes.md).

### Autodiagnóstico (10 minutos, antes de empezar)

Marca lo que recuerdes que te costó en el examen. **No anotes preguntas del examen** (el contenido es confidencial según el código de conducta), solo **temas**:

- [ ] Elegir entre servicios parecidos (Comprehend/Textract/Rekognition, Lex/Q Business/Bedrock, Bedrock/JumpStart).
- [ ] Preguntas sobre agentes, AgentCore, MCP, Kiro o Strands.
- [ ] Métricas de evaluación (cuándo precisión, cuándo recall, ROUGE/BLEU).
- [ ] Herramientas de SageMaker (Clarify, Model Monitor, Model Cards, Ground Truth, Canvas…).
- [ ] Seguridad: IAM, VPC endpoints, CloudTrail, KMS, Macie, responsabilidad compartida.
- [ ] Costos: On-Demand / Batch / Provisioned Throughput, tokens.
- [ ] Preguntas de ordenación o emparejamiento.
- [ ] Me faltó tiempo / leí con prisa / las traducciones eran confusas.

> Si marcaste la última casilla, revisa la sección de inscripción del [playbook](exam-playbook.md#1-inscripción-decisiones-que-cambian-tu-resultado): idioma del examen y **ESL +30 minutos**.

---

## 2. Calendario (≈ 1,5–2 h al día)

**Fecha objetivo del reintento: entre el 5 y el 9 de noviembre de 2026**, siempre que se cumplan los [criterios de "listo"](#3-criterios-para-reservar-el-examen). Resérvala al final de la semana 3, no antes.

### Semana 1 (8–14 oct) — D3, el dominio con más peso

| Día | Tarea | Material | Hecho |
|---|---|---|---|
| Jue 8 | Leer las **novedades v1.1** completas | [v1.1](../domains/00-exam-guide-v1.1-changes.md) | [ ] |
| Vie 9 | D3 §1.1–1.4: Bedrock, selección de modelos, **Knowledge Bases** | [D3](../domains/03-applications-foundation-models/README.md) | [ ] |
| Sáb 10 | D3 §1.5–1.7: **Agents, Guardrails, Custom Models** + AgentCore/Strands/Kiro (v1.1 §5) | D3 + v1.1 | [ ] |
| Dom 11 | **Práctica:** mini-retos de consola o [Lab 01](../labs/lab-01-rag-bedrock-knowledge-bases/README.md) | [Práctica](../resources/hands-on.md) | [ ] |
| Lun 12 | D3 §2: **Bedrock vs. JumpStart** + D3 §3: servicios de IA (tabla "cuándo NO usarlo") | D3 | [ ] |
| Mar 13 | D3 §4–5: prompts, Prompt Management, **evaluación** (LLM-as-a-judge, métricas de negocio) | D3 + v1.1 §6–7 | [ ] |
| Mié 14 | ✍️ [Preguntas D3](../practice-questions/domain-03-questions.md) + escenarios 1–9 y 21–29 de la [matriz](../cheatsheets/exam-decision-matrix.md) + [pares que se confunden §1](../cheatsheets/confusable-pairs.md#1-dominio-3--servicios-de-ia-y-fms-28-) + flashcards D3 | Repo | [ ] |

### Semana 2 (15–21 oct) — D1 y D5

| Día | Tarea | Material | Hecho |
|---|---|---|---|
| Jue 15 | D1 §1–3: jerarquía AI/ML/DL/GenAI/**agéntica**, tipos de aprendizaje, **ML tradicional vs. FMs** | [D1](../domains/01-fundamentals-ai-ml/README.md) + v1.1 §2 | [ ] |
| Vie 16 | D1 §5: **ciclo de vida de ML** y servicios de SageMaker por fase | D1 | [ ] |
| Sáb 17 | D1 §6: **métricas** (haz tú mismo la tabla FP/FN → métrica) | D1 | [ ] |
| Dom 18 | ✍️ [Preguntas D1](../practice-questions/domain-01-questions.md) + [pares §2](../cheatsheets/confusable-pairs.md#2-dominio-1--fundamentos-de-ml-20-) + flashcards D1 | Repo | [ ] |
| Lun 19 | D5 §1–3: **responsabilidad compartida**, Scoping Matrix, IAM, **PrivateLink** | [D5](../domains/05-security-compliance-governance/README.md) | [ ] |
| Mar 20 | D5 §4–6: **CloudTrail vs. invocation logging**, CloudWatch, **costos**, gobernanza + v1.1 §8 (alucinaciones) | D5 + v1.1 | [ ] |
| Mié 21 | ✍️ [Preguntas D5](../practice-questions/domain-05-questions.md) + escenarios 10–16 y 30–35 de la matriz + [pares §4](../cheatsheets/confusable-pairs.md#4-dominio-5--seguridad-cumplimiento-y-gobernanza-14-) | Repo | [ ] |

### Semana 3 (22–28 oct) — D4 y primeros simulacros

| Día | Tarea | Material | Hecho |
|---|---|---|---|
| Jue 22 | D4 completo: pilares, **Clarify, Model Cards, Model Monitor, A2I**, privacidad | [D4](../domains/04-responsible-ai/README.md) | [ ] |
| Vie 23 | ✍️ [Preguntas D4](../practice-questions/domain-04-questions.md) + escenarios 17–20 y 32–33 + [pares §3](../cheatsheets/confusable-pairs.md#3-dominio-4--ia-responsable-14-) | Repo | [ ] |
| Sáb 24 | 🧪 **Official Practice Question Set** (20 preguntas, Skill Builder) | [Oficial](../resources/practice-exams.md) | [ ] |
| Dom 25 | 🧪 **[Simulacro 01](../practice-questions/mock-exam-01.md)** cronometrado en el [simulador](../simulator/README.md) (90 min) | Repo | [ ] |
| Lun 26 | Revisar **todos** los errores del simulacro y anotarlos en tu registro | [Método](../resources/practice-exams.md#2-método-para-sacar-el-máximo-partido) | [ ] |
| Mar 27 | Repasar los dominios donde fallaste | Repo | [ ] |
| Mié 28 | 🧪 Simulacro de terceros n.º 1 (Tutorials Dojo o Maarek) → **¿cumples los criterios? Reserva** | [Exámenes](../resources/practice-exams.md) | [ ] |

### Semana 4 (29 oct – 4 nov) — Consolidación

| Día | Tarea | Hecho |
|---|---|---|
| Jue 29 | Revisión de errores del simulacro n.º 1 | [ ] |
| Vie 30 | 🧪 Simulacro de terceros n.º 2 | [ ] |
| Sáb 31 | 🧪 **[Simulacro 02](../practice-questions/mock-exam-02.md)** en el [simulador](../simulator/README.md) + revisión de errores | [ ] |
| Dom 1 | 🧪 Simulacro de terceros n.º 3 (o el Official Pretest si tienes suscripción) | [ ] |
| Lun 2 | Revisión final de errores | [ ] |
| Mar 3 – Mié 4 | [Repaso final 48 h](../cheatsheets/final-review-48h.md) + [matriz de decisión](../cheatsheets/exam-decision-matrix.md) completa | [ ] |
| **5–9 nov** | 🎯 **Examen** | [ ] |

---

### Hábito diario (15–20 min, todos los días del plan)

1. **Flashcards** del dominio de la semana en Anki ([mazo](../flashcards/README.md)).
2. **Modo "Refuerzo D1 · D3 · D4 · D5"** del [simulador](../simulator/README.md) con corrección inmediata: 10 preguntas.
3. Anota cada fallo en tu registro de errores con el **par confundido** (p. ej., "Clarify vs. Model Monitor").

## 3. Criterios para reservar el examen

Reserva solo cuando cumplas **todos**:

- [ ] ≥ **85 %** en el [Simulacro 01](../practice-questions/mock-exam-01.md) y ≥ **80 %** en el [Simulacro 02](../practice-questions/mock-exam-02.md) (primer intento).
- [ ] ≥ **80 %** en al menos **dos** simulacros de terceros distintos (primer intento).
- [ ] Ningún dominio por debajo del 70 % en los simulacros.
- [ ] Respondes los 40 escenarios de la [matriz de decisión](../cheatsheets/exam-decision-matrix.md) sin mirar y explicas todos los [pares que se confunden](../cheatsheets/confusable-pairs.md).
- [ ] Puedes explicar con tus palabras: RAG vs. fine-tuning, Bedrock vs. JumpStart, CloudTrail vs. invocation logging, precisión vs. recall, Clarify vs. Model Monitor, Bedrock Agents vs. AgentCore.

Si a 28-oct no los cumples, añade una semana más centrada en tus errores en lugar de reservar con prisa.

## 4. Costo del reintento

- El reintento cuesta de nuevo el precio completo (**USD 100**). La promoción de 50 % para el AIF-C01 que se encontró terminó el **30-sep-2026**; revisa la web de AWS Certification por si hay alguna nueva.
- **Inversión mínima recomendada:** un banco de simulacros de terceros (≈ USD 15–20 en oferta), mucho más barato que otro suspenso.
