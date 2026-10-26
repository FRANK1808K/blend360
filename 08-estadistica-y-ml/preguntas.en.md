# 08b · Statistics and ML: 25 practice questions

🌐 [Español](preguntas.md) · **English**

> Try to answer each question in **≤ 60 seconds**. Answers and explanations at the end. Theory: [README.en.md](README.en.md).

---

## Part A: Statistics and A/B tests

**1.** A dataset of salaries is right-skewed by a few very high values. Which measure best represents the typical salary?

- A) Mean
- B) Median
- C) Range
- D) Variance

**2.** Why do we divide by n − 1 when calculating the SAMPLE variance?

- A) To make the calculation faster
- B) To correct the tendency to underestimate the population variance
- C) Because the sample has one outlier
- D) To get a number in the original units

**3.** Q1 = 20 and Q3 = 40. According to Tukey's rule, which value is an outlier?

- A) 5
- B) 45
- C) 65
- D) 75

**4.** In a normal distribution, approximately what percentage of the data falls within ±2 standard deviations of the mean?

- A) 68%
- B) 90%
- C) 95%
- D) 99.7%

**5.** What does the Central Limit Theorem state?

- A) Every population is normally distributed
- B) The distribution of the sample mean is approximately normal for large samples, regardless of the population's shape
- C) The median equals the mean
- D) Large samples have no outliers

**6.** Which distribution best models the NUMBER OF ORDERS received per hour?

- A) Normal
- B) Poisson
- C) Uniform
- D) Bernoulli

**7.** A test detects fraud with 99% sensitivity and a 5% false positive rate. Fraud occurs in 1% of transactions. If a transaction tests positive, the probability that it is really fraud is closest to:

- A) 99%
- B) 95%
- C) 50%
- D) 17%

**8.** What is the correct definition of a p-value?

- A) The probability that the null hypothesis is true
- B) The probability of observing a result at least as extreme as the one observed, assuming the null hypothesis is true
- C) The probability that the alternative hypothesis is true
- D) The size of the effect

**9.** Rejecting the null hypothesis when it is actually TRUE is a:

- A) Type I error (false positive)
- B) Type II error (false negative)
- C) Sampling error
- D) Correct decision

**10.** If you increase the sample size, the 95% confidence interval for the mean becomes:

- A) Wider
- B) Narrower
- C) Exactly the same
- D) Undefined

**11.** You want to compare the average order value across 4 marketing channels. Which test should you use?

- A) Paired t-test
- B) Chi-square test
- C) ANOVA
- D) Two-proportion z-test

**12.** Which test compares two INDEPENDENT groups when the data is NOT normally distributed?

- A) Mann-Whitney U
- B) Paired t-test
- C) Wilcoxon signed-rank
- D) z-test

**13.** An A/B test shows conversion of 10% (A) vs. 12% (B) with 2,000 users per group, and p = 0.043. With α = 0.05, what do you conclude?

- A) The difference is statistically significant
- B) The difference is not significant
- C) B is 43% better
- D) The test must be repeated with the same users

**14.** A team checks its A/B test every day and stops it as soon as p < 0.05. What is the problem?

- A) Nothing, it saves time
- B) Peeking inflates the false positive rate
- C) It reduces the sample ratio
- D) It makes the test one-sided

**15.** Ice cream sales and drownings are positively correlated. What is the best explanation?

- A) Ice cream causes drownings
- B) A confounding variable (hot weather) affects both
- C) The correlation must be a calculation error
- D) Drownings cause ice cream sales

## Part B: Machine learning

**16.** A model scores 99% accuracy on the training data but 70% on the test data. This is most likely:

- A) Underfitting
- B) Overfitting
- C) Data imbalance
- D) A perfect model

**17.** Predicting whether a customer will cancel their subscription (yes/no) is a:

- A) Regression problem
- B) Classification problem
- C) Clustering problem
- D) Dimensionality reduction problem

