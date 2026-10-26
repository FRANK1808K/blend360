# 08 · Estadística y Machine Learning para análisis de datos

🌐 **Español** · [English](README.en.md)

> **¿Por qué este módulo?** Blend360 es una empresa de ciencia de datos, y el programa All Star tiene rutas de **Data Science**, Data Engineering y BI. Los candidatos reportan entrevistas con **conceptos de estadística y machine learning**: pruebas A/B, métricas de modelos, sesgo y varianza. Este módulo cubre lo esencial para la prueba y la entrevista, y está **alineado con tus apuntes** de *AI and Data Scientist Roadmap* (Google Drive).

| Archivo | Contenido |
|---|---|
| Este README | Teoría para el examen + ruta de estudio con tus apuntes |
| [estadistica_ml_practica.py](estadistica_ml_practica.py) | Estadística y ML **desde cero** (solo numpy): cada fórmula de este README implementada y verificada |
| [preguntas.md](preguntas.md) | 25 preguntas de práctica en inglés, con la traducción escondida |
| [../cheatsheets/estadistica-ml.md](../cheatsheets/estadistica-ml.md) | Resumen de una página |

```bash
cd 08-estadistica-y-ml
python3 estadistica_ml_practica.py     # requiere numpy (viene con pandas)
```

---

## Índice

