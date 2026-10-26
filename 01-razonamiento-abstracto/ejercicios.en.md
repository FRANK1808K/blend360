# 01 · Abstract reasoning: 50 exercises with solutions

> **How to practice:** use a timer. Goal: **≤ 60 s per exercise**. Write down your answer and check the solutions at the **end of each section**. For "real" (drawn) figures, also use the [simulator](../simulator/README.en.md).

---

## A. Number series (15)

*Which number comes next?*

| # | Series | A | B | C | D |
|---|---|---|---|---|---|
| A1 | 3, 7, 11, 15, **?** | 18 | 19 | 20 | 21 |
| A2 | 2, 6, 18, 54, **?** | 108 | 148 | 162 | 216 |
| A3 | 1, 4, 9, 16, 25, **?** | 30 | 34 | 36 | 49 |
| A4 | 2, 3, 5, 8, 12, **?** | 15 | 16 | 17 | 20 |
| A5 | 1, 1, 2, 3, 5, 8, **?** | 11 | 12 | 13 | 14 |
| A6 | 5, 10, 8, 16, 14, **?** | 12 | 18 | 24 | 28 |
| A7 | 100, 95, 85, 70, 50, **?** | 20 | 25 | 30 | 35 |
| A8 | 2, 5, 11, 23, 47, **?** | 94 | 95 | 96 | 71 |
| A9 | 3, 8, 15, 24, 35, **?** | 46 | 47 | 48 | 49 |
| A10 | 1, 2, 6, 24, 120, **?** | 240 | 600 | 720 | 840 |
| A11 | 4, 9, 7, 12, 10, 15, **?** | 13 | 17 | 18 | 20 |
| A12 | 1, 3, 7, 15, 31, **?** | 47 | 62 | 63 | 64 |
| A13 | 2, 3, 5, 7, 11, 13, **?** | 15 | 16 | 17 | 19 |
| A14 | 81, 27, 9, 3, **?** | 0 | 1 | 1.5 | 2 |
| A15 | 1, 10, 3, 20, 5, 30, **?** | 7 | 35 | 40 | 6 |

<details>
<summary>Solutions A</summary>

| # | Ans. | Rule |
|---|---|---|
| A1 | **B** 19 | +4 |
| A2 | **C** 162 | ×3 |
| A3 | **C** 36 | Squares: 1², 2², …, 6² |
| A4 | **C** 17 | Differences +1, +2, +3, +4, **+5** |
| A5 | **C** 13 | Fibonacci: each number is the sum of the previous two |
| A6 | **D** 28 | Alternates ×2 and −2: 14 × 2 = 28 |
| A7 | **B** 25 | Differences −5, −10, −15, −20, **−25** |
| A8 | **B** 95 | ×2 + 1 |
| A9 | **C** 48 | n² − 1: 2²−1, 3²−1, …, 7²−1 = 48 (or differences +5, +7, +9, +11, **+13**) |
| A10 | **C** 720 | Factorials (×2, ×3, ×4, ×5, **×6**) |
| A11 | **A** 13 | Alternates +5 and −2 |
| A12 | **C** 63 | ×2 + 1 (or 2ⁿ − 1) |
| A13 | **C** 17 | Prime numbers |
| A14 | **B** 1 | ÷3 |
| A15 | **A** 7 | Two interleaved series: odd numbers 1, 3, 5, **7** and tens 10, 20, 30 |

</details>

## B. Letter series (7)

*Use the English alphabet (26 letters, no Ñ).*

```text
A B C D E F G H I  J  K  L  M  N  O  P  Q  R  S  T  U  V  W  X  Y  Z
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26
```

> 💡 Write the alphabet with its numbers on your scratch paper at the start of the test: it saves a lot of time.

| # | Series | A | B | C | D |
|---|---|---|---|---|---|
| B1 | A, C, E, G, **?** | H | I | J | K |
| B2 | B, E, H, K, **?** | M | N | O | P |
| B3 | Z, X, V, T, **?** | S | Q | R | P |
| B4 | A, B, D, G, K, **?** | O | P | Q | N |
| B5 | AZ, BY, CX, **?** | DV | EW | DW | CW |
| B6 | A1, C3, E5, **?** | F6 | G7 | G6 | H8 |
| B7 | ACE, BDF, CEG, **?** | DFH | DEF | CFH | EGI |

<details>
<summary>Solutions B</summary>

