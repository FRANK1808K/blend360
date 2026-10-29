# Entrance test simulator

[Español](README.md) · **English**

A browser simulator for both parts of the test, with a **code lab for writing code**, available in **English and Spanish** (ES/EN switch at the top):

| Mode | Questions | Time | Content |
|---|---|---|---|
| **Full assessment** | 30 + 40 + 3 queries | 30 + 50 + 40 min | The three sections back to back, like test day: an instructions screen, a timer per section, no going back to a submitted section and a final report with the score per section and per topic |
| **Abstract reasoning** | 30 | 30:00 | **Randomly generated** figures: rotations, amounts, positions, sides, quadrants, two-rule figures, 3×3 matrices, D-48 dominoes, number and letter series. Difficulty increases |
| **Technical (multiple choice)** | 40 | 50:00 | A bank of 60 questions **in English**: SQL (15), Python (15), algorithms (12), databases (8), AWS (10) |
| **Practice by topic** | Unlimited | No timer | Immediate feedback with an explanation. Also includes **12 statistics and ML questions** (practice only) |
| **SQL lab** | 36 | Target per level | Write real queries; they are graded instantly |
| **SQL challenge** | 5 | 60:00 | 5 intermediate-to-challenge queries with no solutions (like the test reported on Glassdoor) |
| **Python lab** | 45 | Target per exercise | 25 Python exercises + 20 algorithm problems, with automated tests |

**Made for learning English:** at the top you choose the **question language**. In **English** (like the real exam) every question has a **"Show Spanish translation"** button; in **Spanish** (to learn a topic) it has **"Show English"** with the original. The interface language (ES/EN) is chosen separately.

**Design:** an assessment-platform interface in Blend's colours (navy, cyan and aqua): a header with the timer, a question navigator, flags for review and a confirmation before submitting each section. **Light** or **dark** mode with the moon or sun button (remembered in your browser), the **Urbanist** font with **Archivo** headings and smooth transitions between screens and when you answer. If your system asks for reduced motion, the animations are turned off.

When you finish a mock exam you see your score, the result **per topic** and a question-by-question review with explanations. Your last 8 attempts are saved in your browser.

> **AWS AI Practitioner Simulator:** To practice the official AIF-C01 exam (65 questions, 90 minutes) with language switching and detailed rationales, visit the [AWS AI Practitioner Simulator](../aws-ai-practitioner/simulator/README.md).

## Code lab

No options to choose from here: **you write the code**, run it, and the lab grades it. It uses the same exercises, solutions and tests as the repository ([`scripts/build_lab.py`](../scripts/build_lab.py) embeds them, and CI checks they are up to date).

- **SQL:** the [35 exercises of module 02](../02-sql/ejercicios.en.md) on the same store database, with SQLite inside the browser ([sql.js](https://sql.js.org/)). **Check** compares your result with the solution's: it tells you if you have too many or too few rows or columns, if the order is wrong or if values differ. It grades the **result**, not how the query is written: aliases, column names and column order do not matter, extra columns cost nothing, row order only counts when the statement asks for it and, when the statement does not say which columns to show, returning the right rows is enough. SQLite errors come with a short explanation. There is a tables panel, a **free editor** and the **challenge of 5 queries in 60 minutes**.
- **Python:** the [25 exercises of module 03](../03-python/ejercicios.py) and the [20 problems of module 04](../04-algoritmos-y-estructuras/problemas.py), with Python 3 in the browser ([Pyodide](https://pyodide.org/)). You see every test case (✓/✗), what you `print()` and errors with their line number. A loop that never ends is stopped after 8 seconds.
- Your code is saved in your browser, so you can close it and continue later. `Ctrl + Enter` runs and `Tab` indents.
- The first time, the engine is downloaded (SQL about 0.7 MB; Python about 12 MB). It needs an internet connection.

## How to open it

- **Online (recommended, works on your phone):** [frank1808k.github.io/blend360/simulador](https://frank1808k.github.io/blend360/simulador/).
- **Locally:** double-click `simulator/index.html` to open it in any browser (nothing to install).
- **GitHub Pages:** the [`pages.yml`](../.github/workflows/pages.yml) workflow republishes it at `/simulador/` every time the simulator or the documentation changes on the repository's default branch, together with the [study hub website](https://frank1808k.github.io/blend360/index.en.html). If it ever stops publishing, check *Settings → Pages → Source: **GitHub Actions***.

**Keyboard shortcuts:** `A`–`D` or `1`–`4` to answer, `←` `→` to move between questions, `T` to show the translation.

> All questions are original practice questions; none come from a real exam.
