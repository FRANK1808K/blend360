# 01 · Razonamiento abstracto: 50 ejercicios con solución

**Español** · [English](ejercicios.en.md)

> **Cómo practicar:** cronómetro en mano. Meta: **≤ 60 s por ejercicio**. Anota tu respuesta y revisa las soluciones al **final de cada sección**. Para figuras "reales" (dibujadas), usa también el [simulador](../simulator/index.html).
>
> Las instrucciones vienen en inglés y español para que te acostumbres: *"Which option comes next in the sequence?"* = ¿Qué opción sigue en la secuencia?

---

## A. Series numéricas (15)

*Which number comes next? / ¿Qué número sigue?*

| # | Serie | A | B | C | D |
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
| A14 | 81, 27, 9, 3, **?** | 0 | 1 | 1,5 | 2 |
| A15 | 1, 10, 3, 20, 5, 30, **?** | 7 | 35 | 40 | 6 |

<details>
<summary>Soluciones A</summary>

| # | Resp. | Regla |
|---|---|---|
| A1 | **B** 19 | +4 |
| A2 | **C** 162 | ×3 |
| A3 | **C** 36 | Cuadrados: 1², 2², …, 6² |
| A4 | **C** 17 | Diferencias +1, +2, +3, +4, **+5** |
| A5 | **C** 13 | Fibonacci: cada número es la suma de los dos anteriores |
| A6 | **D** 28 | Alterna ×2 y −2: 14 × 2 = 28 |
| A7 | **B** 25 | Diferencias −5, −10, −15, −20, **−25** |
| A8 | **B** 95 | ×2 + 1 |
| A9 | **C** 48 | n² − 1: 2²−1, 3²−1, …, 7²−1 = 48 (o diferencias +5, +7, +9, +11, **+13**) |
| A10 | **C** 720 | Factoriales (×2, ×3, ×4, ×5, **×6**) |
| A11 | **A** 13 | Alterna +5 y −2 |
| A12 | **C** 63 | ×2 + 1 (o 2ⁿ − 1) |
| A13 | **C** 17 | Números primos |
| A14 | **B** 1 | ÷3 |
| A15 | **A** 7 | Dos series intercaladas: impares 1, 3, 5, **7** y decenas 10, 20, 30 |

</details>

## B. Series de letras (7)

*Use the English alphabet (26 letters, no Ñ) / Usa el alfabeto inglés (sin Ñ).*

```text
A B C D E F G H I  J  K  L  M  N  O  P  Q  R  S  T  U  V  W  X  Y  Z
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26
```

> **Consejo:** Escribe el alfabeto con sus números en el papel de borrador al empezar la prueba: te ahorra mucho tiempo.

| # | Serie | A | B | C | D |
|---|---|---|---|---|---|
| B1 | A, C, E, G, **?** | H | I | J | K |
| B2 | B, E, H, K, **?** | M | N | O | P |
| B3 | Z, X, V, T, **?** | S | Q | R | P |
| B4 | A, B, D, G, K, **?** | O | P | Q | N |
| B5 | AZ, BY, CX, **?** | DV | EW | DW | CW |
| B6 | A1, C3, E5, **?** | F6 | G7 | G6 | H8 |
| B7 | ACE, BDF, CEG, **?** | DFH | DEF | CFH | EGI |

<details>
<summary>Soluciones B</summary>

| # | Resp. | Regla |
|---|---|---|
| B1 | **B** I | +2 (1, 3, 5, 7, **9**) |
| B2 | **B** N | +3 (2, 5, 8, 11, **14**) |
| B3 | **C** R | −2 (26, 24, 22, 20, **18**) |
| B4 | **B** P | +1, +2, +3, +4, **+5** → 11 + 5 = 16 = P |
| B5 | **C** DW | La 1.ª letra avanza desde A; la 2.ª retrocede desde Z |
| B6 | **B** G7 | Letras +2 y el número es la posición de la letra (G = 7) |
| B7 | **A** DFH | Cada letra avanza +1 en cada grupo |

</details>

## C. Dominós tipo D-48 (6)

*Fichas `[arriba|abajo]` con valores de 0 a 6. **Circular:** después del 6 viene el 0.*

| # | Secuencia | A | B | C | D |
|---|---|---|---|---|---|
| C1 | [1\|2] [2\|3] [3\|4] [4\|5] **[?\|?]** | [5\|5] | [5\|6] | [6\|5] | [6\|6] |
| C2 | [6\|0] [5\|1] [4\|2] [3\|3] **[?\|?]** | [2\|4] | [4\|2] | [3\|4] | [2\|2] |
| C3 | [0\|6] [2\|5] [4\|4] [6\|3] **[?\|?]** | [8\|2] | [0\|2] | [1\|2] | [1\|3] |
| C4 | [2\|1] [4\|2] [6\|3] [1\|4] **[?\|?]** | [3\|5] | [8\|5] | [2\|5] | [3\|4] |
| C5 | [3\|3] [2\|4] [1\|5] [0\|6] **[?\|?]** | [0\|0] | [6\|0] | [1\|6] | [6\|6] |
| C6 | [1\|1] [2\|3] [3\|5] [4\|0] **[?\|?]** | [5\|2] | [5\|1] | [5\|7] | [4\|2] |

<details>
<summary>Soluciones C</summary>

| # | Resp. | Regla |
|---|---|---|
| C1 | **B** [5\|6] | Arriba +1, abajo +1 |
| C2 | **A** [2\|4] | Arriba −1, abajo +1 (la suma siempre es 6) |
| C3 | **C** [1\|2] | Arriba +2 circular (6 + 2 = 8 → **1**); abajo −1 |
| C4 | **A** [3\|5] | Arriba +2 circular (6 + 2 → 1, 1 + 2 = **3**); abajo +1 |
| C5 | **B** [6\|0] | Arriba −1 circular (0 − 1 → **6**); abajo +1 circular (6 + 1 → **0**) |
| C6 | **A** [5\|2] | Arriba +1; abajo +2 circular (1, 3, 5, 7 → **0**, **2**) |

