# Week 3 Quiz: Panel Methods & Synthetic Control

**Instructions**: Answer each question without looking at notes. Check answers afterward.

---

## Section A: Fixed Effects (10 points)

### Q1: Within Transformation (3 points)
Write the within transformation and explain what it removes.

<details>
<summary>Answer</summary>

**Within transformation**:
$$Y_{it} - \bar{Y}_i = \beta(X_{it} - \bar{X}_i) + (\varepsilon_{it} - \bar{\varepsilon}_i)$$

where $\bar{Y}_i = \frac{1}{T}\sum_t Y_{it}$ is the unit-specific mean.

**What it removes**: All time-invariant characteristics—both observed and unobserved. The unit fixed effect $\alpha_i$ is completely differenced out.

**Intuition**: We're comparing each observation to its own unit's average. This exploits within-unit variation over time, removing any constant differences between units.
</details>

---

### Q2: Strict Exogeneity (3 points)
What does strict exogeneity mean and when might it fail?

<details>
<summary>Answer</summary>

**Strict exogeneity**:
$$E[\varepsilon_{it} | X_{i1}, X_{i2}, ..., X_{iT}, \alpha_i] = 0$$

The error at time $t$ is uncorrelated with covariates at ALL time periods (past, present, and future).

**Failures**:
1. **Feedback effects**: Current outcomes affect future treatment (e.g., poor performance → training)
2. **Anticipation**: Future treatment affects current behavior
3. **Lagged dependent variable**: If $Y_{t-1}$ is a regressor, FE is biased (Nickell bias)
4. **Time-varying confounders**: Unobservables that change over time and affect both X and Y

**Why it matters**: FE removes fixed confounders, but if confounding varies over time, FE won't help.
</details>

---

### Q3: Unit vs. Time FE (4 points)
Explain when you would use unit FE, time FE, or both (TWFE).

<details>
<summary>Answer</summary>

**Unit Fixed Effects ($\alpha_i$)**:
- Controls for time-invariant unit characteristics
- Use when: Units differ systematically (e.g., firm culture, individual ability)
- Example: Comparing wages across workers, controlling for unobserved ability

**Time Fixed Effects ($\gamma_t$)**:
- Controls for common shocks affecting all units
- Use when: Macro trends affect everyone (e.g., recession, policy change)
- Example: Year dummies to control for inflation, economic cycles

**Two-Way FE (TWFE)**:
- Both unit AND time effects
- Use when: Both unit heterogeneity and common shocks matter
- Standard in panel data analysis

**⚠️ TWFE Danger**: With staggered treatment adoption, TWFE is BIASED. Already-treated units become "controls" for later-treated with potentially negative weights. Use Callaway-Sant'Anna or Sun-Abraham instead.
</details>

---

## Section B: Synthetic Control (10 points)

### Q4: Synthetic Control Intuition (3 points)
Explain the synthetic control method in one paragraph.

<details>
<summary>Answer</summary>

Synthetic control creates a counterfactual for a treated unit by finding optimal weights on control units such that the weighted average matches the treated unit's pre-treatment outcomes. The key insight is that if we can match the pre-treatment trajectory, we've implicitly matched the unobserved factors driving that trajectory. Post-treatment, the gap between the treated unit and its synthetic counterpart is the treatment effect. Unlike DiD, SC doesn't require parallel trends—it only requires that the convex hull of controls contains the treated unit's pre-treatment values.

**Formula**: $\hat{Y}_{1t}^{SC} = \sum_{j=2}^{J+1} w_j^* Y_{jt}$ where weights minimize pre-treatment MSPE.
</details>

---

### Q5: Placebo Tests (3 points)
How do you conduct inference with synthetic control?

<details>
<summary>Answer</summary>

**Placebo tests (Fisher permutation)**:

1. **In-space placebos**: Apply SC to each control unit as if it were treated
   - Calculate gap for each placebo
   - Compare treated unit's gap to distribution of placebo gaps
   - P-value = fraction of placebos with gaps as large as treated

2. **In-time placebos**: Apply SC at a fake pre-treatment date
   - If method works, should find no effect before actual treatment
   - Validates that pre-treatment fit isn't spurious

3. **MSPE ratio**:
   $$\text{ratio}_j = \frac{\text{Post-MSPE}_j}{\text{Pre-MSPE}_j}$$
   - Units with poor pre-fit have unreliable post-gaps
   - Compare treated unit's ratio to distribution

**Key insight**: This is exact inference—no asymptotic assumptions needed. But power is limited by number of control units.
</details>

---

### Q6: SC Assumptions (4 points)
What are the key assumptions for synthetic control and what violates them?

<details>
<summary>Answer</summary>

**Key Assumptions**:

1. **No anticipation**: Units don't change behavior before treatment
   - Violation: Policy announced early, behavior changes
   - Check: Pre-treatment fit should remain good up to treatment

2. **Convex hull**: Treated unit's pre-treatment values can be matched by weighted controls
   - Violation: Treated unit is an "outlier" (e.g., California vs. small states)
   - Check: Pre-treatment MSPE; if poor, method may fail

3. **No spillovers**: Treatment doesn't affect control units
   - Violation: Controls trade with treated unit, affected by policy
   - Check: Look for changes in controls post-treatment

