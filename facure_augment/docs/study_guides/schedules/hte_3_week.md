# HTE Path: 3-Week Schedule

**Goal**: Master heterogeneous treatment effect estimation for personalization and targeting.
**Time**: ~1.5 hours/day, 5 days/week
**Prerequisites**: Completed Foundations path or equivalent knowledge of ATE methods

---

## Week 1: From ATE to CATE

### Day 1 (Monday) — 1.5 hours
**Morning (45 min)**
- [ ] Read Ch 18: Why Heterogeneity Matters
- [ ] Key concept: $\tau(x) = E[Y(1) - Y(0) | X = x]$

**Evening (45 min)**
- [ ] Run notebook: `18_hte/01_ate_to_cate.ipynb`
- [ ] Review method card: `cate.md`

**Checkpoint**: When would you want CATE instead of ATE?

### Day 2 (Tuesday) — 1.5 hours
**Morning (45 min)**
- [ ] Read Ch 21: Meta-Learners Introduction
- [ ] Key concept: S-learner vs T-learner tradeoff

**Evening (45 min)**
- [ ] Run notebook: `21_meta_learners/01_s_and_t_learner.ipynb`
- [ ] Implement: S-learner from scratch

**Checkpoint**: Why might S-learner "wash out" the treatment effect?

### Day 3 (Wednesday) — 1.5 hours
**Morning (45 min)**
- [ ] Read Ch 21: X-learner
- [ ] Key concept: Cross-imputation of counterfactuals

**Evening (45 min)**
- [ ] Run notebook: `21_meta_learners/02_x_learner.ipynb`
- [ ] Compare: T-learner vs X-learner on imbalanced data

**Checkpoint**: Explain the X-learner's two-stage procedure.

### Day 4 (Thursday) — 1.5 hours
**Morning (45 min)**
- [ ] Read Ch 21: R-learner (Robinson decomposition)
- [ ] Key formula: $Y - \hat{m}(X) = (T - \hat{e}(X))\tau(X) + \varepsilon$

**Evening (45 min)**
- [ ] Run notebook: `21_meta_learners/03_r_learner.ipynb`
- [ ] Practice: When does R-learner outperform T-learner?

**Checkpoint**: Why is R-learner more robust to confounding?

### Day 5 (Friday) — 1.5 hours
**Morning (45 min)**
- [ ] Compare all meta-learners on same dataset
- [ ] Create comparison table: assumptions, pros, cons

**Evening (45 min)**
- [ ] Practice: Choose meta-learner for different scenarios
- [ ] Review interview questions from Ch 21

**Week 1 Deliverable**: Decision tree for meta-learner selection.

---

## Week 2: Machine Learning for Causal Inference

### Day 6 (Monday) — 1.5 hours
**Morning (45 min)**
- [ ] Read Ch 22: DML Motivation
- [ ] Key problem: Why can't we just plug in ML?

**Evening (45 min)**
- [ ] Run notebook: `22_debiased_ml/01_dml_intuition.ipynb`
- [ ] Review method card: `dml.md`

**Checkpoint**: List the 3 problems with naive ML for causal inference.

### Day 7 (Tuesday) — 1.5 hours
**Morning (45 min)**
- [ ] Read Ch 22: Neyman Orthogonality
- [ ] Key concept: Why orthogonal moments help

**Evening (45 min)**
- [ ] Run notebook: `22_debiased_ml/02_dml_estimation.ipynb`
- [ ] Derive: Partially linear model orthogonal moment

**Checkpoint**: Explain Neyman orthogonality in one sentence.

### Day 8 (Wednesday) — 1.5 hours
**Morning (45 min)**
- [ ] Read Ch 22: Cross-fitting
- [ ] Key concept: Breaking overfitting correlation

**Evening (45 min)**
- [ ] Implement: K-fold cross-fitting from scratch
- [ ] Compare: With vs. without cross-fitting

**Checkpoint**: Why is cross-fitting necessary even with good ML?

### Day 9 (Thursday) — 1.5 hours
**Morning (45 min)**
- [ ] Read: Causal Forests (Wager & Athey)
- [ ] Key concept: Honest splitting

**Evening (45 min)**
- [ ] Run notebook: `19_causal_forest/01_forest_basics.ipynb`
- [ ] Practice: Interpret variable importance

**Checkpoint**: How does honest splitting prevent overfitting to treatment?

