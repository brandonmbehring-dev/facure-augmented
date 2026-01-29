# OLS (Regression Adjustment) — Quick Reference

## When to Use
- Selection on observables
- Linear relationship adequate
- Quick baseline estimate
- Covariate adjustment in RCTs (efficiency)

## Key Assumptions
1. **Conditional Ignorability** — $(Y_0, Y_1) \perp T | X$ — Testable? NO
2. **Linearity** — $E[Y|T,X] = \alpha + \tau T + X\beta$ — Testable? YES (specification tests)
3. **Correct functional form** — No omitted interactions — Testable? Partially

## Formula
$$Y_i = \alpha + \tau T_i + X_i'\beta + \varepsilon_i$$

**FWL interpretation**: $\hat{\tau}$ equals coefficient from regressing $\tilde{Y}$ on $\tilde{T}$, where both are residualized against $X$.

## OVB Formula
If we omit confounder $A$:
$$\hat{\tau}_{short} = \tau + \gamma \cdot \delta$$

where $\gamma$ = effect of $A$ on $Y$, $\delta$ = coefficient of $A$ on $T$.

## Gotchas
⚠️ Linearity → Effect is constant across $X$ (may be wrong)
⚠️ Extrapolation → Predicts outside support
⚠️ Bad controls → Don't control for mediators or colliders!
⚠️ OVB → Omitted confounders bias $\hat{\tau}$

## When OLS ≠ ATE
- **Heterogeneous effects** + **imbalance** → OLS gives variance-weighted average, not ATE
- OLS weights by $\text{Var}(T|X)$, so high-variance strata get more weight
- For ATE: use IPW, matching, or DML

## Code (1-liner)
```python
from causal_inference.observational.outcome_regression import ols_ate
result = ols_ate(Y, T, X, robust_se=True)
```

## Interview Question
*"When is OLS a valid causal estimator vs. just a predictive model?"*

→ OLS is causal when: (1) All confounders controlled (CIA holds), (2) No bad controls (colliders/mediators), (3) Functional form correct. In RCTs, OLS is valid (randomization ensures CIA) and controls improve precision. In observational studies, OLS requires defending CIA—which is untestable. Always: draw the DAG first, identify adjustment set, then consider functional form.
