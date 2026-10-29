"""Statistics and machine learning from scratch (only the standard library + numpy).
Estadística y machine learning desde cero (solo la biblioteca estándar + numpy).

Implementing each formula yourself is the best way to understand it, and interviewers
like to hear that you know what happens "under the hood".
Implementar cada fórmula tú mismo es la mejor forma de entenderla, y en las entrevistas
gusta que sepas qué pasa "por dentro".

    pip install numpy          # comes with pandas / viene con pandas
    python3 estadistica_ml_practica.py

Every result is checked with assert / Cada resultado se verifica con assert.
"""
import math
import random
from collections import Counter

import numpy as np


# ---------------------------------------------------------------- 1. Descriptive statistics / Estadística descriptiva

def mean(xs):
    return sum(xs) / len(xs)


def median(xs):
    s = sorted(xs)
    n, mid = len(s), len(s) // 2
    return s[mid] if n % 2 else (s[mid - 1] + s[mid]) / 2       # even n: average of the two middle values / promedio de los dos centrales


def mode(xs):
    return Counter(xs).most_common(1)[0][0]


def variance(xs, sample=True):
    # Sample variance divides by n - 1 (Bessel's correction) / La varianza muestral divide entre n - 1
    m = mean(xs)
    return sum((x - m) ** 2 for x in xs) / (len(xs) - 1 if sample else len(xs))


def std(xs, sample=True):
    return math.sqrt(variance(xs, sample))


def percentile(xs, p):
    # Linear interpolation, the same method as numpy's default / Interpolación lineal, como numpy por defecto
    s = sorted(xs)
    k = (len(s) - 1) * p / 100
    lo, hi = math.floor(k), math.ceil(k)
    return s[lo] + (s[hi] - s[lo]) * (k - lo)


def iqr_outliers(xs):
    q1, q3 = percentile(xs, 25), percentile(xs, 75)
    iqr = q3 - q1
    return [x for x in xs if x < q1 - 1.5 * iqr or x > q3 + 1.5 * iqr]


def z_scores(xs):
    m, s = mean(xs), std(xs)
    return [(x - m) / s for x in xs]


# ---------------------------------------------------------------- 2. Correlation and regression / Correlación y regresión

def pearson(xs, ys):
    mx, my = mean(xs), mean(ys)
    cov = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    return cov / math.sqrt(sum((x - mx) ** 2 for x in xs) * sum((y - my) ** 2 for y in ys))


def linear_regression(xs, ys):
    # Least squares / Mínimos cuadrados: slope = cov(x, y) / var(x), intercept = ȳ - slope · x̄
    mx, my = mean(xs), mean(ys)
    slope = sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / sum((x - mx) ** 2 for x in xs)
    return slope, my - slope * mx


def regression_metrics(y_true, y_pred):
    errors = [t - p for t, p in zip(y_true, y_pred)]
    mae = mean([abs(e) for e in errors])
    mse = mean([e ** 2 for e in errors])
    ss_res = sum(e ** 2 for e in errors)
    ss_tot = sum((t - mean(y_true)) ** 2 for t in y_true)
    return {"MAE": mae, "MSE": mse, "RMSE": math.sqrt(mse), "R2": 1 - ss_res / ss_tot}


# ---------------------------------------------------------------- 3. Classification metrics / Métricas de clasificación

def classification_metrics(y_true, y_pred):
    tp = sum(1 for t, p in zip(y_true, y_pred) if t == 1 and p == 1)
    tn = sum(1 for t, p in zip(y_true, y_pred) if t == 0 and p == 0)
    fp = sum(1 for t, p in zip(y_true, y_pred) if t == 0 and p == 1)     # false alarm / falsa alarma
    fn = sum(1 for t, p in zip(y_true, y_pred) if t == 1 and p == 0)     # missed case / caso no detectado
    precision = tp / (tp + fp) if tp + fp else 0.0
    recall = tp / (tp + fn) if tp + fn else 0.0
    f1 = 2 * precision * recall / (precision + recall) if precision + recall else 0.0
    return {"TP": tp, "TN": tn, "FP": fp, "FN": fn, "accuracy": (tp + tn) / len(y_true),
            "precision": precision, "recall": recall, "F1": f1}


# ---------------------------------------------------------------- 4. Inference and A/B tests / Inferencia y pruebas A/B

def normal_cdf(z):
    return 0.5 * (1 + math.erf(z / math.sqrt(2)))


