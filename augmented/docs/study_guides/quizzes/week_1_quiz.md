# Week 1 Quiz: Foundations & Core Methods

**Instructions**: Answer each question without looking at notes. Check answers afterward.

---

## Section A: Conceptual (2 points each)

### Q1: Potential Outcomes
Why can't we observe the individual treatment effect $\tau_i = Y_i(1) - Y_i(0)$?

<details>
<summary>Answer</summary>

**The Fundamental Problem of Causal Inference**: We can only observe one potential outcome per unit. If unit $i$ is treated, we observe $Y_i(1)$ but not $Y_i(0)$. If untreated, we observe $Y_i(0)$ but not $Y_i(1)$. The counterfactual is fundamentally unobservable.

This is why we estimate *average* effects across units, using various identification strategies.
</details>

---

### Q2: RCT Identification
In an RCT, why does the simple difference in means identify the ATE?

<details>
<summary>Answer</summary>

Randomization ensures $(Y_0, Y_1) \perp T$.

Therefore:
$$E[Y|T=1] - E[Y|T=0] = E[Y_1|T=1] - E[Y_0|T=0]$$
$$= E[Y_1] - E[Y_0] \text{ (by independence)}$$
$$= E[Y_1 - Y_0] = ATE$$

The selection bias term $E[Y_0|T=1] - E[Y_0|T=0] = 0$ because treatment is independent of potential outcomes.
</details>

---

### Q3: Conditional Ignorability
What does $(Y_0, Y_1) \perp T | X$ mean in words?

<details>
<summary>Answer</summary>

**Conditional ignorability** (also called "selection on observables" or "unconfoundedness") means:

*Given the covariates X, treatment assignment is independent of potential outcomes.*

In other words: within groups defined by X, treatment is "as good as random." All confounders are observed and controlled for.

This is **untestable** because it's a statement about potential outcomes, which we don't fully observe.
</details>

---

### Q4: FWL Theorem
Explain what the Frisch-Waugh-Lovell theorem says in one sentence.

<details>
<summary>Answer</summary>

The coefficient on treatment from a multivariate regression equals the coefficient from regressing the *residualized* outcome on the *residualized* treatment, where both are residualized against the other covariates.

Formally: $\hat{\beta}_T$ from $Y = \beta_T T + \beta_X X + \varepsilon$ equals $\hat{\beta}$ from $\tilde{Y} = \beta \tilde{T} + \nu$, where $\tilde{Y} = Y - \hat{Y}_{on X}$ and $\tilde{T} = T - \hat{T}_{on X}$.
</details>

---

### Q5: Bad Controls
Give an example of when adding a control variable INCREASES bias.

<details>
<summary>Answer</summary>

**Collider bias**: If you control for a variable that is *caused by* both treatment and outcome (or their causes), you induce bias.

Example: Education → Job Type ← Ability; Job Type → Salary. If we control for Job Type when estimating education → salary, we open a backdoor path through Ability.

**Mediator**: If you control for a variable on the causal path (T → M → Y), you remove the indirect effect, changing interpretation.

**Post-treatment variables**: Any variable affected by treatment can introduce bias.
</details>

---

## Section B: Formulas (3 points each)

### Q6: Omitted Variable Bias
Write the OVB formula for omitting variable $A$ when estimating $Y = \kappa T + \gamma A + \varepsilon$.

<details>
<summary>Answer</summary>

$$\hat{\kappa}_{short} = \kappa + \gamma \cdot \delta$$

where:
- $\gamma$ = effect of omitted variable $A$ on outcome $Y$
- $\delta = \frac{Cov(A, T)}{Var(T)}$ = coefficient from regressing $A$ on $T$

Bias is zero when either:
- $\gamma = 0$: A doesn't affect Y (not a confounder)
- $\delta = 0$: A is uncorrelated with T (randomization!)
</details>

---

### Q7: IPTW Estimator
Write the Horvitz-Thompson IPW estimator for ATE.

<details>
<summary>Answer</summary>

$$\hat{\tau}_{IPW} = \frac{1}{n}\sum_{i=1}^n \left[ \frac{T_i Y_i}{e(X_i)} - \frac{(1-T_i) Y_i}{1-e(X_i)} \right]$$

where $e(X_i) = P(T_i = 1 | X_i)$ is the propensity score.

The Hajek (normalized) version is more stable:
$$\hat{\mu}_1 = \frac{\sum_i T_i Y_i / e(X_i)}{\sum_i T_i / e(X_i)}, \quad \hat{\mu}_0 = \frac{\sum_i (1-T_i) Y_i / (1-e(X_i))}{\sum_i (1-T_i) / (1-e(X_i))}$$
</details>

---

### Q8: IV Estimator
Derive $\kappa_{IV} = \frac{Cov(Y, Z)}{Cov(T, Z)}$ from the structural equation.

<details>
<summary>Answer</summary>

Starting from: $Y = \beta_0 + \kappa T + v$ where $Cov(T, v) \neq 0$.

Take covariance with instrument $Z$:
$$Cov(Z, Y) = Cov(Z, \beta_0 + \kappa T + v) = \kappa \cdot Cov(Z, T) + Cov(Z, v)$$

By exclusion restriction, $Cov(Z, v) = 0$:
$$Cov(Z, Y) = \kappa \cdot Cov(Z, T)$$

Solve for $\kappa$:
$$\kappa_{IV} = \frac{Cov(Z, Y)}{Cov(Z, T)}$$
</details>

---

## Section C: Application (5 points each)

### Q9: Method Selection
You have observational data on a marketing campaign's effect on purchases. No instrument available. What method would you use and what assumptions do you need?

<details>
<summary>Answer</summary>

**Methods** (in order of preference):
1. **Doubly Robust / DML**: Most robust if you have good covariates
2. **Propensity Score Methods**: IPW, matching, stratification
3. **Regression with controls**: Simplest, but assumes linearity

**Required assumptions**:
1. **Conditional ignorability**: All confounders observed (big assumption!)
2. **Overlap**: Both treated and control exist for all covariate values
3. **SUTVA**: No spillovers (users don't influence each other)
4. **Correct model specification**: For regression-based methods

**What I would do**:
1. Check overlap (PS distribution)
2. Run DR/DML with flexible ML
3. Check balance after weighting/matching
4. Sensitivity analysis for unobserved confounders
</details>

---

### Q10: Critique
A colleague estimates the effect of a training program using OLS regression with "number of hours worked after training" as a control. What's wrong?

<details>
<summary>Answer</summary>

**Problem**: "Hours worked after training" is a **post-treatment variable** (potentially a mediator).

Training → Hours Worked → Wages

If training affects hours worked, and hours affect wages:
1. Controlling for hours removes part of the causal pathway
2. The coefficient on training becomes the "direct effect" only
3. This may not be what we want—we might want total effect

**Additionally**: Hours worked could be a collider if both training and unobserved factors (e.g., motivation) affect it.

**Solution**: Only control for pre-treatment confounders. Draw a DAG first!
</details>

---

## Scoring Guide

| Score | Interpretation |
|-------|----------------|
| 25-30 | Excellent! Ready for interviews |
| 20-24 | Good foundation, review weak areas |
| 15-19 | Need more practice, re-read chapters |
| < 15 | Start over with careful study |