| # | Ans. | Rule |
|---|---|---|
| B1 | **B** I | +2 (1, 3, 5, 7, **9**) |
| B2 | **B** N | +3 (2, 5, 8, 11, **14**) |
| B3 | **C** R | −2 (26, 24, 22, 20, **18**) |
| B4 | **B** P | +1, +2, +3, +4, **+5** → 11 + 5 = 16 = P |
| B5 | **C** DW | The 1st letter moves forward from A; the 2nd moves backward from Z |
| B6 | **B** G7 | Letters +2, and the number is the letter's position (G = 7) |
| B7 | **A** DFH | Every letter moves +1 in each group |

</details>

## C. D-48 style dominoes (6)

*Tiles `[top|bottom]` with values from 0 to 6. **Circular:** after 6 comes 0.*

| # | Sequence | A | B | C | D |
|---|---|---|---|---|---|
| C1 | [1\|2] [2\|3] [3\|4] [4\|5] **[?\|?]** | [5\|5] | [5\|6] | [6\|5] | [6\|6] |
| C2 | [6\|0] [5\|1] [4\|2] [3\|3] **[?\|?]** | [2\|4] | [4\|2] | [3\|4] | [2\|2] |
| C3 | [0\|6] [2\|5] [4\|4] [6\|3] **[?\|?]** | [8\|2] | [0\|2] | [1\|2] | [1\|3] |
| C4 | [2\|1] [4\|2] [6\|3] [1\|4] **[?\|?]** | [3\|5] | [8\|5] | [2\|5] | [3\|4] |
| C5 | [3\|3] [2\|4] [1\|5] [0\|6] **[?\|?]** | [0\|0] | [6\|0] | [1\|6] | [6\|6] |
| C6 | [1\|1] [2\|3] [3\|5] [4\|0] **[?\|?]** | [5\|2] | [5\|1] | [5\|7] | [4\|2] |

<details>
<summary>Solutions C</summary>

| # | Ans. | Rule |
|---|---|---|
| C1 | **B** [5\|6] | Top +1, bottom +1 |
| C2 | **A** [2\|4] | Top −1, bottom +1 (the sum is always 6) |
| C3 | **C** [1\|2] | Top +2 circular (6 + 2 = 8 → **1**); bottom −1 |
| C4 | **A** [3\|5] | Top +2 circular (6 + 2 → 1, 1 + 2 = **3**); bottom +1 |
| C5 | **B** [6\|0] | Top −1 circular (0 − 1 → **6**); bottom +1 circular (6 + 1 → **0**) |
| C6 | **A** [5\|2] | Top +1; bottom +2 circular (1, 3, 5, 7 → **0**, **2**) |

</details>

## D. Figure series (9)

*Which figure comes next?*

**D1.** `↑  →  ↓  ←  ↑  →  ?`  A) `↑`  B) `←`  C) `↓`  D) `→`

**D2.** `↑  ↗  →  ↘  ?`  A) `↙`  B) `↓`  C) `←`  D) `↗`

**D3.** `○  ◔  ◑  ◕  ?`  A) `◔`  B) `○`  C) `◑`  D) `●`

**D4.** `■□□□  □■□□  □□■□  ?`  A) `■□□□`  B) `□□□■`  C) `□■□□`  D) `□□■■`

**D5.** `▲  ▲▲  ▲▲▲  ?`  A) `▲▲▲▲`  B) `▲▲`  C) `△△△△`  D) `▲▲▲▲▲`

**D6.** `◐  ◓  ◑  ◒  ?`  A) `◑`  B) `◓`  C) `◐`  D) `●`

**D7.** `○  ●●  ○○○  ?`  A) `○○○○`  B) `●●●●`  C) `●●●`  D) `○●○●`

**D8.** The dot moves on a 3×3 grid:

```text
 1       2       3       ?
●··     ·●·     ··●
···     ···     ···
···     ···     ···

 A       B       C       D
···     ···     ●··     ···
··●     ···     ···     ●··
···     ··●     ···     ···
```

**D9.** `★☆☆  ☆★☆  ☆☆★  ?`  A) `☆☆☆`  B) `★☆☆`  C) `☆★☆`  D) `★★★`

<details>
<summary>Solutions D</summary>

| # | Ans. | Rule |
|---|---|---|
| D1 | **C** `↓` | Rotates 90° clockwise |
| D2 | **B** `↓` | Rotates 45° clockwise |
| D3 | **D** `●` | One quarter is filled at each step |
| D4 | **B** `□□□■` | The black square moves one position to the right |
| D5 | **A** `▲▲▲▲` | +1 triangle; the color stays the same (black) |
| D6 | **C** `◐` | The black half rotates 90° clockwise: left → top → right → bottom → **left** |
| D7 | **B** `●●●●` | **Two rules:** the amount goes up by 1 and the color alternates (white, black, white, **black**) |
| D8 | **A** | The dot goes around the **border** clockwise: top-left → top-center → top-right → **middle-right** |
| D9 | **B** `★☆☆` | The star moves right and goes back to the start (cycle of 3) |

