# 07 · Problem solving (+ logic, math and basic statistics)

🌐 [Español](README.md) · **English**

> In a test from a data company, "problem solving" usually mixes three things:
>
> 1. **Programming problems** that you must break down and solve.
> 2. **Logical-mathematical reasoning** (percentages, ratios, probability, counting).
> 3. **Business/analytics cases**: "sales dropped, what would you do?".
>
> Here you have a **method** for each one, plus solved exercises.

---

## 1. A method for programming problems (UMPIRE)

| Step | What you do | Time (in a 20-min problem) |
|---|---|---|
| **U**nderstand | Read it **twice**. Underline the input, the output and the constraints. Restate the problem in one sentence | 2–3 min |
| **M**atch | Which pattern does it look like? (hash map, two pointers, window, BFS…) See the [pattern table](../04-algoritmos-y-estructuras/README.en.md#6-patterns-that-solve-80--of-the-problems) | 1 min |
| **P**lan | Write the steps as comments or pseudocode. Start with **brute force** if you see nothing else | 3 min |
| **I**mplement | Code following the plan. Use clear names | 8 min |
| **R**eview | Walk through the code by hand with the example **and** with the edge cases | 3 min |
| **E**valuate | State the complexity and whether it can be improved | 1 min |

> 🔑 **A correct O(n²) solution is worth more than an O(n) one that does not work.** Make it work first, then optimize if you have time left.

### Edge case checklist

- [ ] **Empty** input (`[]`, `""`, 0 rows)
- [ ] **A single** element
- [ ] All elements **equal** / **duplicates**
- [ ] **Negative** numbers, **zero**, very large numbers
- [ ] Already **sorted** / sorted in reverse
- [ ] **NULL / None** / missing values (real data always has them!)
- [ ] Uppercase/lowercase, extra spaces, accents
- [ ] Limits: first and last index (*off-by-one*)
- [ ] Ties

### A step-by-step solved example

> **Problem:** *Given a list of transactions `(customer_id, amount)`, return the customer IDs whose total amount is at least 1000, sorted by total descending.*

**U:** The input is a list of tuples; the output, a list of IDs. We must **sum per customer**, **filter** totals ≥ 1000 and **sort** from highest to lowest.
**M:** Group and sum → a **dictionary** (like a `GROUP BY` + `HAVING` + `ORDER BY`).
**P:**

1. Go through the transactions and accumulate `totals[customer] += amount`.
2. Keep the totals ≥ 1000.
3. Sort by total, descending.

**I:**

```python
from collections import defaultdict

def big_customers(transactions, threshold=1000):
    totals = defaultdict(float)
    for customer_id, amount in transactions:
        totals[customer_id] += amount
    selected = [(c, t) for c, t in totals.items() if t >= threshold]
    selected.sort(key=lambda x: x[1], reverse=True)
    return [c for c, _ in selected]
```

**R:** `[(1, 600), (2, 1500), (1, 500)]` → totals `{1: 1100, 2: 1500}` → `[2, 1]` ✅. Empty list → `[]` ✅. Exactly 1000 → included (≥) ✅.
**E:** O(n + k log k), where k = number of customers. Space O(k).

**The same problem in SQL:**

```sql
SELECT customer_id
FROM transactions
GROUP BY customer_id
HAVING SUM(amount) >= 1000
ORDER BY SUM(amount) DESC;
```

## 2. Time management in the technical test (90 min)

1. **Minutes 0–3:** look at **all** the questions or sections. Identify the easy ones and what is worth the most points.
2. Do what you know first. **Flag and skip** anything that blocks you for more than 2 minutes (multiple choice) or more than 5 minutes without progress (code).
3. In code: **submit something that runs**. If the platform has test cases, run them often; partial credit counts.
4. Keep the **last 5–10 min** to review the flagged questions and leave **nothing** blank (if wrong answers are not penalized, guess).
5. Track your pace: 90 min ÷ number of questions = your pace. For example, 40 questions → ~2 min per question.

## 3. Logical-mathematical reasoning

### Percentages (very frequent!)

| Situation | Formula | Example |
|---|---|---|
| % change | (new − old) / old × 100 | 80 → 100: +25 %. 100 → 80: −20 % |
| Increase by x % | value × (1 + x/100) | 200 + 15 % = 230 |
| Successive increases | They **multiply**, they do not add | +10 % then +10 % = ×1.21 → +21 % |
| Up and down by the same % | It does **not** return to the original | 100 → +20 % → 120 → −20 % → 96 |
| Percentage points vs. % | From 10 % to 12 % = +2 **percentage points** = +20 % **relative** | |
| Original value | final / (1 + x/100) | If it is 150 after +25 %, it was 120 before |

### Ratios, averages and work

- **Rule of three:** if 3 analysts process 12 reports, 5 analysts process 12 × 5/3 = 20 (in the same time).
- **Weighted average:** 2 classes with 30 students (average 4.0) and 10 students (average 3.0) → (30·4 + 10·3) / 40 = **3.75**. It is not 3.5.
- **Working together:** A takes 6 h and B takes 3 h → together: 1/(1/6 + 1/3) = **2 h**.
- **Average speed for a round trip** at 60 and 40 km/h → 2·60·40 / (60 + 40) = **48 km/h** (harmonic mean, not 50).

### Counting and probability

| Concept | Formula | Example |
|---|---|---|
| Multiplication principle | a × b × … | 3 shirts × 4 pants = 12 combinations |
| Permutations (order matters) | n! / (n−k)! | Podium of 3 among 8 runners: 8·7·6 = 336 |
| Combinations (order does not matter) | n! / (k!(n−k)!) | A team of 2 out of 5: 10 |
| Probability | favorable cases / possible cases | Rolling an even number with a die: 3/6 = 1/2 |
| "And" (independent) | P(A) × P(B) | Two heads with 2 coins: 1/4 |
| "Or" (mutually exclusive) | P(A) + P(B) | Rolling a 1 or a 2 with a die: 2/6 |
| "At least one" | 1 − P(none) | At least one head with 3 coins: 1 − 1/8 = 7/8 |
| Conditional | P(A\|B) = P(A and B) / P(B) | The basis of Bayes' theorem |

### Classic logic problems

- **Truth-tellers/liars:** assume one tells the truth and look for a contradiction.
- **Orderings:** "Ana is taller than Beto; Carlos is shorter than Beto…" → draw a line and place each one.
- **Syllogisms:** "All A are B; some B are C" → are some A C? **Not necessarily**. Draw Venn diagrams.
- **Conditionals:** "If it rains, the street gets wet". What you **can** conclude: if the street is **not** wet → it did not rain (contrapositive). What you **cannot**: if the street is wet → it rained (fallacy of affirming the consequent).

## 4. Basic statistics for data analysis

| Measure | What it is | Watch out |
|---|---|---|
| **Mean** | Sum / n | Sensitive to **outliers** |
| **Median** | The middle value when sorted | **Robust** to outliers: use it for income or prices |
| **Mode** | The most frequent value | Works for categorical data |
| **Range** | max − min | |
| **Variance / standard deviation** | Spread around the mean | The standard deviation is in the same units as the data |
| **Percentiles / quartiles** | Q1 = p25, Q2 = median, Q3 = p75; **IQR** = Q3 − Q1 | Outlier if < Q1 − 1.5·IQR or > Q3 + 1.5·IQR |
| **Correlation** (−1 to 1) | Linear relationship between two variables | **Correlation ≠ causation** |

- **Right-skewed distribution** (like income): mean > median.
- **Normal distribution:** ~68 % of the data within ±1σ, ~95 % within ±2σ and ~99.7 % within ±3σ.
- **A/B test:** you compare version A (control) with version B (variant), assigning users **at random**. The **p-value** is the probability of seeing a difference this large if there really were no difference. If p < 0.05, it is considered *statistically significant*.
- **Sample vs. population**, **selection bias** and **Simpson's paradox** (a trend that reverses when the data is grouped).

## 5. Business cases (open analytics questions)

A structure to answer (you can say it in English in the interview, see [phrases](../english/entrevista-y-frases.en.md)):

1. **Clarify:** clarify the metric, the period and the definition. *"How do we define 'sales'? Compared to which period?"*
2. **Check the data:** is it a data error? (broken pipeline, tracking change, holiday).
3. **Segment:** split by region, channel, product, new vs. returning customer, device…
4. **Hypothesize:** internal factors (price, campaign, stock, website change) vs. external ones (competition, seasonality, economy).
5. **Validate** each hypothesis with data and **recommend** a measurable action.

> **Example:** *"Weekly sales dropped 20%. How would you investigate?"*
> → I confirm that the number is real (did the pipeline fail?) → I compare with the same week last year (seasonality) → I segment by channel, region and product to locate the drop → I check the funnel (visits → cart → purchase) to see at which step it drops → I check recent changes (prices, campaigns, website deployments) → I recommend an action and define a KPI to monitor it.

## 6. Exercises

**Logic and math:**

1. A product costs 250. It goes up 20 % and then down 20 %. Final price?
2. In a company, 60 % are engineers and 25 % of the engineers work in data. What % of the total are data engineers?
3. Sales went from 1,200 to 1,500. Growth %?
4. How many different 3-digit codes (0–9, no repetition) are there?
5. Two dice are rolled. What is the probability that they add up to 7?
6. Data: 2, 3, 3, 5, 100. Mean, median and mode. Which one best represents the center?
7. "All analysts know SQL. Pedro knows SQL." Is Pedro an analyst?
8. If 5 machines make 5 parts in 5 minutes, how long do 100 machines take to make 100 parts?
9. A conversion rate went from 4 % to 5 %. Express it in percentage points and in relative %.
10. A team of 4 people is chosen from 6. How many possible teams are there?

**Programming (solve them in Python and in SQL when it applies):**

1. Given a list of a user's login dates (`"YYYY-MM-DD"`), return the longest streak of consecutive days.
2. Given a text, return the 3 most frequent words (case-insensitive).
3. Given a list of daily prices, return for each day how many days you must wait for a higher price (0 if never).

<details>
<summary>Solutions (logic and math)</summary>

1. 250 × 1.2 × 0.8 = **240**.
2. 0.60 × 0.25 = **15 %**.
3. (1500 − 1200) / 1200 = **25 %**.
4. 10 × 9 × 8 = **720**.
5. There are 6 favorable pairs, (1,6), (2,5), (3,4), (4,3), (5,2) and (6,1), out of 36 possible → **1/6**.
6. Mean = 113/5 = **22.6**; median = **3**; mode = **3**. The **median** represents the center best because 100 is an outlier.
7. **Not necessarily** (fallacy of affirming the consequent): other people also know SQL.
8. **5 minutes**: each machine makes 1 part in 5 minutes.
9. **+1 percentage point** = **+25 %** relative.
10. C(6,4) = 6!/(4!·2!) = **15**.

</details>

<details>
<summary>Solutions (programming)</summary>

```python
from collections import Counter
from datetime import date, timedelta

# 1. Streak of consecutive days (gaps and islands)
def longest_streak(dates):
    days = sorted({date.fromisoformat(d) for d in dates})   # set: removes duplicates
    best = current = 1 if days else 0
    for prev, cur in zip(days, days[1:]):
        current = current + 1 if cur - prev == timedelta(days=1) else 1
        best = max(best, current)
    return best

# 2. Top 3 words
def top_words(text, k=3):
    return [w for w, _ in Counter(text.lower().split()).most_common(k)]

# 3. Days until a higher price (monotonic stack, O(n))
def days_until_higher(prices):
    result = [0] * len(prices)
    stack = []                      # indexes of prices not "beaten" yet
    for i, p in enumerate(prices):
        while stack and prices[stack[-1]] < p:
            j = stack.pop()
            result[j] = i - j
        stack.append(i)
    return result

assert longest_streak(["2024-01-01", "2024-01-02", "2024-01-04", "2024-01-05", "2024-01-06"]) == 3
assert top_words("a b a c b a") == ["a", "b", "c"]
assert days_until_higher([73, 74, 75, 71, 69, 72, 76, 73]) == [1, 1, 4, 2, 1, 1, 0, 0]
```

SQL for problem 1 (*gaps and islands*): subtracting each date's row number produces the same value for every day of the same streak.

```sql
WITH d AS (
    SELECT DISTINCT login_date FROM logins WHERE user_id = 1
), g AS (
    SELECT login_date,
           julianday(login_date) - ROW_NUMBER() OVER (ORDER BY login_date) AS grp
    FROM d
)
SELECT MAX(streak) AS longest_streak
FROM (SELECT grp, COUNT(*) AS streak FROM g GROUP BY grp);
```

</details>

---

**Next:** [01 · Abstract reasoning](../01-razonamiento-abstracto/README.en.md)
