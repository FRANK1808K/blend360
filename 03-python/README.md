# 03 · Python — Lo que necesitas para la prueba técnica

**Español** · [English](README.en.md)

> Según los reportes de candidatos, la prueba online de Blend360 suele traer **problemas de programación en Python (o R) junto con SQL**, con tiempo limitado. Además, pueden aparecer preguntas de opción múltiple tipo "¿qué imprime este código?". Aquí cubres las dos cosas.

**Material de este módulo:**

| Archivo | Para qué |
|---|---|
| Este README | Teoría + trampas típicas + quiz "¿qué imprime?" |
| [ejercicios.py](ejercicios.py) | 25 funciones para que **tú** las implementes |
| [soluciones.py](soluciones.py) | Soluciones comentadas (ábrelas solo después de intentarlo) |
| [test_ejercicios.py](test_ejercicios.py) | Corrector automático |
| [pandas.md](pandas.md) | Análisis de datos con pandas (equivalencias con SQL) |
| [Laboratorio Python](../simulator/README.md#laboratorio-de-código) | Los mismos 25 ejercicios en el navegador, con las mismas pruebas, sin instalar nada |

```bash
cd 03-python
python3 test_ejercicios.py              # corrige TUS respuestas (ejercicios.py)
python3 test_ejercicios.py soluciones   # verifica las soluciones de referencia
```

---

## Índice

1. [Tipos de datos y operadores](#1-tipos-de-datos-y-operadores)
2. [Strings](#2-strings)
3. [Listas, tuplas, sets y diccionarios](#3-listas-tuplas-sets-y-diccionarios)
4. [Control de flujo](#4-control-de-flujo)
5. [Funciones](#5-funciones)
6. [Comprensiones](#6-comprensiones)
7. [Herramientas que ahorran tiempo en la prueba](#7-herramientas-que-ahorran-tiempo-en-la-prueba)
8. [Errores y excepciones](#8-errores-y-excepciones)
9. [Clases (POO básica)](#9-clases-poo-básica)
10. [Mutabilidad y referencias (trampa #1)](#10-mutabilidad-y-referencias-trampa-1)
11. [Quiz: ¿qué imprime?](#11-quiz-qué-imprime)

---

## 1. Tipos de datos y operadores

| Tipo | Ejemplo | Mutable |
|---|---|---|
| `int` | `42` | — |
| `float` | `3.14` | — |
| `bool` | `True`, `False` (son subclase de `int`: `True + True == 2`) | — |
| `str` | `"hola"` | ✗ No |
| `list` | `[1, 2, 3]` | ✓ Sí |
| `tuple` | `(1, 2, 3)` — una tupla de un solo elemento es `(1,)` | ✗ No |
| `set` | `{1, 2, 3}` — sin orden, sin duplicados. **`{}` es un dict vacío**; set vacío = `set()` | ✓ Sí |
| `dict` | `{"a": 1}` — mantiene el orden de inserción (Python 3.7+) | ✓ Sí |
| `None` | Ausencia de valor | — |

| Operador | Resultado | Ojo |
|---|---|---|
| `7 / 2` | `3.5` | `/` **siempre** devuelve float |
| `7 // 2` | `3` | División entera (hacia abajo): `-7 // 2 == -4` |
| `7 % 2` | `1` | Módulo (residuo). `n % 2 == 0` → par |
| `2 ** 10` | `1024` | Potencia |
| `==` vs `is` | `==` compara **valor**; `is` compara **identidad** (mismo objeto) | Usa `is` solo con `None`: `x is None` |
| `and`, `or`, `not` | Devuelven uno de los operandos: `0 or "x"` → `"x"` | Evaluación en cortocircuito |

**Valores "falsy"** (se comportan como `False`): `0`, `0.0`, `""`, `[]`, `{}`, `set()`, `None`, `False`. Todo lo demás es "truthy".

## 2. Strings

```python
s = "Blend360 Data"
s[0]        # 'B'
s[-1]       # 'a'           (índices negativos cuentan desde el final)
s[0:5]      # 'Blend'       (el final NO se incluye)
s[::-1]     # 'ataD 063dnelB'  (invertir)
s.lower(), s.upper()
s.split()             # ['Blend360', 'Data']    (por espacios)
"a,b,,c".split(",")   # ['a', 'b', '', 'c']
"-".join(["a", "b"])  # 'a-b'
s.replace("Data", "AI")
s.strip()             # quita espacios al inicio/final
s.startswith("Bl"), s.endswith("ta")
s.find("360")         # 5   (-1 si no existe)
"360" in s            # True
s.isdigit(), s.isalpha(), s.isalnum()
f"{3.14159:.2f}"      # '3.14'  (f-strings)
```

> Los strings son **inmutables**: `s[0] = "b"` → `TypeError`. Hay que crear uno nuevo.

## 3. Listas, tuplas, sets y diccionarios

```python
# LISTAS
nums = [5, 3, 8]
nums.append(1)          # [5, 3, 8, 1]
nums.extend([7, 7])     # [5, 3, 8, 1, 7, 7]
nums.insert(0, 9)       # inserta en la posición 0
nums.pop()              # quita y devuelve el último
nums.remove(7)          # quita la PRIMERA aparición del valor 7
nums.sort()             # ordena IN-PLACE, devuelve None
sorted(nums)            # devuelve una lista NUEVA ordenada
nums.reverse()          # invierte in-place
len(nums), sum(nums), min(nums), max(nums)
nums.index(8), nums.count(7)

# SETS: pertenencia en O(1) y operaciones de conjuntos
a, b = {1, 2, 3}, {2, 3, 4}
a | b   # unión          {1, 2, 3, 4}
a & b   # intersección   {2, 3}
a - b   # diferencia     {1}
a ^ b   # diferencia simétrica {1, 4}

# DICCIONARIOS
d = {"ana": 3, "luis": 5}
d["maria"] = 2              # agregar/actualizar
d.get("pedro", 0)           # 0 si no existe (d["pedro"] → KeyError)
d.keys(), d.values(), d.items()
for k, v in d.items(): ...
"ana" in d                  # busca en las CLAVES, O(1)
d.pop("ana")
{k: v for k, v in sorted(d.items(), key=lambda kv: kv[1], reverse=True)}  # ordenar por valor
```

## 4. Control de flujo

```python
for i in range(5):          # 0,1,2,3,4      range(inicio, fin_exclusivo, paso)
    if i == 3:
        break               # sale del bucle
    if i % 2 == 0:
        continue            # salta a la siguiente iteración
else:
    print("solo se ejecuta si NO hubo break")

while n > 0:
    n -= 1

x = "par" if n % 2 == 0 else "impar"    # operador ternario
```

## 5. Funciones

```python
def saludar(nombre, saludo="Hola", *args, **kwargs):
    """Docstring: describe la función."""
    return f"{saludo}, {nombre}"

saludar("Ana")                       # 'Hola, Ana'
saludar(saludo="Hi", nombre="Ana")   # argumentos por nombre

cuadrado = lambda x: x ** 2          # función anónima
sorted(palabras, key=len)            # lambda/función como criterio
```

- Una función sin `return` devuelve `None`.
- `*args` recibe posicionales extra como **tupla**; `**kwargs` recibe nombrados extra como **dict**.
- **Argumento por defecto mutable:** `def f(x, lista=[])` comparte la **misma** lista entre llamadas. Usa `lista=None` y dentro `if lista is None: lista = []`.
- **Alcance (scope) LEGB:** Local → Enclosing → Global → Built-in.

## 6. Comprensiones

```python
cuadrados = [x**2 for x in range(10)]
pares     = [x for x in nums if x % 2 == 0]
etiquetas = ["par" if x % 2 == 0 else "impar" for x in nums]   # if-else va ANTES del for
matriz_t  = [[fila[i] for fila in matriz] for i in range(len(matriz[0]))]
plano     = [x for fila in matriz for x in fila]               # aplanar
conteo    = {c: palabra.count(c) for c in set(palabra)}        # dict comprehension
unicos    = {x % 3 for x in nums}                              # set comprehension
gen       = (x**2 for x in range(10**6))                       # generador: no ocupa memoria
```

## 7. Herramientas que ahorran tiempo en la prueba

```python
from collections import Counter, defaultdict, deque
import heapq, itertools, math

Counter("banana")                  # Counter({'a': 3, 'n': 2, 'b': 1})
Counter(words).most_common(2)      # [('x', 5), ('y', 3)]

grupos = defaultdict(list)         # no hay KeyError: crea [] automáticamente
for nombre, depto in pares:
    grupos[depto].append(nombre)

q = deque([1, 2]); q.append(3); q.popleft()    # cola O(1) en ambos extremos

heapq.nlargest(3, nums); heapq.nsmallest(3, nums)
heapq.heappush(h, x); heapq.heappop(h)         # min-heap

for i, x in enumerate(lista): ...              # índice + valor
for a, b in zip(lista1, lista2): ...           # recorrer en paralelo
any(x > 10 for x in nums); all(x > 0 for x in nums)
sorted(personas, key=lambda p: (-p["edad"], p["nombre"]))  # orden por varios criterios
math.inf, math.sqrt(16), math.ceil(2.1), math.floor(2.9)
itertools.combinations([1, 2, 3], 2)          # (1,2) (1,3) (2,3)
itertools.permutations([1, 2, 3], 2)
```

## 8. Errores y excepciones

```python
try:
    resultado = 10 / int(valor)
except ValueError:
    print("no es un número")
except ZeroDivisionError as e:
    print("división entre cero:", e)
else:
    print("sin errores")       # solo si no hubo excepción
finally:
    print("siempre se ejecuta")

raise ValueError("mensaje")    # lanzar una excepción
```

Las más comunes: `TypeError` (tipo incorrecto, p. ej. `"a" + 1`), `ValueError` (tipo correcto con valor inválido, p. ej. `int("x")`), `KeyError`, `IndexError`, `ZeroDivisionError`, `AttributeError`, `NameError`.

## 9. Clases (POO básica)

```python
class Cuenta:
    tasa = 0.01                         # atributo de CLASE (compartido)

    def __init__(self, titular, saldo=0):
        self.titular = titular          # atributos de INSTANCIA
        self.saldo = saldo

    def depositar(self, monto):
        if monto <= 0:
            raise ValueError("monto inválido")
        self.saldo += monto
        return self.saldo

    def __repr__(self):
        return f"Cuenta({self.titular!r}, {self.saldo})"

class CuentaAhorro(Cuenta):             # herencia
    def depositar(self, monto):         # sobrescritura (override)
        return super().depositar(monto * (1 + self.tasa))
```

Los 4 pilares: **encapsulamiento**, **abstracción**, **herencia** y **polimorfismo**.

## 10. Mutabilidad y referencias (trampa #1)

```python
a = [1, 2, 3]
b = a            # b apunta a la MISMA lista en memoria
b.append(4)
print(a)         # [1, 2, 3, 4]  ← ¡a también cambió!

c = a.copy()     # copia superficial (también a[:] o list(a))
import copy
d = copy.deepcopy(matriz)   # copia profunda (listas dentro de listas)

m = [[0] * 3] * 3   # 3 referencias a la MISMA fila
m[0][0] = 1         # [[1,0,0],[1,0,0],[1,0,0]]
m = [[0] * 3 for _ in range(3)]   # ✓ forma correcta
```

### Argumentos mutables por defecto (la trampa de entrevista #1)

En Python, los argumentos por defecto se evalúan **una sola vez**, al momento de *definir* la función, no en cada llamada:

```python
def agregar_elemento(elem, lista=[]):    # ❌ PELIGRO: lista mutable compartida
    lista.append(elem)
    return lista

print(agregar_elemento(1))  # [1]
print(agregar_elemento(2))  # [1, 2]  ← ¡No devolvió [2]! La lista persiste en memoria

# Forma idiomática y correcta:
def agregar_elemento_correcto(elem, lista=None):
    if lista is None:
        lista = []
    lista.append(elem)
    return lista
```

### Generadores vs Comprensiones de listas (eficiencia de memoria)

En pruebas con grandes volúmenes de datos, crear listas completas puede agotar la memoria (*Memory Limit Exceeded*):

```python
# List comprehension: genera TODOS los elementos en RAM de inmediato
cuadrados_lista = [x ** 2 for x in range(10_000_000)]  # Ocupa ~400 MB de RAM

# Generator expression: genera valores bajo demanda (Lazy evaluation, O(1) memoria)
cuadrados_gen = (x ** 2 for x in range(10_000_000))    # Ocupa ~120 Bytes de RAM

# Función generadora con yield:
def contador(limite):
    n = 0
    while n < limite:
        yield n
        n += 1
```

### Lectura de entradas en Coderbyte / HackerRank

En plataformas de código, a menudo los datos no llegan como parámetros directos, sino por `sys.stdin` o como strings que debes parsear:

```python
import sys
import ast

# 1. Leer todas las líneas de la consola / prueba
lineas = sys.stdin.read().splitlines()

# 2. Parsear arrays que vienen como strings, ej. "[1, 2, 3, 4]"
entrada_cruda = "[1, 2, 3, 4]"
numeros = ast.literal_eval(entrada_cruda)  # [1, 2, 3, 4] como lista real
# o sin bibliotecas:
numeros = [int(x.strip()) for x in entrada_cruda.strip("[]").split(",") if x.strip()]

# 3. Leer números separados por espacio en una sola línea
valores = list(map(int, sys.stdin.readline().split()))
```

## 11. Quiz: ¿qué imprime?

Este tipo de preguntas es muy común en las pruebas de opción múltiple. Respóndelas **sin ejecutar** y después verifica.

```python
# Q1
print(type(7 / 7))

# Q2
x = [1, 2, 3]
y = x
y += [4]
print(len(x))

# Q3
print("data"[1:3] * 2)

# Q4
def f(a, lst=[]):
    lst.append(a)
    return lst
f(1)
print(f(2))

# Q5
print(bool([]) or 0 or "ok")

# Q6
d = {"a": 1, "b": 2}
d["a"] += d.get("c", 10)
print(d["a"])

# Q7
print([i * 2 for i in range(5) if i % 2 == 1])

# Q8
s = {3, 1, 3, 2, 1}
print(len(s))

# Q9
t = (1, 2, [3])
t[2].append(4)
print(t)

# Q10
print(-7 // 2, -7 % 2)

# Q11
nums = [3, 1, 2]
print(nums.sort())

# Q12
print(sorted(["banana", "Apple", "cherry"]))
```

<details>
<summary>Respuestas</summary>

| # | Salida | Por qué |
|---|---|---|
| 1 | `<class 'float'>` | `/` siempre devuelve float |
| 2 | `4` | `y` y `x` son la misma lista; `+=` en listas modifica in-place |
| 3 | `atat` | `"data"[1:3]` = `"at"`; `* 2` lo repite |
| 4 | `[1, 2]` | El argumento por defecto mutable se comparte entre llamadas |
| 5 | `ok` | `[]` y `0` son falsy; `or` devuelve el primer valor truthy |
| 6 | `11` | `get` devuelve 10 porque "c" no existe → 1 + 10 |
| 7 | `[2, 6]` | `i` impares: 1 y 3 → 2 y 6 |
| 8 | `3` | El set elimina duplicados: {1, 2, 3} |
| 9 | `(1, 2, [3, 4])` | La tupla es inmutable, pero la lista que contiene **sí** se puede modificar |
| 10 | `-4 1` | `//` redondea hacia −∞; `-4 * 2 + 1 = -7` |
| 11 | `None` | `.sort()` ordena in-place y devuelve `None` |
| 12 | `['Apple', 'banana', 'cherry']` | Las mayúsculas van antes que las minúsculas en el orden Unicode |

</details>

---

**Siguiente:** resuelve [ejercicios.py](ejercicios.py) y después pasa a [pandas.md](pandas.md).
