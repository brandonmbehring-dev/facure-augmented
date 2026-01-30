# PSM (Propensity Score Matching) — Quick Reference

## When to Use
- Selection on observables plausible
- Want explicit comparison (matched pairs)
- Overlap/balance diagnostics important

## Key Assumptions
1. **Conditional Ignorability** — $(Y_0, Y_1) \perp T | X$ — Testable? NO
2. **Overlap/Positivity** — $0 < e(X) < 1$ — Testable? YES (check PS distribution)
3. **Correct PS model** — $e(X)$ correctly specified — Testable? Partially (balance after matching)

## Formula (ATT)
$$\hat{\tau}_{ATT} = \frac{1}{n_1} \sum_{i:T_i=1} [Y_i - Y_{j(i)}]$$

where $j(i)$ is the matched control for treated unit $i$.

## Propensity Score
$$e(X) = P(T=1|X)$$

Balancing property: $X \perp T | e(X)$

## Gotchas
⚠️ Matching with replacement → Abadie-Imbens SE (NOT bootstrap!)
⚠️ No overlap regions → Cannot match, consider trimming
⚠️ PS model wrong → Balance will be poor, check SMD
⚠️ Curse of dimensionality → PS solves this by reducing to 1 dimension

## Code (1-liner)
```python
from causal_inference.psm.matching import nearest_neighbor_matching
result = nearest_neighbor_matching(Y, T, X, distance='propensity')
```

## Interview Question
*"Why is the propensity score a balancing score?"*

→ Rosenbaum-Rubin (1983) proved that conditioning on $e(X)$ balances all covariates: $X \perp T | e(X)$. Within strata of the propensity score, treated and control have the same covariate distribution on average. This reduces the matching problem from $p$ dimensions to 1.
