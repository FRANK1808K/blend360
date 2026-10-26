# Playbook del Examen AIF-C01 — Inscripción, Estrategia y Técnica

## 1. Inscripción: decisiones que cambian tu resultado

### 1.1 ¿En qué idioma hago el examen?

| Opción | Ventajas | Inconvenientes | Recomendación |
|---|---|---|---|
| **Español** (Latinoamérica o España) | Lees más rápido y entiendes mejor los escenarios. | Las traducciones de términos técnicos pueden resultar raras ("rendimiento aprovisionado", "barreras de protección"); **no** se aplica ESL +30. | Si tu inglés técnico es básico o intermedio. Estudia el [glosario](../cheatsheets/glossary.md) para reconocer las traducciones. |
| **Inglés + ESL +30** | Los nombres de servicios y términos coinciden con la documentación y con casi todo el material de práctica; **120 minutos en lugar de 90**. | Exige leer con soltura en inglés. | Si lees documentación técnica en inglés con comodidad. **Los 30 minutos extra son una gran ventaja.** |

### 1.2 Cómo pedir ESL +30 (solo si haces el examen en inglés)

1. Entra en tu cuenta de AWS Certification.
2. *Request Exam Accommodations* → *Request Accommodation* → tipo **ESL +30 MINUTES** → *Create*.
3. Se pide **una sola vez y ANTES de reservar**; se aplica a todos tus exámenes futuros. Si ya reservaste sin ella, tienes que cancelar la reserva, solicitar la adaptación y volver a reservar.