**18.** Which technique groups customers into segments WITHOUT labels?

- A) Logistic regression
- B) k-means
- C) Linear regression
- D) Random forest

**19.** A fraud model: TP = 30, FN = 20, FP = 10, TN = 940. What is the RECALL?

- A) 0.75
- B) 0.60
- C) 0.97
- D) 0.30

**20.** Only 5% of the transactions are fraud. A model that always predicts "not fraud" has 95% accuracy. Which metric reveals that it is useless?

- A) Accuracy
- B) Recall
- C) R²
- D) MAE

**21.** When fitting a StandardScaler, what is the correct way to avoid data leakage?

- A) Fit it on the full dataset
- B) Fit it on the training set only, then apply it to the test set
- C) Fit it on the test set only
- D) Do not scale the training data

**22.** Which regularization can shrink some coefficients exactly to ZERO, performing feature selection?

- A) L2 (Ridge)
- B) L1 (Lasso)
- C) Dropout
- D) Batch normalization

**23.** Which algorithm builds MANY decision trees on random samples of rows and features and combines their votes?

- A) Gradient boosting
- B) Random forest
- C) k-NN
- D) Naive Bayes

**24.** For which algorithm is feature SCALING least important?

- A) k-NN
- B) k-means
- C) Decision tree
- D) SVM

**25.** In gradient descent, what happens if the learning rate is too HIGH?

- A) It converges more slowly
- B) It may overshoot the minimum and diverge
- C) It always finds the global minimum
- D) Nothing changes

---

<details>
<summary><b>Answer key and explanations</b></summary>

| # | Ans. | Explanation |
|---|---|---|
| 1 | **B** | The median is robust to outliers; the mean is pulled toward the high values. |
| 2 | **B** | It is Bessel's correction: the sample mean already used one degree of freedom. |
| 3 | **D** | IQR = 20 → limits 20 − 30 = −10 and 40 + 30 = 70. Only 75 is outside. |
| 4 | **C** | Empirical rule 68-95-99.7. |
| 5 | **B** | That is why confidence intervals and z/t tests work. |
| 6 | **B** | Poisson models counts of events in an interval. |
| 7 | **D** | Bayes: 0.0099 / (0.0099 + 0.0495) ≈ 16.7%. Base rate fallacy. |
| 8 | **B** | The p-value is computed assuming H₀ is true; it is not the probability of H₀. |
| 9 | **A** | Its probability is α. |
| 10 | **B** | The standard error is s/√n: it falls as n grows. |
| 11 | **C** | 3 or more groups with means → ANOVA (then multiple comparisons). |
| 12 | **A** | Mann-Whitney is non-parametric for independent samples; Wilcoxon is for related pairs. |
| 13 | **A** | p = 0.043 < 0.05 → reject H₀. Still, check whether the lift matters to the business. |
| 14 | **B** | The sample size is decided beforehand and respected. |
| 15 | **B** | Correlation ≠ causation. |
| 16 | **B** | High variance: it memorized the training set. Use regularization, cross-validation or more data. |
| 17 | **B** | The output is a category → supervised classification. |
| 18 | **B** | k-means is unsupervised learning (clustering). |
| 19 | **B** | Recall = TP / (TP + FN) = 30/50 = 0.60. (Precision = 30/40 = 0.75.) |
| 20 | **B** | Its recall is 0: it detects no fraud at all (accuracy paradox). |
| 21 | **B** | The test set must simulate unseen data. |
| 22 | **B** | L1/Lasso zeroes coefficients; L2/Ridge only shrinks them. |
| 23 | **B** | Random forest = bagging of trees. Boosting builds them sequentially. |
| 24 | **C** | Trees split on thresholds, not distances. |
| 25 | **B** | Steps that are too large jump over the minimum; too small ones take too long. |

**Score:** 22–25 excellent · 17–21 good · < 17 review the [README](README.en.md).

</details>
