# RCT (Randomized Controlled Trial) — Quick Reference

## When to Use
- Treatment can be randomly assigned
- Ethical and practical to randomize
- You need the "gold standard" causal estimate

## Key Assumptions
1. **Randomization** — $(Y_0, Y_1) \perp T$ — Testable? No (by design, always holds)
2. **SUTVA** — No interference, no hidden treatments — Testable? Partially (check for spillovers)
3. **Compliance** — Units receive assigned treatment — Testable? Yes (measure actual treatment)

## Formula
$$\hat{ATE} = \bar{Y}_1 - \bar{Y}_0 = \frac{1}{n_1}\sum_{i:T_i=1} Y_i - \frac{1}{n_0}\sum_{i:T_i=0} Y_i$$

## Variance (Neyman)
$$Var(\hat{ATE}) = \frac{\sigma_1^2}{n_1} + \frac{\sigma_0^2}{n_0}$$

## Gotchas
⚠️ Non-compliance → Use ITT or IV for LATE
⚠️ Attrition → Can reintroduce selection bias
⚠️ Spillovers → SUTVA violation, clustered designs
⚠️ Finite sample imbalance → Use stratification or ANCOVA

## Code (1-liner)
```python
from causal_inference.rct.simple_ate import simple_ate
result = simple_ate(outcome, treatment)
```

## Interview Question
*"Why is randomization sufficient for causal identification?"*

→ Randomization makes treatment independent of potential outcomes. The difference in means equals the ATE because $E[Y_0|T=1] = E[Y_0|T=0]$ by construction.
