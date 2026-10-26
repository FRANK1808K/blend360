# Repaso final: últimas 48 horas (16–17 de diciembre)

> **Regla de oro:** las últimas 48 horas **no** son para aprender cosas nuevas. Son para **repasar, descansar y llegar con la mente fresca**.

## 48 horas antes (16 de diciembre)

| Bloque | Qué hacer | Tiempo |
|---|---|---|
| Mañana | Lee los 4 cheatsheets: [SQL](sql.md) · [Python](python.md) · [Algoritmos](algoritmos.md) · [AWS + BD](aws-y-bases-de-datos.md) | 1 h |
| Mañana | Rehaz **sin mirar** los SQL 16, 26, 28, 32 y 34 de [ejercicios.md](../02-sql/ejercicios.md) | 45 min |
| Tarde | 1 simulacro de razonamiento abstracto de 30 min en el [simulador](../simulator/index.html) | 30 min |
| Tarde | Repasa **solo** los errores que anotaste en tus simulacros | 45 min |
| Noche | Flashcards (20 min) + lee en voz alta tu presentación en inglés | 30 min |

## 24 horas antes (17 de diciembre)

- [ ] **Máximo 2 horas de estudio ligero:** cheatsheets + flashcards. Nada nuevo.
- [ ] Si la prueba es online: verifica el **computador, la cámara, el micrófono, internet** y el cargador. Cierra las apps que puedan interrumpir (actualizaciones, notificaciones).
- [ ] Prepara: documento de identidad, agua, **papel y lápiz** (si están permitidos) para las cuentas y el alfabeto.
- [ ] Revisa el correo de citación: **hora (ojo con la zona horaria)**, enlace, plataforma y reglas.
- [ ] Haz ejercicio suave, cena liviana y **duerme 7–8 horas**.

## El día del examen (18 de diciembre)

- [ ] Desayuna. Llega o conéctate **15 minutos antes**.
- [ ] En el papel de borrador escribe: el alfabeto con números (A1…Z26) y el orden SQL (`FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY`).
- [ ] **Razonamiento (30 min):** ~1 minuto por pregunta. Si no ves la regla en 60 s → **marca, adivina, sigue**. Revisa con la checklist **FORMA-CPR** (forma, orientación, relleno, movimiento, aumento, combinación, proporción, repetición).
- [ ] **Técnico (90 min):** mira primero todas las preguntas. Resuelve primero lo fácil. En código, entrega **algo que funcione** antes de optimizar. Prueba los casos borde.
- [ ] **Inglés:** lee primero la **última oración**. Busca NOT / EXCEPT / LEAST / at least. No traduzcas palabra por palabra.
- [ ] No dejes preguntas en blanco (si no hay penalización por error).
- [ ] Respira. Si una pregunta te pone nervioso, sáltala: **una pregunta no define el resultado**.

## Las 15 cosas que más se olvidan

1. `WHERE` filtra filas; `HAVING` filtra grupos.
2. `= NULL` nunca funciona → `IS NULL`.
3. `COUNT(*)` vs. `COUNT(col)` (este ignora los NULL).
4. `LEFT JOIN` + filtro en el `WHERE` = `INNER JOIN`.
5. `RANK` 1, 1, 3 vs. `DENSE_RANK` 1, 1, 2.
6. División entera: `100.0 *`.
7. Python: `.sort()` devuelve `None`; `sorted()` devuelve una lista nueva.
8. `b = a` no copia la lista.
9. Búsqueda binaria O(log n) y solo sobre datos **ordenados**.
10. Pila = LIFO; cola = FIFO; BFS usa una cola.
11. Merge sort O(n log n) siempre; quick sort O(n²) en el peor caso.
12. 3NF = sin dependencias transitivas; ACID: Atomicidad = todo o nada.
13. Athena = SQL serverless sobre S3; Redshift = data warehouse; Glue = ETL + catálogo.
14. Kinesis Data Streams = tiempo real; Firehose = entrega sin código.
15. CloudTrail = quién hizo qué; responsabilidad compartida: los datos y el IAM son del cliente.

**¡Tú puedes! 💪 You've got this!**
