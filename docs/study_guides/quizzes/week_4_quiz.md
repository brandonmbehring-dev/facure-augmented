# Week 4 Quiz: HTE & Machine Learning Methods

**Instructions**: Answer each question without looking at notes. Check answers afterward.

---

## Section A: Heterogeneous Treatment Effects (10 points)

### Q1: CATE Definition (3 points)
Define CATE and explain how it differs from ATE. When would you estimate CATE?

<details>
<summary>Answer</summary>

**CATE (Conditional Average Treatment Effect)**:
$$\tau(x) = E[Y(1) - Y(0) | X = x]$$

The average treatment effect for units with covariates $X = x$.

**ATE (Average Treatment Effect)**:
$$\tau = E[Y(1) - Y(0)] = E[\tau(X)]$$

CATE is conditional on $X$; ATE averages over the distribution of $X$.

**When to estimate CATE**:
1. **Personalization**: Different treatments for different people
2. **Targeting**: Who benefits most?
3. **Policy optimization**: Maximize welfare given budget constraints
4. **Understanding mechanisms**: WHY does treatment work?

**Key distinction**: CATE is the effect FOR people with $X=x$, NOT the effect OF $X$.
</details>

---

### Q2: Meta-Learner Selection (4 points)
You have a dataset with 10,000 treated units and 1,000 control units. Which meta-learner would you use and why?

<details>
<summary>Answer</summary>

**Use X-learner**.

**Reasoning**:
- **Imbalanced groups**: 10:1 ratio of treated to control
- T-learner would train a weak model on 1,000 controls
- S-learner might wash out treatment effect
- X-learner excels with imbalanced data

**X-learner procedure**:
1. Train $\hat{\mu}_0$ on 1,000 controls, $\hat{\mu}_1$ on 10,000 treated
2. Impute counterfactuals:
   - For treated: $\tilde{\tau}_1 = Y_1 - \hat{\mu}_0(X_1)$ (use strong control model)
   - For control: $\tilde{\tau}_0 = \hat{\mu}_1(X_0) - Y_0$ (use strong treated model)
3. Model $\tilde{\tau}$ separately, then combine with propensity weights

**Why it works**: The imputation step leverages both models optimally. For treated units, we have actual $Y_1$ and impute $Y_0$ from the (admittedly smaller) control model. For controls, we have actual $Y_0$ and impute $Y_1$ from the large treated model. The propensity weighting then optimally combines these estimates.

**Alternatives if X-learner unavailable**: R-learner handles confounding well but doesn't directly address imbalance.
</details>

---

### Q3: HTE Interpretation (3 points)
A colleague finds that CATE is higher for older patients. They conclude "age causes larger treatment effects." What's wrong with this interpretation?

<details>
<summary>Answer</summary>

**The error**: Confusing effect HETEROGENEITY with effect OF age.

**CATE(age) tells us**: Treatment effect differs BY age group
**CATE(age) does NOT tell us**: Age CAUSES the heterogeneity

**Why the distinction matters**:
- Age correlates with many things (health, income, behavior)
- Higher CATE for elderly might be because they're sicker, not because of age itself
- Causal interpretation would require: "What happens if we make someone older?"

**Correct interpretation**: "Among older patients, the treatment effect is larger on average." This is descriptive heterogeneity, useful for targeting but not for understanding mechanisms.

**To understand mechanisms**: Need to either:
1. Identify mediators and do mediation analysis
2. Have exogenous variation in the moderator itself
3. Use domain knowledge about WHY age matters

**Interview tip**: This is a common gotcha. Always distinguish between "effect heterogeneity" and "causal effect of the moderator."
</details>

---

## Section B: Double Machine Learning (10 points)

### Q4: Why Not Naive ML? (3 points)
List and explain the three problems with using ML directly for causal inference.

<details>
<summary>Answer</summary>

**Three problems with naive ML**:

1. **Regularization bias**:
   - ML uses L1/L2 penalties, pruning, early stopping
   - These shrink coefficients toward zero
   - For prediction: Good (reduces variance)
   - For causal inference: Bad (biases treatment effect toward zero)

2. **Overfitting correlation**:
   - If we train $\hat{g}(X)$ on full data, then $\hat{g}(X_i)$ is correlated with $Y_i$
   - This correlation doesn't vanish as $n \to \infty$
   - Creates bias in treatment effect estimate
   - Sample splitting alone doesn't fix orthogonality

3. **Invalid inference**:
   - Standard ML doesn't provide valid confidence intervals for treatment effects
   - Need special structure (Neyman orthogonality) for $\sqrt{n}$-consistent inference
   - Bootstrap on ML predictions gives wrong coverage

**DML solution**:
- Neyman orthogonal moments: First-order insensitive to nuisance errors
- Cross-fitting: Breaks the correlation by never predicting on training data
- Result: $\sqrt{n}$-consistent, asymptotically normal treatment effect estimates
</details>

