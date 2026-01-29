# DiD (Difference-in-Differences) — Quick Reference

## When to Use
- Treatment varies across groups and time
- Parallel trends assumption is plausible
- Panel data or repeated cross-sections available

## Key Assumptions
1. **Parallel Trends** — $E[Y_0(post) - Y_0(pre)|D=1] = E[Y_0(post) - Y_0(pre)|D=0]$ — Testable? NO (about counterfactuals)
2. **No anticipation** — Treatment doesn't affect pre-period outcomes — Testable? Partially
3. **SUTVA** — No spillovers across groups — Testable? No

## Formula
$$\hat{ATT}_{DiD} = (\bar{Y}_{T,post} - \bar{Y}_{T,pre}) - (\bar{Y}_{C,post} - \bar{Y}_{C,pre})$$

## Regression Form
$$Y_{it} = \alpha + \beta \cdot D_i + \gamma \cdot Post_t + \tau \cdot (D_i \times Post_t) + \varepsilon_{it}$$

$\tau$ is the DiD estimate.

## Gotchas
⚠️ Pre-trends ≠ Parallel trends → Pre-trend test is necessary but not sufficient
⚠️ TWFE with staggered adoption → Biased! Use Callaway-Sant'Anna or Sun-Abraham
⚠️ Few clusters → Cluster SEs biased, use wild cluster bootstrap
⚠️ Differential time trends → Consider synthetic control or triple-diff

## Code (1-liner)
```python
from causal_inference.did.classic_did import classic_did
result = classic_did(outcome, treatment, post, cluster=unit_id)
```

## Interview Question
*"Explain the parallel trends assumption. Why is it untestable?"*

→ Parallel trends says treated and control would have followed the same trend absent treatment. It's about the *counterfactual* trend for treated units—which we never observe. Pre-trend tests are informative but not conclusive.
