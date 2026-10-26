# Cheatsheet: algoritmos y estructuras (1 página)

🌐 **Español** · [English](algoritmos.en.md)

**Big O (de mejor a peor):** O(1) < O(log n) < O(n) < O(n log n) < O(n²) < O(2ⁿ) < O(n!)
Bucles seguidos → se **suman**. Bucles anidados → se **multiplican**. Dividir a la mitad en cada paso → **log n**.

| Estructura | Clave | Operaciones | Python |
|---|---|---|---|
| Lista/arreglo | Índice | Acceso O(1), buscar O(n), insertar en medio O(n) | `list` |
| Pila | **LIFO** | push/pop O(1) | `list.append/pop` |
| Cola | **FIFO** | enqueue/dequeue O(1) | `deque.append/popleft` |
| Hash table | Clave → valor | Buscar/insertar O(1) promedio | `dict`, `set` |
| Heap | Mínimo arriba | Ver mín. O(1), push/pop O(log n) | `heapq` |
| BST | Izq < nodo < der | O(log n) balanceado, O(n) peor caso | — |
| Grafo | Nodos + aristas | BFS/DFS O(V + E) | `dict` de listas |

| Ordenamiento | Promedio | Peor | Estable | Nota |
|---|---|---|---|---|
| Bubble / Insertion | O(n²) | O(n²) | ✅ | O(n) si ya está ordenado |
| Selection | O(n²) | O(n²) | ❌ | |
| **Merge** | O(n log n) | **O(n log n)** | ✅ | Espacio O(n) |
| **Quick** | O(n log n) | **O(n²)** | ❌ | Pivote malo |
| Heap | O(n log n) | O(n log n) | ❌ | Espacio O(1) |

**Búsqueda binaria:** requiere datos **ordenados**, O(log n): ~10 pasos para 1.000 elementos y ~20 para 1.000.000.

**Recorridos de árbol:** in-order (I-N-D, sale **ordenado** en un BST) · pre-order (N-I-D) · post-order (I-D-N) · por niveles (BFS).

| Señal en el enunciado | Patrón |
|---|---|
| "par que suma", "¿ya apareció?", "frecuencia" | Hash map / set |
| Arreglo ordenado, pares, palíndromo | Dos punteros |
| Substring/subarreglo **contiguo** más largo | Ventana deslizante |
| Paréntesis, "el más reciente" | Pila |
| Camino más corto sin pesos | BFS + cola |
| Islas, componentes, explorar todo | DFS |
| Top k | Heap / ordenar |
| "Número de formas", "mínimo costo" | Programación dinámica |
| Suma de rangos | Prefix sum |

**Recursión:** caso base + caso recursivo. Memoización: Fibonacci de O(2ⁿ) a O(n).
**Checklist de casos borde:** vacío · un elemento · duplicados · negativos/cero · ya ordenado · None · empates · off-by-one.
