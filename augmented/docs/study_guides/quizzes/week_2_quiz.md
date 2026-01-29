# Week 2 Quiz: Advanced Methods

**Instructions**: Answer each question without looking at notes. Check answers afterward.

---

## Section A: Difference-in-Differences (10 points)

### Q1: Parallel Trends (3 points)
Write the parallel trends assumption mathematically and explain why it's untestable.

<details>
<summary>Answer</summary>

**Parallel Trends**:
$$E[Y_0(post) - Y_0(pre) | D=1] = E[Y_0(post) - Y_0(pre) | D=0]$$

In words: Absent treatment, treated and control groups would have experienced the same change in outcomes.

**Why untestable**: The left side involves $Y_0(post)|D=1$—the counterfactual outcome for treated units without treatment. This is fundamentally unobservable because the treatment happened.

Pre-trend tests check $E[Y(t_2) - Y(t_1) | D=1] = E[Y(t_2) - Y(t_1) | D=0]$ for $t_1, t_2 < t_{treatment}$. This is necessary but not sufficient—trends could diverge exactly at treatment time.
</details>

---

### Q2: TWFE Bias (3 points)
Why is two-way fixed effects (TWFE) biased with staggered adoption?

<details>
<summary>Answer</summary>

**The problem**: With staggered treatment timing and heterogeneous effects, TWFE uses already-treated units as "controls" for later-treated units.

**Decomposition**: TWFE estimates a weighted average of:
1. Comparisons of treated vs. never-treated ✓
2. Comparisons of treated vs. not-yet-treated ✓
3. Comparisons of later-treated vs. already-treated **with negative weights!** ✗

**Result**: If treatment effects evolve over time (dynamic effects), TWFE can give wrong sign or magnitude.

**Solution**: Use Callaway-Sant'Anna, Sun-Abraham, or similar modern DiD estimators that properly handle staggered adoption.
</details>

---

### Q3: DiD Formula (4 points)
Write the DiD estimator as a "difference of differences" and as a regression.

<details>
<summary>Answer</summary>

**As difference of differences**:
$$\hat{\tau}_{DiD} = (\bar{Y}_{T,post} - \bar{Y}_{T,pre}) - (\bar{Y}_{C,post} - \bar{Y}_{C,pre})$$

**As regression**:
$$Y_{it} = \alpha + \gamma D_i + \lambda Post_t + \tau (D_i \times Post_t) + \varepsilon_{it}$$

where:
- $D_i$ = treatment group indicator
- $Post_t$ = post-treatment period indicator
- $\tau$ = DiD estimate (coefficient on interaction)

The four cell means are:
- $\alpha$ = Control, Pre
- $\alpha + \gamma$ = Treated, Pre
- $\alpha + \lambda$ = Control, Post
- $\alpha + \gamma + \lambda + \tau$ = Treated, Post
</details>

---

## Section B: RDD (10 points)

### Q4: Continuity (3 points)
What is the continuity assumption and what could violate it?

<details>
<summary>Answer</summary>

**Continuity assumption**:
$$\lim_{r \to c^-} E[Y_0|R=r] = \lim_{r \to c^+} E[Y_0|R=r]$$

Potential outcomes are smooth through the cutoff.

**Violations**:
1. **Manipulation**: Units sort around cutoff (test retaking, income manipulation)
2. **Compound treatments**: Multiple things change at cutoff (age 21: drinking AND other rights)
3. **Covariate discontinuities**: Other characteristics jump at cutoff
4. **Anticipation**: Behavior changes in anticipation of crossing cutoff

**Diagnostics**:
- McCrary density test (bunching)
- Covariate balance at cutoff
- Placebo cutoffs
</details>

---

### Q5: Local Effect (3 points)
Why is the RDD estimate "local" and what are the implications?

<details>
<summary>Answer</summary>

**RDD is local in two senses**:

1. **Local in running variable**: Effect identified only at $R = c$. Cannot extrapolate to other values.

2. **Local in population** (Fuzzy RDD): Effect only for compliers who change treatment at cutoff.

**Implications**:
- Effect at age 21 may differ from effect at age 18 or 25
- Cannot aggregate to population ATE without additional assumptions
- If treatment effects are heterogeneous, cutoff effect may not generalize

**When local = good enough**: If the policy question IS about the cutoff (e.g., "should we change the drinking age from 21?"), the local effect is exactly what we need.
</details>

---

### Q6: Sharp vs. Fuzzy (4 points)
Explain the difference between sharp and fuzzy RDD.

<details>
<summary>Answer</summary>

**Sharp RDD**:
- Treatment is deterministic: $D_i = \mathbf{1}\{R_i \geq c\}$
- Treatment probability jumps from 0 to 1
- Estimate: OLS at cutoff

**Fuzzy RDD**:
- Treatment probability jumps but not 0→1
- Example: 30% compliance below, 80% above
- The threshold is an **instrument** for treatment
- Estimate: IV using threshold as instrument

