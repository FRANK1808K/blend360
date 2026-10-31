# 01 · Razonamiento abstracto (30 minutos)

**Español** · [English](README.en.md)

> Un candidato que presentó el proceso de Blend360 en **Bogotá (mayo de 2026)** reportó pruebas de **lógica y razonamiento abstracto "bastante exigentes"**. La buena noticia es que el razonamiento abstracto **se entrena**: hay pocos tipos de reglas y se repiten. Si aprendes a reconocerlas, vas a ir mucho más rápido.

| Archivo | Contenido |
|---|---|
| Este README | Tipos de pregunta, reglas de transformación, estrategia de tiempo |
| [ejercicios.md](ejercicios.md) | 50 ejercicios con solución explicada |
| [../simulator/](../simulator/index.html) | Simulador con **figuras generadas al azar** (ejercicios ilimitados) y cronómetro de 30 min |

---

## 1. ¿Qué mide?

La capacidad de **descubrir reglas y patrones en información nueva** (figuras, números, letras) **sin conocimientos previos**. Es lo que en psicometría se llama *inteligencia fluida*. En el trabajo de datos equivale a "ver el patrón" en un problema que nunca has visto.

**Formato típico:** entre 20 y 40 preguntas en 30 minutos → **45 a 90 segundos por pregunta**. La dificultad suele **aumentar** a medida que avanzas, así que **no te quedes atascado en las primeras**.

## 2. Tipos de pregunta

| Tipo | Cómo se ve | Ejemplo de test |
|---|---|---|
| **Series de figuras** | 4–5 figuras en secuencia; elige la siguiente | Tests tipo "abstract reasoning" (SHL, Aon/cut-e, Mettl) |
| **Matrices 3×3** | Cuadrícula con una casilla vacía | **Raven** (Matrices Progresivas) |
| **Dominós** | Fichas con puntos de 0 a 6; elige la ficha que falta | **D-48 / D-70** (muy usado en Latinoamérica) |
| **Analogías** | A es a B como C es a ? | — |
| **Elemento diferente** | ¿Cuál no pertenece al grupo? | — |
| **Series numéricas y de letras** | 2, 6, 18, 54, ? | Pruebas de aptitud numérica/lógica |
| **Grupos A / B** | El conjunto A sigue una regla y el B otra; ¿a cuál pertenece la figura? | Tests tipo SHL "inductive" |
| **Espacial** | Rotar, reflejar, plegar cubos | — |

## 3. Las reglas que se repiten: checklist **"FORMA-CPR"**

Cuando veas una secuencia, revisa **en este orden** qué cambia de una figura a la siguiente:

| Letra | Qué revisar | Preguntas que te haces |
|---|---|---|
| **F**orma | ¿Cambia el tipo de figura? | ¿Círculo → cuadrado → triángulo? ¿Aumentan los lados (3, 4, 5…)? |
| **O**rientación | **Rotación** o **reflexión** | ¿Gira 45°, 90° o 180°? ¿En sentido horario o antihorario? ¿Se refleja como en un espejo? |
| **R**elleno / color | Blanco, negro, rayado | ¿Alterna? ¿Rota el color entre los elementos? |
| **M**ovimiento / posición | Dónde está cada elemento | ¿Avanza 1 casilla? ¿Recorre las esquinas en sentido horario? ¿Rebota al llegar al borde? |
| **A**umento / cantidad | Número de elementos, lados, puntos, líneas | ¿+1, −1, ×2? ¿Suma de los anteriores? |
| **C**ombinación | Superposición de figuras | ¿La 3.ª figura = 1.ª + 2.ª? ¿Se eliminan las líneas comunes (XOR)? |
| **P**roporción / tamaño | Grande, mediano, pequeño | ¿Crece y decrece? |
| **R**epetición / ciclo | Patrón que vuelve a empezar | ¿Se repite cada 2, 3 o 4 pasos? |

> **Clave:** casi siempre hay **2 o 3 reglas a la vez** sobre elementos **distintos**. Por ejemplo, la flecha gira 90° **y** el punto alterna entre negro y blanco. Analiza **cada elemento por separado**.

### Rotaciones que debes reconocer al instante

```text
Horario 90°:        ↑ → ↓ ← ↑
Horario 45°:        ↑ ↗ → ↘ ↓ ↙ ← ↖ ↑
Antihorario 90°:    ↑ ← ↓ → ↑
180°:               ↑ ↓ ↑ ↓
Reflexión vertical (espejo izquierda-derecha): ↗ ↔ ↖ ,  ◐ ↔ ◑
```

### Matrices 3×3: las 6 reglas más comunes

