# IV (Instrumental Variables) — Quick Reference

## When to Use
- Unobserved confounders are the problem
- You have a valid instrument (affects T, not Y directly)
- LATE at cutoff is acceptable

## Key Assumptions
1. **Relevance** — $Cov(Z, T) \neq 0$ — Testable? YES (first-stage F > 10)
2. **Exogeneity** — $Cov(Z, u) = 0$ — Testable? NO (argue from theory)
3. **Exclusion** — Z → Y only via T — Testable? NO (argue from theory)
4. **Monotonicity** — No defiers (for LATE) — Testable? NO

## Formula
$$\kappa_{IV} = \frac{Cov(Y, Z)}{Cov(T, Z)} = \frac{\text{Reduced Form}}{\text{First Stage}}$$

## Wald Estimator (binary Z)
$$\kappa_{Wald} = \frac{E[Y|Z=1] - E[Y|Z=0]}{E[T|Z=1] - E[T|Z=0]}$$

## Gotchas
⚠️ Weak instruments (F < 10) → Biased toward OLS, use LIML or AR
⚠️ Many weak instruments → Even worse bias
⚠️ Exclusion violation → No fix, estimate is wrong
⚠️ LATE ≠ ATE → Only identifies effect for compliers

## Code (1-liner)
```python
from causal_inference.iv.two_stage import TwoStageLeastSquares
result = TwoStageLeastSquares().fit(Y, T, Z, controls)
```

## Interview Question
*"Your first-stage F is 7. What do you do?"*

→ F = 7 is below Stock-Yogo threshold of 10. Options: (1) LIML estimator (less biased), (2) Anderson-Rubin confidence sets (valid regardless of strength), (3) Find stronger instruments.
