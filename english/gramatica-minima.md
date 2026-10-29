# Gramática mínima para la prueba técnica

**Español** · [English](gramatica-minima.en.md)

> Solo lo que **realmente** aparece en enunciados técnicos y lo que necesitas para **explicar tu solución**. Ni más ni menos.

---

## 1. Presente simple: describir qué hace algo

La estructura más común en los enunciados.

| Afirmativa | Negativa | Pregunta |
|---|---|---|
| The function **returns** a list. | The function **does not (doesn't) return** anything. | **Does** the function **return** a list? |
| The tables **contain** data. | The tables **don't contain** nulls. | **Do** the tables **contain** nulls? |

> **Atención:** Con *he / she / it / the function / the query* se agrega **-s** al verbo: *it return**s***, *it sort**s***, *it do**es***.

## 2. Voz pasiva: lo que más se usa en documentación técnica

**Estructura:** `is / are` + participio (verbo en *-ed* o irregular).

| Pasiva | Español |
|---|---|
| The data **is stored** in S3. | Los datos **se almacenan** en S3. |
| The results **are sorted** by date. | Los resultados **se ordenan** por fecha. |
| Duplicates **are removed**. | **Se eliminan** los duplicados. |
| The table **was created** in 2024. | La tabla **fue creada** en 2024. |
| The query **is executed** every hour. | La consulta **se ejecuta** cada hora. |
| Null values **should be ignored**. | Los valores nulos **deben ignorarse**. |

**Participios irregulares que vas a ver:** *write → **written***, *run → **run***, *choose → **chosen***, *give → **given***, *take → **taken***, *build → **built***, *send → **sent***, *find → **found***, *keep → **kept***, *get → **got / gotten***.

## 3. Imperativo: las instrucciones

Verbo en forma base, sin sujeto: ***Write** a query… **Return** the list… **Assume** that… **Do not use** built-in functions.*

## 4. Modales: obligación, posibilidad y consejo

| Modal | Significado | Ejemplo |
|---|---|---|
| **must** | obligación fuerte | *The solution **must** run in O(n).* |
| **should** | debería (recomendación) | *You **should** handle empty lists.* |
| **can** | puede (capacidad/permiso) | *You **can** assume the input is valid.* |
| **may** | puede (posibilidad/permiso formal) | *The list **may** contain duplicates.* = puede tener duplicados |
| **will** | futuro / certeza | *The function **will** receive a string.* |
| **would** | condicional / cortesía | *Which service **would** you use?* = ¿Qué servicio usarías? |
| **need to** | necesitar | *The company **needs to** reduce costs.* |

## 5. Condicionales: lógica de programación

| Tipo | Estructura | Ejemplo |
|---|---|---|
| Hecho general | *If* + presente, presente | ***If** the list **is** empty, the function **returns** None.* |
| Posibilidad real | *If* + presente, *will* + verbo | ***If** you **use** Parquet, the queries **will be** faster.* |
| Hipotético | *If* + pasado, *would* + verbo | ***If** I **had** more time, I **would** optimize it.* |

*unless* = *if not*: ***Unless** the value is null, add it.* = Si el valor no es nulo, súmalo.

## 6. Comparativos y superlativos

| Adjetivo | Comparativo | Superlativo |
|---|---|---|
| fast | fast**er** (than) | **the** fast**est** |
| cheap | cheap**er** | **the** cheap**est** |
| large | larg**er** | **the** larg**est** |
| big | big**ger** | **the** big**gest** |
| expensive | **more** expensive | **the most** expensive |
| efficient | **more** efficient | **the most** efficient |
| good | **better** | **the best** |
| bad | **worse** | **the worst** |
| little / few | **less** / **fewer** | **the least** / **the fewest** |

*"Return the **second highest** salary"* · *"the **most frequent** element"* · *"the **least** expensive option"*.

## 7. There is / there are

- ***There is** a null value in the column.* (singular)
- ***There are** three duplicate rows.* (plural)
- ***Is there** a faster solution?*

## 8. Pasado simple: hablar de tus proyectos en la entrevista

| Regular (-ed) | Irregular |
|---|---|
| I **created** a dashboard. | I **built** a pipeline. (*build*) |
| I **analyzed** sales data. | I **wrote** SQL queries. (*write*) |
| I **cleaned** the dataset. | I **made** a model. (*make*) |
| I **worked** with Python. | I **learned** / **learnt** AWS. (*learn*) |
| I **used** pandas. | I **did** an internship. (*do*) |
| I **improved** the process by 20%. | I **led** a team of 3. (*lead*) |

**Negativa y pregunta:** *I **didn't use** Spark.* · ***Did** you **use** AWS?* → *Yes, I **did**.*

## 9. Conectores para explicar una solución en orden

| Conector | Uso |
|---|---|
| **First,** … **Then,** … **Next,** … **Finally,** … | Pasos en orden |
| **Because** / **since** | Porque / ya que |
| **So** / **therefore** | Entonces / por lo tanto |
| **However** / **but** | Sin embargo / pero |
| **For example** / **for instance** | Por ejemplo |
| **In other words** | En otras palabras |
| **Instead of** + -ing | En lugar de… (*instead of using a loop*) |
| **In order to** | Para (propósito) |
| **On the other hand** | Por otro lado |

**Ejemplo:** *"**First**, I join the orders table with the customers table. **Then**, I group by customer **in order to** calculate the total. **Finally**, I sort the result in descending order. I use a LEFT JOIN **because** some customers don't have orders."*

---

**Siguiente:** [entrevista-y-frases.md](entrevista-y-frases.md)