4. **Stable weights assumption**: Pre-treatment match implies post-treatment counterfactual
   - Violation: Structural break at treatment time
   - Check: Pre-treatment fit should be driven by fundamentals, not coincidence

**Diagnostics**:
- Pre-treatment MSPE (fit quality)
- Weight distribution (sparse vs. diffuse)
- Placebo tests (gap distribution)
</details>

---

## Section C: Method Comparison (10 points)

### Q7: DiD vs. Synthetic Control (4 points)
Compare DiD and Synthetic Control. When would you prefer each?

<details>
<summary>Answer</summary>

| Aspect | DiD | Synthetic Control |
|--------|-----|-------------------|
| **Parallel trends** | Required | Not required (matches levels) |
| **Sample size** | Many treated units OK | Typically single treated unit |
| **Control selection** | All controls weighted equally | Optimal weights on controls |
| **Inference** | Standard errors | Placebo tests |
| **Pre-treatment fit** | Doesn't matter | Must match well |

**Prefer DiD when**:
- Many treated units available
- Parallel trends plausible
- Standard inference needed
- Treatment is staggered (use modern DiD)

**Prefer SC when**:
- Single treated unit (e.g., one state, one country)
- Parallel trends implausible
- Rich pre-treatment data available
- Want explicit counterfactual construction

**Key insight**: DiD requires parallel TRENDS; SC requires matching LEVELS. SC is more data-hungry in time dimension but more flexible in assumption.
</details>

---

### Q8: Panel Methods Selection (3 points)
You have panel data and want to estimate a treatment effect. How do you choose between FE, DiD, and SC?

<details>
<summary>Answer</summary>

**Decision tree**:

1. **How many treated units?**
   - One → Synthetic Control
   - Many → FE or DiD

2. **Is treatment timing staggered?**
   - No (single treatment time) → Classic DiD
   - Yes → Modern DiD (Callaway-Sant'Anna) or FE with caution

3. **Are there time-varying confounders?**
   - No (only fixed confounders) → FE is sufficient
   - Yes → Need DiD parallel trends or SC matching

4. **Is parallel trends plausible?**
   - Yes → DiD (test with pre-trends)
   - No → SC (if single unit) or other method

**Rule of thumb**:
- FE removes what's fixed, DiD removes common trends
- SC matches pre-treatment to build counterfactual
- All have different identifying assumptions—don't conflate them
</details>

---

### Q9: Staggered DiD (3 points)
Why is TWFE biased with staggered treatment and what's the fix?

<details>
<summary>Answer</summary>

**The problem**: With staggered adoption, TWFE decomposes into:

1. **Good comparisons**: Never-treated vs. treated ✓
2. **OK comparisons**: Not-yet-treated vs. treated ✓
3. **Bad comparisons**: Already-treated vs. later-treated ✗

The third comparison uses already-treated units as "controls," and with heterogeneous treatment effects over time, these get **negative weights**. The result can have wrong sign or magnitude.

**Intuition**: If early adopters' treatment effects are growing over time, they look like they're "improving" relative to late adopters. This subtracts from the estimate.

**Solutions**:
1. **Callaway-Sant'Anna (2021)**: Aggregate only clean 2×2 DiD comparisons
2. **Sun-Abraham (2021)**: Interaction-weighted estimator with cohort × time interactions
3. **Borusyak et al. (2021)**: Imputation approach

**Key**: Modern DiD estimators restrict to comparisons where treatment status INCREASES, never decreases.
</details>

---

## Section D: Application (10 points)

### Q10: Research Design
A state implements a minimum wage increase in 2020. You have quarterly earnings data for workers in that state and neighboring states from 2015-2023. How would you estimate the employment effect?

<details>
<summary>Answer</summary>

**Three approaches**:

**1. Difference-in-Differences**:
- Treated: Workers in treatment state
- Control: Workers in neighboring states
- Pre: 2015-2019, Post: 2020-2023

Requirements:
- Parallel trends in pre-period
- No anticipation effects
- No spillovers to neighboring states

Implementation:
$$Y_{ist} = \alpha_i + \gamma_t + \tau \cdot \text{Treat}_s \cdot \text{Post}_t + \varepsilon_{ist}$$

**2. Synthetic Control** (if treatment state is unique):
- Create synthetic control from weighted combination of other states
- Match on pre-2020 employment trends
- Compare actual vs. synthetic post-2020

Requirements:
- Good pre-treatment fit
- No spillovers
- Treatment state within convex hull

**3. Event Study** (recommended):
- Estimate dynamic effects by quarter
- Visualize pre-trends
- Test parallel trends assumption

$$Y_{ist} = \alpha_i + \gamma_t + \sum_{k \neq -1} \tau_k \cdot \text{Treat}_s \cdot \mathbf{1}(t = k) + \varepsilon_{ist}$$

**My recommendation**:
1. Start with event study to check pre-trends
2. If parallel trends hold, report DiD estimate
3. If parallel trends questionable, try SC as robustness
4. Check for spillovers (bordering workers commuting)
5. Cluster standard errors at state level
</details>

---

## Scoring Guide

| Score | Interpretation |
|-------|----------------|
| 35-40 | Excellent! Panel methods mastered |
| 28-34 | Solid understanding, review weak areas |
| 20-27 | Need more practice on specific methods |
| < 20 | Review Week 3 material carefully |