1. [Cómo usar este módulo con tus apuntes](#1-cómo-usar-este-módulo-con-tus-apuntes)
2. [Estadística descriptiva](#2-estadística-descriptiva)
3. [Probabilidad y distribuciones](#3-probabilidad-y-distribuciones)
4. [Inferencia: muestreo, intervalos y pruebas de hipótesis](#4-inferencia-muestreo-intervalos-y-pruebas-de-hipótesis)
5. [Pruebas A/B paso a paso](#5-pruebas-ab-paso-a-paso)
6. [Correlación y regresión](#6-correlación-y-regresión)
7. [Fundamentos de machine learning](#7-fundamentos-de-machine-learning)
8. [Algoritmos que debes reconocer](#8-algoritmos-que-debes-reconocer)
9. [Métricas de evaluación](#9-métricas-de-evaluación)
10. [Optimización e hiperparámetros](#10-optimización-e-hiperparámetros)
11. [Casos de uso en analítica de marketing (el negocio de Blend360)](#11-casos-de-uso-en-analítica-de-marketing-el-negocio-de-blend360)
12. [Cómo explicarlo en la entrevista (en inglés)](#12-cómo-explicarlo-en-la-entrevista-en-inglés)

---

## 1. Cómo usar este módulo con tus apuntes

Tus apuntes son **muy completos** (cientos de notebooks). Para el examen no necesitas todos. Este es el orden recomendado: lee primero la sección de este README y después profundiza con el notebook indicado.

| Prioridad | Tema | Sección aquí | Tus apuntes (Drive / Colab) |
|---|---|---|---|
| 🔴 1 | Medidas de tendencia central y dispersión | [§2](#2-estadística-descriptiva) | [2.14 · 2_Exploracion_de_Datos](https://colab.research.google.com/drive/1Y7Th93YoCECN2sQdfh9GnAoL0Mmc94ke) |
| 🔴 1 | Probabilidad | [§3](#3-probabilidad-y-distribuciones) | [2.14 · 4_Probabilidades](https://colab.research.google.com/drive/160mjn6EGhD7PcXBWnKsXRBY4ghzV1UkW) |
| 🔴 1 | Muestreo, estimación e intervalos de confianza | [§4](#4-inferencia-muestreo-intervalos-y-pruebas-de-hipótesis) | [2.14 · 5_Inferencia_Estadistica](https://colab.research.google.com/drive/1DZKE4lqH36PKPbpwK2h0biBdo0SWuV4q) |
| 🔴 1 | Pruebas de hipótesis (t, z, Wilcoxon, Mann-Whitney) | [§4](#4-inferencia-muestreo-intervalos-y-pruebas-de-hipótesis) | [2.14 · 6_Pruebas_de_Hipotesis](https://colab.research.google.com/drive/1ZE1wdffToTFR0PyMMM5Z92j6-IqlHw7o) |
| 🔴 1 | Pruebas A/B y tamaño de muestra | [§5](#5-pruebas-ab-paso-a-paso) | [2.4 · 01 Guía de pruebas estadísticas](https://colab.research.google.com/drive/12rSdaGatp0pxuDGohbh6hVXMdA_2LOzt) · [2.4 · 02 Planificar una prueba A/B](https://colab.research.google.com/drive/1-T_MmnHkE8mE3mn90XXh7yKfjLsyLtDK) |
| 🔴 1 | Regresión y correlación | [§6](#6-correlación-y-regresión) | [2.14 · 7_Regresion_y_Correlacion](https://colab.research.google.com/drive/1XKMxtZeCgeY2kFGKXEYlCXIoBh2Q1C8a) |
| 🔴 1 | Introducción a ML, aprendizaje supervisado y métricas | [§7](#7-fundamentos-de-machine-learning)–[§9](#9-métricas-de-evaluación) | [6.6 · 1_Introducción](https://colab.research.google.com/drive/1rjcCgp-4bGShLpbhaMHscueHHlPogs95) · [6.6 · 3_Aprendizaje_Supervisado](https://colab.research.google.com/drive/1oBGFIvpHb8aKkttwrzubDtBQt_Q4_Zx5) |
| 🟡 2 | Aprendizaje no supervisado (clustering, PCA) | [§8](#8-algoritmos-que-debes-reconocer) | [6.6 · 4_Aprendizaje_No_Supervisado](https://colab.research.google.com/drive/17CRby9GwGD_2RYj2WE_J8ZwcxhHBazRl) |
| 🟡 2 | Optimización e hiperparámetros | [§10](#10-optimización-e-hiperparámetros) | [6.6 · 6_Optimizacion_y_Ajuste_de_Modelos](https://colab.research.google.com/drive/19xt9q9yDQMIFepefqm3xRhOJYlkXslrt) |
| 🟡 2 | ANOVA | [§4](#4-inferencia-muestreo-intervalos-y-pruebas-de-hipótesis) | [2.14 · 8_Analisis_de_Varianza](https://colab.research.google.com/drive/17P-GChbs0RkW4i5VogdRquHdNPPZLU_S) |
| 🟡 2 | Limpieza: imputación, outliers, selección de características, balance de clases | [§7](#7-fundamentos-de-machine-learning) | [Carpeta 5.6 Python para Ciencia de Datos](https://drive.google.com/drive/folders/1gPElqNmiRgILVW8BxcmaEGe2P_cPy46q) |
| 🟡 2 | Estadística aplicada a negocios (30 notebooks cortos) | §2–§6 | [Carpeta 2.7 Estadística para DS y análisis de negocios](https://drive.google.com/drive/folders/195rqdNaTDYkgSabS_J4LjLDJlqO6w6qq) |
| 🟡 2 | Desafíos avanzados (desbalance, interpretabilidad…) | [§7](#7-fundamentos-de-machine-learning) | [6.6 · 7_Desafios_Especificos_y_Avanzados](https://colab.research.google.com/drive/1fZXWsLrTa9jgzzoTu9dXbZfmZxq-iwj8) |
| 🟢 3 | BI: Power BI y Tableau (si te asignan a la ruta de BI) | — | [9.1 Power BI](https://drive.google.com/drive/folders/1VCb3HzCAn993uOKz3GMbm80IBzOwkyDP) · [9.2 Power BI BI](https://drive.google.com/drive/folders/1CEtcyNU_0ApDLeyKs_85YrwsLuU6qKsf) · [9.3 Tableau](https://drive.google.com/drive/folders/10CT_Oqul35pgpj18jvPr4dfD0D0AAjuw) |
| 🟢 3 | Estadística bayesiana, series de tiempo | [§3](#3-probabilidad-y-distribuciones) | [2.11 Bayesiana](https://drive.google.com/drive/folders/1w8DdhE8nJEcUjhy3xvFzHpVpQl2BYx07) · [6.3 Series temporales](https://drive.google.com/drive/folders/1b81vt_LsJoByu2OJFOSboBlwTLL8mXJU) |

> 🔒 Los enlaces abren **tu** Google Drive y Colab: solo funcionan con tu cuenta. Carpeta raíz: [AI_and_Data_Scientist_Roadmap](https://drive.google.com/drive/folders/1VTugpYpYc67DBrTzooJ5gnMk9HXcgcqp).
>
> ⏱️ **Si tienes poco tiempo:** haz solo las filas 🔴. Deep learning y MLOps (carpetas 7 y 8) **no** son prioridad para esta prueba.

## 2. Estadística descriptiva

| Medida | Fórmula / idea | Cuándo usarla | Ojo |
|---|---|---|---|
| **Media** | Σx / n | Datos simétricos | Sensible a outliers |
| **Mediana** | Valor central de los datos ordenados (con n par, el promedio de los dos centrales) | Ingresos, precios, datos sesgados | Robusta a outliers |
| **Moda** | Valor más frecuente | Datos categóricos | Puede haber varias (bimodal) |
| **Rango** | máx − mín | Visión rápida | Solo usa 2 valores |
| **Varianza** | Σ(x − x̄)² / (n − 1) en una **muestra**; / n en la **población** | Dispersión | Está en unidades² |
| **Desviación estándar** | √varianza | Dispersión en las unidades de los datos | |
| **Percentiles / cuartiles** | Q1 = p25, Q2 = mediana, Q3 = p75 | Distribución, boxplots | |
| **IQR** | Q3 − Q1 | Dispersión robusta | Outlier si < Q1 − 1,5·IQR o > Q3 + 1,5·IQR (regla de Tukey) |
| **Puntaje z** | (x − x̄) / s | Comparar escalas distintas, detectar outliers | \|z\| > 3 suele ser atípico |
| **Asimetría (skewness)** | Sesgo a la derecha ⇒ media > mediana | Elegir media o mediana | Ingresos: sesgo a la derecha |

**Ejemplo verificado** (`estadistica_ml_practica.py`): salarios (en millones) 2, 3, 3, 5, 100 → media **22,6**, mediana **3**, moda **3**; el IQR detecta el **100** como outlier. La mediana representa mejor el "salario típico".

> **¿Por qué n − 1?** La media muestral ya "usó" un grado de libertad. Dividir entre n − 1 (**corrección de Bessel**) corrige la tendencia a **subestimar** la varianza real de la población.

## 3. Probabilidad y distribuciones

**Reglas básicas:** P(A o B) = P(A) + P(B) − P(A y B) · si son independientes, P(A y B) = P(A)·P(B) · P(al menos uno) = 1 − P(ninguno).

**Teorema de Bayes:** P(A|B) = P(B|A)·P(A) / P(B).

> **Ejemplo clásico:** una prueba detecta fraude con 99 % de sensibilidad y 5 % de falsos positivos, y el fraude ocurre en el 1 % de las transacciones. Si una transacción sale positiva, ¿qué probabilidad hay de que sea fraude? P = 0,99·0,01 / (0,99·0,01 + 0,05·0,99) ≈ **16,7 %**. La mayoría de las alertas son falsas porque el fraude es raro: es el **error de la tasa base**.

| Distribución | Tipo | Modela | Ejemplo |
|---|---|---|---|
| **Normal** (Gauss) | Continua | Fenómenos que se agrupan alrededor de una media | Estaturas, errores de medición |
| **Binomial** | Discreta | Número de éxitos en n intentos independientes con probabilidad p | Conversiones de 1.000 visitas |
| **Bernoulli** | Discreta | Un solo intento sí/no | ¿Este usuario compró? |
| **Poisson** | Discreta | Conteo de eventos en un intervalo | Pedidos por hora |
| **Uniforme** | Continua o discreta | Todos los valores son igual de probables | Un dado justo |
| **Exponencial** | Continua | Tiempo entre eventos | Minutos entre llegadas de clientes |

- **Regla empírica (68-95-99,7):** en una normal, ~68 % de los datos está a ±1σ, ~95 % a ±2σ y ~99,7 % a ±3σ.
- **Teorema del límite central (CLT):** la **media muestral** se distribuye aproximadamente **normal** cuando n es grande (regla práctica: n ≥ 30), **sin importar** la forma de la población. Es la razón por la que funcionan los intervalos de confianza y las pruebas z/t.
- **Ley de los grandes números:** al aumentar n, la media muestral se acerca a la media real.

## 4. Inferencia: muestreo, intervalos y pruebas de hipótesis

### Muestreo

| Método | Cómo | Riesgo |
|---|---|---|
| Aleatorio simple | Todos tienen la misma probabilidad | Puede dejar fuera grupos pequeños |
| **Estratificado** | Se divide en estratos (p. ej., por país) y se muestrea cada uno | Requiere conocer los estratos |
| Sistemático | Uno de cada k | Periodicidad oculta en los datos |
| Por conglomerados | Se eligen grupos completos (p. ej., tiendas) | Grupos poco representativos |
| Por conveniencia | Los que están a la mano | **Sesgo de selección** ❌ |

### Intervalo de confianza (IC)

**IC del 95 % para la media:** x̄ ± 1,96 · s / √n (con n pequeño, usa el valor t en lugar de 1,96).

- **Interpretación correcta:** si repitieras el muestreo muchas veces, el 95 % de los intervalos construidos así contendría la media real.
- ❌ **Error común:** "hay 95 % de probabilidad de que la media esté en *este* intervalo".
- Un **n mayor** produce un intervalo **más estrecho** (más precisión): el error estándar baja con √n.

Ejemplo verificado: datos 10, 12, 9, 11, 13, 10, 12, 11, 9, 13 → x̄ = 11, s ≈ 1,49 → IC 95 % ≈ **(10,08; 11,92)**.

### Pruebas de hipótesis

| Concepto | Definición |
|---|---|
| **H₀ (nula)** | No hay efecto ni diferencia (lo que se pone a prueba) |
| **H₁ (alternativa)** | Hay efecto; puede ser bilateral (≠) o unilateral (> o <) |
| **α (nivel de significancia)** | Probabilidad de error tipo I que aceptas (normalmente 0,05) |
| **p-valor** | Probabilidad de observar un resultado al menos tan extremo **si H₀ fuera cierta** |
| **Decisión** | p < α → rechazas H₀ ("estadísticamente significativo") |
| **Error tipo I (α)** | Rechazar H₀ cuando es verdadera (**falso positivo**) |
| **Error tipo II (β)** | No rechazar H₀ cuando es falsa (**falso negativo**) |
| **Potencia (1 − β)** | Probabilidad de detectar un efecto que sí existe (meta: ≥ 0,8) |

> ❌ El p-valor **no** es la probabilidad de que H₀ sea cierta. Y "no rechazar H₀" **no** prueba que H₀ sea cierta.

**¿Qué prueba uso?**

| Situación | Prueba |
|---|---|
| Una media vs. un valor, σ desconocida | **t de una muestra**: t = (x̄ − μ₀) / (s/√n) |
| Una media vs. un valor, σ conocida o n grande | **z** |
| Dos grupos independientes (medias) | **t de dos muestras** (Welch si las varianzas difieren) |
| Mismo grupo antes/después | **t pareada** |
| Dos proporciones (conversión A vs. B) | **z de dos proporciones** |
| 3 o más grupos (medias) | **ANOVA** (y después comparaciones múltiples, p. ej., Tukey) |
| Variables categóricas (asociación) | **Chi-cuadrado** |
| Datos no normales / ordinales, 2 grupos independientes | **Mann-Whitney U** (no paramétrica) |
| Datos no normales, pares relacionados | **Wilcoxon** de rangos con signo |

## 5. Pruebas A/B paso a paso

Basado en tu notebook *02 Planificar una prueba A/B*, más el análisis del resultado:

1. **Hipótesis** específica y medible: "Cambiar el botón a verde aumentará la conversión".
2. **Línea base:** la conversión actual (por ejemplo, 10 %).
3. **Tamaño de efecto mínimo** que le importa al negocio (por ejemplo, +5 % relativo → 10,5 %).
4. **Análisis de potencia** → tamaño de muestra (α = 0,05, potencia = 0,8).
5. **Duración** = tamaño de muestra ÷ tráfico diario (corre al menos **semanas completas**, por la estacionalidad semanal).
6. **Alinear** con las partes interesadas **antes** de lanzar: qué decisión se tomará con cada resultado.
7. **Aleatorizar** usuarios (no sesiones) y **no mirar** el resultado antes de tiempo (*peeking*).
8. **Analizar:** prueba z de dos proporciones + IC de la diferencia; revisar significancia **estadística** y **práctica**.

**Ejemplos verificados** (`estadistica_ml_practica.py`):

| Caso | Resultado | Conclusión |
|---|---|---|
| A: 200/2.000 (10 %) vs. B: 240/2.000 (12 %) | z = 2,02 · **p = 0,043** | Significativo con α = 0,05 |
| Las mismas tasas con 10 veces menos usuarios (20/200 vs. 24/200) | **p = 0,52** | No significativo: **falta potencia** |
| Tamaño de muestra para detectar 10 % → 10,5 % | **≈ 57.763 por grupo** | Los efectos pequeños requieren muestras enormes (tu notebook calcula ≈ 57.756) |
| Tamaño de muestra para detectar 10 % → 12 % | ≈ 3.841 por grupo | Un efecto 4 veces mayor necesita ~15 veces menos usuarios |

**Errores típicos (preguntas de entrevista):** detener la prueba apenas sale significativa (*peeking*) · probar muchas métricas o variantes sin corregir las **comparaciones múltiples** (Bonferroni) · **efecto novedad** · *sample ratio mismatch* (la división 50/50 no se cumple) · confundir significancia estadística con impacto de negocio.

## 6. Correlación y regresión

| Coeficiente | Mide | Cuándo |
|---|---|---|
| **Pearson (r)** | Relación **lineal** entre −1 y 1 | Datos continuos, aprox. normales |
| **Spearman (ρ)** | Relación **monótona** (con rangos) | Ordinales u outliers |
| **Kendall (τ)** | Concordancia de rankings | Muestras pequeñas, rankings |

> ⚠️ **Correlación ≠ causalidad.** Las ventas de helado y los ahogamientos se correlacionan porque ambos dependen del calor (**variable de confusión**). Para probar causalidad se necesita un **experimento** (A/B) o métodos causales.

**Regresión lineal:** Y = β₀ + β₁X + ε. Mínimos cuadrados: β₁ = cov(X, Y) / var(X) y β₀ = ȳ − β₁x̄.

- **Interpretación:** "por cada unidad adicional de X, Y cambia en β₁ unidades, *manteniendo lo demás constante*".
- **R²:** proporción de la varianza de Y explicada por el modelo (0 a 1).
- **Supuestos (LINE):** **L**inealidad, **I**ndependencia de los errores, **N**ormalidad de los residuos, **E**qual variance (homocedasticidad).
- **Multicolinealidad:** variables X muy correlacionadas entre sí → coeficientes inestables (revisa el VIF).

Ejemplo verificado: inversión en publicidad 1, 2, 3, 4, 5 → ventas 3, 5, 7, 9, 11 ⇒ **ventas = 2·inversión + 1**, r = 1.

**Regresión logística:** P(Y = 1) = 1 / (1 + e^−(β₀ + β₁X)). Pese a su nombre, es un modelo de **clasificación**: produce una probabilidad entre 0 y 1, y con un umbral (normalmente 0,5) se decide la clase.

## 7. Fundamentos de machine learning

| Tipo | Datos | Objetivo | Ejemplos |
|---|---|---|---|
| **Supervisado** | Con etiqueta (y) | **Regresión** (número) o **clasificación** (categoría) | Predecir ventas; predecir churn |
| **No supervisado** | Sin etiqueta | Encontrar estructura | Segmentar clientes (clustering), reducir dimensiones (PCA) |
| **Por refuerzo** | Recompensas | Aprender acciones | Pujas de anuncios, juegos |

**Flujo de trabajo:** definir el problema y la métrica de negocio → recolectar y **limpiar** los datos → EDA → **ingeniería de variables** → dividir **train / validation / test** → entrenar → evaluar → ajustar hiperparámetros → desplegar → **monitorear** (drift).

| Concepto | Qué es | Cómo se maneja |
|---|---|---|
| **Overfitting** (sobreajuste) | Memoriza el train: muy bien en train, mal en test (**alta varianza**) | Más datos, modelo más simple, regularización, validación cruzada, *early stopping* |
| **Underfitting** (subajuste) | Demasiado simple: mal en train y en test (**alto sesgo**) | Modelo más complejo, mejores variables |
| **Trade-off sesgo-varianza** | Bajar uno suele subir el otro | Buscar el punto de menor error en validación |
| **Validación cruzada k-fold** | Entrenar k veces, validando en un pliegue distinto cada vez | Estimación más estable del rendimiento |
| **Regularización** | Penaliza coeficientes grandes: **L1/Lasso** (puede dejar coeficientes en 0 → selecciona variables) y **L2/Ridge** (los encoge) | Controla el overfitting |
| **Fuga de datos** (*data leakage*) | Información del test o del futuro entra al entrenamiento | Ajusta el escalado y la imputación **solo con train**; respeta el orden temporal |
| **Maldición de la dimensionalidad** | Con muchas variables, los datos se vuelven "dispersos" | Selección de variables, PCA |

**Preparación de datos** (tu carpeta 5.6):

- **Valores faltantes:** eliminar, o imputar con media o mediana, con KNN, o con un indicador de "faltante".
- **Outliers:** IQR o z-score; decidir si son errores o casos reales.
- **Escalado:** estandarización (z) o normalización min-max. **Importa** en k-NN, SVM, regresión regularizada y k-means; **no** en árboles.
- **Codificación:** one-hot para variables **nominales**; ordinal para variables **ordenadas**.
- **Clases desbalanceadas:** sobremuestreo (SMOTE), submuestreo, pesos por clase, y métricas adecuadas (no la exactitud).

## 8. Algoritmos que debes reconocer

| Algoritmo | Tipo | Idea en una frase | Ventajas | Desventajas |
|---|---|---|---|---|
| Regresión lineal | Regresión | Recta que minimiza el error cuadrático | Interpretable, rápida | Solo relaciones lineales |
| Regresión logística | Clasificación | Probabilidad con la función sigmoide | Interpretable, probabilística | Fronteras lineales |
| Árbol de decisión | Ambos | Preguntas sí/no que dividen los datos (Gini o entropía) | Muy interpretable, sin escalado | Se sobreajusta fácil |
| **Random forest** | Ambos | Muchos árboles con datos y variables aleatorias (*bagging*) que votan | Robusto, buen punto de partida | Menos interpretable |
| **Gradient boosting** (XGBoost, LightGBM) | Ambos | Árboles secuenciales que corrigen los errores del anterior | Suele ser el más preciso en datos tabulares | Más hiperparámetros |
| k-NN | Ambos | La clase de los k vecinos más cercanos | Simple | Lento con muchos datos; requiere escalado |
| Naive Bayes | Clasificación | Bayes asumiendo variables independientes | Rápido; bueno para texto | El supuesto rara vez se cumple |
| SVM | Ambos | Hiperplano con el **margen** máximo | Bueno en alta dimensión | Lento con muchos datos |
| **k-means** | Clustering | k centroides; asignar al más cercano y recalcular | Simple, escalable | Hay que elegir k (método del codo, silueta) |
| Jerárquico / DBSCAN | Clustering | Árbol de grupos / densidad | No requiere k (DBSCAN detecta ruido) | Costoso / sensible a parámetros |
| **PCA** | Reducción | Nuevos ejes que conservan la mayor varianza | Menos variables, menos ruido | Componentes difíciles de interpretar |

**Impureza de Gini** = 1 − Σpᵢ². Un nodo puro tiene Gini = 0; un nodo 50/50 tiene 0,5 (verificado en el script).

## 9. Métricas de evaluación

**Regresión:**

| Métrica | Fórmula | Nota |
|---|---|---|
| MAE | promedio de \|y − ŷ\| | En las unidades de y; robusta a outliers |
| MSE / **RMSE** | promedio de (y − ŷ)² / su raíz | Penaliza más los errores grandes |
| **R²** | 1 − SS_res / SS_tot | Varianza explicada |

**Clasificación: matriz de confusión**

```text
                   Predicho: 1    Predicho: 0
Real: 1 (positivo)   TP = 3         FN = 1      ← recall = TP / (TP + FN) = 0.75
Real: 0 (negativo)   FP = 1         TN = 5
                     ↑ precision = TP / (TP + FP) = 0.75
accuracy = (TP + TN) / total = 8/10 = 0.80        F1 = 2·P·R / (P + R) = 0.75
```

| Métrica | Pregunta que responde | Prioriza cuando… |
|---|---|---|
| **Precision** | De los que marqué como positivos, ¿cuántos lo eran? | Un **falso positivo** es caro (spam, oferta costosa) |
| **Recall** (sensibilidad) | De los positivos reales, ¿cuántos encontré? | Un **falso negativo** es caro (fraude, enfermedad, churn) |
| **F1** | Equilibrio entre precision y recall | Clases desbalanceadas |
| **ROC-AUC** | Capacidad de ordenar positivos sobre negativos (0,5 = azar; 1 = perfecto) | Comparar modelos sin fijar un umbral |

> ⚠️ **Paradoja de la exactitud:** con 5 % de fraude, un modelo que dice siempre "no fraude" tiene **95 % de accuracy** y **0 % de recall** (verificado en el script). Con clases desbalanceadas, mira precision, recall, F1 o AUC.

## 10. Optimización e hiperparámetros

- **Descenso del gradiente:** θ ← θ − α·∇J(θ). Con una **tasa de aprendizaje α** muy alta diverge; muy baja, tarda mucho. Variantes: SGD, mini-batch, **Adam** y RMSprop (tasa adaptativa).
- **Parámetros vs. hiperparámetros:** los parámetros se **aprenden** (coeficientes); los hiperparámetros se **eligen** (profundidad del árbol, k, α).
- **Búsqueda de hiperparámetros:** **Grid search** (todas las combinaciones), **random search** (combinaciones al azar; suele ser más eficiente) y **optimización bayesiana** (un modelo probabilístico decide qué probar después). Siempre con **validación cruzada** y **sin tocar el test**.

## 11. Casos de uso en analítica de marketing (el negocio de Blend360)

| Problema de negocio | Tipo de ML | Métrica clave | En AWS |
|---|---|---|---|
| ¿Qué clientes se irán? (**churn**) | Clasificación | Recall / AUC | SageMaker AI |
| **Segmentar** clientes | Clustering (k-means sobre **RFM**: recencia, frecuencia, valor monetario) | Silueta + interpretabilidad de negocio | SageMaker AI |
| ¿Quién comprará si le envío la oferta? (**propensión**) | Clasificación | AUC, lift | SageMaker AI |
| ¿A quién le **cambia** la decisión la campaña? (**uplift**) | Causal / A/B | Incremento | — |
| ¿Cuánto vale un cliente en su vida? (**CLV**) | Regresión | RMSE / MAE | SageMaker AI |
| ¿Cuánto aporta cada canal? (**Marketing Mix Modeling**) | Regresión | ROI por canal | SageMaker AI |
| ¿Cuánto venderemos? (**pronóstico**) | Series de tiempo | MAPE / RMSE | SageMaker AI / Forecast |
| ¿Qué producto recomendar? | Sistemas de recomendación | Precision@k | Amazon Personalize |

## 12. Cómo explicarlo en la entrevista (en inglés)

| Pregunta típica | Respuesta corta (léela en voz alta) |
|---|---|
| *What is a p-value?* | *It's the probability of seeing a result at least this extreme if the null hypothesis were true. If it's below 0.05, we reject the null hypothesis.* |
| *How would you design an A/B test?* | *First, I define the hypothesis and the metric. Then I calculate the sample size with a power analysis, randomize users, run the test for full weeks, and analyze it with a two-proportion z-test.* |
| *What is overfitting?* | *The model learns the training data too well, including the noise, so it performs badly on new data. I prevent it with cross-validation, regularization or a simpler model.* |
| *Precision or recall?* | *It depends on the cost of errors. For fraud, I prioritize recall, because missing a fraud case is expensive.* |
| *Correlation vs. causation?* | *Correlation means two variables move together. Causation means one causes the other. To prove causation, we need an experiment like an A/B test.* |
| *Why is accuracy not enough?* | *With imbalanced classes, a model can have high accuracy and still miss all the positive cases. I prefer F1, recall or AUC.* |

---

**Practica:** [preguntas.md](preguntas.md) · **Repasa:** [cheatsheet de estadística y ML](../cheatsheets/estadistica-ml.md)
