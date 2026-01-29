# SCM (Synthetic Control Method) — Quick Reference

## When to Use
- Single treated unit (or few units)
- Multiple control units available
- Panel data with pre-treatment periods
- Policy/program evaluation at aggregate level

## Key Assumptions
1. **No anticipation** — Treatment effects only after intervention — Testable? Partially
2. **Convex hull** — Treated unit can be approximated by weighted controls — Testable? YES (check fit)
3. **No spillovers** — Control units unaffected by treatment — Testable? NO
4. **Stable weights** — Pre-treatment fit implies post-treatment counterfactual — Testable? NO

## Formula
$$\hat{Y}_{1t}^{SC} = \sum_{j=2}^{J+1} w_j^* Y_{jt}$$

where $w^*$ minimizes pre-treatment MSPE subject to $\sum w_j = 1$, $w_j \geq 0$.

**Treatment effect**:
$$\hat{\tau}_t = Y_{1t} - \hat{Y}_{1t}^{SC}$$

## Gotchas
⚠️ Poor pre-treatment fit → Invalid counterfactual
⚠️ Extrapolation → If treated outside convex hull, weights can't work
⚠️ Inference → Placebo tests required (Fisher permutation)
⚠️ N=1 problem → No classical standard errors possible

## Code (1-liner)
```python
from causal_inference.scm.basic_sc import synthetic_control
result = synthetic_control(Y_panel, treated_unit=1, treatment_time=t0)
```

## Interview Question
*"How do you do inference with synthetic control when N=1?"*

→ Placebo tests: Apply SC method to each control unit as if it were treated. If the treated unit's gap is extreme relative to placebos, effect is significant. This is Fisher's exact test logic—we're testing whether the treated unit's gap is unusual compared to the null distribution of fake gaps.
