# RDD (Regression Discontinuity Design) — Quick Reference

## When to Use
- Treatment assigned by threshold/cutoff rule
- Running variable is observed
- Effect at cutoff is policy-relevant

## Key Assumptions
1. **Continuity** — $E[Y_0|R]$ and $E[Y_1|R]$ continuous at cutoff — Testable? Partially (covariates)
2. **No manipulation** — Units cannot precisely sort around cutoff — Testable? YES (McCrary test)
3. **SUTVA** — No spillovers — Testable? No

## Formula (Sharp RDD)
$$\tau_{RDD} = \lim_{r \to c^+} E[Y|R=r] - \lim_{r \to c^-} E[Y|R=r]$$

## Estimation
Local linear regression:
$$Y_i = \alpha + \tau \cdot D_i + \beta_1(R_i - c) + \beta_2 \cdot D_i(R_i - c) + \varepsilon_i$$

with triangular kernel weights.

## Gotchas
⚠️ Bandwidth choice matters → Use optimal (IK or CCT) and report sensitivity
⚠️ Manipulation → McCrary test has low power, check density visually
⚠️ Discrete running variable → Local randomization framework
⚠️ Fuzzy RDD → Treatment probability jumps but ≠ 0→1, use IV
⚠️ LOCAL effect only → Cannot extrapolate away from cutoff

## Code (1-liner)
```python
from causal_inference.rdd.sharp_rdd import sharp_rdd
result = sharp_rdd(outcome, running_var, cutoff=21, bandwidth='optimal')
```

## Interview Question
*"RDD requires continuity at cutoff. Does this mean treatment is 'as good as random'?"*

→ Not exactly. Continuity means potential outcomes are smooth at the cutoff—no other discontinuity. This is weaker than randomization. Near the cutoff, treatment is quasi-random, but we still need to model the running variable relationship. RDD identifies a local effect, not a global one.