Fuente: [AWS Certification — Before testing](https://aws.amazon.com/certification/policies/before-testing/).

### 1.3 ¿Centro de pruebas u online?

| | Centro Pearson VUE | Online (OnVUE) |
|---|---|---|
| Riesgos técnicos | Ninguno para ti | Conexión, webcam, comprobación del entorno |
| Normas | Estándar | Muy estrictas: sala vacía, mesa despejada, no hablar, no tapar la boca, no mirar fuera de la pantalla |
| Recomendación | ✅ Si tienes un centro cerca, **reduce el estrés** | Haz el *system test* el día anterior y conéctate 30 min antes |

## 2. Formato y gestión del tiempo

| Dato | Valor |
|---|---|
| Preguntas | 65 (50 puntúan y 15 no, sin identificar cuáles) |
| Tiempo | 90 min (120 min con ESL +30) |
| Ritmo objetivo | **≈ 1 min por pregunta** en la primera pasada (≈ 1,5 min con ESL) |
| Aprobado | 700 / 1000, puntuación **compensatoria** (no hay mínimo por dominio) |
| Penalización por error | **Ninguna: nunca dejes preguntas en blanco** |

### Estrategia de dos pasadas

```text
Pasada 1 (≈ 60 min): responde todo. Si dudas > 90 s → elige la mejor opción, MARCA (flag) y sigue.
Pasada 2 (≈ 20 min): revisa solo las marcadas.
Últimos 10 min: comprueba que no queda ninguna sin responder.
```

> **No cambies una respuesta** en la revisión salvo que encuentres un dato concreto del enunciado que pasaste por alto. El primer instinto informado suele ser correcto.

## 3. Técnica para responder

### 3.1 Lee la pregunta en este orden

1. **La última frase primero** (qué te preguntan exactamente).
2. **El requisito clave** (qué quieren lograr).
3. **La restricción** (*menor esfuerzo operativo*, *más rentable*, *sin re-entrenar*, *datos privados*, *en tiempo real*…). **La restricción decide la respuesta.**
4. Después, las opciones.

### 3.2 Palabras clave que deciden la respuesta

| Si el enunciado dice… | Piensa en… |
|---|---|
| "menor esfuerzo operativo", "totalmente gestionado", "sin gestionar infraestructura" | Bedrock o un servicio de IA gestionado, **no** SageMaker ni EC2 |
| "control total", "elegir instancia", "modelo open source concreto" | SageMaker AI / JumpStart |
| "más rentable" + "no urgente" | Batch inference |
| "datos que cambian", "documentos internos", "citar fuentes" | RAG / Knowledge Bases |
| "estilo", "formato", "tarea especializada" + ejemplos etiquetados | Fine-tuning |
| "acciones", "llamar APIs", "multi-paso", "herramientas" | Agentes (Bedrock Agents / AgentCore) |
| "conectar el agente a herramientas externas de forma estándar" | MCP (AgentCore Gateway) |
| "versionar prompts", "rollback de prompts" | Bedrock Prompt Management |
| "quién hizo la llamada" | CloudTrail |
| "contenido de prompts y respuestas" | Model Invocation Logging |
| "sin pasar por Internet" | VPC endpoint (PrivateLink) |
| "sesgo", "explicar predicciones" | SageMaker Clarify |
| "drift en producción" | SageMaker Model Monitor |
| "revisión humana" | Amazon A2I |
| "decisión regulada sobre datos tabulares que hay que explicar" | ML tradicional (+ Clarify), no un LLM |
| "modernizar mainframe / .NET / VMware con IA" | AWS Transform |
| "IDE con especificaciones" | Kiro |

### 3.3 Técnica de descarte

1. Elimina las opciones que **no resuelven el requisito**.
2. Elimina las que **incumplen la restricción** (p. ej., SageMaker cuando piden "sin gestionar infraestructura").
3. Elimina las que **sobran** (soluciones más complejas o caras de lo necesario).
4. Entre dos opciones válidas, elige la **más gestionada, simple y específica** para el caso.

### 3.4 Tipos de pregunta

| Tipo | Consejo |
|---|---|
| Opción múltiple | Una correcta. Aplica el descarte. |
| Respuesta múltiple | El enunciado dice cuántas elegir ("elige DOS"). Evalúa cada opción por separado como verdadero/falso. No se puntúan respuestas parciales. |
| **Ordenación** | Identifica primero el **primer** y el **último** paso; el resto encaja. Típico: ciclo de vida de ML, flujo RAG, pasos de fine-tuning. |
| **Emparejamiento** | Empieza por los pares que tengas claros; el resto se resuelve por eliminación. Típico: servicio ↔ caso de uso, métrica ↔ tarea. |
| **Caso de estudio** | Un escenario con varias preguntas. Lee el escenario una vez con atención y vuelve a él en cada pregunta. |

## 4. Checklists

### 4.1 Semana anterior

- [ ] Cumples los [criterios de "listo"](retake-plan.md#3-criterios-para-reservar-el-examen).
- [ ] Reserva confirmada (idioma y ESL comprobados).
- [ ] Si es online: *system test* hecho en el mismo equipo y red.

### 4.2 Día anterior

- [ ] Solo [repaso final 48 h](../cheatsheets/final-review-48h.md) y la [matriz de decisión](../cheatsheets/exam-decision-matrix.md). Nada nuevo.
- [ ] Documento de identidad válido, con el **mismo nombre** que en la cuenta de AWS Certification.
- [ ] Dormir al menos 7 h.

### 4.3 Día del examen

- [ ] Llegar 30 min antes (o conectarse 30 min antes si es online).
- [ ] Comer algo ligero; ir al baño antes de empezar.
- [ ] Aplicar la estrategia de dos pasadas. Respirar hondo si una pregunta te bloquea: márcala y sigue.

### 4.4 Después

- Recibes el resultado normalmente en unos días (a veces en horas) en tu cuenta de AWS Certification.
- **Si apruebas:** según varias fuentes, recibes un **cupón de descuento del 50 %** para tu próximo examen de AWS (compruébalo en tu cuenta). Siguientes pasos naturales: *AWS Certified Machine Learning Engineer – Associate* o *AWS Certified Generative AI Developer – Professional*.
- **Si no apruebas:** espera 14 días y sigue el [plan de reintento](retake-plan.md) con tu nuevo desglose por dominios.
- **Confidencialidad:** el contenido del examen es confidencial. No publiques ni compartas preguntas.
