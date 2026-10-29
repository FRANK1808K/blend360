# 08b · Estadística y ML: 25 preguntas de práctica

**Español** · [English](preguntas.en.md)

> Las preguntas están **en inglés**, como en la prueba. **Primero intenta en inglés**; abre la traducción solo si te bloqueas. Respuestas y explicaciones al final. Teoría: [README.md](README.md).

---

## Parte A: Estadística y pruebas A/B

**1.** A dataset of salaries is right-skewed by a few very high values. Which measure best represents the typical salary?

- A) Mean
- B) Median
- C) Range
- D) Variance

<details>
<summary>Traducción al español</summary>

Un conjunto de salarios está sesgado a la derecha por unos pocos valores muy altos. ¿Qué medida representa mejor el salario típico?

- A) Media
- B) Mediana
- C) Rango
- D) Varianza

</details>

**2.** Why do we divide by n − 1 when calculating the SAMPLE variance?

- A) To make the calculation faster
- B) To correct the tendency to underestimate the population variance
- C) Because the sample has one outlier
- D) To get a number in the original units

<details>
<summary>Traducción al español</summary>

¿Por qué se divide entre n − 1 al calcular la varianza MUESTRAL?

- A) Para que el cálculo sea más rápido
- B) Para corregir la tendencia a subestimar la varianza poblacional
- C) Porque la muestra tiene un outlier
- D) Para obtener un número en las unidades originales

</details>

**3.** Q1 = 20 and Q3 = 40. According to Tukey's rule, which value is an outlier?

- A) 5
- B) 45
- C) 65
- D) 75

<details>
<summary>Traducción al español</summary>

Q1 = 20 y Q3 = 40. Según la regla de Tukey, ¿qué valor es un outlier?

</details>

**4.** In a normal distribution, approximately what percentage of the data falls within ±2 standard deviations of the mean?

- A) 68%
- B) 90%
- C) 95%
- D) 99.7%

<details>
<summary>Traducción al español</summary>

En una distribución normal, ¿aproximadamente qué porcentaje de los datos está a ±2 desviaciones estándar de la media?

</details>

**5.** What does the Central Limit Theorem state?

- A) Every population is normally distributed
- B) The distribution of the sample mean is approximately normal for large samples, regardless of the population's shape
- C) The median equals the mean
- D) Large samples have no outliers

<details>
<summary>Traducción al español</summary>

¿Qué dice el teorema del límite central?

- A) Toda población tiene distribución normal
- B) La distribución de la media muestral es aproximadamente normal con muestras grandes, sin importar la forma de la población
- C) La mediana es igual a la media
- D) Las muestras grandes no tienen outliers

</details>

**6.** Which distribution best models the NUMBER OF ORDERS received per hour?

- A) Normal
- B) Poisson
- C) Uniform
- D) Bernoulli

<details>
<summary>Traducción al español</summary>

¿Qué distribución modela mejor el NÚMERO DE PEDIDOS recibidos por hora?

</details>

**7.** A test detects fraud with 99% sensitivity and a 5% false positive rate. Fraud occurs in 1% of transactions. If a transaction tests positive, the probability that it is really fraud is closest to:

- A) 99%
- B) 95%
- C) 50%
- D) 17%

<details>
<summary>Traducción al español</summary>

Una prueba detecta fraude con 99 % de sensibilidad y 5 % de falsos positivos. El fraude ocurre en el 1 % de las transacciones. Si una transacción sale positiva, la probabilidad de que sea fraude es cercana a:

</details>

**8.** What is the correct definition of a p-value?

- A) The probability that the null hypothesis is true
- B) The probability of observing a result at least as extreme as the one observed, assuming the null hypothesis is true
- C) The probability that the alternative hypothesis is true
- D) The size of the effect

<details>
<summary>Traducción al español</summary>

¿Cuál es la definición correcta del p-valor?

- A) La probabilidad de que la hipótesis nula sea cierta
- B) La probabilidad de observar un resultado al menos tan extremo como el observado, suponiendo que la hipótesis nula es cierta
- C) La probabilidad de que la hipótesis alternativa sea cierta
- D) El tamaño del efecto

</details>

**9.** Rejecting the null hypothesis when it is actually TRUE is a:

- A) Type I error (false positive)
- B) Type II error (false negative)
- C) Sampling error
- D) Correct decision

<details>
<summary>Traducción al español</summary>

Rechazar la hipótesis nula cuando en realidad es VERDADERA es un:

- A) Error tipo I (falso positivo)
- B) Error tipo II (falso negativo)
- C) Error de muestreo
- D) Decisión correcta

</details>

**10.** If you increase the sample size, the 95% confidence interval for the mean becomes:

- A) Wider
- B) Narrower
- C) Exactly the same
- D) Undefined

<details>
<summary>Traducción al español</summary>

Si aumentas el tamaño de la muestra, el intervalo de confianza del 95 % para la media se vuelve:

