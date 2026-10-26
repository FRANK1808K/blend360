# Ejercicios de inglés técnico (con respuestas)

🌐 **Español** · [English](ejercicios-ingles.en.md)

> Hazlos **sin traductor**. Las respuestas están al final de cada sección.

---

## 1. ¿Qué te piden? (comprensión de enunciados)

Para cada enunciado, escribe **en español y en una frase** qué hay que hacer. Fíjate en las palabras en negrita.

1. *Write a query to find the customers who have placed **at least** two orders.*
2. *Return the names of the employees who do **not** have a manager.*
3. *Which of the following is **NOT** a characteristic of a data lake?*
4. *Given an array of integers, return the **indices** of the two numbers **such that** they add up to a target.*
5. *Find the **second highest** salary. If there is **no** second highest salary, return NULL.*
6. *Remove the duplicates **in-place** and return the **new length**.*
7. *Calculate the **month-over-month** revenue growth, **rounded to two decimal places**.*
8. *All of the following services are serverless **EXCEPT**:*
9. *Return the top 3 products **by** revenue **for each** category. In case of **ties**, order by product name.*
10. *Which solution meets the requirements with the **LEAST operational overhead**?*

<details>
<summary>Respuestas</summary>

1. Clientes con **2 o más** pedidos (`HAVING COUNT(*) >= 2`).
2. Nombres de los empleados **sin** jefe (`manager_id IS NULL`).
3. Te piden la característica que **no** tiene un data lake (la opción falsa).
4. Dado un arreglo de enteros, devuelve las **posiciones** de los dos números **que** suman el objetivo.
5. El **segundo** salario más alto; si **no existe**, devuelve NULL.
6. Quita los duplicados **sin crear otra lista** y devuelve la **nueva longitud**.
7. El crecimiento de ingresos **mes contra mes**, **redondeado a 2 decimales**.
8. Todos son serverless **excepto** uno: busca el que **no** es serverless.
9. Los 3 productos con más ingresos **en cada** categoría; en caso de **empate**, ordena por nombre.
10. La solución que **menos trabajo de administración/operación** requiera (normalmente un servicio gestionado/serverless).

</details>

## 2. Traduce al español (lectura técnica)

1. *The query returns all rows from the left table, even if there is no match in the right table.*
2. *Amazon S3 is designed for 99.999999999% durability.*
3. *The function should handle empty strings and return an empty list.*
4. *Partitioning the data reduces the amount of data scanned by each query.*
5. *Each customer can place many orders, but each order belongs to only one customer.*
6. *If the input list is already sorted, insertion sort runs in linear time.*

<details>
<summary>Respuestas</summary>

1. La consulta devuelve todas las filas de la tabla izquierda, aunque no haya coincidencia en la tabla derecha. (= LEFT JOIN)
2. Amazon S3 está diseñado para una durabilidad del 99,999999999 %.
3. La función debe manejar cadenas vacías y devolver una lista vacía.
4. Particionar los datos reduce la cantidad de datos escaneados por cada consulta.
5. Cada cliente puede hacer muchos pedidos, pero cada pedido pertenece a un solo cliente. (= relación 1:N)
6. Si la lista de entrada ya está ordenada, insertion sort se ejecuta en tiempo lineal.

</details>

## 3. Completa con la palabra correcta

Banco de palabras: **returns · stored · least · between · each · null · faster · ascending · because · must**

1. The data is ______ in Amazon S3.
2. The function ______ the sum of the list.
3. Sort the results in ______ order (from smallest to largest).
4. Choose the ______ expensive option.
5. Calculate the total for ______ department.
6. `BETWEEN` includes the values at both ends: it selects values ______ 10 and 20, inclusive.
7. `COUNT(column)` ignores ______ values.
8. Binary search is ______ than linear search on sorted data.
9. I used a LEFT JOIN ______ I needed all the customers.
10. The solution ______ run in O(n) time.

<details>
<summary>Respuestas</summary>

1. stored · 2. returns · 3. ascending · 4. least · 5. each · 6. between · 7. null · 8. faster · 9. because · 10. must

</details>

## 4. Relaciona cada término con su definición

| # | Term | | Definition |
|---|---|---|---|
| 1 | Primary key | A | A function that calculates over a set of rows without collapsing them |
| 2 | Window function | B | Data structure: last in, first out |
| 3 | Stack | C | Uniquely identifies each row in a table |
| 4 | Serverless | D | Running code without managing servers |
| 5 | Outlier | E | Extract, transform and load data |
| 6 | ETL | F | A value very different from the others |
| 7 | Queue | G | Data structure: first in, first out |

<details>
<summary>Respuestas</summary>

1-C · 2-A · 3-B · 4-D · 5-F · 6-E · 7-G

</details>

## 5. Corrige el error (gramática que aparece al explicar)

1. *The function return a list.*
2. *The data are store in S3.*
3. *I have use Python in my last project.*
4. *This solution is more fast than the other.*
5. *If the list is empty, the function will returns zero.*
6. *Yesterday I write a query.*

<details>
<summary>Respuestas</summary>

1. The function **returns** a list. (3.ª persona: -s)
2. The data **is stored** / **are stored** in S3. (pasiva: participio *stored*)
3. I **have used** Python… o I **used** Python in my last project.
4. This solution is **faster** than the other.
5. …the function **will return** zero. (después de *will*, el verbo va sin -s)
6. Yesterday I **wrote** a query. (pasado irregular de *write*)

</details>

## 6. Speaking: practica en voz alta (sin respuesta única)

Graba con tu celular una respuesta de **30–60 segundos** a cada una:

1. Explain in English what this query does: `SELECT department, AVG(salary) FROM employees GROUP BY department HAVING AVG(salary) > 8000;`
2. Explain the difference between a list and a set in Python.
3. Explain what Amazon S3 is and why it is used for data lakes.
4. Describe a project you did, using the STAR method.
5. Why do you want to join Blend360?

<details>
<summary>Ejemplo de respuesta para la 1</summary>

*"This query shows the average salary for each department. First, it groups the employees by department. Then, it calculates the average salary of each group. Finally, the HAVING clause keeps only the departments where the average salary is greater than eight thousand."*

</details>