</details>

## E. 3×3 matrices (6)

*Which option completes the matrix?*

**E1.**

| | | |
|---|---|---|
| 2 | 4 | 6 |
| 3 | 5 | 8 |
| 4 | 7 | **?** |

A) 10  B) 11  C) 12  D) 9

**E2.**

| | | |
|---|---|---|
| ○ | △ | □ |
| △ | □ | ○ |
| □ | ○ | **?** |

A) ○  B) □  C) △  D) ◇

**E3.**

| | | |
|---|---|---|
| ● | ●● | ●●● |
| ■ | ■■ | ■■■ |
| ▲ | ▲▲ | **?** |

A) ▲  B) ▲▲▲  C) ■■■  D) △△△

**E4.**

| | | |
|---|---|---|
| 2 | 3 | 6 |
| 4 | 5 | 20 |
| 6 | 2 | **?** |

A) 8  B) 10  C) 12  D) 14

**E5.**

| | | |
|---|---|---|
| ○ | ● | ◐ |
| □ | ■ | ◧ |
| △ | ▲ | **?** |

A) △  B) ▲  C) ◭  D) ◐

**E6.**

| | | |
|---|---|---|
| 3 | 4 | 5 |
| 9 | 16 | 25 |
| 27 | 64 | **?** |

A) 100  B) 125  C) 75  D) 36

<details>
<summary>Solutions E</summary>

| # | Ans. | Rule |
|---|---|---|
| E1 | **B** 11 | Column 3 = column 1 + column 2 (4 + 7) |
| E2 | **C** △ | Each row and each column contains ○, △ and □ once (like a sudoku) |
| E3 | **B** ▲▲▲ | The shape is constant per row; the amount grows per column |
| E4 | **C** 12 | Column 3 = column 1 × column 2 (6 × 2) |
| E5 | **C** ◭ | The shape is constant per row; the fill per column: white, black, **half** |
| E6 | **B** 125 | Each column: n, n², n³ → 5³ = 125 |

</details>

## F. Analogies and odd one out (7)

| # | Question | A | B | C | D |
|---|---|---|---|---|---|
| F1 | `○` is to `●` as `□` is to **?** | ○ | ■ | △ | □ |
| F2 | `↑` is to `↓` as `→` is to **?** | ↑ | → | ← | ↗ |
| F3 | 2 is to 8 as 3 is to **?** | 9 | 12 | 27 | 6 |
| F4 | Which one does **not** belong? 3, 5, 7, 9, 11 | 3 | 5 | 9 | 11 |
| F5 | Which one does **not** belong? △ □ ⬠ ○ ⬡ | △ | ⬠ | ○ | ⬡ |
| F6 | Which one does **not** belong? ↑ → ↓ ↗ ← | ↑ | ↗ | ↓ | ← |
| F7 | Which one does **not** belong? 16, 25, 36, 48, 64 | 16 | 36 | 48 | 64 |

<details>
<summary>Solutions F</summary>

| # | Ans. | Rule |
|---|---|---|
| F1 | **B** ■ | The same figure, filled in black |
| F2 | **C** ← | Opposite direction (180° rotation) |
| F3 | **C** 27 | Cube: 2³ = 8 and 3³ = 27 |
| F4 | **C** 9 | The others are prime (9 = 3 × 3) |
| F5 | **C** ○ | The others are polygons (they have sides and vertices) |
| F6 | **B** ↗ | The others point in 90° directions (horizontal/vertical); ↗ is diagonal |
| F7 | **C** 48 | The others are perfect squares (4², 5², 6², 8²) |

</details>

---

## Your result

| Correct (out of 50) | Level | What to do |
|---|---|---|
| 45–50 | Excellent | Move on to the simulator with a timer (30 min) |
| 35–44 | Good | Review the [FORMA-CPR checklist](README.en.md#3-the-rules-that-repeat-the-forma-cpr-checklist) and redo your mistakes in 2 days |
| < 35 | Building up | Do them again without a timer, writing down the rule of each one |

> Remember: the real test uses **drawn figures** with several rules at once. Complement this with the [simulator](../simulator/README.en.md) and the [Mensa Norway test](https://test.mensa.no/).