---

### Q5: Cross-Fitting (3 points)
Explain the cross-fitting procedure and why sample splitting alone isn't enough.

<details>
<summary>Answer</summary>

**Cross-fitting procedure** (K=5):
1. Split data into 5 folds
2. For each fold $k$:
   - Train nuisance models on folds $\{1,...,K\} \setminus k$
   - Predict on fold $k$
3. Combine all predictions
4. Estimate treatment effect using cross-fitted residuals

**Why sample splitting alone isn't enough**:

Simple 50/50 split:
- Use half for nuisance, half for treatment effect
- Wastes data: Only 50% for final estimation
- Still need orthogonal moments to handle regularization bias

Cross-fitting advantages:
- Uses ALL data for both nuisance and treatment estimation
- Each observation's nuisance prediction is out-of-sample
- More efficient (smaller variance) than simple splitting

**Key insight**: Cross-fitting addresses the overfitting problem (nuisance predicted out-of-sample), but you still need Neyman orthogonality to address regularization bias. DML uses BOTH.

**Analogy**: Cross-fitting is like cross-validation, but for causal inference instead of model selection.
</details>

---

### Q6: DML Formula (4 points)
Write the partially linear DML estimator and explain each component.

<details>
<summary>Answer</summary>

**Partially Linear Model**:
$$Y = \tau T + g(X) + \varepsilon$$
$$T = m(X) + \nu$$

where $E[\varepsilon|X,T] = 0$ and $E[\nu|X] = 0$.

**DML Estimator**:
$$\hat{\tau}_{DML} = \left(\sum_{i=1}^n \tilde{T}_i^2\right)^{-1} \sum_{i=1}^n \tilde{T}_i \tilde{Y}_i$$

where:
- $\tilde{T}_i = T_i - \hat{m}(X_i)$ — residualized treatment (treatment variation unexplained by $X$)
- $\tilde{Y}_i = Y_i - \hat{g}(X_i)$ — residualized outcome (outcome variation unexplained by $X$)
- $\hat{m}, \hat{g}$ are ML models trained via cross-fitting

**Component interpretation**:
1. $\hat{m}(X)$: Propensity model (predicts treatment from covariates)
2. $\hat{g}(X)$: Outcome model (predicts outcome from covariates)
3. $\tilde{T}$: "Pure" treatment variation, uncorrelated with $X$
4. $\tilde{Y}$: "Pure" outcome variation, uncorrelated with $X$
5. Final step: OLS of residualized outcome on residualized treatment

**Why this works**: By FWL theorem, this is equivalent to regressing $Y$ on $T$ controlling for $X$, but now $X$'s effect is flexibly modeled by ML.
</details>

---

## Section C: Causal Forests (10 points)

### Q7: Honest Trees (3 points)
What is "honest" splitting in causal forests and why is it important?

<details>
<summary>Answer</summary>

**Honest splitting**:
- Split the sample: one half for determining tree structure, one half for estimating leaf effects
- Structure sample: Used to decide where to split
- Estimation sample: Used to compute treatment effects in each leaf

**Why it matters**:
1. **Prevents overfitting to treatment**: Regular trees might create splits that happen to separate high/low outcomes by chance
2. **Valid inference**: Honesty is required for asymptotic normality of CATE estimates
3. **Confidence intervals**: Without honesty, CIs have wrong coverage

**Contrast with prediction forests**:
- Prediction: Overfitting to $Y$ is the concern, cross-validation helps
- Causal: Overfitting to treatment EFFECT is the concern, need honesty

**Implementation**: In `grf` package, `honest = TRUE` by default. Each tree uses different subsamples for splitting and estimation.

**Key insight**: Even with infinite data, dishonest trees can have biased CATE estimates because the splits were chosen to maximize apparent heterogeneity.
</details>

---

### Q8: Causal Forest Assumptions (4 points)
What assumptions does Causal Forest require? How do they compare to meta-learners?

<details>
<summary>Answer</summary>

**Causal Forest Assumptions**:

1. **Unconfoundedness**: $(Y(0), Y(1)) \perp T | X$
   - Same as all selection-on-observables methods
   - No unobserved confounders

2. **Overlap**: $\eta < e(X) < 1-\eta$ for some $\eta > 0$
   - Propensity bounded away from 0 and 1
   - Needed for all CATE methods

3. **Regularity conditions**:
   - Smoothness of $\tau(x)$
   - Sufficient variation in treatment
   - For valid asymptotic inference

**Comparison with Meta-Learners**:

| Aspect | Causal Forest | Meta-Learners |
|--------|---------------|---------------|
| Core assumptions | Same (CIA + overlap) | Same |
| Functional form | Nonparametric (trees) | Depends on base learner |
| Inference | Built-in CIs via honesty | Need bootstrap (often wrong) |
| Interpretability | Variable importance | Model-dependent |
| Propensity | Uses local centering | T-learner doesn't use PS |