### Day 10 (Friday) — 1.5 hours
**Morning (45 min)**
- [ ] Compare: DML vs. Causal Forest
- [ ] When to use each approach

**Evening (45 min)**
- [ ] Complete interview questions from Ch 22
- [ ] Review: Assumptions comparison table

**Week 2 Deliverable**: Comparison table of DML, Causal Forest, and meta-learners.

---

## Week 3: Advanced Topics & Applications

### Day 11 (Monday) — 1.5 hours
**Morning (45 min)**
- [ ] Read: DR-Learner
- [ ] Key concept: Doubly robust CATE estimation

**Evening (45 min)**
- [ ] Implement: DR-learner using DML framework
- [ ] Compare: R-learner vs. DR-learner

**Checkpoint**: How does DR-learner get double robustness?

### Day 12 (Tuesday) — 1.5 hours
**Morning (45 min)**
- [ ] Read: Policy Learning
- [ ] Key concept: Optimal treatment rules

**Evening (45 min)**
- [ ] Practice: Given CATEs, derive optimal policy
- [ ] Analyze: Policy value vs. treating everyone

**Checkpoint**: How do you evaluate a treatment policy?

### Day 13 (Wednesday) — 1.5 hours
**Morning (45 min)**
- [ ] Read: Uplift modeling in industry
- [ ] Key applications: Marketing, healthcare, pricing

**Evening (45 min)**
- [ ] Case study: Implement targeting strategy
- [ ] Calculate: Incremental profit from targeting

**Checkpoint**: What's the difference between uplift and churn prediction?

### Day 14 (Thursday) — 1.5 hours
**Morning (45 min)**
- [ ] Review: Challenges in HTE estimation
- [ ] Key issues: Overlap, interpretability, validation

**Evening (45 min)**
- [ ] Practice: Full pipeline (data → CATE → policy → evaluation)
- [ ] Address: Common pitfalls in HTE projects

**Checkpoint**: How do you validate CATE estimates without ground truth?

### Day 15 (Friday) — 1.5 hours
**Morning (45 min)**
- [ ] Final synthesis: Complete HTE decision framework
- [ ] Review all method cards

**Evening (45 min)**
- [ ] Mock interview: HTE scenarios
- [ ] Self-assessment: Ready for HTE projects?

**Week 3 Deliverable**: Complete HTE pipeline implementation + decision framework.

---

## Key Formulas to Memorize

### CATE Definition
$$\tau(x) = E[Y(1) - Y(0) | X = x]$$

### Meta-Learners
| Learner | Key Formula |
|---------|-------------|
| S-learner | $\hat{\tau}(x) = \hat{\mu}(x, 1) - \hat{\mu}(x, 0)$ |
| T-learner | $\hat{\tau}(x) = \hat{\mu}_1(x) - \hat{\mu}_0(x)$ |
| X-learner | $\hat{\tau}(x) = g(x)\hat{\tau}_0(x) + (1-g(x))\hat{\tau}_1(x)$ |
| R-learner | $(Y - \hat{m}) = (T - \hat{e})\tau(X) + \varepsilon$ |

### DML (Partially Linear)
$$\hat{\tau} = \left(\sum_i \tilde{T}_i^2\right)^{-1} \sum_i \tilde{T}_i \tilde{Y}_i$$

where $\tilde{T} = T - \hat{e}(X)$, $\tilde{Y} = Y - \hat{m}(X)$

---

## Assessment Checkpoints

| Day | Self-Check | Pass Criteria |
|-----|------------|---------------|
| 5 | Meta-learner selection | Correctly choose learner for 4/5 scenarios |
| 10 | DML explanation | Explain 3 problems + solutions fluently |
| 15 | Full pipeline | Implement end-to-end HTE analysis |

## Common Interview Questions

1. "When would you use T-learner vs. X-learner?"
2. "Explain why cross-fitting is necessary in DML"
3. "How do you validate heterogeneous treatment effects?"
4. "What's the difference between CATE and treatment effect OF X?"
5. "Design a personalized pricing strategy using causal inference"

## Next Steps After Completion

- **Deep dive**: Original papers (Athey & Imbens, Chernozhukov et al.)
- **Production**: Implement HTE pipeline for real business problem
- **Advanced**: Multi-armed bandits, contextual bandits, reinforcement learning
