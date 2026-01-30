# FE (Fixed Effects) — Quick Reference

## When to Use
- Panel data (repeated observations over time)
- Time-invariant unobserved confounders
- Want to control for "individual heterogeneity"
- Within-unit variation is meaningful

## Key Assumptions
1. **Strict exogeneity** — $E[\varepsilon_{it} | X_{i1}, ..., X_{iT}, \alpha_i] = 0$ — Testable? Partially
2. **No time-varying confounders** — Unobservables that change over time are uncorrelated with treatment — Testable? NO
3. **Sufficient within-variation** — Treatment must vary within units — Testable? YES

## Formula
$$Y_{it} = \alpha_i + \beta X_{it} + \varepsilon_{it}$$

**Within transformation** (demean):
$$Y_{it} - \bar{Y}_i = \beta(X_{it} - \bar{X}_i) + (\varepsilon_{it} - \bar{\varepsilon}_i)$$

Equivalently: OLS with unit dummies.

## Types
| Type | Controls For | Removes |
|------|--------------|---------|
| Unit FE | $\alpha_i$ | Time-invariant unit confounders |
| Time FE | $\gamma_t$ | Common time shocks |
| TWFE | $\alpha_i + \gamma_t$ | Both (but see TWFE bias!) |

## Gotchas
⚠️ TWFE + staggered treatment → BIASED (use Callaway-Sant'Anna)
⚠️ Time-varying confounders → Not controlled
⚠️ Short panels → Incidental parameters problem
⚠️ Clustering → Usually cluster at unit level

## Code (1-liner)
```python
from causal_inference.panel.fixed_effects import panel_fe
result = panel_fe(Y, T, entity_id, time_id, cluster='entity')
```

## Interview Question
*"When does TWFE fail and what should you use instead?"*

→ TWFE fails with staggered adoption + heterogeneous effects. Already-treated units become "controls" for later-treated units with negative weights. Use modern DiD estimators: Callaway-Sant'Anna (2021) aggregates clean 2x2 comparisons, Sun-Abraham (2021) uses interaction-weighted estimator, or Borusyak et al. (2021) imputation approach.
