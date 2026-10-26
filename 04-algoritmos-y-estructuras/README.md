# 04 · Algoritmos básicos y estructuras de datos

🌐 **Español** · [English](README.en.md)

> El temario dice **"habilidades en algoritmo básico, estructura de datos y resolución de problemas"**. En pruebas de 90 minutos esto suele aparecer de dos formas:
>
> 1. **Opción múltiple:** "¿cuál es la complejidad?", "¿qué estructura usarías?", "¿qué devuelve este pseudocódigo?".
> 2. **Problemas de código** de nivel *easy/medium* (estilo LeetCode/HackerRank).
>
> Este módulo cubre las dos.

| Archivo | Contenido |
|---|---|
| Este README | Teoría: Big O, estructuras, algoritmos, patrones, trazado de pseudocódigo |
| [problemas.py](problemas.py) | 20 problemas clásicos para resolver |
| [soluciones.py](soluciones.py) | Soluciones explicadas, con complejidad |
| [test_problemas.py](test_problemas.py) | Corrector: `python3 test_problemas.py` o `python3 test_problemas.py soluciones` |

---

## 1. Complejidad: notación Big O

Big O describe **cómo crece** el tiempo (o la memoria) de un algoritmo cuando crece el tamaño de la entrada `n`. Se queda con el término dominante y se ignoran las constantes: `3n² + 5n + 2` → **O(n²)**.

| Big O | Nombre | Ejemplo | n = 1.000 → operaciones aprox. |
|---|---|---|---|
| O(1) | Constante | Acceder a `lista[i]`, buscar en un dict/set | 1 |
| O(log n) | Logarítmica | Búsqueda binaria | 10 |
| O(n) | Lineal | Recorrer una lista una vez | 1.000 |
| O(n log n) | Linealítmica | Merge sort, `sorted()` | 10.000 |
| O(n²) | Cuadrática | Dos bucles anidados sobre n | 1.000.000 |
| O(2ⁿ) | Exponencial | Fibonacci recursivo ingenuo, todos los subconjuntos | astronómico |
| O(n!) | Factorial | Todas las permutaciones | astronómico |

**Reglas rápidas para calcularla:**

- Bucles **secuenciales** → se suman: O(n) + O(n) = O(n).
- Bucles **anidados** → se multiplican: O(n) × O(n) = O(n²).
- Si en cada paso **divides el problema a la mitad** → O(log n).
- Recursión → (número de llamadas) × (trabajo por llamada).
- **Espacio:** la memoria extra. Crear una lista nueva de tamaño n = O(n); usar unas pocas variables = O(1).

**¿Qué complejidad aguanta la prueba?** (aprox. 10⁸ operaciones simples por segundo en C++; Python es ~10–50 veces más lento):

| Tamaño de n | Complejidad máxima razonable |
|---|---|
| n ≤ 20 | O(2ⁿ) |
| n ≤ 1.000 | O(n²) |
| n ≤ 100.000 | O(n log n) |
| n ≤ 10.000.000 | O(n) |

## 2. Estructuras de datos

| Estructura | Acceso | Búsqueda | Insertar | Eliminar | En Python | Úsala cuando… |
|---|---|---|---|---|---|---|
| **Arreglo / lista** | O(1) | O(n) | O(1) al final, O(n) en medio | O(n) | `list` | Necesitas orden e índice |
| **Lista enlazada** | O(n) | O(n) | O(1) si tienes el nodo | O(1) si tienes el nodo | (se implementa con clases) | Muchas inserciones/borrados en medio |
| **Pila (stack)** — LIFO | O(1) tope | — | O(1) `push` | O(1) `pop` | `list` (`append`/`pop`) | Deshacer, paréntesis, recursión, DFS |
| **Cola (queue)** — FIFO | O(1) frente | — | O(1) `enqueue` | O(1) `dequeue` | `collections.deque` | Turnos, BFS, procesamiento en orden |
| **Tabla hash** | — | O(1) promedio | O(1) promedio | O(1) promedio | `dict`, `set` | Búsquedas rápidas, conteos, "¿ya lo vi?" |
| **Heap (montículo)** | O(1) el mínimo | O(n) | O(log n) | O(log n) el mínimo | `heapq` | Top-k, prioridad, mínimo dinámico |
| **Árbol binario de búsqueda (BST)** | — | O(log n) balanceado / O(n) peor caso | O(log n) | O(log n) | (clases) | Datos ordenados dinámicos |
| **Grafo** | — | BFS/DFS O(V + E) | — | — | dict de listas (lista de adyacencia) | Redes, rutas, relaciones |

**Conceptos de árboles que preguntan:**

