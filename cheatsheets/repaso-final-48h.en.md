# Final review: the last 48 hours (December 16–17)

[Español](repaso-final-48h.md) · **English**

> **Golden rule:** the last 48 hours are **not** for learning new things. They are for **reviewing, resting and arriving with a fresh mind**.

## 48 hours before (December 16)

| Block | What to do | Time |
|---|---|---|
| Morning | Read the 5 cheat sheets: [SQL](sql.en.md) · [Python](python.en.md) · [Algorithms](algoritmos.en.md) · [AWS + DB](aws-y-bases-de-datos.en.md) · [Statistics + ML](estadistica-ml.en.md) | 1 h |
| Morning | Redo SQL 16, 26, 28, 32 and 34 from the [exercises](../02-sql/ejercicios.en.md) **without looking** | 45 min |
| Afternoon | 1 abstract reasoning mock exam of 30 min in the [simulator](../simulator/README.en.md) | 30 min |
| Afternoon | Review **only** the mistakes you wrote down in your mock exams | 45 min |
| Evening | Flashcards (20 min) + read your self-introduction out loud | 30 min |

## 24 hours before (December 17)

- [ ] **At most 2 hours of light study:** cheat sheets + flashcards. Nothing new.
- [ ] If the test is online: check your **computer, camera, microphone, Internet** and charger. Close apps that could interrupt you (updates, notifications).
- [ ] Prepare: ID document, water, **paper and pencil** (if allowed) for calculations and the alphabet.
- [ ] Check the invitation email: **time (watch the time zone)**, link, platform and rules.
- [ ] Light exercise, a light dinner and **7–8 hours of sleep**.

## Exam day (December 18)

- [ ] Have breakfast. Arrive or log in **15 minutes early**.
- [ ] On your scratch paper write: the alphabet with numbers (A1…Z26) and the SQL order (`FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY`).
- [ ] **Reasoning (30 min):** ~1 minute per question. If you do not see the rule in 60 s → **flag, guess, move on**. Check with the **FORMA-CPR** checklist (form, orientation, fill, movement, amount, combination, proportion, repetition).
- [ ] **Technical (90 min):** look at all the questions first. Solve the easy ones first. In code, submit **something that works** before optimizing. Test the edge cases.
- [ ] **English:** read the **last sentence** first. Look for NOT / EXCEPT / LEAST / at least. Do not translate word by word.
- [ ] Do not leave questions blank (if wrong answers are not penalized).
- [ ] Breathe. If a question makes you nervous, skip it: **one question does not decide the result**.

## The 15 things people forget most

1. `WHERE` filters rows; `HAVING` filters groups.
2. `= NULL` never works → `IS NULL`.
3. `COUNT(*)` vs. `COUNT(col)` (the second ignores NULLs).
4. `LEFT JOIN` + a filter in the `WHERE` = `INNER JOIN`.
5. `RANK` 1, 1, 3 vs. `DENSE_RANK` 1, 1, 2.
6. Integer division: `100.0 *`.
7. Python: `.sort()` returns `None`; `sorted()` returns a new list.
8. `b = a` does not copy the list.
9. Binary search is O(log n) and only works on **sorted** data.
10. Stack = LIFO; queue = FIFO; BFS uses a queue.
11. Merge sort is always O(n log n); quick sort is O(n²) in the worst case.
12. 3NF = no transitive dependencies; ACID: Atomicity = all or nothing.
13. Athena = serverless SQL on S3; Redshift = data warehouse; Glue = ETL + catalog.
14. Kinesis Data Streams = real time; Firehose = delivery without code.
15. CloudTrail = who did what; shared responsibility: data and IAM belong to the customer.

**You've got this! ¡Tú puedes!**
