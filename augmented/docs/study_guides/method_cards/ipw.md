# IPW (Inverse Propensity Weighting) — Quick Reference

## When to Use
- Selection on observables
- Want to reweight sample to balance confounders
- Semiparametric approach (no outcome model needed)
- Can handle non-linear treatment effects

## Key Assumptions
1. **Conditional Ignorability** — $(Y_0, Y_1) \perp T | X$ — Testable? NO
2. **Overlap/Positivity** — $0 < e(X) < 1$ for all $X$ — Testable? YES
3. **Correct PS model** — $\hat{e}(X) \approx e(X)$ — Testable? Partially (balance)

## Formula (Horvitz-Thompson)
$$\hat{\tau}_{IPW} = \frac{1}{n}\sum_{i=1}^n \left[ \frac{T_i Y_i}{e(X_i)} - \frac{(1-T_i) Y_i}{1-e(X_i)} \right]$$

**Hajek (normalized) estimator** — More stable:
$$\hat{\mu}_1 = \frac{\sum_i T_i Y_i / e(X_i)}{\sum_i T_i / e(X_i)}, \quad \hat{\mu}_0 = \frac{\sum_i (1-T_i) Y_i / (1-e(X_i))}{\sum_i (1-T_i) / (1-e(X_i))}$$

## Weight Targets
| Estimand | Treated Weight | Control Weight |
|----------|----------------|----------------|
| ATE | $1/e(X)$ | $1/(1-e(X))$ |
| ATT | $1$ | $e(X)/(1-e(X))$ |
| ATC | $(1-e(X))/e(X)$ | $1$ |

## Gotchas
⚠️ Extreme PS (near 0 or 1) → Exploding variance
⚠️ PS trimming → Changes estimand (no longer ATE)
⚠️ Weight instability → Check effective sample size
⚠️ Model misspecification → Combine with outcome model (DR)

## Code (1-liner)
```python
from causal_inference.observational.propensity import ipw_ate
result = ipw_ate(Y, T, X, ps_model=LogisticRegression(), trimming=0.01)
```

## Interview Question
*"What's the difference between Horvitz-Thompson and Hajek estimators?"*

→ Horvitz-Thompson uses raw inverse weights; Hajek normalizes by sum of weights. Hajek is more stable (weights sum to 1) but introduces small bias. In practice, Hajek is preferred because HT can have enormous variance when PS near 0 or 1. Both are consistent; Hajek trades slight bias for much better MSE.
