# Cheatsheet: estadística y ML (1 página)

**Español** · [English](estadistica-ml.en.md)

**Descriptiva:** media (sensible a outliers) · **mediana** (robusta; úsala con ingresos) · moda · varianza muestral Σ(x − x̄)²/(**n − 1**) · desviación estándar = √var · IQR = Q3 − Q1 · outlier si < Q1 − 1,5·IQR o > Q3 + 1,5·IQR · z = (x − x̄)/s · sesgo a la derecha ⇒ media > mediana.

**Probabilidad:** P(A o B) = P(A) + P(B) − P(A y B) · independientes: P(A)·P(B) · al menos uno = 1 − P(ninguno) · **Bayes:** P(A|B) = P(B|A)·P(A)/P(B) (cuidado con la tasa base).
**Distribuciones:** Normal (68-95-99,7) · Binomial (éxitos en n intentos) · Bernoulli (sí/no) · **Poisson** (conteos por intervalo) · Uniforme · Exponencial (tiempo entre eventos).
**CLT:** la media muestral ≈ normal con n grande (≥ 30), sin importar la forma de la población.

**Inferencia:** IC 95 % = x̄ ± 1,96·s/√n (más n → IC más estrecho) · H₀ = sin efecto · **p-valor** = P(resultado tan extremo | H₀ cierta) · p < α (0,05) → rechazar H₀ · **Tipo I** = falso positivo (α) · **Tipo II** = falso negativo (β) · **potencia** = 1 − β (≥ 0,8).

| Situación | Prueba |
|---|---|
| Media vs. valor (σ desconocida) | t de una muestra |
| 2 grupos independientes / antes-después | t de dos muestras / t pareada |
| 2 proporciones (A/B de conversión) | z de dos proporciones |
| 3 o más grupos | ANOVA |
| Categóricas | Chi-cuadrado |
| No normal: independientes / pareadas | Mann-Whitney U / Wilcoxon |

**A/B:** hipótesis → línea base → efecto mínimo → **tamaño de muestra** (α = 0,05, potencia = 0,8) → duración en semanas completas → aleatorizar usuarios → **no hacer peeking** → z de proporciones. Ejemplos: 10 % vs. 12 % con 2.000 por grupo → p = 0,043 ✓ · con 200 por grupo → p = 0,52 ✗ · detectar 10 % → 10,5 % requiere ≈ 57.763 por grupo.

**Correlación ≠ causalidad** · Pearson (lineal) · Spearman (rangos) · **Regresión lineal:** β₁ = cov/var, β₀ = ȳ − β₁x̄; R² = varianza explicada; supuestos LINE · **Logística** = clasificación (sigmoide).

**ML:** supervisado (regresión / clasificación) · no supervisado (clustering, PCA) · train/val/test · **overfitting** = alta varianza (bien en train, mal en test) · **underfitting** = alto sesgo · k-fold CV · L1/Lasso (coeficientes a 0) vs. L2/Ridge (encoge) · **data leakage**: ajustar el escalado solo con train · escalar para k-NN, SVM y k-means, no para árboles · one-hot (nominales).

**Algoritmos:** árbol (Gini = 1 − Σp²) · **random forest** = bagging · **gradient boosting** = árboles secuenciales (el mejor en tabulares) · k-NN · Naive Bayes · SVM (margen máximo) · **k-means** (elegir k: codo, silueta) · PCA.

**Métricas:** MAE · RMSE · R² · **precision** = TP/(TP+FP) (falso positivo caro) · **recall** = TP/(TP+FN) (falso negativo caro: fraude, churn) · F1 = 2PR/(P+R) · ROC-AUC (0,5 = azar) · **paradoja de la exactitud** con clases desbalanceadas.

**Marketing (Blend360):** churn (clasificación) · segmentación RFM + k-means · propensión · uplift · CLV · Marketing Mix Modeling · pronóstico · recomendación (Amazon Personalize).
