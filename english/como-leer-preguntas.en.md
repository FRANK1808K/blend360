# How to read exam questions in English (without freezing)

> In a technical test, **one single word** can change the answer: *NOT*, *EXCEPT*, *LEAST*, *at least*. This guide teaches you to spot them and to avoid "false friends".

---

## 1. A 4-step reading strategy (for every question)

1. **Read the LAST sentence first:** that is where the real question is (*"Which service should the company use?"*).
2. **Look for the words that change the meaning** (table 2): NOT, EXCEPT, LEAST, MOST, BEST, TWO…
3. **Read the scenario** looking for the **technical keywords** (*real-time*, *serverless*, *lowest cost*, *without code*). You do not need to understand every word.
4. **Eliminate options** and choose. If a word blocks you, **skip it** and infer it from the context.

> 🧠 **Do not translate word by word.** Look for *what they ask* + the *constraints*.

## 2. Words that change EVERYTHING (memorize them)

| English | Spanish | Example | Trap |
|---|---|---|---|
| **NOT** | NO | *Which is **NOT** a benefit…?* | They want the **false** one |
| **EXCEPT** | EXCEPTO | *All of the following are true **EXCEPT**…* | They want the **false** one |
| **LEAST** | MENOS | *the **least** expensive* = the cheapest | The opposite of *most* |
| **MOST** | MÁS | *the **most** cost-effective* = the best cost-benefit option | |
| **BEST** | MEJOR | *Which option **best** describes…* | Several may be correct; choose the best |
| **Choose TWO / Select all that apply** | Elige DOS / todas las que apliquen | | Mark exactly the number asked |
| **at least** | al menos (≥) | *at least 3 orders* = 3 or more | ≥, not > |
| **at most** | como máximo (≤) | *at most 5* = 5 or fewer | ≤ |
| **more than / greater than** | más que (>) | *more than 3* = 4, 5… | Does **not** include 3 |
| **fewer than / less than** | menos que (<) | | |
| **between X and Y** | entre X y Y | In SQL, `BETWEEN` **includes** both ends | |
| **inclusive / exclusive** | incluido / excluido | *range 1 to 10 inclusive* | |
| **only** | solo / únicamente | *return **only** the customers who…* | A filter |
| **each / every / per** | cada / por | *revenue **per** month* = `GROUP BY month` | Grouping |
| **unique / distinct** | únicos / distintos | *count **distinct** users* = `COUNT(DISTINCT ...)` | |
| **both… and** | tanto… como (los dos) | *bought **both** A **and** B* | A group condition (`HAVING`) |
| **either… or** | o… o (uno de los dos) | | |
| **neither… nor** | ni… ni | | |
| **unless** | a menos que | | = *if not* |
| **otherwise** | de lo contrario / si no | *return the value, **otherwise** return -1* | The `else` |
| **respectively** | respectivamente | | Order matters |
| **assume** | suponga | *Assume the list is sorted* | A condition you can use |
| **given** | dado(s) | *Given an array of integers…* | The input |
| **return** | devolver / retornar | *Return the index…* | The output |
| **output** | salida / qué imprime | *What is the **output** of this code?* | |
| **in-place** | sin crear otra estructura | *sort the array **in-place*** | O(1) space |
| **consecutive** | consecutivos | *3 **consecutive** days* | In a row, no gaps |
| **ascending / descending** | ascendente / descendente | *sorted in **descending** order* | Highest to lowest |
| **round to 2 decimals** | redondear a 2 decimales | | `ROUND(x, 2)` |
| **null / missing / empty** | nulo / faltante / vacío | | Edge cases |
| **edge case** | caso borde / límite | | |
| **ties** | empates | *In case of **ties**, return…* | Check how to break ties |

## 3. Scenario keywords (especially in AWS)