```text
        8          ← raíz (root)
      /   \
     3     10      ← 3 y 10 son hijos de 8
    / \      \
   1   6      14   ← 1, 6 y 14 son hojas (leaves): no tienen hijos
```

- **BST:** todo lo de la izquierda < nodo < todo lo de la derecha.
- **Altura:** número de niveles (aquí 3).
- **Recorridos:**
  - **In-order** (izquierda, nodo, derecha) → `1 3 6 8 10 14`: en un BST sale **ordenado**.
  - **Pre-order** (nodo, izquierda, derecha) → `8 3 1 6 10 14`.
  - **Post-order** (izquierda, derecha, nodo) → `1 6 3 14 10 8`.
  - **Por niveles** (BFS) → `8 3 10 1 6 14`.

**Pila vs. cola: ejemplo de trazado**

```text
Pila: push 1, push 2, push 3, pop, push 4, pop, pop  → salen: 3, 4, 2
Cola: enqueue 1, enqueue 2, enqueue 3, dequeue, enqueue 4, dequeue → salen: 1, 2
```

## 3. Algoritmos de búsqueda

| Algoritmo | Requisito | Complejidad |
|---|---|---|
| Búsqueda lineal | Ninguno | O(n) |
| Búsqueda binaria | Lista **ordenada** | O(log n) |

```python
def binary_search(arr, target):
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            lo = mid + 1          # descartar la mitad izquierda
        else:
            hi = mid - 1          # descartar la mitad derecha
    return -1
```

> ¿Cuántas comparaciones necesita como máximo la búsqueda binaria con 1.000 elementos? ⌈log₂ 1000⌉ = **10**. Con 1.000.000 → **20**.

## 4. Algoritmos de ordenamiento

| Algoritmo | Mejor | Promedio | Peor | Espacio | Estable | Idea |
|---|---|---|---|---|---|---|
| Bubble sort | O(n) | O(n²) | O(n²) | O(1) | ✅ | Intercambia vecinos desordenados; el mayor "burbujea" al final |
| Selection sort | O(n²) | O(n²) | O(n²) | O(1) | ❌ | Busca el mínimo y lo pone al inicio |
| Insertion sort | O(n) | O(n²) | O(n²) | O(1) | ✅ | Inserta cada elemento en su lugar (como las cartas en la mano). Muy bueno con datos casi ordenados |
| Merge sort | O(n log n) | O(n log n) | O(n log n) | O(n) | ✅ | Divide a la mitad, ordena cada mitad y **mezcla** |
| Quick sort | O(n log n) | O(n log n) | O(n²) | O(log n) | ❌ | Elige un pivote, pone menores a la izquierda y mayores a la derecha |
| Heap sort | O(n log n) | O(n log n) | O(n log n) | O(1) | ❌ | Usa un heap |
| Timsort (`sorted()` de Python) | O(n) | O(n log n) | O(n log n) | O(n) | ✅ | Híbrido de merge + insertion |

- **Estable:** mantiene el orden relativo de los elementos iguales.
- El límite inferior para ordenar **por comparaciones** es O(n log n).
- Peor caso de quick sort: el pivote siempre es el mínimo o el máximo (por ejemplo, el primer elemento con datos ya ordenados).

**Trazado de bubble sort** sobre `[5, 1, 4, 2]`:

```text
Pasada 1: [1,5,4,2] → [1,4,5,2] → [1,4,2,5]   (el 5 llegó al final)
Pasada 2: [1,4,2,5] → [1,2,4,5]
Pasada 3: sin intercambios → termina
```

## 5. Recursión

Toda función recursiva necesita:

1. Un **caso base** que la detenga.
2. Un **caso recursivo** que se acerque al caso base.

Sin caso base → `RecursionError` (stack overflow). Python tiene un límite de ~1000 llamadas por defecto.

```python
def suma_lista(nums):
    if not nums:                  # caso base
        return 0
    return nums[0] + suma_lista(nums[1:])   # caso recursivo
```