**Unique CF features**:
- Automatic adaptation to local signal-to-noise
- Built-in inference without bootstrap
- Local linear corrections for smoothness
- Propensity weighting handles confounding

**When CF excels**: Moderate-dimensional $X$, sufficient sample size, want valid CIs
</details>

---

### Q9: CATE Validation (3 points)
How do you validate CATE estimates when you can't observe individual treatment effects?

<details>
<summary>Answer</summary>

**The fundamental problem**: We never observe $\tau_i = Y_i(1) - Y_i(0)$ for any individual.

**Validation strategies**:

1. **Calibration by subgroup**:
   - Group units by predicted CATE quantiles
   - Estimate ATE within each group
   - Plot: Predicted CATE vs. observed group ATE
   - Good model: Points on 45° line

2. **RATE (Rank-Average Treatment Effect)**:
   - Rank units by predicted CATE
   - Estimate ATE for top K%, top 2K%, etc.
   - Good model: RATE decreases as we include lower-ranked units

3. **AUTOC (Area Under TOC Curve)**:
   - TOC: Treatment Operating Characteristic
   - Cumulative gain from treating top-ranked units
   - Compare to random ordering baseline

4. **Cross-validation on transformed outcomes**:
   - R-learner loss: $(Y - \hat{m})^2 / (T - \hat{e})^2$ weighted
   - Compare different CATE models

5. **Simulation/semi-synthetic**:
   - Use real $X$ data
   - Simulate $Y(0), Y(1)$ with known $\tau(X)$
   - Evaluate on known truth

**Key insight**: All validation is indirect. We can check if CATE ordering is correct (targeting) but not if magnitudes are correct without assumptions.
</details>

---

## Section D: Integration (10 points)

### Q10: Method Selection
A company wants to personalize discounts. They have observational data with 100K customers, 20K received a discount, and they track purchases. How would you approach CATE estimation?

<details>
<summary>Answer</summary>

**Approach in 5 steps**:

**1. Assess the data situation**:
- Imbalanced: 20K treated vs 80K control (20% treatment rate)
- Observational: Selection bias likely (why did some get discounts?)
- Sample size: Large enough for ML methods

**2. Identify confounders**:
- Prior purchase history
- Customer demographics
- Engagement metrics
- How discounts were assigned (targeting rule)

**3. Choose CATE method**:
Given imbalance and observational data, consider:
- **X-learner**: Handles imbalance well
- **Causal Forest**: Built-in inference, handles confounding
- **DR-learner**: Doubly robust, good with strong confounding

**4. Implementation plan**:
```python
# Step 1: Check overlap
# Plot propensity scores, trim extremes if needed

# Step 2: Estimate CATE
from econml.dml import CausalForestDML
cf = CausalForestDML(
    model_y=LGBMRegressor(),
    model_t=LGBMClassifier(),
    n_estimators=500
)
cf.fit(Y, T, X=X, W=confounders)
cate = cf.effect(X_new)

# Step 3: Validate
# - Calibration plot
# - RATE curve
# - Placebo test on pre-treatment outcomes
```

**5. Business application**:
- Rank customers by predicted CATE
- Calculate ROI: incremental revenue - discount cost
- Set targeting threshold: Discount only if CATE > cost
- A/B test the policy before full rollout

**Key considerations**:
- Don't target based on price sensitivity → race to bottom
- Consider long-term effects (future purchases)
- Watch for manipulation (customers gaming targeting)
- Ethical review: Is this fair differential pricing?

**Validation is critical**: Before deployment, run an A/B test where treatment assignment follows your model vs. random. If model-based targeting doesn't beat random, something is wrong.
</details>

---

## Scoring Guide

| Score | Interpretation |
|-------|----------------|
| 35-40 | Excellent! Ready for ML causal inference roles |
| 28-34 | Solid understanding, review DML details |
| 20-27 | Need more practice on specific methods |
| < 20 | Review Week 4 material carefully |

---

## Key Formulas Reference

### CATE
$$\tau(x) = E[Y(1) - Y(0) | X = x]$$

### Meta-Learners
- S: $\hat{\tau}(x) = \hat{\mu}(x,1) - \hat{\mu}(x,0)$
- T: $\hat{\tau}(x) = \hat{\mu}_1(x) - \hat{\mu}_0(x)$
- X: Cross-impute, weight by propensity
- R: $(Y-\hat{m}) = (T-\hat{e})\tau(X) + \varepsilon$

### DML
$$\hat{\tau} = \frac{\sum_i (T_i - \hat{e}(X_i))(Y_i - \hat{m}(X_i))}{\sum_i (T_i - \hat{e}(X_i))^2}$$
