# DR (Doubly Robust) — Quick Reference

## When to Use
- Selection on observables
- Want insurance against model misspecification
- Combining PS and outcome regression benefits

## Key Assumptions
1. **Conditional Ignorability** — $(Y_0, Y_1) \perp T | X$ — Testable? NO
2. **Overlap** — $0 < e(X) < 1$ — Testable? YES
3. **At least one model correct** — PS OR outcome model — Key insight!

## Formula
$$\hat{\tau}_{DR} = \frac{1}{n}\sum_i \left[ \hat{\mu}_1(X_i) - \hat{\mu}_0(X_i) + \frac{T_i(Y_i - \hat{\mu}_1(X_i))}{\hat{e}(X_i)} - \frac{(1-T_i)(Y_i - \hat{\mu}_0(X_i))}{1-\hat{e}(X_i)} \right]$$

## Why "Doubly Robust"
- If outcome model correct: IPTW terms → 0 in expectation
- If PS model correct: IPTW provides consistent correction
- Only ONE needs to be right!

## Gotchas
⚠️ Both models wrong → Can still be biased (not "always robust")
⚠️ Extreme PS → High variance, consider trimming
⚠️ Without cross-fitting → Regularization bias (use DML approach)

## Code (1-liner)
```python
from causal_inference.observational.doubly_robust import doubly_robust_ate
result = doubly_robust_ate(Y, T, X, ps_model=GBM, outcome_model=RF)
```

## Interview Question
*"Write the doubly robust formula and explain each term."*

→ First term ($\hat{\mu}_1 - \hat{\mu}_0$) is outcome model prediction. Second term corrects for treated residuals using IPTW. Third term corrects for control residuals. If outcome model is perfect, residuals are zero. If PS model is correct, IPTW weights fix any outcome model errors.