1. **Progresión** en la fila o en la columna (crece, gira, se mueve).
2. **Cada fila contiene una vez cada elemento** (como un sudoku: ○ △ □ en distinto orden).
3. **Suma/resta:** la columna 3 = columna 1 + columna 2 (o la superposición).
4. **XOR:** la columna 3 muestra solo lo que **no** coincide entre la 1 y la 2.
5. **Atributo constante** por fila (misma forma) y **variable** por columna (distinto relleno).
6. **Conteo:** el número de elementos sigue una regla (1, 2, 3 o una suma).

> Revisa **filas** primero. Si no encuentras la regla, revisa **columnas** y después **diagonales**.

### Dominós (D-48)

- Cada mitad tiene de **0 a 6** puntos y la secuencia es **circular**: después del 6 viene el 0 (6 + 1 = 0; 0 − 1 = 6).
- Analiza la **mitad superior** y la **mitad inferior por separado**.
- Patrones típicos: +1, −1, +2, alternancia, la mitad inferior de una ficha igual a la superior de la siguiente, suma constante.

### Razonamiento espacial: Despliegue y doblado de cubos (Cube Folding)

Muy común en pruebas psicométricas de consultoras tecnológicas (SHL, Aon/cut-e):

```text
Patrón de la Cruz (Desarrollo 2D de un cubo):
          ┌───┐
          │ 1 │  ← Cara superior
      ┌───┼───┼───┬───┐
      │ 2 │ 3 │ 4 │ 5 │  ← Caras laterales (línea continua de 4)
      └───┼───┼───┴───┘
          │ 6 │  ← Cara inferior
          └───┘
```

#### Reglas de oro para descartar cubos 3D al instante

- **La regla de las caras opuestas (crucial):**
  - En una cruz o tira desplegada, dos caras separadas por exactamente una cara intermedia son **caras opuestas**.
  - En el diagrama: **(1 y 6)** son opuestas; **(2 y 4)** son opuestas; **(3 y 5)** son opuestas.
  - **Regla:** Dos caras opuestas **NUNCA pueden ser visibles al mismo tiempo** en una vista 3D isométrica ni compartir una arista común. Si una opción 3D muestra la cara 2 y la cara 4 juntas → **descartada de inmediato**.
- **Orientación de símbolos relativos:** Si dos caras adyacentes tienen flechas o líneas, comprueba hacia dónde apuntan al doblar la arista (ej. si la flecha apunta hacia la cara con un círculo).

## 4. Estrategia para los 30 minutos

1. **Primero mira las opciones de respuesta:** te dicen **qué cambia**. Si todas las opciones son la misma flecha en distintos ángulos, la regla es de **rotación**.
2. **Elimina opciones** que violan la regla más obvia; a menudo te quedan 2.
3. **Regla de los 60 segundos:** si en 1 minuto no ves nada, **marca, adivina y avanza**. Regresa al final.
4. **No dejes nada en blanco** si no hay penalización por respuesta incorrecta.
5. **Verifica tu regla** con **todas** las figuras, no solo con las dos primeras.
6. **Habla contigo mismo** con palabras simples: "gira 90 a la derecha, el punto alterna, se suma un lado".
7. Lleva el ritmo: a los **15 minutos** deberías ir por la mitad.

### Técnica del descarte agresivo en 15 segundos

En 30 minutos para 30–40 preguntas dispones de ~45 a 60 segundos por pregunta. No intentes deducir la figura entera desde cero:

- **Paso 1 (Aislar un elemento):** Elige el detalle más simple (ej. el punto negro en la esquina o la dirección de la flecha).
- **Paso 2 (Aplicar su regla):** Si la flecha gira 90° en sentido horario, elimina de inmediato todas las opciones donde la flecha no apunte en esa dirección. Usualmente **eliminas 3 de las 5 opciones en 15 segundos**.
- **Paso 3 (Desempatar):** Entre las 2 opciones restantes, busca cuál es la única diferencia entre ellas (ej. el sombreado de un círculo) y verifica solo esa regla específica.

## 5. Plan de entrenamiento

| Semana | Diario (15–20 min) |
|---|---|
| 1 | 10 series numéricas/letras + 10 de figuras ([ejercicios.md](ejercicios.md)) **sin tiempo**, para aprender las reglas |
| 2 | Simulador en modo práctica, 20 preguntas con cronómetro: meta de 75 s por pregunta |
| 3+ | Simulacro completo de **30 minutos** 3 veces por semana: meta de 45–60 s por pregunta |

**Recursos externos gratuitos** (todos con figuras reales):

- [Mensa Norway IQ test](https://test.mensa.no/): 35 matrices en 25 minutos, **muy parecido** a la prueba real.
- [123test: abstract reasoning](https://www.123test.com/): tests de práctica en inglés.
- [Nibcode: test de razonamiento abstracto](https://www.nibcode.com/es/formacion-psicometrica/test-de-razonamiento-abstracto) (en español).
- Busca en YouTube "test D-48 dominós resuelto" y "Raven matrices explained".

---

**Empieza a practicar:** [ejercicios.md](ejercicios.md)
