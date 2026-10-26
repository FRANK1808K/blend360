# Blend360 All Star: entrance exam preparation

🌐 [Español](README.md) · **English**

[![Checks](https://github.com/FRANK1808K/blend360/actions/workflows/checks.yml/badge.svg)](https://github.com/FRANK1808K/blend360/actions/workflows/checks.yml)
![Exam](https://img.shields.io/badge/exam-Dec%2018%2C%202026-0d6e66)
![AWS AIF-C01](https://img.shields.io/badge/AWS%20AIF--C01-Nov%2016%2C%202026-FF9900?logo=amazonwebservices&logoColor=white)
![Languages](https://img.shields.io/badge/languages-English%20%7C%20Espa%C3%B1ol-1f4e79)

A study repository for the entrance exam of **Blend360's All Star program (talent program) in Colombia**:

| Part | Duration | Topics |
|---|---|---|
| **Abstract reasoning** | 30 min | Figure sequences, matrices, dominoes, number and letter series |
| **Technical test** (in English) | 90 min | SQL · Python · what AWS is and data analytics on AWS · basic algorithms · databases · data structures · problem solving |

Every document exists in **English and Spanish**. The exercises and mock exams are **in English**, like the real test, with a **Spanish translation hidden below each question** for when you get stuck. There is also a technical English module for A2-level speakers. All code solutions are **automatically verified**.

> **Disclaimer:** community study material, **unofficial** and not affiliated with Blend360. All questions are original. What is known about the hiring process comes from public candidate reviews ([see the research](guides/que-evalua-blend360.en.md)).

---

## Where do I start?

| Your situation | Start here |
|---|---|
| 📅 **I want to know what to study each day** | [Study plan: Oct 26 → Dec 18](guides/plan-de-estudio.en.md) (includes the AWS AIF-C01 exam on Nov 16) |
| 🔎 **I want to know how Blend360 evaluates candidates** | [What Blend360 evaluates](guides/que-evalua-blend360.en.md): process reported by candidates, the AWS partnership, questions for the recruiter |
| 🧪 **I want to measure my level now** | [Interactive simulator](simulator/README.en.md) · [Technical mock exam](simulacros/simulacro-tecnico-01.en.md) · [Reasoning mock exam](simulacros/simulacro-razonamiento-01.en.md) |
| 🇬🇧 **My English is basic and I'm worried** | [English plan](english/README.en.md) → [how to read exam questions in English](english/como-leer-preguntas.en.md) |
| ⏰ **The exam is in 2 days** | [48-hour final review](cheatsheets/repaso-final-48h.en.md) + [cheat sheets](cheatsheets/README.en.md) |

## How to use the two languages

1. **Learn** each topic in Spanish first ([Español](README.md)) if the English version is too hard.
2. **Re-read** the same section in English. You will recognize the content, so you learn the English words in context.
3. **Practice** always in English. Open the Spanish translation only when you are blocked, and write down the words you did not know in your [flashcards](flashcards/README.en.md).

## Modules

| # | Module | Content | Practice |
|---|---|---|---|
| 01 | [Abstract reasoning](01-razonamiento-abstracto/README.en.md) | Question types, the **FORMA-CPR** checklist, a strategy for the 30 minutes | [50 exercises](01-razonamiento-abstracto/ejercicios.en.md) + unlimited figures in the [simulator](simulator/README.en.md) |
| 02 | [SQL](02-sql/README.en.md) | From `SELECT` to window functions, NULLs, JOINs, CTEs, interview patterns | [35 exercises](02-sql/ejercicios.en.md) on a real database (SQLite) |
| 03 | [Python](03-python/README.en.md) + [pandas](03-python/pandas.en.md) | Fundamentals, traps, "what is the output?" quiz, pandas ↔ SQL | [25 exercises](03-python/ejercicios.py) with an automatic grader |
| 04 | [Algorithms and data structures](04-algoritmos-y-estructuras/README.en.md) | Big O, data structures, searching and sorting, recursion, patterns, pseudocode | [20 classic problems](04-algoritmos-y-estructuras/problemas.py) with a grader |
| 05 | [Databases](05-bases-de-datos/README.en.md) | Keys, normalization, ACID, indexes, OLTP/OLAP, star schema, lake/warehouse, NoSQL | Self-assessment |
| 06 | [AWS](06-aws/README.en.md) + [data analytics on AWS](06-aws/analisis-de-datos.en.md) | Cloud, IAM, services, pricing; S3, Glue, Athena, Redshift, EMR, Kinesis, QuickSight | [30 questions](06-aws/preguntas.en.md) |
| 07 | [Problem solving](07-resolucion-de-problemas/README.en.md) | The UMPIRE method, time management, logic, percentages, probability, statistics, business cases | Solved exercises |
| 08 | [Statistics and machine learning](08-estadistica-y-ml/README.en.md) | Descriptive stats, probability, inference, **A/B tests**, regression, ML, metrics; a study route through your Drive notes | [25 questions](08-estadistica-y-ml/preguntas.en.md) + [from-scratch script](08-estadistica-y-ml/estadistica_ml_practica.py) |
| EN | [Technical English (A2 → functional)](english/README.en.md) | Exam keywords, false friends, vocabulary, minimum grammar, interview | [Exercises](english/ejercicios-ingles.en.md) + [209 flashcards](flashcards/README.en.md) |

## Practice

```bash
git clone https://github.com/FRANK1808K/blend360.git && cd blend360

# SQL: create the practice database and open a console
cd 02-sql && python3 setup_db.py --shell

# Python: grade your exercises
cd ../03-python && python3 test_ejercicios.py

# Algorithms: grade your problems
cd ../04-algoritmos-y-estructuras && python3 test_problemas.py

# Simulator: open simulator/index.html in your browser
```

You only need **Python 3.8+** (and `pip install pandas` for the pandas practice). There are no other dependencies.

## Structure

```text
blend360/
├── guides/                     Dated study plan + research on the hiring process
├── 01-razonamiento-abstracto/  Abstract reasoning: theory + 50 exercises
├── 02-sql/                     Theory + SQLite database + 35 verified exercises
├── 03-python/                  Theory + 25 exercises + pandas
├── 04-algoritmos-y-estructuras/Algorithms and data structures: theory + 20 problems
├── 05-bases-de-datos/          Databases: theory
├── 06-aws/                     Cloud + data analytics + 30 questions
├── 07-resolucion-de-problemas/ Problem solving: method, logic, statistics, cases
├── 08-estadistica-y-ml/        Statistics, A/B tests and ML + 25 questions
├── english/                    Technical English for A2 speakers
├── simulacros/                 Mock exams: technical (90 min) + reasoning (30 min)
├── simulator/                  Interactive simulator with a timer (ES/EN)
├── cheatsheets/                One-page reviews + 48-hour plan
└── flashcards/                 209 Anki cards
```

Every `X.md` file (Spanish) has an `X.en.md` twin (English).

## Quality

The CI pipeline ([`checks.yml`](.github/workflows/checks.yml)) verifies on every change that:

- The **36 SQL solutions** in both languages run and produce exactly the published "expected result" (`02-sql/check_solutions.py`).
- The **25 Python solutions**, the **20 algorithm solutions** and the statistics and ML formulas (`08-estadistica-y-ml/estadistica_ml_practica.py`) pass their tests.
- The Markdown follows the style rules (`markdownlint`), every document has its twin in the other language and every internal link works (`scripts/check_docs.py`).

## Key dates

| Date | Event |
|---|---|
| Oct 26, 2026 | The plan starts |
| **Nov 16, 2026** | AWS Certified AI Practitioner (AIF-C01) |
| Nov 17, 2026 | The "Blend360 in depth" phase starts |
| Dec 16–17, 2026 | Final review |
| **Dec 18, 2026** | Blend360 All Star exam |