</details>

## D. Series de figuras (9)

*Which figure comes next? / ¿Qué figura sigue?*

**D1.** `↑  →  ↓  ←  ↑  →  ?`  A) `↑`  B) `←`  C) `↓`  D) `→`

**D2.** `↑  ↗  →  ↘  ?`  A) `↙`  B) `↓`  C) `←`  D) `↗`

**D3.** `○  ◔  ◑  ◕  ?`  A) `◔`  B) `○`  C) `◑`  D) `●`

**D4.** `■□□□  □■□□  □□■□  ?`  A) `■□□□`  B) `□□□■`  C) `□■□□`  D) `□□■■`

**D5.** `▲  ▲▲  ▲▲▲  ?`  A) `▲▲▲▲`  B) `▲▲`  C) `△△△△`  D) `▲▲▲▲▲`

**D6.** `◐  ◓  ◑  ◒  ?`  A) `◑`  B) `◓`  C) `◐`  D) `●`

**D7.** `○  ●●  ○○○  ?`  A) `○○○○`  B) `●●●●`  C) `●●●`  D) `○●○●`

**D8.** El punto se mueve en una cuadrícula de 3×3:

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
<summary>Soluciones D</summary>

| # | Resp. | Regla |
|---|---|---|
| D1 | **C** `↓` | Gira 90° en sentido horario |
| D2 | **B** `↓` | Gira 45° en sentido horario |
| D3 | **D** `●` | Se rellena un cuarto en cada paso |
| D4 | **B** `□□□■` | El cuadrado negro avanza una posición a la derecha |
| D5 | **A** `▲▲▲▲` | +1 triángulo; color constante (negro) |
| D6 | **C** `◐` | La mitad negra gira 90° en sentido horario: izquierda → arriba → derecha → abajo → **izquierda** |
| D7 | **B** `●●●●` | **Dos reglas:** la cantidad sube +1 y el color alterna (blanco, negro, blanco, **negro**) |
| D8 | **A** | El punto recorre el **borde** en sentido horario: arriba-izq → arriba-centro → arriba-der → **centro-der** |
| D9 | **B** `★☆☆` | La estrella avanza a la derecha y vuelve al inicio (ciclo de 3) |

</details>

## E. Matrices 3×3 (6)

*Which option completes the matrix? / ¿Qué opción completa la matriz?*

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
<summary>Soluciones E</summary>

| # | Resp. | Regla |
|---|---|---|
| E1 | **B** 11 | Columna 3 = columna 1 + columna 2 (4 + 7) |
| E2 | **C** △ | Cada fila y cada columna contiene ○, △ y □ una vez (como un sudoku) |
| E3 | **B** ▲▲▲ | La forma es constante por fila; la cantidad crece por columna |
| E4 | **C** 12 | Columna 3 = columna 1 × columna 2 (6 × 2) |
| E5 | **C** ◭ | La forma es constante por fila; el relleno por columna: blanco, negro, **mitad** |
| E6 | **B** 125 | Cada columna: n, n², n³ → 5³ = 125 |

</details>

## F. Analogías y elemento diferente (7)

| # | Pregunta | A | B | C | D |
|---|---|---|---|---|---|
| F1 | `○` es a `●` como `□` es a **?** | ○ | ■ | △ | □ |
| F2 | `↑` es a `↓` como `→` es a **?** | ↑ | → | ← | ↗ |
| F3 | 2 es a 8 como 3 es a **?** | 9 | 12 | 27 | 6 |
| F4 | ¿Cuál **no** pertenece? 3, 5, 7, 9, 11 | 3 | 5 | 9 | 11 |
| F5 | ¿Cuál **no** pertenece? △ □ ⬠ ○ ⬡ | △ | ⬠ | ○ | ⬡ |
| F6 | ¿Cuál **no** pertenece? ↑ → ↓ ↗ ← | ↑ | ↗ | ↓ | ← |
| F7 | ¿Cuál **no** pertenece? 16, 25, 36, 48, 64 | 16 | 36 | 48 | 64 |

<details>
<summary>Soluciones F</summary>

| # | Resp. | Regla |
|---|---|---|
| F1 | **B** ■ | La misma figura, rellena de negro |
| F2 | **C** ← | Dirección opuesta (giro de 180°) |
| F3 | **C** 27 | Elevar al cubo: 2³ = 8 y 3³ = 27 |
| F4 | **C** 9 | Los demás son primos (9 = 3 × 3) |
| F5 | **C** ○ | Los demás son polígonos (tienen lados y vértices) |
| F6 | **B** ↗ | Los demás apuntan en direcciones de 90° (horizontal/vertical); ↗ es diagonal |
| F7 | **C** 48 | Los demás son cuadrados perfectos (4², 5², 6², 8²) |

</details>

---

## Tu resultado

| Correctas (de 50) | Nivel | Qué hacer |
|---|---|---|
| 45–50 | Excelente | Pasa al simulador con tiempo (30 min) |
| 35–44 | Bien | Repasa la [checklist FORMA-CPR](README.md#3-las-reglas-que-se-repiten-checklist-forma-cpr) y repite los fallos en 2 días |
| < 35 | En construcción | Vuelve a hacerlos sin tiempo, escribiendo la regla de cada uno |

> Recuerda: la prueba real usa **figuras dibujadas** con varias reglas simultáneas. Complementa con el [simulador](../simulator/index.html) y con el [test de Mensa Noruega](https://test.mensa.no/).