def confidence_interval_mean(xs, z=1.96):
    # 95 % CI with the normal approximation / IC del 95 % con aproximación normal
    se = std(xs) / math.sqrt(len(xs))
    return mean(xs) - z * se, mean(xs) + z * se


def one_sample_t(xs, mu0):
    # t = (x̄ - μ0) / (s / √n): use it when σ is unknown / úsala cuando no conoces σ
    return (mean(xs) - mu0) / (std(xs) / math.sqrt(len(xs)))


def normal_ppf(p):
    # Inverse of the normal CDF by bisection / Inversa de la CDF normal por bisección
    lo, hi = -10.0, 10.0
    for _ in range(100):
        mid = (lo + hi) / 2
        lo, hi = (mid, hi) if normal_cdf(mid) < p else (lo, mid)
    return (lo + hi) / 2


def sample_size_two_proportions(p0, p1, alpha=0.05, power=0.80):
    # Users needed PER GROUP to detect p0 → p1 / Usuarios necesarios POR GRUPO para detectar p0 → p1
    z_a, z_b = normal_ppf(1 - alpha / 2), normal_ppf(power)
    p_bar = (p0 + p1) / 2
    num = z_a * math.sqrt(2 * p_bar * (1 - p_bar)) + z_b * math.sqrt(p0 * (1 - p0) + p1 * (1 - p1))
    return math.ceil((num / (p1 - p0)) ** 2)


def two_proportion_ztest(conv_a, n_a, conv_b, n_b):
    p_a, p_b = conv_a / n_a, conv_b / n_b
    p_pool = (conv_a + conv_b) / (n_a + n_b)
    se = math.sqrt(p_pool * (1 - p_pool) * (1 / n_a + 1 / n_b))
    z = (p_b - p_a) / se
    p_value = 2 * (1 - normal_cdf(abs(z)))                              # two-sided / bilateral
    return z, p_value


# ---------------------------------------------------------------- 5. ML from scratch / ML desde cero

def train_test_split(rows, test_size=0.2, seed=360):
    rng = random.Random(seed)                                           # fixed seed → reproducible / semilla fija → reproducible
    shuffled = rows[:]
    rng.shuffle(shuffled)
    cut = int(len(shuffled) * (1 - test_size))
    return shuffled[:cut], shuffled[cut:]


def standardize(column):
    # Fit on train only to avoid data leakage / Ajustar solo con train para evitar fuga de datos
    m, s = mean(column), std(column)
    return [(x - m) / s for x in column], (m, s)


def one_hot(values):
    categories = sorted(set(values))
    return [[1 if v == c else 0 for c in categories] for v in values], categories


def knn_predict(train_x, train_y, point, k=3):
    dist = sorted((math.dist(x, point), y) for x, y in zip(train_x, train_y))
    return Counter(y for _, y in dist[:k]).most_common(1)[0][0]


def kmeans(points, centroids, iterations=10):
    pts = np.array(points, dtype=float)
    cents = np.array(centroids, dtype=float)
    for _ in range(iterations):
        labels = np.argmin(((pts[:, None, :] - cents[None, :, :]) ** 2).sum(axis=2), axis=1)   # assign / asignar
        cents = np.array([pts[labels == k].mean(axis=0) for k in range(len(cents))])           # update / actualizar
    return labels.tolist(), cents.round(2).tolist()


def gini(labels):
    # Impurity used by decision trees: 0 = pure node / Impureza de los árboles de decisión: 0 = nodo puro
    n = len(labels)
    return 1 - sum((c / n) ** 2 for c in Counter(labels).values())


# ---------------------------------------------------------------- Demo + checks / Demostración + verificaciones

