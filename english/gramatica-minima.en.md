# Minimum grammar for the technical test

🌐 [Español](gramatica-minima.md) · **English**

> Only what **really** appears in technical statements, and what you need to **explain your solution**. No more, no less. Each example has its Spanish meaning so you can check that you understood.

---

## 1. Present simple: describing what something does

The most common structure in exam statements.

| Affirmative | Negative | Question |
|---|---|---|
| The function **returns** a list. | The function **does not (doesn't) return** anything. | **Does** the function **return** a list? |
| The tables **contain** data. | The tables **don't contain** nulls. | **Do** the tables **contain** nulls? |

> ⚠️ With *he / she / it / the function / the query*, add **-s** to the verb: *it return**s***, *it sort**s***, *it do**es***.

## 2. Passive voice: the most used structure in technical documentation

**Structure:** `is / are` + past participle (verb ending in *-ed* or irregular).

| Passive | Spanish |
|---|---|
| The data **is stored** in S3. | Los datos **se almacenan** en S3. |
| The results **are sorted** by date. | Los resultados **se ordenan** por fecha. |
| Duplicates **are removed**. | **Se eliminan** los duplicados. |
| The table **was created** in 2024. | La tabla **fue creada** en 2024. |
| The query **is executed** every hour. | La consulta **se ejecuta** cada hora. |
| Null values **should be ignored**. | Los valores nulos **deben ignorarse**. |

**Irregular participles you will see:** *write → **written***, *run → **run***, *choose → **chosen***, *give → **given***, *take → **taken***, *build → **built***, *send → **sent***, *find → **found***, *keep → **kept***, *get → **got / gotten***.

## 3. Imperative: the instructions

The base form of the verb, with no subject: ***Write** a query… **Return** the list… **Assume** that… **Do not use** built-in functions.*

## 4. Modal verbs: obligation, possibility and advice

| Modal | Meaning | Example |
|---|---|---|
| **must** | strong obligation (*debe*) | *The solution **must** run in O(n).* |
| **should** | recommendation (*debería*) | *You **should** handle empty lists.* |
| **can** | ability/permission (*puede*) | *You **can** assume the input is valid.* |
| **may** | possibility/formal permission (*puede que*) | *The list **may** contain duplicates.* |
| **will** | future / certainty | *The function **will** receive a string.* |
| **would** | conditional / politeness | *Which service **would** you use?* = ¿Qué servicio usarías? |
| **need to** | necessity (*necesitar*) | *The company **needs to** reduce costs.* |

## 5. Conditionals: programming logic

| Type | Structure | Example |
|---|---|---|
| General fact | *If* + present, present | ***If** the list **is** empty, the function **returns** None.* |
| Real possibility | *If* + present, *will* + verb | ***If** you **use** Parquet, the queries **will be** faster.* |
| Hypothetical | *If* + past, *would* + verb | ***If** I **had** more time, I **would** optimize it.* |

*unless* = *if not*: ***Unless** the value is null, add it.* = If the value is not null, add it.

## 6. Comparatives and superlatives

| Adjective | Comparative | Superlative |
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

## 8. Past simple: talking about your projects in the interview

| Regular (-ed) | Irregular |
|---|---|
| I **created** a dashboard. | I **built** a pipeline. (*build*) |
| I **analyzed** sales data. | I **wrote** SQL queries. (*write*) |
| I **cleaned** the dataset. | I **made** a model. (*make*) |
| I **worked** with Python. | I **learned** / **learnt** AWS. (*learn*) |
| I **used** pandas. | I **did** an internship. (*do*) |
| I **improved** the process by 20%. | I **led** a team of 3. (*lead*) |

**Negative and question:** *I **didn't use** Spark.* · ***Did** you **use** AWS?* → *Yes, I **did**.*

## 9. Connectors to explain a solution in order

| Connector | Use |
|---|---|
| **First,** … **Then,** … **Next,** … **Finally,** … | Steps in order |
| **Because** / **since** | Reason (*porque / ya que*) |
| **So** / **therefore** | Consequence (*entonces / por lo tanto*) |
| **However** / **but** | Contrast (*sin embargo / pero*) |
| **For example** / **for instance** | Example |
| **In other words** | Rephrasing (*en otras palabras*) |
| **Instead of** + -ing | *instead of using a loop* (*en lugar de*) |
| **In order to** | Purpose (*para*) |
| **On the other hand** | Alternative (*por otro lado*) |

**Example:** *"**First**, I join the orders table with the customers table. **Then**, I group by customer **in order to** calculate the total. **Finally**, I sort the result in descending order. I use a LEFT JOIN **because** some customers don't have orders."*

---

**Next:** [entrevista-y-frases.en.md](entrevista-y-frases.en.md)