**Fuzzy RDD formula**:
$$\tau_{Fuzzy} = \frac{\lim_{r \to c^+} E[Y|R] - \lim_{r \to c^-} E[Y|R]}{\lim_{r \to c^+} E[D|R] - \lim_{r \to c^-} E[D|R]} = \frac{\text{ITT}}{\text{First Stage}}$$

This is LATE for compliers at the cutoff.
</details>

---

## Section C: DML & HTE (10 points)

### Q7: Why DML? (3 points)
Why can't you just plug ML into regression for causal inference?

<details>
<summary>Answer</summary>

**Three problems with naive ML**:

1. **Regularization bias**: ML uses regularization (L1, L2, pruning) which shrinks coefficients. For prediction this is good; for causal inference it biases the treatment effect toward zero.

2. **Overfitting creates correlation**: If you train $\hat{g}(X)$ on the same data used for treatment effect estimation, the predictions are correlated with the error term. This bias doesn't vanish with more data.

3. **Invalid inference**: Standard ML doesn't provide valid CIs for treatment effects. Need special structure (Neyman orthogonality) for valid inference.

**DML fixes these via**:
- Neyman orthogonal moments (insensitive to nuisance errors)
- Cross-fitting (breaks correlation)
- Result: $\sqrt{n}$-consistent with valid CIs
</details>

---

### Q8: Cross-Fitting (3 points)
Explain the cross-fitting procedure and why it's necessary.

<details>
<summary>Answer</summary>

**Cross-fitting procedure**:
1. Split data into K folds (typically K=5)
2. For each fold k:
   - Train ML models on all OTHER folds
   - Predict on fold k
3. Combine all cross-fitted predictions
4. Estimate treatment effect using these predictions

**Why necessary**: Without cross-fitting, $\hat{g}(X_i)$ is trained on data including $(X_i, Y_i)$. This creates correlation between $\hat{g}(X_i)$ and $\varepsilon_i$ that doesn't vanish as $n \to \infty$.

With cross-fitting, $\hat{g}_{-k}(X_i)$ is trained WITHOUT observation $i$. No correlation, no overfitting bias.

**Sample splitting alternative**: Could use half for nuisance, half for estimation. But cross-fitting uses all data efficiently.
</details>

---

### Q9: Meta-Learners (4 points)
Describe the S-learner, T-learner, and X-learner. When would you use each?

<details>
<summary>Answer</summary>

**S-learner** (Single model):
- Fit one model: $\hat{\mu}(X, T)$
- CATE: $\hat{\tau}(x) = \hat{\mu}(x, 1) - \hat{\mu}(x, 0)$
- Use when: Treatment effect is small relative to outcome variation
- Problem: Treatment can be "washed out" by regularization

**T-learner** (Two models):
- Fit separately: $\hat{\mu}_1(X)$ on treated, $\hat{\mu}_0(X)$ on control
- CATE: $\hat{\tau}(x) = \hat{\mu}_1(x) - \hat{\mu}_0(x)$
- Use when: Groups are large enough, different relationships
- Problem: Separate models = less data per model

**X-learner** (Cross-imputation):
- Step 1: Fit $\hat{\mu}_0, \hat{\mu}_1$ like T-learner
- Step 2: Impute ITEs: $\tilde{\tau}_1 = Y_1 - \hat{\mu}_0(X_1)$, $\tilde{\tau}_0 = \hat{\mu}_1(X_0) - Y_0$
- Step 3: Model $\tilde{\tau}$ separately, combine with propensity weights
- Use when: Imbalanced groups (e.g., few treated units)
- Advantage: Leverages structure from both groups
</details>

---

## Section D: Integration (10 points)

### Q10: Method Selection
A company wants to know if their new checkout flow increases purchases. They have observational data (users self-selected into old vs. new flow), panel data (user-level over time), and the new flow was rolled out to users above a certain engagement score. What method(s) would you recommend and why?

<details>
<summary>Answer</summary>

**Three possible approaches**:

1. **RDD** (if engagement score cutoff is sharp):
   - Running variable: engagement score
   - Cutoff: threshold for new flow rollout
   - Strength: Strong identification near cutoff
   - Limitation: Local effect only

2. **DiD** (using panel structure):
   - Treated: users who got new flow
   - Control: users who kept old flow
   - Time: before vs. after rollout
   - Requires: Parallel trends assumption
   - Advantage: Broader effect, uses time variation

3. **DML/DR** (if selection on observables):
   - Control for engagement, past behavior, demographics
   - Requires: All confounders observed
   - Advantage: Uses all data, flexible

**My recommendation**:
1. **Primary**: RDD if cutoff is enforced strictly—strongest identification
2. **Robustness**: DiD using panel structure—different identifying assumption
3. **If they agree**: Strong evidence
4. **If they disagree**: Investigate why (different populations? Assumption violation?)

**Red flags to check**:
- Manipulation around cutoff (users gaming engagement)
- Pre-trends in DiD
- Overlap for DML
</details>

---

## Scoring Guide

| Score | Interpretation |
|-------|----------------|
| 35-40 | Excellent! Ready for L6+ interviews |
| 28-34 | Solid understanding, polish weak areas |
| 20-27 | Need more practice on specific methods |
| < 20 | Review Week 2 material carefully |