**Memoización:** guardar resultados ya calculados. Convierte Fibonacci de O(2ⁿ) a O(n):

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    return n if n < 2 else fib(n - 1) + fib(n - 2)
```

## 6. Patrones que resuelven el 80 % de los problemas

| Si el problema dice… | Piensa en… | Ejemplo |
|---|---|---|
| "¿Existe un par que sume X?", "¿ya apareció?", "cuenta frecuencias" | **Hash map / set** | Two Sum, primer carácter no repetido |
| Arreglo **ordenado**, pares, invertir, palíndromo | **Dos punteros** | Two Sum en arreglo ordenado, quitar duplicados |
| "Subarreglo/substring **contiguo** más largo/corto que cumple…" | **Ventana deslizante** | Substring más largo sin repetir |
| Arreglo ordenado + "buscar", "mínimo que cumple" | **Búsqueda binaria** | Buscar elemento, raíz cuadrada entera |
| Paréntesis, "el más reciente", deshacer | **Pila** | Paréntesis balanceados |
| Camino más corto en grid/grafo **sin pesos** | **BFS** (cola) | Laberinto |
| Explorar todo, islas, componentes conectados | **DFS** (recursión/pila) | Contar islas |
| "Los k más grandes/frecuentes" | **Heap** o ordenar | Top-k frecuentes |
| "Número de formas", "mínimo costo", subproblemas repetidos | **Programación dinámica** | Escaleras, cambio de monedas |
| Elegir lo mejor localmente funciona | **Greedy (voraz)** | Máximo beneficio de acciones, intervalos |
| Suma de rangos repetida | **Prefix sum** (sumas acumuladas) | Suma de subarreglo i..j en O(1) |

## 7. Trazado de pseudocódigo (muy común en opción múltiple)

Practica "ser la computadora": haz una tabla con cada variable y actualízala línea por línea.

```text
función misterio(n):
    resultado ← 0
    mientras n > 0:
        resultado ← resultado * 10 + (n mod 10)
        n ← n div 10
    retornar resultado

misterio(1230) = ?
```

| Iteración | n mod 10 | resultado | n |
|---|---|---|---|
| inicio | — | 0 | 1230 |
| 1 | 0 | 0 | 123 |
| 2 | 3 | 3 | 12 |
| 3 | 2 | 32 | 1 |
| 4 | 1 | 321 | 0 |

**Respuesta: 321** (invierte los dígitos; el 0 del final se pierde).

### Practica tú

```text
A) x ← 1
   para i desde 1 hasta 4:
       x ← x * i
   imprimir x

B) a ← [3, 8, 1, 9, 4]
   m ← a[0]
   para cada v en a:
       si v < m: m ← v
   imprimir m

C) contador ← 0
   para i desde 1 hasta n:
       para j desde 1 hasta n:
           contador ← contador + 1
   ¿Valor final de contador y complejidad?

D) función f(n):
       si n ≤ 1: retornar 1
       retornar f(n - 1) + f(n - 2)
   f(5) = ?

E) i ← 1
   mientras i < n:
       i ← i * 2
   ¿Complejidad?
```

<details>
<summary>Respuestas</summary>

- **A)** `24` (calcula 4! = 1·2·3·4).
- **B)** `1` (es el mínimo).
- **C)** `n²` iteraciones → **O(n²)**.
- **D)** f(0)=1, f(1)=1, f(2)=2, f(3)=3, f(4)=5, f(5)=**8**. Complejidad O(2ⁿ) sin memoización.
- **E)** `i` se duplica en cada paso → **O(log n)**.

</details>

## 8. Preguntas conceptuales rápidas

<details>
<summary>1. ¿Por qué buscar en un <code>set</code> es más rápido que en una <code>list</code>?</summary>

El `set` usa una tabla hash: calcula el hash del valor y va directo a su "casilla", en O(1) en promedio. La lista tiene que revisar elemento por elemento, en O(n).

</details>

<details>
<summary>2. ¿Qué estructura usarías para implementar el botón "Deshacer" (undo)?</summary>

Una **pila** (LIFO): la última acción realizada es la primera que se deshace.

</details>

<details>
<summary>3. ¿Qué estructura usarías para atender solicitudes en orden de llegada?</summary>

Una **cola** (FIFO).

</details>

<details>
<summary>4. ¿Qué es una colisión en una tabla hash?</summary>

Cuando dos claves distintas producen el mismo índice (hash). Se resuelve con *encadenamiento* (una lista en cada casilla) o con *direccionamiento abierto* (buscar otra casilla libre). Con muchas colisiones, la búsqueda se degrada hacia O(n).

</details>

<details>
<summary>5. ¿Cuándo es mejor una lista enlazada que un arreglo?</summary>

Cuando insertas o eliminas muchos elementos al inicio o en medio y no necesitas acceso por índice. El arreglo tiene que desplazar elementos (O(n)); la lista enlazada solo reconecta punteros (O(1), si ya tienes el nodo).

</details>

<details>
<summary>6. Diferencia entre BFS y DFS</summary>

**BFS** (amplitud) explora por niveles usando una **cola** y encuentra el camino más corto en grafos sin pesos. **DFS** (profundidad) va lo más hondo posible antes de retroceder, usando una **pila** o recursión; sirve para explorar componentes, detectar ciclos y hacer backtracking. Ambos son O(V + E).

</details>

---

**Siguiente:** resuelve [problemas.py](problemas.py) y luego estudia [07 · Resolución de problemas](../07-resolucion-de-problemas/README.md).
