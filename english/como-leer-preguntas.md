# Cómo leer preguntas de examen en inglés (sin bloquearte)

> En una prueba técnica, **una sola palabra** puede cambiar la respuesta: *NOT*, *EXCEPT*, *LEAST*, *at least*. Esta guía te enseña a encontrarlas y a no caer en los "falsos amigos".

---

## 1. Estrategia de lectura en 4 pasos (para cada pregunta)

1. **Lee primero la ÚLTIMA oración:** ahí está la pregunta real (*"Which service should the company use?"*).
2. **Busca las palabras que cambian el sentido** (tabla 2): NOT, EXCEPT, LEAST, MOST, BEST, TWO…
3. **Lee el escenario** buscando las **palabras clave técnicas** (*real-time*, *serverless*, *lowest cost*, *without code*). No necesitas entender cada palabra.
4. **Elimina opciones** y elige. Si una palabra te bloquea, **sáltala** y deduce por contexto.

> 🧠 **No traduzcas palabra por palabra.** Busca el *qué piden* + las *restricciones*.

## 2. Palabras que cambian TODO (memorízalas)

| Inglés | Español | Ejemplo | Trampa |
|---|---|---|---|
| **NOT** | NO | *Which is **NOT** a benefit…?* | Te piden la **falsa** |
| **EXCEPT** | EXCEPTO | *All of the following are true **EXCEPT**…* | Te piden la **falsa** |
| **LEAST** | MENOS | *the **least** expensive* = el más barato | Lo contrario de *most* |
| **MOST** | MÁS | *the **most** cost-effective* = el más económico (mejor relación costo-beneficio) | |
| **BEST** | MEJOR | *Which option **best** describes…* | Puede haber varias correctas; elige la mejor |
| **Choose TWO / Select all that apply** | Elige DOS / todas las que apliquen | | Marca exactamente las que pide |
| **at least** | al menos (≥) | *at least 3 orders* = 3 o más | ≥, no > |
| **at most** | como máximo (≤) | *at most 5* = 5 o menos | ≤ |
| **more than / greater than** | más que (>) | *more than 3* = 4, 5… | **No** incluye el 3 |
| **fewer than / less than** | menos que (<) | | |
| **between X and Y** | entre X y Y | En SQL `BETWEEN` **incluye** los extremos | |
| **inclusive / exclusive** | incluido / excluido | *range 1 to 10 inclusive* | |
| **only** | solo/únicamente | *return **only** the customers who…* | Filtro |
| **each / every / per** | cada / por | *revenue **per** month* = `GROUP BY month` | Agrupación |
| **unique / distinct** | únicos / distintos | *count **distinct** users* = `COUNT(DISTINCT ...)` | |
| **both… and** | tanto… como (los dos) | *bought **both** A **and** B* | Condición de grupo (`HAVING`) |
| **either… or** | o… o (uno de los dos) | | |
| **neither… nor** | ni… ni | | |
| **unless** | a menos que | | = *if not* |
| **otherwise** | de lo contrario / si no | *return the value, **otherwise** return -1* | El `else` |
| **respectively** | respectivamente | | El orden importa |
| **assume** | suponga | *Assume the list is sorted* | Te da una condición que puedes usar |
| **given** | dado(s) | *Given an array of integers…* | La entrada |
| **return** | devolver/retornar | *Return the index…* | La salida |
| **output** | salida / qué imprime | *What is the **output** of this code?* | |
| **in-place** | sin crear otra estructura | *sort the array **in-place*** | Espacio O(1) |
| **consecutive** | consecutivos | *3 **consecutive** days* | Seguidos, sin saltos |
| **ascending / descending** | ascendente / descendente | *sorted in **descending** order* | Mayor a menor |
| **round to 2 decimals** | redondear a 2 decimales | | `ROUND(x, 2)` |
| **null / missing / empty** | nulo / faltante / vacío | | Casos borde |
| **edge case** | caso borde/límite | | |
| **ties** | empates | *In case of **ties**, return…* | Mira cómo desempatar |

## 3. Palabras clave de escenario (sobre todo en AWS)

