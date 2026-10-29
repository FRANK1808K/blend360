# Blend360 All Star: entrance exam preparation

[Español](README.md) · **English**

[![Checks](https://github.com/FRANK1808K/blend360/actions/workflows/checks.yml/badge.svg)](https://github.com/FRANK1808K/blend360/actions/workflows/checks.yml)
![Exam](https://img.shields.io/badge/exam-Dec%2018%2C%202026-043058)
![AWS AIF-C01](https://img.shields.io/badge/AWS%20AIF--C01-Nov%2016%2C%202026-FF9900?logo=amazonwebservices&logoColor=white)
![Languages](https://img.shields.io/badge/languages-English%20%7C%20Espa%C3%B1ol-0b6e86)

A study repository for the entrance exam of **Blend360's All Star program (talent program) in Colombia**:

| Part | Duration | Topics |
|---|---|---|
| **Abstract reasoning** | 30 min | Figure sequences, matrices, dominoes, number and letter series |
| **Technical test** (in English) | 90 min | SQL · Python · what AWS is and data analytics on AWS · basic algorithms · databases · data structures · problem solving |

Every document exists in **English and Spanish**. The exercises and mock exams are **in English**, like the real test, with a **Spanish translation hidden below each question** for when you get stuck. There is also a technical English module for A2-level speakers. All code solutions are **automatically verified**.

> **Disclaimer:** community study material, **unofficial** and not affiliated with Blend360. All questions are original. What is known about the hiring process comes from public candidate reviews ([see the research](guides/que-evalua-blend360.en.md)).

**Online, nothing to install (also on your phone):** [Study hub website](https://frank1808k.github.io/blend360/index.en.html) (all the material organised into *Study · Assess · Review*, search, light/dark mode, **saved progress**) · [Simulator + code lab](https://frank1808k.github.io/blend360/simulador/) · [AIF-C01 simulator](https://frank1808k.github.io/blend360/simulador-aif/)

---

## Where do I start?

| Your situation | Start here |
|---|---|
| **I want to know what to study each day** | [Study plan: Oct 26 → Dec 18](guides/plan-de-estudio.en.md) (includes the AWS AIF-C01 exam on Nov 16) |
| **I want to know how Blend360 evaluates candidates** | [What Blend360 evaluates](guides/que-evalua-blend360.en.md): process reported by candidates, the AWS partnership, questions for the recruiter |
| **I want to measure my level now** | [Interactive simulator](simulator/README.en.md) · [Technical mock exam](simulacros/simulacro-tecnico-01.en.md) · [Reasoning mock exam](simulacros/simulacro-razonamiento-01.en.md) |
| **I want to practice writing code** | [The simulator's code lab](simulator/README.en.md#code-lab): write SQL or Python in the browser (also on your phone) and get it graded instantly |
| **My English is basic and I'm worried** | [English plan](english/README.en.md) → [how to read exam questions in English](english/como-leer-preguntas.en.md) |
| **The exam is in 2 days** | [48-hour final review](cheatsheets/repaso-final-48h.en.md) + [cheat sheets](cheatsheets/README.en.md) |

## How to use the two languages

1. **Learn** each topic in Spanish first ([Español](README.md)) if the English version is too hard.
2. **Re-read** the same section in English. You will recognize the content, so you learn the English words in context.
3. **Practice** always in English. Open the Spanish translation only when you are blocked, and write down the words you did not know in your [flashcards](flashcards/README.en.md).

## Modules

| # | Module | Content | Practice |
|---|---|---|---|
| 01 | [Abstract reasoning](01-razonamiento-abstracto/README.en.md) | Question types, the **FORMA-CPR** checklist, a strategy for the 30 minutes | [50 exercises](01-razonamiento-abstracto/ejercicios.en.md) + unlimited figures in the [simulator](simulator/README.en.md) |
| 02 | [SQL](02-sql/README.en.md) | From `SELECT` to window functions, NULLs, JOINs, CTEs, interview patterns | [35 exercises](02-sql/ejercicios.en.md) on a real database (SQLite), also in the [SQL lab](simulator/README.en.md#code-lab) |
| 03 | [Python](03-python/README.en.md) + [pandas](03-python/pandas.en.md) | Fundamentals, traps, "what is the output?" quiz, pandas ↔ SQL | [25 exercises](03-python/ejercicios.py) with an automatic grader, also in the [Python lab](simulator/README.en.md#code-lab) |
| 04 | [Algorithms and data structures](04-algoritmos-y-estructuras/README.en.md) | Big O, data structures, searching and sorting, recursion, patterns, pseudocode | [20 classic problems](04-algoritmos-y-estructuras/problemas.py) with a grader, also in the [code lab](simulator/README.en.md#code-lab) |
| 05 | [Databases](05-bases-de-datos/README.en.md) | Keys, normalization, ACID, indexes, OLTP/OLAP, star schema, lake/warehouse, NoSQL | Self-assessment |
| 06 | [AWS](06-aws/README.en.md) + [data analytics on AWS](06-aws/analisis-de-datos.en.md) | Cloud, IAM, services, pricing; S3, Glue, Athena, Redshift, EMR, Kinesis, QuickSight | [30 questions](06-aws/preguntas.en.md) |
| 07 | [Problem solving](07-resolucion-de-problemas/README.en.md) | The UMPIRE method, time management, logic, percentages, probability, statistics, business cases | Solved exercises |
| 08 | [Statistics and machine learning](08-estadistica-y-ml/README.en.md) | Descriptive stats, probability, inference, **A/B tests**, regression, ML, metrics; a study route through your Drive notes | [25 questions](08-estadistica-y-ml/preguntas.en.md) + [from-scratch script](08-estadistica-y-ml/estadistica_ml_practica.py) |
| EN | [Technical English (A2 → functional)](english/README.en.md) | Exam keywords, false friends, vocabulary, minimum grammar, interview | [Exercises](english/ejercicios-ingles.en.md) + [209 flashcards](flashcards/README.en.md) |
| AI | [AWS AI Practitioner (AIF-C01)](aws-ai-practitioner/README.en.md) | 5 official domains (v1.1), Bedrock, SageMaker, responsible AI, governance, RAG lab, cheatsheets | [2 mock exams (130 questions)](aws-ai-practitioner/practice-questions/README.md) + [simulator](aws-ai-practitioner/simulator/README.md) + [109 flashcards](aws-ai-practitioner/flashcards/README.md) |

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

## Study website (Quarto)

The [study hub](https://frank1808k.github.io/blend360/index.en.html) brings the whole repository together in a site built with [Quarto](https://quarto.org/), organised by goal:

| Section | What it contains |
|---|---|
| **Study** | Study map with priorities and hours, the theory of every module and technical English |
| **Assess** | Assessment path with goals, exercises by topic, mock exams and the simulator |
| **Review** | Cheat sheets (with a print button), the final 48-hour review and flashcards |
| **AIF-C01** | The 5 domains, questions per domain, 2 mock exams, cheat sheets, strategy, lab and resources |
| **Progress** | Pages studied, mock exam log with a chart, mistake notebook with review dates, simulator attempts and a backup |

**Design:** Blend360's palette (navy `#043058`, cyan `#1DF3F4`, aqua `#A2F3F3` on a warm background), geometric type (Urbanist, Archivo headings), line icons with no emojis, light or dark mode, page-to-page transitions and smooth animations that turn off if your system asks for reduced motion. The simulator uses the same identity and an assessment-platform interface.

Also: the home page shows **what to do this week** according to the plan and the countdown to both exams; the study plan's checkboxes can be ticked and are saved; every page has buttons to mark it as studied, show or hide all solutions and print it; and the AIF-C01 module's diagrams are drawn.

The repository's Markdown remains the single source: [`scripts/build_site.py`](scripts/build_site.py) adapts it and renders it together with [`quarto/`](quarto/) (config, theme, home page, hubs and JavaScript). To build it on your computer you need [Quarto](https://quarto.org/docs/get-started/) 1.10 or later (CI uses 1.10.18):

```bash
python3 scripts/build_site.py            # → _site/ (open _site/index.html)
python3 scripts/build_site.py --preview  # live preview
```

> When you add a new document, add it to `NAV` in `scripts/build_site.py`: the build fails if a page is not in the navigation.

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
├── aws-ai-practitioner/        Full AWS Certified AI Practitioner (AIF-C01) preparation
├── 07-resolucion-de-problemas/ Problem solving: method, logic, statistics, cases
├── 08-estadistica-y-ml/        Statistics, A/B tests and ML + 25 questions
├── english/                    Technical English for A2 speakers
├── simulacros/                 Mock exams: technical (90 min) + reasoning (30 min)
├── simulator/                  Simulator + code lab (ES/EN, light/dark mode)
├── quarto/                     Study website (Quarto): config, theme, home page, hubs and progress
├── scripts/                    Document checks and the lab and website builders
├── cheatsheets/                One-page reviews + 48-hour plan
└── flashcards/                 209 Anki cards
```

Every `X.md` file (Spanish) has an `X.en.md` twin (English).

## Quality

The CI pipeline ([`checks.yml`](.github/workflows/checks.yml)) verifies on every change that:

- The **36 SQL solutions** in both languages run and produce exactly the published "expected result" (`02-sql/check_solutions.py`).
- The **25 Python solutions**, the **20 algorithm solutions** and the statistics and ML formulas (`08-estadistica-y-ml/estadistica_ml_practica.py`) pass their tests.
- The Markdown follows the style rules (`markdownlint`), every document has its twin in the other language and every internal link works (`scripts/check_docs.py`).
- The Quarto study website builds with no warnings or broken links/anchors, and every page is in the navigation (`scripts/build_site.py --strict`).
- The simulator's code lab uses exactly the same exercises, solutions and tests as the repository (`scripts/build_lab.py --check`).

## Key dates

| Date | Event |
|---|---|
| Oct 26, 2026 | The plan starts |
| **Nov 16, 2026** | AWS Certified AI Practitioner (AIF-C01) |
| Nov 17, 2026 | The "Blend360 in depth" phase starts |
| Dec 16–17, 2026 | Final review |
| **Dec 18, 2026** | Blend360 All Star exam |