- A) Más ancho
- B) Más estrecho
- C) Exactamente igual
- D) Indefinido

</details>

**11.** You want to compare the average order value across 4 marketing channels. Which test should you use?

- A) Paired t-test
- B) Chi-square test
- C) ANOVA
- D) Two-proportion z-test

<details>
<summary>Traducción al español</summary>

Quieres comparar el ticket promedio entre 4 canales de marketing. ¿Qué prueba debes usar?

- A) Prueba t pareada
- B) Chi-cuadrado
- C) ANOVA
- D) Prueba z de dos proporciones

</details>

**12.** Which test compares two INDEPENDENT groups when the data is NOT normally distributed?

- A) Mann-Whitney U
- B) Paired t-test
- C) Wilcoxon signed-rank
- D) z-test

<details>
<summary>Traducción al español</summary>

¿Qué prueba compara dos grupos INDEPENDIENTES cuando los datos NO son normales?

- A) Mann-Whitney U
- B) Prueba t pareada
- C) Wilcoxon de rangos con signo
- D) Prueba z

</details>

**13.** An A/B test shows conversion of 10% (A) vs. 12% (B) with 2,000 users per group, and p = 0.043. With α = 0.05, what do you conclude?

- A) The difference is statistically significant
- B) The difference is not significant
- C) B is 43% better
- D) The test must be repeated with the same users

<details>
<summary>Traducción al español</summary>

Una prueba A/B muestra conversión de 10 % (A) vs. 12 % (B) con 2.000 usuarios por grupo y p = 0,043. Con α = 0,05, ¿qué concluyes?

- A) La diferencia es estadísticamente significativa
- B) La diferencia no es significativa
- C) B es 43 % mejor
- D) Hay que repetir la prueba con los mismos usuarios

</details>

**14.** A team checks its A/B test every day and stops it as soon as p < 0.05. What is the problem?

- A) Nothing, it saves time
- B) Peeking inflates the false positive rate
- C) It reduces the sample ratio
- D) It makes the test one-sided

<details>
<summary>Traducción al español</summary>

Un equipo revisa su prueba A/B todos los días y la detiene apenas p < 0,05. ¿Cuál es el problema?

- A) Ninguno, ahorra tiempo
- B) Mirar antes de tiempo (peeking) infla la tasa de falsos positivos
- C) Reduce la proporción de la muestra
- D) Vuelve la prueba unilateral

</details>

**15.** Ice cream sales and drownings are positively correlated. What is the best explanation?

- A) Ice cream causes drownings
- B) A confounding variable (hot weather) affects both
- C) The correlation must be a calculation error
- D) Drownings cause ice cream sales

<details>
<summary>Traducción al español</summary>

Las ventas de helado y los ahogamientos tienen correlación positiva. ¿Cuál es la mejor explicación?

- A) El helado causa ahogamientos
- B) Una variable de confusión (el calor) afecta a ambas
- C) La correlación debe ser un error de cálculo
- D) Los ahogamientos causan ventas de helado

</details>

## Parte B: Machine learning

**16.** A model scores 99% accuracy on the training data but 70% on the test data. This is most likely:

- A) Underfitting
- B) Overfitting
- C) Data imbalance
- D) A perfect model

<details>
<summary>Traducción al español</summary>

Un modelo tiene 99 % de exactitud en entrenamiento pero 70 % en prueba. Lo más probable es:

- A) Subajuste
- B) Sobreajuste
- C) Desbalance de datos
- D) Un modelo perfecto

</details>

**17.** Predicting whether a customer will cancel their subscription (yes/no) is a:

- A) Regression problem
- B) Classification problem
- C) Clustering problem
- D) Dimensionality reduction problem

<details>
<summary>Traducción al español</summary>

Predecir si un cliente cancelará su suscripción (sí/no) es un problema de:

- A) Regresión
- B) Clasificación
- C) Clustering
- D) Reducción de dimensionalidad

</details>

**18.** Which technique groups customers into segments WITHOUT labels?

- A) Logistic regression
- B) k-means
- C) Linear regression
- D) Random forest

<details>
<summary>Traducción al español</summary>

¿Qué técnica agrupa clientes en segmentos SIN etiquetas?

</details>

**19.** A fraud model: TP = 30, FN = 20, FP = 10, TN = 940. What is the RECALL?

- A) 0.75
- B) 0.60
- C) 0.97
- D) 0.30

<details>
<summary>Traducción al español</summary>

Un modelo de fraude: TP = 30, FN = 20, FP = 10, TN = 940. ¿Cuál es el RECALL?

</details>

**20.** Only 5% of the transactions are fraud. A model that always predicts "not fraud" has 95% accuracy. Which metric reveals that it is useless?

- A) Accuracy
- B) Recall
- C) R²
- D) MAE

<details>
<summary>Traducción al español</summary>

Solo el 5 % de las transacciones son fraude. Un modelo que siempre predice "no fraude" tiene 95 % de exactitud. ¿Qué métrica revela que es inútil?