| Inglés | Significa | Te apunta a… |
|---|---|---|
| *cost-effective / lowest cost / cheapest* | lo más barato | Spot, S3 Glacier, serverless, Athena |
| *least operational overhead / fully managed* | lo que menos trabajo de administración requiere | Servicios serverless/gestionados |
| *without managing servers / serverless* | sin servidores | Lambda, Athena, Glue, Fargate |
| *real time / near real time* | tiempo real / casi tiempo real | Kinesis Data Streams / Firehose |
| *highly available / fault tolerant* | alta disponibilidad / tolerante a fallos | Multi-AZ |
| *scalable / scale automatically* | escalable / escala solo | Auto Scaling, serverless |
| *ad hoc queries* | consultas puntuales, no planificadas | Athena |
| *without writing code / no-code* | sin programar | DataBrew, AppFlow, Firehose, QuickSight |
| *compliance / audit* | cumplimiento / auditoría | CloudTrail, Config |
| *sensitive data / PII* | datos personales sensibles | Macie, KMS, Lake Formation |
| *least privilege* | mínimo privilegio | IAM roles/policies |
| *long-term / rarely accessed / archive* | largo plazo / acceso raro / archivar | Glacier |

## 4. Falsos amigos (palabras que parecen español pero NO lo son)

| Inglés | ❌ No significa | ✅ Significa |
|---|---|---|
| **actual / actually** | actual / actualmente | **real / en realidad** |
| **eventually** | eventualmente (a veces) | **finalmente, con el tiempo** (*eventual consistency* = consistencia que se alcanza con el tiempo) |
| **library** | librería | **biblioteca** (de código) |
| **record** | recordar | **registro** (una fila) |
| **argument** | argumento (discusión) | **argumento/parámetro** de una función (este sí coincide) |
| **assist** | asistir (ir a) | **ayudar** |
| **attend** | atender | **asistir** (a una reunión) |
| **realize** | realizar | **darse cuenta** |
| **support** | soportar (aguantar) | **dar soporte, ser compatible con, apoyar** |
| **sensible** | sensible | **sensato** (*sensitive* = sensible) |
| **exit** | éxito | **salida** (*success* = éxito) |
| **current** | corriente | **actual** (*current version*) |
| **commit** | cometer | **confirmar** (cambios en git / transacción) |
| **deprecated** | depreciado | **obsoleto** (no se recomienda usar) |
| **fault** | falta | **fallo, error** |
| **expire** | expirar (morir) | **vencer, caducar** |
| **compliance** | complacencia | **cumplimiento normativo** |
| **constraint** | constreñimiento | **restricción** (de BD) |
| **instance** | instancia (trámite) | **instancia** (servidor, objeto) |

## 5. Verbos de instrucción en enunciados de código

| Verbo | Qué te piden |
|---|---|
| *Write a query/function that…* | Escribe una consulta/función que… |
| *Implement* | Implementa (programa) |
| *Find / Retrieve / Fetch* | Encuentra / obtén |
| *List / Display / Show* | Lista / muestra |
| *Count* | Cuenta |
| *Calculate / Compute* | Calcula |
| *Determine* | Determina |
| *Rank* | Ordena por posición (ranking) |
| *Filter out* | **Excluye** (¡quita!) |
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

## 6. Ejemplo guiado

> *A company stores clickstream data in Amazon S3 as CSV files. Analysts run ad hoc SQL queries on the data using Amazon Athena. The company wants to **reduce query costs** with the **LEAST operational overhead**. Which solution meets these requirements?*

1. **Última oración:** *Which solution meets these requirements?* → ¿Qué solución cumple los requisitos?
2. **Palabras clave:** *reduce query costs* (bajar el costo de las consultas) + *LEAST operational overhead* (lo que menos administración requiera).
3. **Escenario:** S3 + CSV + Athena + consultas ad hoc.
4. **Respuesta probable:** convertir a **Parquet** y **particionar** (con Glue o Firehose). Athena cobra por datos escaneados, y Parquet + particiones escanean menos.

---

**Practica:** [ejercicios-ingles.md](ejercicios-ingles.md) · [vocabulario técnico](vocabulario-tecnico.md)