def main():
    salaries = [2, 3, 3, 5, 100]                                        # thousands / miles
    assert mean(salaries) == 22.6 and median(salaries) == 3 and mode(salaries) == 3
    assert iqr_outliers(salaries) == [100]
    data = [2, 4, 4, 4, 5, 5, 7, 9]
    assert variance(data, sample=False) == 4 and std(data, sample=False) == 2
    assert round(std(data), 4) == 2.1381
    assert percentile(data, 50) == np.percentile(data, 50) and percentile(data, 90) == np.percentile(data, 90)
    assert [round(z, 2) for z in z_scores([10, 20, 30])] == [-1.0, 0.0, 1.0]
    print("1. Descriptive / Descriptiva:", {"mean": 22.6, "median": 3, "outliers (IQR)": iqr_outliers(salaries)})

    ad_spend = [1, 2, 3, 4, 5]                                          # thousands USD / miles USD
    sales = [3, 5, 7, 9, 11]
    assert round(pearson(ad_spend, sales), 6) == 1.0
    slope, intercept = linear_regression(ad_spend, sales)
    assert (slope, intercept) == (2.0, 1.0)                             # sales = 2·spend + 1
    metrics = regression_metrics([3, 5, 7, 9], [2.5, 5.0, 7.5, 9.0])
    assert metrics["MAE"] == 0.25 and metrics["MSE"] == 0.125 and metrics["R2"] == 0.975
    print("2. Regression / Regresión: sales = %.1f·spend + %.1f" % (slope, intercept), metrics)

    y_true = [1, 1, 1, 1, 0, 0, 0, 0, 0, 0]
    y_pred = [1, 1, 1, 0, 1, 0, 0, 0, 0, 0]
    m = classification_metrics(y_true, y_pred)
    assert (m["TP"], m["FP"], m["FN"], m["TN"]) == (3, 1, 1, 5)
    assert m["accuracy"] == 0.8 and m["precision"] == 0.75 and m["recall"] == 0.75 and m["F1"] == 0.75
    always_zero = classification_metrics([1] * 5 + [0] * 95, [0] * 100)  # imbalanced data / datos desbalanceados
    assert always_zero["accuracy"] == 0.95 and always_zero["recall"] == 0.0
    print("3. Classification / Clasificación:", m, "| accuracy paradox / paradoja:", always_zero["accuracy"], always_zero["recall"])

    z, p = two_proportion_ztest(200, 2000, 240, 2000)                   # A: 10 %, B: 12 %
    assert round(z, 2) == 2.02 and round(p, 3) == 0.043
    z_small, p_small = two_proportion_ztest(20, 200, 24, 200)           # same rates, 10× fewer users / 10× menos usuarios
    assert p_small > 0.05
    assert round(normal_ppf(0.975), 2) == 1.96 and round(normal_ppf(0.80), 2) == 0.84
    n_needed = sample_size_two_proportions(0.10, 0.105)               # +5 % relative lift / mejora relativa del 5 %
    assert 57_700 <= n_needed <= 57_800
    assert sample_size_two_proportions(0.10, 0.12) < 5_000             # bigger effect → far fewer users / efecto mayor → muchos menos usuarios
    assert round(one_sample_t([52, 48, 55, 50, 53, 49, 51, 54], 50), 2) == 1.73
    lo, hi = confidence_interval_mean([10, 12, 9, 11, 13, 10, 12, 11, 9, 13])
    assert round(lo, 2) == 10.08 and round(hi, 2) == 11.92
    print(f"4. A/B test: z = {z:.2f}, p = {p:.3f} (significant / significativo) · n=200: p = {p_small:.2f} · 95% CI = ({lo:.2f}, {hi:.2f})")
    print(f"   Sample size / Tamaño de muestra 10% → 10.5%: {n_needed:,} per group / por grupo · 10% → 12%: {sample_size_two_proportions(0.10, 0.12):,}")

    rows = list(range(100))
    train, test = train_test_split(rows)
    assert len(train) == 80 and len(test) == 20 and not set(train) & set(test)
    scaled, (mu, sigma) = standardize([10, 20, 30])
    assert [round(v, 2) for v in scaled] == [-1.0, 0.0, 1.0] and (mu, sigma) == (20, 10)
    encoded, cats = one_hot(["web", "app", "web", "store"])
    assert cats == ["app", "store", "web"] and encoded[0] == [0, 0, 1]
    train_x = [(1, 1), (1, 2), (2, 1), (8, 8), (8, 9), (9, 8)]
    train_y = ["low", "low", "low", "high", "high", "high"]
    assert knn_predict(train_x, train_y, (2, 2)) == "low" and knn_predict(train_x, train_y, (7, 7)) == "high"
    labels, centroids = kmeans(train_x, centroids=[(0, 0), (10, 10)])
    assert labels == [0, 0, 0, 1, 1, 1] and centroids == [[1.33, 1.33], [8.33, 8.33]]
    assert gini(["a", "a", "a", "a"]) == 0 and gini(["a", "a", "b", "b"]) == 0.5
    print("5. ML: split 80/20 ✓ · scaling ✓ · one-hot", cats, "· k-NN ✓ · k-means centroids", centroids, "· Gini ✓")
    print("\nAll checks passed / Todas las verificaciones pasaron ✓")


if __name__ == "__main__":
    main()
