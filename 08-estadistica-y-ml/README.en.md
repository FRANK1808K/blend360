# 08 · Statistics and Machine Learning for data analysis

[Español](README.md) · **English**

> **Why this module?** Blend360 is a data science company, and the All Star program has **Data Science**, Data Engineering and BI tracks. Candidates report interviews with **statistics and machine learning concepts**: A/B tests, model metrics, bias and variance. This module covers the essentials for the test and the interview, and it is **aligned with your notes** from *AI and Data Scientist Roadmap* (Google Drive).

| File | Content |
|---|---|
| This README | Exam theory + a study route through your notes |
| [estadistica_ml_practica.py](estadistica_ml_practica.py) | Statistics and ML **from scratch** (numpy only): every formula in this README implemented and verified |
| [preguntas.en.md](preguntas.en.md) | 25 practice questions |
| [../cheatsheets/estadistica-ml.en.md](../cheatsheets/estadistica-ml.en.md) | One-page summary |

```bash
cd 08-estadistica-y-ml
python3 estadistica_ml_practica.py     # requires numpy (comes with pandas)
```

---

## Contents

1. [How to use this module with your notes](#1-how-to-use-this-module-with-your-notes)
2. [Descriptive statistics](#2-descriptive-statistics)
3. [Probability and distributions](#3-probability-and-distributions)
4. [Inference: sampling, intervals and hypothesis tests](#4-inference-sampling-intervals-and-hypothesis-tests)
5. [A/B tests step by step](#5-ab-tests-step-by-step)
6. [Correlation and regression](#6-correlation-and-regression)
7. [Machine learning fundamentals](#7-machine-learning-fundamentals)
8. [Algorithms you must recognize](#8-algorithms-you-must-recognize)
9. [Evaluation metrics](#9-evaluation-metrics)
10. [Optimization and hyperparameters](#10-optimization-and-hyperparameters)
11. [Marketing analytics use cases (Blend360's business)](#11-marketing-analytics-use-cases-blend360s-business)
12. [How to explain it in the interview](#12-how-to-explain-it-in-the-interview)

---

## 1. How to use this module with your notes

Your notes are **very complete** (hundreds of notebooks). You do not need all of them for the exam. This is the recommended order: read the section of this README first, then go deeper with the notebook listed.

| Priority | Topic | Section here | Your notes (Drive / Colab) |
|---|---|---|---|
| 1 · High | Central tendency and dispersion | [§2](#2-descriptive-statistics) | [2.14 · 2_Exploracion_de_Datos](https://colab.research.google.com/drive/1Y7Th93YoCECN2sQdfh9GnAoL0Mmc94ke) |
| 1 · High | Probability | [§3](#3-probability-and-distributions) | [2.14 · 4_Probabilidades](https://colab.research.google.com/drive/160mjn6EGhD7PcXBWnKsXRBY4ghzV1UkW) |
| 1 · High | Sampling, estimation and confidence intervals | [§4](#4-inference-sampling-intervals-and-hypothesis-tests) | [2.14 · 5_Inferencia_Estadistica](https://colab.research.google.com/drive/1DZKE4lqH36PKPbpwK2h0biBdo0SWuV4q) |
| 1 · High | Hypothesis tests (t, z, Wilcoxon, Mann-Whitney) | [§4](#4-inference-sampling-intervals-and-hypothesis-tests) | [2.14 · 6_Pruebas_de_Hipotesis](https://colab.research.google.com/drive/1ZE1wdffToTFR0PyMMM5Z92j6-IqlHw7o) |
| 1 · High | A/B tests and sample size | [§5](#5-ab-tests-step-by-step) | [2.4 · 01 Statistical tests guide](https://colab.research.google.com/drive/12rSdaGatp0pxuDGohbh6hVXMdA_2LOzt) · [2.4 · 02 Planning an A/B test](https://colab.research.google.com/drive/1-T_MmnHkE8mE3mn90XXh7yKfjLsyLtDK) |
| 1 · High | Regression and correlation | [§6](#6-correlation-and-regression) | [2.14 · 7_Regresion_y_Correlacion](https://colab.research.google.com/drive/1XKMxtZeCgeY2kFGKXEYlCXIoBh2Q1C8a) |
| 1 · High | Introduction to ML, supervised learning and metrics | [§7](#7-machine-learning-fundamentals)–[§9](#9-evaluation-metrics) | [6.6 · 1_Introducción](https://colab.research.google.com/drive/1rjcCgp-4bGShLpbhaMHscueHHlPogs95) · [6.6 · 3_Aprendizaje_Supervisado](https://colab.research.google.com/drive/1oBGFIvpHb8aKkttwrzubDtBQt_Q4_Zx5) |
| 2 · Medium | Unsupervised learning (clustering, PCA) | [§8](#8-algorithms-you-must-recognize) | [6.6 · 4_Aprendizaje_No_Supervisado](https://colab.research.google.com/drive/17CRby9GwGD_2RYj2WE_J8ZwcxhHBazRl) |
| 2 · Medium | Optimization and hyperparameters | [§10](#10-optimization-and-hyperparameters) | [6.6 · 6_Optimizacion_y_Ajuste_de_Modelos](https://colab.research.google.com/drive/19xt9q9yDQMIFepefqm3xRhOJYlkXslrt) |
| 2 · Medium | ANOVA | [§4](#4-inference-sampling-intervals-and-hypothesis-tests) | [2.14 · 8_Analisis_de_Varianza](https://colab.research.google.com/drive/17P-GChbs0RkW4i5VogdRquHdNPPZLU_S) |
| 2 · Medium | Cleaning: imputation, outliers, feature selection, class balance | [§7](#7-machine-learning-fundamentals) | [Folder 5.6 Python for Data Science](https://drive.google.com/drive/folders/1gPElqNmiRgILVW8BxcmaEGe2P_cPy46q) |
| 2 · Medium | Statistics applied to business (30 short notebooks) | §2–§6 | [Folder 2.7 Statistics for DS and business analysis](https://drive.google.com/drive/folders/195rqdNaTDYkgSabS_J4LjLDJlqO6w6qq) |
| 2 · Medium | Advanced challenges (imbalance, interpretability…) | [§7](#7-machine-learning-fundamentals) | [6.6 · 7_Desafios_Especificos_y_Avanzados](https://colab.research.google.com/drive/1fZXWsLrTa9jgzzoTu9dXbZfmZxq-iwj8) |
| 3 · Low | BI: Power BI and Tableau (if you are placed on the BI track) | — | [9.1 Power BI](https://drive.google.com/drive/folders/1VCb3HzCAn993uOKz3GMbm80IBzOwkyDP) · [9.2 Power BI BI](https://drive.google.com/drive/folders/1CEtcyNU_0ApDLeyKs_85YrwsLuU6qKsf) · [9.3 Tableau](https://drive.google.com/drive/folders/10CT_Oqul35pgpj18jvPr4dfD0D0AAjuw) |
| 3 · Low | Bayesian statistics, time series | [§3](#3-probability-and-distributions) | [2.11 Bayesian](https://drive.google.com/drive/folders/1w8DdhE8nJEcUjhy3xvFzHpVpQl2BYx07) · [6.3 Time series](https://drive.google.com/drive/folders/1b81vt_LsJoByu2OJFOSboBlwTLL8mXJU) |

> The links open **your** Google Drive and Colab: they only work with your account. Root folder: [AI_and_Data_Scientist_Roadmap](https://drive.google.com/drive/folders/1VTugpYpYc67DBrTzooJ5gnMk9HXcgcqp).
>
> **Short on time:** do only the priority 1 rows. Deep learning and MLOps (folders 7 and 8) are **not** a priority for this test.

## 2. Descriptive statistics

| Measure | Formula / idea | When to use it | Watch out |
|---|---|---|---|
| **Mean** | Σx / n | Symmetric data | Sensitive to outliers |
| **Median** | Middle value of the sorted data (with even n, the average of the two middle values) | Income, prices, skewed data | Robust to outliers |
| **Mode** | Most frequent value | Categorical data | There can be several (bimodal) |
| **Range** | max − min | A quick view | Uses only 2 values |
| **Variance** | Σ(x − x̄)² / (n − 1) for a **sample**; / n for the **population** | Dispersion | In units² |
| **Standard deviation** | √variance | Dispersion in the data's units | |
| **Percentiles / quartiles** | Q1 = p25, Q2 = median, Q3 = p75 | Distribution, box plots | |
| **IQR** | Q3 − Q1 | Robust dispersion | Outlier if < Q1 − 1.5·IQR or > Q3 + 1.5·IQR (Tukey's rule) |
| **z-score** | (x − x̄) / s | Compare different scales, detect outliers | \|z\| > 3 is usually unusual |
| **Skewness** | Right-skewed ⇒ mean > median | Choosing mean or median | Income is right-skewed |

**Verified example** (`estadistica_ml_practica.py`): salaries (millions) 2, 3, 3, 5, 100 → mean **22.6**, median **3**, mode **3**; the IQR flags **100** as an outlier. The median represents the "typical salary" better.

> **Why n − 1?** The sample mean has already "used" one degree of freedom. Dividing by n − 1 (**Bessel's correction**) fixes the tendency to **underestimate** the real population variance.

## 3. Probability and distributions

**Basic rules:** P(A or B) = P(A) + P(B) − P(A and B) · if independent, P(A and B) = P(A)·P(B) · P(at least one) = 1 − P(none).

**Bayes' theorem:** P(A|B) = P(B|A)·P(A) / P(B).

> **Classic example:** a test detects fraud with 99 % sensitivity and 5 % false positives, and fraud happens in 1 % of transactions. If a transaction tests positive, what is the probability that it is fraud? P = 0.99·0.01 / (0.99·0.01 + 0.05·0.99) ≈ **16.7 %**. Most alerts are false because fraud is rare: this is the **base rate fallacy**.

| Distribution | Type | Models | Example |
|---|---|---|---|
| **Normal** (Gaussian) | Continuous | Phenomena that cluster around a mean | Heights, measurement errors |
| **Binomial** | Discrete | Number of successes in n independent trials with probability p | Conversions out of 1,000 visits |
| **Bernoulli** | Discrete | A single yes/no trial | Did this user buy? |
| **Poisson** | Discrete | Count of events in an interval | Orders per hour |
| **Uniform** | Continuous or discrete | Every value is equally likely | A fair die |
| **Exponential** | Continuous | Time between events | Minutes between customer arrivals |

- **Empirical rule (68-95-99.7):** in a normal distribution, ~68 % of the data is within ±1σ, ~95 % within ±2σ and ~99.7 % within ±3σ.
- **Central limit theorem (CLT):** the **sample mean** is approximately **normally** distributed when n is large (rule of thumb: n ≥ 30), **regardless** of the population's shape. This is why confidence intervals and z/t tests work.
- **Law of large numbers:** as n grows, the sample mean approaches the true mean.

## 4. Inference: sampling, intervals and hypothesis tests

### Sampling

| Method | How | Risk |
|---|---|---|
| Simple random | Everyone has the same probability | May leave out small groups |
| **Stratified** | Split into strata (e.g., by country) and sample each one | You must know the strata |
| Systematic | One out of every k | Hidden periodicity in the data |
| Cluster | Whole groups are chosen (e.g., stores) | Unrepresentative groups |
| Convenience | Whoever is at hand | **Selection bias** ✗ |

### Confidence interval (CI)

**95 % CI for the mean:** x̄ ± 1.96 · s / √n (with a small n, use the t value instead of 1.96).

- **Correct interpretation:** if you repeated the sampling many times, 95 % of the intervals built this way would contain the true mean.
- ✗ **Common mistake:** "there is a 95 % probability that the mean is in *this* interval".
- A **larger n** gives a **narrower** interval (more precision): the standard error falls with √n.

Verified example: data 10, 12, 9, 11, 13, 10, 12, 11, 9, 13 → x̄ = 11, s ≈ 1.49 → 95 % CI ≈ **(10.08, 11.92)**.

### Hypothesis tests

| Concept | Definition |
|---|---|
| **H₀ (null)** | There is no effect or difference (what is being tested) |
| **H₁ (alternative)** | There is an effect; two-sided (≠) or one-sided (> or <) |
| **α (significance level)** | The probability of a type I error you accept (usually 0.05) |
| **p-value** | Probability of observing a result at least as extreme **if H₀ were true** |
| **Decision** | p < α → reject H₀ ("statistically significant") |
| **Type I error (α)** | Rejecting H₀ when it is true (**false positive**) |
| **Type II error (β)** | Not rejecting H₀ when it is false (**false negative**) |
| **Power (1 − β)** | Probability of detecting an effect that really exists (goal: ≥ 0.8) |

> ✗ The p-value is **not** the probability that H₀ is true. And "not rejecting H₀" does **not** prove H₀ is true.

**Which test do I use?**

| Situation | Test |
|---|---|
| One mean vs. a value, σ unknown | **One-sample t**: t = (x̄ − μ₀) / (s/√n) |
| One mean vs. a value, σ known or large n | **z** |
| Two independent groups (means) | **Two-sample t** (Welch if the variances differ) |
| Same group before/after | **Paired t** |
| Two proportions (conversion A vs. B) | **Two-proportion z** |
| 3 or more groups (means) | **ANOVA** (then multiple comparisons, e.g., Tukey) |
| Categorical variables (association) | **Chi-square** |
| Non-normal / ordinal data, 2 independent groups | **Mann-Whitney U** (non-parametric) |
| Non-normal data, related pairs | **Wilcoxon** signed-rank |

## 5. A/B tests step by step

Based on your notebook *02 Planning an A/B test*, plus the analysis of the result:

1. A specific, measurable **hypothesis**: "Changing the button to green will increase conversion".
2. **Baseline:** the current conversion rate (e.g., 10 %).
3. The **minimum effect size** the business cares about (e.g., +5 % relative → 10.5 %).
4. **Power analysis** → sample size (α = 0.05, power = 0.8).
5. **Duration** = sample size ÷ daily traffic (run for **full weeks**, because of weekly seasonality).
6. **Align** with stakeholders **before** launching: which decision will be made for each outcome.
7. **Randomize** users (not sessions) and **do not peek** at the result early.
8. **Analyze:** two-proportion z-test + CI of the difference; check **statistical** and **practical** significance.

**Verified examples** (`estadistica_ml_practica.py`):

| Case | Result | Conclusion |
|---|---|---|
| A: 200/2,000 (10 %) vs. B: 240/2,000 (12 %) | z = 2.02 · **p = 0.043** | Significant at α = 0.05 |
| The same rates with 10 times fewer users (20/200 vs. 24/200) | **p = 0.52** | Not significant: **not enough power** |
| Sample size to detect 10 % → 10.5 % | **≈ 57,763 per group** | Small effects need huge samples (your notebook computes ≈ 57,756) |
| Sample size to detect 10 % → 12 % | ≈ 3,841 per group | An effect 4 times larger needs ~15 times fewer users |

**Typical mistakes (interview questions):** stopping the test as soon as it becomes significant (*peeking*) · testing many metrics or variants without correcting for **multiple comparisons** (Bonferroni) · the **novelty effect** · *sample ratio mismatch* (the 50/50 split does not hold) · confusing statistical significance with business impact.

## 6. Correlation and regression

| Coefficient | Measures | When |
|---|---|---|
| **Pearson (r)** | **Linear** relationship between −1 and 1 | Continuous, roughly normal data |
| **Spearman (ρ)** | **Monotonic** relationship (with ranks) | Ordinal data or outliers |
| **Kendall (τ)** | Agreement between rankings | Small samples, rankings |

> **Correlation ≠ causation.** Ice cream sales and drownings are correlated because both depend on hot weather (a **confounding variable**). To prove causation you need an **experiment** (A/B) or causal methods.

**Linear regression:** Y = β₀ + β₁X + ε. Least squares: β₁ = cov(X, Y) / var(X) and β₀ = ȳ − β₁x̄.

- **Interpretation:** "for each additional unit of X, Y changes by β₁ units, *holding everything else constant*".
- **R²:** share of the variance of Y explained by the model (0 to 1).
- **Assumptions (LINE):** **L**inearity, **I**ndependence of errors, **N**ormality of residuals, **E**qual variance (homoscedasticity).
- **Multicollinearity:** X variables highly correlated with each other → unstable coefficients (check the VIF).

Verified example: ad spend 1, 2, 3, 4, 5 → sales 3, 5, 7, 9, 11 ⇒ **sales = 2·spend + 1**, r = 1.

**Logistic regression:** P(Y = 1) = 1 / (1 + e^−(β₀ + β₁X)). Despite its name, it is a **classification** model: it outputs a probability between 0 and 1, and a threshold (usually 0.5) decides the class.

## 7. Machine learning fundamentals

| Type | Data | Goal | Examples |
|---|---|---|---|
| **Supervised** | Labeled (y) | **Regression** (a number) or **classification** (a category) | Predict sales; predict churn |
| **Unsupervised** | Unlabeled | Find structure | Customer segmentation (clustering), dimensionality reduction (PCA) |
| **Reinforcement** | Rewards | Learn actions | Ad bidding, games |

**Workflow:** define the problem and the business metric → collect and **clean** the data → EDA → **feature engineering** → split **train / validation / test** → train → evaluate → tune hyperparameters → deploy → **monitor** (drift).

| Concept | What it is | How to handle it |
|---|---|---|
| **Overfitting** | Memorizes the training set: great on train, poor on test (**high variance**) | More data, simpler model, regularization, cross-validation, early stopping |
| **Underfitting** | Too simple: poor on train and test (**high bias**) | More complex model, better features |
| **Bias-variance trade-off** | Lowering one usually raises the other | Find the point of lowest validation error |
| **k-fold cross-validation** | Train k times, validating on a different fold each time | A more stable performance estimate |
| **Regularization** | Penalizes large coefficients: **L1/Lasso** (can set coefficients to 0 → feature selection) and **L2/Ridge** (shrinks them) | Controls overfitting |
| **Data leakage** | Information from the test set or the future leaks into training | Fit scaling and imputation **on train only**; respect time order |
| **Curse of dimensionality** | With many features, the data becomes "sparse" | Feature selection, PCA |

**Data preparation** (your folder 5.6):

- **Missing values:** drop, or impute with the mean or median, with KNN, or with a "missing" indicator.
- **Outliers:** IQR or z-score; decide whether they are errors or real cases.
- **Scaling:** standardization (z) or min-max normalization. It **matters** for k-NN, SVM, regularized regression and k-means; **not** for trees.
- **Encoding:** one-hot for **nominal** variables; ordinal for **ordered** ones.
- **Imbalanced classes:** oversampling (SMOTE), undersampling, class weights, and suitable metrics (not accuracy).

## 8. Algorithms you must recognize

| Algorithm | Type | Idea in one sentence | Pros | Cons |
|---|---|---|---|---|
| Linear regression | Regression | A line that minimizes squared error | Interpretable, fast | Linear relationships only |
| Logistic regression | Classification | Probability with the sigmoid function | Interpretable, probabilistic | Linear boundaries |
| Decision tree | Both | Yes/no questions that split the data (Gini or entropy) | Very interpretable, no scaling | Overfits easily |
| **Random forest** | Both | Many trees on random rows and features (*bagging*) that vote | Robust, a good baseline | Less interpretable |
| **Gradient boosting** (XGBoost, LightGBM) | Both | Sequential trees that fix the previous one's errors | Often the most accurate on tabular data | More hyperparameters |
| k-NN | Both | The class of the k nearest neighbors | Simple | Slow on large data; needs scaling |
| Naive Bayes | Classification | Bayes assuming independent features | Fast; good for text | The assumption rarely holds |
| SVM | Both | The hyperplane with the maximum **margin** | Good in high dimensions | Slow on large data |
| **k-means** | Clustering | k centroids; assign to the nearest and recompute | Simple, scalable | You must choose k (elbow, silhouette) |
| Hierarchical / DBSCAN | Clustering | A tree of groups / density | No k needed (DBSCAN finds noise) | Expensive / parameter-sensitive |
| **PCA** | Reduction | New axes that keep the most variance | Fewer features, less noise | Components are hard to interpret |

**Gini impurity** = 1 − Σpᵢ². A pure node has Gini = 0; a 50/50 node has 0.5 (verified in the script).

## 9. Evaluation metrics

**Regression:**

| Metric | Formula | Note |
|---|---|---|
| MAE | mean of \|y − ŷ\| | In y's units; robust to outliers |
| MSE / **RMSE** | mean of (y − ŷ)² / its square root | Penalizes large errors more |
| **R²** | 1 − SS_res / SS_tot | Explained variance |

**Classification: confusion matrix**

```text
                   Predicted: 1   Predicted: 0
Actual: 1 (positive)  TP = 3         FN = 1      ← recall = TP / (TP + FN) = 0.75
Actual: 0 (negative)  FP = 1         TN = 5
                      ↑ precision = TP / (TP + FP) = 0.75
accuracy = (TP + TN) / total = 8/10 = 0.80        F1 = 2·P·R / (P + R) = 0.75
```

| Metric | Question it answers | Prioritize when… |
|---|---|---|
| **Precision** | Of the ones I flagged as positive, how many were? | A **false positive** is expensive (spam, a costly offer) |
| **Recall** (sensitivity) | Of the real positives, how many did I find? | A **false negative** is expensive (fraud, disease, churn) |
| **F1** | Balance between precision and recall | Imbalanced classes |
| **ROC-AUC** | Ability to rank positives above negatives (0.5 = chance; 1 = perfect) | Comparing models without fixing a threshold |

> **Accuracy paradox:** with 5 % fraud, a model that always says "no fraud" has **95 % accuracy** and **0 % recall** (verified in the script). With imbalanced classes, look at precision, recall, F1 or AUC.

## 10. Optimization and hyperparameters

- **Gradient descent:** θ ← θ − α·∇J(θ). With a **learning rate α** that is too high it diverges; too low, it is slow. Variants: SGD, mini-batch, **Adam** and RMSprop (adaptive learning rate).
- **Parameters vs. hyperparameters:** parameters are **learned** (coefficients); hyperparameters are **chosen** (tree depth, k, α).
- **Hyperparameter search:** **grid search** (every combination), **random search** (random combinations; usually more efficient) and **Bayesian optimization** (a probabilistic model decides what to try next). Always with **cross-validation** and **without touching the test set**.

## 11. Marketing analytics use cases (Blend360's business)

| Business problem | ML type | Key metric | On AWS |
|---|---|---|---|
| Which customers will leave? (**churn**) | Classification | Recall / AUC | SageMaker AI |
| **Segment** customers | Clustering (k-means on **RFM**: recency, frequency, monetary value) | Silhouette + business interpretability | SageMaker AI |
| Who will buy if I send the offer? (**propensity**) | Classification | AUC, lift | SageMaker AI |
| Whose decision does the campaign **change**? (**uplift**) | Causal / A/B | Incremental lift | — |
| How much is a customer worth over their lifetime? (**CLV**) | Regression | RMSE / MAE | SageMaker AI |
| How much does each channel contribute? (**Marketing Mix Modeling**) | Regression | ROI per channel | SageMaker AI |
| How much will we sell? (**forecasting**) | Time series | MAPE / RMSE | SageMaker AI / Forecast |
| Which product should we recommend? | Recommender systems | Precision@k | Amazon Personalize |

## 12. How to explain it in the interview

| Typical question | Short answer (read it out loud) |
|---|---|
| *What is a p-value?* | *It's the probability of seeing a result at least this extreme if the null hypothesis were true. If it's below 0.05, we reject the null hypothesis.* |
| *How would you design an A/B test?* | *First, I define the hypothesis and the metric. Then I calculate the sample size with a power analysis, randomize users, run the test for full weeks, and analyze it with a two-proportion z-test.* |
| *What is overfitting?* | *The model learns the training data too well, including the noise, so it performs badly on new data. I prevent it with cross-validation, regularization or a simpler model.* |
| *Precision or recall?* | *It depends on the cost of errors. For fraud, I prioritize recall, because missing a fraud case is expensive.* |
| *Correlation vs. causation?* | *Correlation means two variables move together. Causation means one causes the other. To prove causation, we need an experiment like an A/B test.* |
| *Why is accuracy not enough?* | *With imbalanced classes, a model can have high accuracy and still miss all the positive cases. I prefer F1, recall or AUC.* |

---

**Practice:** [preguntas.en.md](preguntas.en.md) · **Review:** [statistics and ML cheat sheet](../cheatsheets/estadistica-ml.en.md)
