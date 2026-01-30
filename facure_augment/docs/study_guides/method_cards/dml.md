# DML (Double/Debiased Machine Learning) — Quick Reference

## When to Use
- Selection on observables, but many/complex confounders
- Want flexible ML for nuisance functions
- Need valid inference (CIs, p-values)

## Key Assumptions
1. **Conditional Ignorability** — $(Y_0, Y_1) \perp T | X$ — Testable? NO
2. **Overlap** — $0 < e(X) < 1$ — Testable? YES (check PS distribution)
3. **Regularity** — Nuisance functions converge at $n^{-1/4}$ — Technical condition

## Formula (Partially Linear Model)
$$\hat{\theta}_{DML} = \frac{\sum_i \tilde{T}_i \tilde{Y}_i}{\sum_i \tilde{T}_i^2}$$

where:
- $\tilde{Y}_i = Y_i - \hat{m}(X_i)$ (residualized outcome)
- $\tilde{T}_i = T_i - \hat{e}(X_i)$ (residualized treatment)

## Why It Works
1. **Neyman orthogonality**: Moment is insensitive to nuisance errors
2. **Cross-fitting**: Avoids overfitting bias
3. **Result**: $\sqrt{n}$-consistent with valid CIs

## Gotchas
⚠️ Cross-fitting is REQUIRED → Without it, bias doesn't vanish
⚠️ Hyperparameter tuning → Use nested CV, never tune on treatment effect
⚠️ First-stage matters → Check $R^2$ diagnostics
⚠️ Not magic → Still requires selection on observables

## Code (1-liner)
```python
from causal_inference.cate.dml import DoubleML
result = DoubleML(model_y=GBM, model_t=GBM, n_folds=5).fit(Y, T, X)
```

## Interview Question
*"Why can't you just plug ML into regression for causal inference?"*

→ Three problems: (1) Regularization bias—ML shrinks coefficients, biasing treatment effect. (2) Overfitting—same data for nuisance and treatment creates spurious correlation. (3) Invalid inference—no valid CIs. DML fixes these via orthogonal moments and cross-fitting.
