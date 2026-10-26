# Interactive simulator: Simulacro 30·90

🌐 [Español](README.md) · **English**

A browser simulator for both parts of the test, available in **English and Spanish** (ES/EN switch at the top):

| Mode | Questions | Time | Content |
|---|---|---|---|
| **Abstract reasoning** | 30 | 30:00 | **Randomly generated** figures: rotations, amounts, positions, sides, quadrants, two-rule figures, 3×3 matrices, D-48 dominoes, number and letter series. Difficulty increases |
| **Technical (multiple choice)** | 40 | 50:00 | A bank of 60 questions **in English**: SQL (15), Python (15), algorithms (12), databases (8), AWS (10) |
| **Practice by topic** | Unlimited | No timer | Immediate feedback with an explanation. Also includes **12 statistics and ML questions** (practice only) |

**Made for learning English:** every technical question has a **"Show translation"** button that reveals the Spanish version. Try to answer in English first, like in the real exam.

When you finish a mock exam you see your score, the result **per topic** and a question-by-question review with explanations. Your last 8 attempts are saved in your browser.

## How to open it

- **Online (recommended, works on your phone):** the published version at the link Claude shared with you.
- **Locally:** double-click `simulator/index.html` to open it in any browser (nothing to install).
- **GitHub Pages:** the [`pages.yml`](../.github/workflows/pages.yml) workflow publishes the simulator at `https://frank1808k.github.io/blend360/` every time it changes on `main`. One-time setup: *Settings → Pages → Source: **GitHub Actions***. Your repository is **private**: on GitHub's free plan, Pages only works if you make it public. With GitHub Pro, create the variable `PAGES_ENABLED = true` (*Settings → Secrets and variables → Actions → Variables*). Until then, the workflow is skipped without failing.

**Keyboard shortcuts:** `A`–`D` or `1`–`4` to answer, `←` `→` to move between questions, `T` to show the translation.

> All questions are original practice questions; none come from a real exam.
