# CATE (Conditional Average Treatment Effects) — Quick Reference

## When to Use
- Treatment effects may vary across subgroups
- Personalization/targeting decisions needed
- Policy optimization questions

## Key Concepts

**CATE Definition**:
$$\tau(x) = E[Y(1) - Y(0) | X = x]$$

**Meta-Learners**:

| Learner | Approach | When to Use |
|---------|----------|-------------|
| **S-learner** | Single model with T as feature | Simple, but T may be "washed out" |
| **T-learner** | Separate models for T=0, T=1 | Treatment groups differ, good overlap |
| **X-learner** | Cross-impute counterfactuals | Imbalanced groups (few treated) |
| **R-learner** | Residualize, then regress | Strong confounding |

## Key Assumptions
1. **Conditional Ignorability** — $(Y_0, Y_1) \perp T | X$ — Same as ATE methods
2. **Overlap** — For all $x$: $0 < e(x) < 1$
3. **SUTVA** — No interference

## Gotchas
⚠️ HTE ≠ Prediction → Optimizing CATE ≠ optimizing prediction loss
⚠️ S-learner bias → Treatment effect can be shrunk to zero
⚠️ T-learner variance → Separate models = less data per model
⚠️ Interpretation → CATE is conditional, not causal effect OF X

## Code (1-liner)
```python
from causal_inference.cate.meta_learners import TLearner
cate = TLearner(model=GBM).fit(Y, T, X).effect(X_new)
```

## Interview Question
*"When would you estimate heterogeneous treatment effects?"*

→ When: (1) Effects plausibly vary across subgroups, (2) Targeting/personalization decisions are needed, (3) You want to understand for WHOM the treatment works. Be careful: CATE estimation is harder than ATE—requires stronger overlap and more data. Start with ATE, then explore heterogeneity.
