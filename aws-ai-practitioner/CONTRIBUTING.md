# Guía de Contribución

Gracias por ayudar a mejorar esta guía de preparación para **AWS Certified AI Practitioner (AIF-C01)**. Este documento define las convenciones que mantienen el repositorio coherente, verificable y útil.

## 1. Principios editoriales

1. **Exactitud técnica primero:** toda afirmación sobre un servicio de AWS debe poder verificarse en la documentación oficial. Si un dato cambia con frecuencia (precios, cuotas, modelos disponibles), indícalo y fecha la información.
2. **Orientación al examen:** cada sección debe ayudar a responder preguntas del tipo *"¿qué servicio/configuración elegir y por qué?"*. Prioriza criterios de decisión sobre descripciones de marketing.
3. **Concisión:** tablas y listas antes que párrafos largos.
4. **Contenido original:** está prohibido copiar preguntas de exámenes reales (*dumps*) o contenido con derechos de autor.

## 2. Convención de nombres

| Elemento | Regla | Ejemplo |
|---|---|---|
| Directorios | `kebab-case`, en inglés | `cheatsheets/`, `practice-questions/` |
| Dominios | `NN-<tema>` con número del dominio oficial | `domains/04-responsible-ai/` |
| Laboratorios | `lab-NN-<tema>` | `labs/lab-02-bedrock-guardrails/` |
| Documento principal de una carpeta | `README.md` | `labs/lab-01-rag-bedrock-knowledge-bases/README.md` |
| Preguntas | `domain-NN-questions.md` | `practice-questions/domain-03-questions.md` |
| Políticas | `<identidad>-<tipo>-policy.json` | `kb-trust-policy.json`, `app-query-policy.json` |
| Scripts | `snake_case.py` con verbo | `create_vector_index.py` |
| Marcadores en plantillas | `__MAYUSCULAS__` | `__ACCOUNT_ID__`, `__REGION__` |

## 3. Guía de estilo

### 3.1 Idioma

- Español neutro, en registro técnico y directo (segunda persona del singular: "configura", "elige").
- Los nombres de servicios, APIs, acciones IAM, parámetros y términos técnicos consolidados se mantienen en inglés: *Amazon Bedrock*, `RetrieveAndGenerate`, `bedrock:InvokeModel`, *fine-tuning*, *chunking*.
- En la primera aparición de un término, incluye su traducción o equivalente: *recall (sensibilidad)*.
- Usa **Exactitud (Accuracy)** y **Precisión (Precision)** para evitar la ambigüedad habitual en español.

### 3.2 Estructura de los documentos de dominio

1. Título `# Dominio N — <Nombre> (peso %)` y bloque de cita con peso y objetivo.
2. Tabla **"Mapeo a los task statements oficiales"**.
3. Secciones numeradas (`## 1.`, `### 1.1`).
4. Sección final **"Autoevaluación rápida"** con casillas `- [ ]`.
5. Navegación al dominio anterior/siguiente.

### 3.3 Markdown

- Un solo encabezado `#` por archivo; no saltes niveles.
- Bloques de código **siempre** con lenguaje: `bash`, `json`, `python`, `yaml`, `text`, `mermaid`.
- Diagramas de flujo en **Mermaid**; jerarquías y estructuras en ASCII dentro de bloques `text`.
- Las tablas de decisión incluyen, cuando aplique, una columna **"Cuándo NO usarlo"**.
- Enlaces internos **relativos** (`../domains/...`), nunca URLs absolutas de GitHub.

### 3.4 Seguridad en ejemplos

- **Nunca** incluyas credenciales, claves, IDs de cuenta, ARNs reales ni datos personales.
- Usa la cuenta de documentación `111122223333` o marcadores `__ACCOUNT_ID__`.
- Las políticas IAM deben aplicar **mínimo privilegio**: recurso concreto en lugar de `*` siempre que sea posible, y condiciones (`aws:SourceAccount`, `aws:SourceArn`, `aws:ResourceAccount`) en roles de servicio.

## 4. Laboratorios

- Parte de [`labs/template.md`](labs/template.md) y completa **todas** las secciones: objetivos, arquitectura, IAM mínimo viable, pasos, validación, troubleshooting, costos y **limpieza**.
- Prueba el laboratorio de principio a fin en una cuenta limpia e indica la región y el mes de la última verificación.
- Las políticas van en `policies/`, los scripts en `scripts/` (con `requirements.txt`) y los datos de ejemplo, ficticios, en `sample-data/`.

## 5. Preguntas de práctica

- Usa la plantilla de [`practice-questions/README.md`](practice-questions/README.md).
- Escenario realista, una sola pregunta, opciones plausibles.
- Justifica **todas** las opciones (✅/❌) y enlaza la sección del dominio que la respalda.
- Varía los tipos: opción múltiple, respuesta múltiple, ordenación y emparejamiento.

## 6. Flujo de trabajo

1. Abre un *issue* describiendo el cambio (o comenta uno existente).
2. Crea una rama: `docs/<tema>`, `feat/<lab-o-funcionalidad>` o `fix/<corrección>`.
3. Usa [Conventional Commits](https://www.conventionalcommits.org/es/v1.0.0/):

   ```text
   docs(d3): añade sección de Bedrock Flows
   feat(labs): añade lab 02 de Bedrock Guardrails
   fix(questions): corrige la justificación de D2-Q4
   chore(ci): actualiza la versión de markdownlint
   ```

4. Valida localmente antes de abrir el *pull request*:

   ```bash
   npx --yes markdownlint-cli2@0.23.2
   python .github/scripts/check_links.py
   ```

5. Abre el *pull request* describiendo el cambio y las fuentes oficiales consultadas. La CI debe pasar en verde.

## 7. Checklist del pull request

- [ ] El contenido está alineado con la guía oficial del examen AIF-C01.
- [ ] Las afirmaciones técnicas están verificadas en la documentación oficial de AWS.
- [ ] No hay credenciales, IDs de cuenta ni datos personales.
- [ ] Los nombres de archivo siguen la convención.
- [ ] `markdownlint` y la validación de enlaces pasan sin errores.
- [ ] Si se añade un laboratorio: incluye costos estimados y limpieza probada.
