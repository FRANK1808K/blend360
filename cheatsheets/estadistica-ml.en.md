# Cheat sheet: statistics and ML (1 page)

[Español](estadistica-ml.md) · **English**

**Descriptive:** mean (sensitive to outliers) · **median** (robust; use it for income) · mode · sample variance Σ(x − x̄)²/(**n − 1**) · standard deviation = √var · IQR = Q3 − Q1 · outlier if < Q1 − 1.5·IQR or > Q3 + 1.5·IQR · z = (x − x̄)/s · right-skewed ⇒ mean > median.

**Probability:** P(A or B) = P(A) + P(B) − P(A and B) · independent: P(A)·P(B) · at least one = 1 − P(none) · **Bayes:** P(A|B) = P(B|A)·P(A)/P(B) (watch the base rate).
**Distributions:** Normal (68-95-99.7) · Binomial (successes in n trials) · Bernoulli (yes/no) · **Poisson** (counts per interval) · Uniform · Exponential (time between events).
**CLT:** the sample mean is ≈ normal for large n (≥ 30), regardless of the population's shape.

**Inference:** 95 % CI = x̄ ± 1.96·s/√n (larger n → narrower CI) · H₀ = no effect · **p-value** = P(result this extreme | H₀ true) · p < α (0.05) → reject H₀ · **Type I** = false positive (α) · **Type II** = false negative (β) · **power** = 1 − β (≥ 0.8).

| Situation | Test |
|---|---|
| Mean vs. a value (σ unknown) | One-sample t |
| 2 independent groups / before-after | Two-sample t / paired t |
| 2 proportions (conversion A/B) | Two-proportion z |
| 3 or more groups | ANOVA |
| Categorical | Chi-square |
| Non-normal: independent / paired | Mann-Whitney U / Wilcoxon |

**A/B:** hypothesis → baseline → minimum effect → **sample size** (α = 0.05, power = 0.8) → duration in full weeks → randomize users → **no peeking** → two-proportion z. Examples: 10 % vs. 12 % with 2,000 per group → p = 0.043 ✓ · with 200 per group → p = 0.52 ✗ · detecting 10 % → 10.5 % needs ≈ 57,763 per group.

**Correlation ≠ causation** · Pearson (linear) · Spearman (ranks) · **Linear regression:** β₁ = cov/var, β₀ = ȳ − β₁x̄; R² = explained variance; LINE assumptions · **Logistic** = classification (sigmoid).

**ML:** supervised (regression / classification) · unsupervised (clustering, PCA) · train/val/test · **overfitting** = high variance (good on train, bad on test) · **underfitting** = high bias · k-fold CV · L1/Lasso (coefficients to 0) vs. L2/Ridge (shrinks) · **data leakage**: fit scaling on train only · scale for k-NN, SVM and k-means, not for trees · one-hot (nominal).

**Algorithms:** tree (Gini = 1 − Σp²) · **random forest** = bagging · **gradient boosting** = sequential trees (best on tabular data) · k-NN · Naive Bayes · SVM (maximum margin) · **k-means** (choose k: elbow, silhouette) · PCA.

**Metrics:** MAE · RMSE · R² · **precision** = TP/(TP+FP) (false positives are costly) · **recall** = TP/(TP+FN) (false negatives are costly: fraud, churn) · F1 = 2PR/(P+R) · ROC-AUC (0.5 = chance) · **accuracy paradox** with imbalanced classes.

**Marketing (Blend360):** churn (classification) · RFM segmentation + k-means · propensity · uplift · CLV · Marketing Mix Modeling · forecasting · recommendations (Amazon Personalize).