- A) Accuracy (exactitud)
- B) Recall
- C) R²
- D) MAE

</details>

**21.** When fitting a StandardScaler, what is the correct way to avoid data leakage?

- A) Fit it on the full dataset
- B) Fit it on the training set only, then apply it to the test set
- C) Fit it on the test set only
- D) Do not scale the training data

<details>
<summary>Traducción al español</summary>

Al ajustar un StandardScaler, ¿cuál es la forma correcta de evitar la fuga de datos?

- A) Ajustarlo con todo el dataset
- B) Ajustarlo solo con el train y luego aplicarlo al test
- C) Ajustarlo solo con el test
- D) No escalar el train

</details>

**22.** Which regularization can shrink some coefficients exactly to ZERO, performing feature selection?

- A) L2 (Ridge)
- B) L1 (Lasso)
- C) Dropout
- D) Batch normalization

<details>
<summary>Traducción al español</summary>

¿Qué regularización puede llevar algunos coeficientes exactamente a CERO, seleccionando variables?

</details>

**23.** Which algorithm builds MANY decision trees on random samples of rows and features and combines their votes?

- A) Gradient boosting
- B) Random forest
- C) k-NN
- D) Naive Bayes

<details>
<summary>Traducción al español</summary>

¿Qué algoritmo construye MUCHOS árboles de decisión sobre muestras aleatorias de filas y variables y combina sus votos?

</details>

**24.** For which algorithm is feature SCALING least important?

- A) k-NN
- B) k-means
- C) Decision tree
- D) SVM

<details>
<summary>Traducción al español</summary>

¿Para qué algoritmo es MENOS importante escalar las variables?

- A) k-NN
- B) k-means
- C) Árbol de decisión
- D) SVM

</details>

**25.** In gradient descent, what happens if the learning rate is too HIGH?

- A) It converges more slowly
- B) It may overshoot the minimum and diverge
- C) It always finds the global minimum
- D) Nothing changes

<details>
<summary>Traducción al español</summary>

En el descenso del gradiente, ¿qué pasa si la tasa de aprendizaje es demasiado ALTA?

- A) Converge más lento
- B) Puede pasarse del mínimo y diverger
- C) Siempre encuentra el mínimo global
- D) No cambia nada

</details>

---

<details>
<summary><b>Respuestas y explicaciones</b></summary>

| # | Resp. | Explicación |
|---|---|---|
| 1 | **B** | La mediana es robusta a los outliers; la media se va hacia los valores altos. |
| 2 | **B** | Es la corrección de Bessel: la media muestral ya usó un grado de libertad. |
| 3 | **D** | IQR = 20 → límites 20 − 30 = −10 y 40 + 30 = 70. Solo 75 queda fuera. |
| 4 | **C** | Regla empírica 68-95-99,7. |
| 5 | **B** | Por eso funcionan los intervalos de confianza y las pruebas z/t. |
| 6 | **B** | Poisson modela conteos de eventos en un intervalo. |
| 7 | **D** | Bayes: 0,0099 / (0,0099 + 0,0495) ≈ 16,7 %. Error de la tasa base. |
| 8 | **B** | El p-valor se calcula suponiendo H₀ verdadera; no es la probabilidad de H₀. |
| 9 | **A** | Su probabilidad es α. |
| 10 | **B** | El error estándar es s/√n: baja al crecer n. |
| 11 | **C** | 3 o más grupos con medias → ANOVA (y luego comparaciones múltiples). |
| 12 | **A** | Mann-Whitney es no paramétrica para muestras independientes; Wilcoxon es para pares relacionados. |
| 13 | **A** | p = 0,043 < 0,05 → se rechaza H₀. Aun así, revisa si la mejora importa al negocio. |
| 14 | **B** | El tamaño de muestra se decide antes y se respeta. |
| 15 | **B** | Correlación ≠ causalidad. |
| 16 | **B** | Alta varianza: memorizó el train. Usa regularización, validación cruzada o más datos. |
| 17 | **B** | La salida es una categoría → clasificación supervisada. |
| 18 | **B** | k-means es aprendizaje no supervisado (clustering). |
| 19 | **B** | Recall = TP / (TP + FN) = 30/50 = 0,60. (Precision = 30/40 = 0,75.) |
| 20 | **B** | Su recall es 0: no detecta ningún fraude (paradoja de la exactitud). |
| 21 | **B** | El test debe simular datos nunca vistos. |
| 22 | **B** | L1/Lasso anula coeficientes; L2/Ridge solo los encoge. |
| 23 | **B** | Random forest = bagging de árboles. Boosting los construye en secuencia. |
| 24 | **C** | Los árboles dividen por umbrales, no por distancias. |
| 25 | **B** | Pasos demasiado grandes saltan el mínimo; demasiado pequeños tardan mucho. |

**Puntaje:** 22–25 excelente · 17–21 bien · < 17 repasa el [README](README.md).

</details>
