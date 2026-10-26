# 07 · Resolución de problemas (+ lógica, matemática y estadística básica)

> "Resolución de problemas" en una prueba de una empresa de datos suele mezclar tres cosas:
>
> 1. **Problemas de programación** que debes descomponer y resolver.
> 2. **Razonamiento lógico-matemático** (porcentajes, proporciones, probabilidad, conteo).
> 3. **Casos de negocio/analítica**: "las ventas cayeron, ¿qué harías?".
>
> Aquí tienes un **método** para cada una, más ejercicios resueltos.

---

## 1. Método para problemas de programación (UMPIRE)

| Paso | Qué haces | Tiempo (en un problema de 20 min) |
|---|---|---|
| **U**nderstand | Lee **dos veces**. Subraya la entrada, la salida y las restricciones. Reformula el problema en una frase | 2–3 min |
| **M**atch | ¿A qué patrón se parece? (hash map, dos punteros, ventana, BFS…) Ver la [tabla de patrones](../04-algoritmos-y-estructuras/README.md#6-patrones-que-resuelven-el-80--de-los-problemas) | 1 min |
| **P**lan | Escribe los pasos en comentarios o pseudocódigo. Empieza por la **fuerza bruta** si no ves otra cosa | 3 min |
| **I**mplement | Codifica siguiendo el plan. Usa nombres claros | 8 min |
| **R**eview | Recorre el código a mano con el ejemplo **y** con los casos borde | 3 min |
| **E**valuate | Indica la complejidad y si se puede mejorar | 1 min |

> 🔑 **Una solución correcta O(n²) vale más que una O(n) que no funciona.** Primero haz que funcione y después optimiza si te sobra tiempo.

### Checklist de casos borde (edge cases)

- [ ] Entrada **vacía** (`[]`, `""`, 0 filas)
- [ ] **Un solo** elemento
- [ ] Todos los elementos **iguales** / **duplicados**
- [ ] Números **negativos**, **cero**, números muy grandes
- [ ] Ya **ordenado** / ordenado al revés
- [ ] **NULL / None** / valores faltantes (¡en datos reales siempre hay!)
- [ ] Mayúsculas/minúsculas, espacios extra, tildes
- [ ] Límites: primer y último índice (*off-by-one*)
- [ ] Empates

### Ejemplo resuelto paso a paso

> **Problem:** *Given a list of transactions `(customer_id, amount)`, return the customer IDs whose total amount is at least 1000, sorted by total descending.*

**U:** La entrada es una lista de tuplas; la salida, una lista de IDs. Hay que **sumar por cliente**, **filtrar** los totales ≥ 1000 y **ordenar** de mayor a menor.
**M:** Agrupar y sumar → **diccionario** (como un `GROUP BY` + `HAVING` + `ORDER BY`).
**P:**

1. Recorrer las transacciones y acumular en `totals[customer] += amount`.
2. Filtrar las que tienen total ≥ 1000.
3. Ordenar por total descendente.

**I:**

```python
from collections import defaultdict

def big_customers(transactions, threshold=1000):
    totals = defaultdict(float)
    for customer_id, amount in transactions:
        totals[customer_id] += amount
    selected = [(c, t) for c, t in totals.items() if t >= threshold]
    selected.sort(key=lambda x: x[1], reverse=True)
    return [c for c, _ in selected]
```

**R:** `[(1, 600), (2, 1500), (1, 500)]` → totales `{1: 1100, 2: 1500}` → `[2, 1]` ✅. Lista vacía → `[]` ✅. Exactamente 1000 → se incluye (≥) ✅.
**E:** O(n + k log k), con k = número de clientes. Espacio O(k).

**El mismo problema en SQL:**

```sql
SELECT customer_id
FROM transactions
GROUP BY customer_id
HAVING SUM(amount) >= 1000
ORDER BY SUM(amount) DESC;
```

## 2. Gestión del tiempo en la prueba técnica (90 min)

1. **Minuto 0–3:** mira **todas** las preguntas o secciones. Identifica las fáciles y lo que vale más puntos.
2. Haz primero lo que sabes. **Marca y salta** lo que te bloquee más de 2 minutos (opción múltiple) o más de 5 minutos sin avanzar (código).
3. En código: **entrega algo que corra**. Si la plataforma tiene casos de prueba, ejecútalos a menudo; los puntos parciales cuentan.
4. Reserva los **últimos 5–10 min** para revisar las marcadas y no dejar **nada** sin responder (si no hay penalización por error, adivina).
5. Lleva el control: 90 min ÷ número de preguntas = tu ritmo. Por ejemplo, con 40 preguntas → ~2 min por pregunta.

## 3. Razonamiento lógico-matemático

### Porcentajes (¡muy frecuentes!)

| Situación | Fórmula | Ejemplo |
|---|---|---|
| % de cambio | (nuevo − viejo) / viejo × 100 | 80 → 100: +25 %. 100 → 80: −20 % |
| Aumentar x % | valor × (1 + x/100) | 200 + 15 % = 230 |
| Aumentos sucesivos | Se **multiplican**, no se suman | +10 % y luego +10 % = ×1,21 → +21 % |
| Subir y bajar el mismo % | **No** vuelve al original | 100 → +20 % → 120 → −20 % → 96 |
| Puntos porcentuales vs. % | De 10 % a 12 % = +2 **puntos porcentuales** = +20 % **relativo** | |
| Valor original | final / (1 + x/100) | Si tras +25 % vale 150, antes valía 120 |

### Proporciones, promedios y trabajo

- **Regla de tres:** si 3 analistas procesan 12 reportes, 5 analistas procesan 12 × 5/3 = 20 (en el mismo tiempo).
- **Promedio ponderado:** 2 cursos con 30 alumnos (promedio 4,0) y 10 alumnos (promedio 3,0) → (30·4 + 10·3) / 40 = **3,75**. No es 3,5.
- **Trabajo conjunto:** A tarda 6 h y B tarda 3 h → juntos: 1/(1/6 + 1/3) = **2 h**.
- **Velocidad media de ida y vuelta** a 60 y 40 km/h → 2·60·40 / (60 + 40) = **48 km/h** (media armónica, no 50).

### Conteo y probabilidad

| Concepto | Fórmula | Ejemplo |
|---|---|---|
| Principio multiplicativo | a × b × … | 3 camisas × 4 pantalones = 12 combinaciones |
| Permutaciones (importa el orden) | n! / (n−k)! | Podio de 3 entre 8 corredores: 8·7·6 = 336 |
| Combinaciones (no importa el orden) | n! / (k!(n−k)!) | Equipo de 2 entre 5: 10 |
| Probabilidad | casos favorables / casos posibles | Sacar par con un dado: 3/6 = 1/2 |
| "Y" (independientes) | P(A) × P(B) | Dos caras en 2 monedas: 1/4 |
| "O" (excluyentes) | P(A) + P(B) | Sacar 1 o 2 con un dado: 2/6 |
| "Al menos uno" | 1 − P(ninguno) | Al menos una cara en 3 monedas: 1 − 1/8 = 7/8 |
| Condicional | P(A\|B) = P(A y B) / P(B) | Base del teorema de Bayes |

### Problemas lógicos clásicos

- **Verdaderos/mentirosos:** supón que uno dice la verdad y busca una contradicción.
- **Ordenamientos:** "Ana es más alta que Beto; Carlos es más bajo que Beto…" → dibuja una línea y ubica a cada uno.
- **Silogismos:** "Todos los A son B; algunos B son C" → ¿algunos A son C? **No necesariamente**. Dibuja diagramas de Venn.
- **Condicionales:** "Si llueve, la calle se moja". Lo que **sí** se puede concluir: si la calle **no** está mojada → no llovió (contrarrecíproco). Lo que **no**: si la calle está mojada → llovió (falacia de afirmar el consecuente).

## 4. Estadística básica para análisis de datos

| Medida | Qué es | Ojo |
|---|---|---|
| **Media** (mean) | Suma / n | Sensible a **outliers** |
| **Mediana** (median) | Valor central ordenado | **Robusta** a outliers: úsala con ingresos o precios |
| **Moda** (mode) | Valor más frecuente | Sirve para datos categóricos |
| **Rango** | máx − mín | |
| **Varianza / desviación estándar** | Dispersión alrededor de la media | La desviación estándar está en las mismas unidades que los datos |
| **Percentiles / cuartiles** | Q1 = p25, Q2 = mediana, Q3 = p75; **IQR** = Q3 − Q1 | Outlier si < Q1 − 1,5·IQR o > Q3 + 1,5·IQR |
| **Correlación** (−1 a 1) | Relación lineal entre dos variables | **Correlación ≠ causalidad** |

- **Distribución sesgada a la derecha** (*right-skewed*, como los ingresos): media > mediana.
- **Distribución normal:** ~68 % de los datos dentro de ±1σ, ~95 % dentro de ±2σ y ~99,7 % dentro de ±3σ.
- **A/B test:** comparas la versión A (control) con la B (variante) asignando usuarios **al azar**. El **p-valor** es la probabilidad de ver una diferencia así de grande si en realidad no hubiera diferencia. Si p < 0,05, se considera *estadísticamente significativo*.
- **Muestra vs. población**, **sesgo de selección** y **paradoja de Simpson** (una tendencia que se invierte al agrupar los datos).

## 5. Casos de negocio (preguntas abiertas de analítica)

Estructura para responder (puedes decirla en inglés en la entrevista, ver [frases](../english/entrevista-y-frases.md)):

1. **Clarify:** aclara la métrica, el periodo y la definición. *"How do we define 'sales'? Compared to which period?"*
2. **Check the data:** ¿es un error de datos? (pipeline caído, cambio de tracking, fecha festiva).
3. **Segment:** divide por región, canal, producto, cliente nuevo vs. recurrente, dispositivo…
4. **Hypothesize:** factores internos (precio, campaña, stock, cambio en la web) vs. externos (competencia, estacionalidad, economía).
5. **Validate** cada hipótesis con datos y **recommend** una acción medible.

> **Ejemplo:** *"Weekly sales dropped 20%. How would you investigate?"*
> → Confirmo que el dato es real (¿se cayó el pipeline?) → comparo con la misma semana del año anterior (estacionalidad) → segmento por canal, región y producto para ubicar la caída → reviso el embudo (visitas → carrito → compra) para ver en qué paso cae → reviso cambios recientes (precios, campañas, despliegues en la web) → recomiendo una acción y defino un KPI para monitorearla.

## 6. Ejercicios

**Lógica y matemática:**

1. Un producto cuesta 250. Sube 20 % y luego baja 20 %. ¿Precio final?
2. En una empresa, 60 % son ingenieros y el 25 % de los ingenieros trabaja en datos. ¿Qué % del total son ingenieros de datos?
3. Las ventas pasaron de 1.200 a 1.500. ¿Crecimiento %?
4. ¿Cuántos códigos de 3 dígitos distintos (0–9, sin repetir) existen?
5. Se lanzan 2 dados. ¿Probabilidad de que sumen 7?
6. Datos: 2, 3, 3, 5, 100. Media, mediana y moda. ¿Cuál representa mejor el centro?
7. "Todos los analistas saben SQL. Pedro sabe SQL." ¿Pedro es analista?
8. Si 5 máquinas hacen 5 piezas en 5 minutos, ¿cuánto tardan 100 máquinas en hacer 100 piezas?
9. Una tasa de conversión pasó de 4 % a 5 %. Exprésalo en puntos porcentuales y en % relativo.
10. Un equipo de 4 personas se elige de 6. ¿Cuántos equipos posibles hay?

**Programación (resuélvelos en Python y en SQL cuando aplique):**

1. Dada una lista de fechas de login de un usuario (`"YYYY-MM-DD"`), devuelve la racha más larga de días consecutivos.
2. Dado un texto, devuelve las 3 palabras más frecuentes (sin distinguir mayúsculas).
3. Dada una lista de precios diarios, devuelve para cada día cuántos días hay que esperar a un precio mayor (0 si nunca).

<details>
<summary>Soluciones (lógica y matemática)</summary>

1. 250 × 1,2 × 0,8 = **240**.
2. 0,60 × 0,25 = **15 %**.
3. (1500 − 1200) / 1200 = **25 %**.
4. 10 × 9 × 8 = **720**.
5. Hay 6 pares favorables, (1,6), (2,5), (3,4), (4,3), (5,2) y (6,1), sobre 36 posibles → **1/6**.
6. Media = 113/5 = **22,6**; mediana = **3**; moda = **3**. La **mediana** representa mejor el centro porque el 100 es un outlier.
7. **No necesariamente** (falacia de afirmar el consecuente): otras personas también saben SQL.
8. **5 minutos**: cada máquina hace 1 pieza en 5 minutos.
9. **+1 punto porcentual** = **+25 %** relativo.
10. C(6,4) = 6!/(4!·2!) = **15**.

</details>

<details>
<summary>Soluciones (programación)</summary>

```python
from collections import Counter
from datetime import date, timedelta

# 1. Racha de días consecutivos (gaps and islands)
def longest_streak(dates):
    days = sorted({date.fromisoformat(d) for d in dates})   # set: quita duplicados
    best = current = 1 if days else 0
    for prev, cur in zip(days, days[1:]):
        current = current + 1 if cur - prev == timedelta(days=1) else 1
        best = max(best, current)
    return best

# 2. Top 3 palabras
def top_words(text, k=3):
    return [w for w, _ in Counter(text.lower().split()).most_common(k)]

# 3. Días hasta un precio mayor (pila monótona, O(n))
def days_until_higher(prices):
    result = [0] * len(prices)
    stack = []                      # índices con precios aún sin "superar"
    for i, p in enumerate(prices):
        while stack and prices[stack[-1]] < p:
            j = stack.pop()
            result[j] = i - j
        stack.append(i)
    return result

assert longest_streak(["2024-01-01", "2024-01-02", "2024-01-04", "2024-01-05", "2024-01-06"]) == 3
assert top_words("a b a c b a") == ["a", "b", "c"]
assert days_until_higher([73, 74, 75, 71, 69, 72, 76, 73]) == [1, 1, 4, 2, 1, 1, 0, 0]
```

SQL del problema 1 (*gaps and islands*): restarle a cada fecha su número de fila produce el mismo valor para todos los días de una misma racha.

```sql
WITH d AS (
    SELECT DISTINCT login_date FROM logins WHERE user_id = 1
), g AS (
    SELECT login_date,
           julianday(login_date) - ROW_NUMBER() OVER (ORDER BY login_date) AS grp
    FROM d
)
SELECT MAX(streak) AS longest_streak
FROM (SELECT grp, COUNT(*) AS streak FROM g GROUP BY grp);
```

</details>

---

**Siguiente:** [01 · Razonamiento abstracto](../01-razonamiento-abstracto/README.md)