| English | Meaning | Points you to… |
|---|---|---|
| *cost-effective / lowest cost / cheapest* | the cheapest | Spot, S3 Glacier, serverless, Athena |
| *least operational overhead / fully managed* | the least administration work | Serverless/managed services |
| *without managing servers / serverless* | no servers | Lambda, Athena, Glue, Fargate |
| *real time / near real time* | instantly / almost instantly | Kinesis Data Streams / Firehose |
| *highly available / fault tolerant* | keeps working if something fails | Multi-AZ |
| *scalable / scale automatically* | grows by itself | Auto Scaling, serverless |
| *ad hoc queries* | one-off, unplanned queries | Athena |
| *without writing code / no-code* | no programming | DataBrew, AppFlow, Firehose, QuickSight |
| *compliance / audit* | regulations / auditing | CloudTrail, Config |
| *sensitive data / PII* | personal sensitive data | Macie, KMS, Lake Formation |
| *least privilege* | minimum permissions | IAM roles/policies |
| *long-term / rarely accessed / archive* | long term / rare access / archive | Glacier |

## 4. False friends (words that look like Spanish but are NOT)

| English | ❌ It does not mean | ✅ It means |
|---|---|---|
| **actual / actually** | actual / actualmente | **real / in reality** |
| **eventually** | eventualmente (sometimes) | **finally, over time** (*eventual consistency* = consistency reached over time) |
| **library** | librería (bookshop) | **biblioteca** (code library) |
| **record** | recordar (remember) | **registro** (a row) |
| **argument** | argumento (a discussion) | **argument/parameter** of a function (this one matches) |
| **assist** | asistir (to attend) | **to help** |
| **attend** | atender (to serve) | **to attend** (a meeting) |
| **realize** | realizar (to carry out) | **to notice / darse cuenta** |
| **support** | soportar (to tolerate) | **to support, be compatible with** |
| **sensible** | sensible (sensitive) | **sensato** (*sensitive* = sensible) |
| **exit** | éxito (success) | **salida** (*success* = éxito) |
| **current** | corriente (ordinary) | **actual** (*current version*) |
| **commit** | cometer (a crime) | **to confirm** (git changes / a transaction) |
| **deprecated** | depreciado | **obsolete** (not recommended) |
| **fault** | falta (a foul) | **failure, error** |
| **expire** | expirar (to die) | **to expire, to become invalid** |
| **compliance** | complacencia | **regulatory compliance** |
| **constraint** | constreñimiento | **restricción** (database) |
| **instance** | instancia (a legal step) | **instance** (a server, an object) |

## 5. Instruction verbs in coding statements

| Verb | What they ask |
|---|---|
| *Write a query/function that…* | Escribe una consulta/función que… |
| *Implement* | Implementa (programa) |
| *Find / Retrieve / Fetch* | Encuentra / obtén |
| *List / Display / Show* | Lista / muestra |
| *Count* | Cuenta |
| *Calculate / Compute* | Calcula |
| *Determine* | Determina |
| *Rank* | Ordena por posición (ranking) |
| *Filter out* | **Exclude** (remove!) |
| *Group by* | Agrupa por |
| *Sort / Order by* | Ordena |
| *Handle* (*handle null values*) | Maneja / trata |
| *Ignore* | Ignora |
| *Merge / Join* | Une |
| *Swap* | Intercambia |
| *Traverse / Iterate over* | Recorre |
| *Split* | Divide |
| *Trim / Strip* | Quita espacios |
| *Optimize* | Optimiza |

## 6. A guided example

> *A company stores clickstream data in Amazon S3 as CSV files. Analysts run ad hoc SQL queries on the data using Amazon Athena. The company wants to **reduce query costs** with the **LEAST operational overhead**. Which solution meets these requirements?*

1. **Last sentence:** *Which solution meets these requirements?* → which solution satisfies the requirements?
2. **Keywords:** *reduce query costs* + *LEAST operational overhead* (the least administration work).
3. **Scenario:** S3 + CSV + Athena + ad hoc queries.
4. **Likely answer:** convert to **Parquet** and **partition** (with Glue or Firehose). Athena charges per data scanned, and Parquet + partitions scan less.

---

**Practice:** [ejercicios-ingles.en.md](ejercicios-ingles.en.md) · [technical vocabulary](vocabulario-tecnico.en.md)
