# Learning Paths

Four guided study sequences tailored to different goals and backgrounds.

---

## Prerequisite Graph

Understanding which chapters depend on which:

```
FOUNDATIONS (No prerequisites)
├── 01 Introduction to Causality
│   └── 02 Randomized Experiments
│   └── 04 Graphical Causal Models
├── 03 Stats Review (reference)
└── 05 Linear Regression [CORE]
    ├── 05b Intro to Double ML
    ├── 06 Grouped/Dummy Regression
    ├── 07 Beyond Confounders
    ├── 08 Instrumental Variables [CORE]
    │   └── 09 Non-Compliance & LATE
    ├── 10 Matching
    │   └── 11 Propensity Score
    │       └── 12 Doubly Robust
    │       └── A3 PS Debiasing
    ├── 13 Difference-in-Differences [CORE]
    │   ├── 14 Panel Data & Fixed Effects
    │   ├── 15 Synthetic Control
    │   │   └── A1 Conformal SCM
    │   │   └── 25 Synthetic DiD
    │   └── 24 The DiD Saga
    └── 16 Regression Discontinuity [CORE]

ML METHODS (Requires Ch 5)
├── 17 Predictive Models 101
│   └── 18 Heterogeneous Effects
│       ├── 19 Evaluating Causal Models
│       │   └── A5 Causal Metrics
│       ├── 20 F-Learner
│       │   └── 21 Meta-Learners
│       │       └── 22 Debiased ML [CORE]
│       └── 23 Challenges with Heterogeneity
│       └── A4 When Prediction Fails
└── A2 Orthogonalization (FWL refresher)
```

---

## Path 1: Foundations First

**For**: Systematic learners building from first principles
**Duration**: 4-6 weeks (~35-40 hours)
**Goal**: Comprehensive understanding of causal inference methods

### Week 1: Conceptual Foundations (~6 hours)

| Day | Chapter | Focus | Time |
|-----|---------|-------|------|
| 1-2 | 01 | Potential outcomes, ATE, counterfactuals | ~1.5h |
| 3 | 02 | Why randomization works | ~1.5h |
| 4-5 | 03 | Stats review (SE, CI, p-values) | ~2h |
| 6-7 | 04 | DAGs, d-separation, backdoor criterion | ~2h |

**Checkpoint**: Can you explain the fundamental problem of causal inference? Draw a DAG with a confounder and identify the backdoor path.

### Week 2: Regression Foundation (~6 hours)

| Day | Chapter | Focus | Time |
|-----|---------|-------|------|
| 1-2 | 05 (1-2) | Regression basics, FWL theorem | ~2.5h |
| 3-4 | 05 (3-4) | Non-random data, OVB formula | ~2h |
| 5-7 | 06 | Grouped data, interactions | ~1.5h |

**Checkpoint**: Can you state and prove the FWL theorem? Derive the OVB formula?

### Week 3: Confounders & Matching (~6 hours)

| Day | Chapter | Focus | Time |
|-----|---------|-------|------|
| 1-2 | 07 | Good/bad controls, colliders | ~2h |
| 3-5 | 10 | Matching intuition, distance metrics | ~2h |
| 6-7 | 11 (1-2) | Propensity scores, IPTW | ~2h |

**Checkpoint**: Why is controlling for a collider bad? What is the balancing property of propensity scores?

### Week 4: Weighting & Robustness (~5 hours)

| Day | Chapter | Focus | Time |
|-----|---------|-------|------|
| 1-2 | 11 (3-4) | PS matching, diagnostics | ~2h |
| 3-5 | 12 | Doubly robust estimation | ~1.5h |
| 6-7 | A3 | IPTW practical issues | ~1h |

**Checkpoint**: Write the doubly robust estimator formula. Why is it called "doubly robust"?

### Week 5: Design-Based Methods (~6 hours)

| Day | Chapter | Focus | Time |
|-----|---------|-------|------|
| 1-2 | 08 (1-2) | IV intuition, 2SLS | ~2h |
| 3-4 | 13 (1-2) | DiD intuition, estimation | ~1.5h |
| 5-7 | 16 | RDD sharp and fuzzy | ~2h |

**Checkpoint**: What are the two IV assumptions? State the parallel trends assumption.

### Week 6: Advanced Topics (~6 hours)

| Day | Chapter | Focus | Time |
|-----|---------|-------|------|
| 1-2 | 09 | LATE, non-compliance | ~2h |
| 3-4 | 14 | Fixed effects | ~2h |
| 5-7 | 15 | Synthetic control | ~2h |

**Final Assessment**: Complete all interview questions from CORE chapters (5, 8, 13, 16).

---

## Path 2: Interview Fast Track

**For**: Interview preparation, experienced practitioners
**Duration**: 2 weeks (~20-25 hours)
**Goal**: Master the 5 CORE chapters with interview-ready knowledge

### Week 1: Regression & IV (~12 hours)

| Day | Chapter | Focus | Est. Time |
|-----|---------|-------|-----------|
| 1-2 | **05** [CORE] | FWL theorem, OVB formula | ~2.5h |
| 3-4 | 05b (1-2) | Robinson, Neyman orthogonality | ~2h |
| 5-6 | **08** [CORE] | 2SLS, weak instruments, F>10 | ~2.5h |
| 7 | 08 (interview) | Practice all interview Qs | ~2h |

**Key Interview Topics**:
- Derive FWL theorem (algebraic or geometric)
- What is the OVB formula? Sign of bias?
- Two IV assumptions and why each matters
- What is a weak instrument? How to detect?

### Week 2: DiD, RDD, DML (~12 hours)

| Day | Chapter | Focus | Est. Time |
|-----|---------|-------|-----------|
| 1-2 | **13** [CORE] | Parallel trends, TWFE | ~2h |
| 3 | 24 (2) | TWFE bias (Goodman-Bacon) | ~1h |
| 4-5 | **16** [CORE] | Sharp/fuzzy RDD, bandwidth | ~2h |
| 6-7 | **22** [CORE] | DML algorithm, cross-fitting | ~2h |
| 8 | All CORE | Interview Q marathon | ~3h |

**Key Interview Topics**:
- What is the parallel trends assumption? How to test?
- Why does TWFE fail with staggered adoption?
- RDD is "local" — what does this mean?
- Why does DML use cross-fitting?

### Interview Question Inventory

From CORE chapters, practice these Advanced-level questions:

1. **Ch 5**: "Derive the OVB formula. When is bias positive?"
2. **Ch 5b**: "Why does Neyman orthogonality enable ML for causal inference?"
3. **Ch 8**: "Explain the difference between LATE and ATE"
4. **Ch 8**: "A company runs an A/B test with non-compliance. Design the analysis."
5. **Ch 13**: "When does TWFE give wrong answers?"
6. **Ch 16**: "Explain the McCrary test. Why is density manipulation a problem?"
7. **Ch 22**: "Walk through the DML algorithm step by step."

---

## Path 3: Advanced HTE Deep Dive

**For**: CATE specialists, ML practitioners moving into causality
**Duration**: 3 weeks (~25-30 hours)
**Goal**: Master heterogeneous treatment effect estimation

### Prerequisites
Complete Ch 5 (Linear Regression) before starting.

### Week 1: ML Foundations for Causality (~9 hours)

| Day | Chapter | Focus | Time |
|-----|---------|-------|------|
| 1-2 | 17 | Prediction vs. causation, policies | ~1.5h |
| 3-4 | 18 | ATE to CATE, heterogeneity | ~2h |
| 5-6 | 19 | Evaluating CATE models | ~2h |
| 7 | A4 | When prediction fails | ~1.5h |
| 8 | A5 | R² failures, cumulative elasticity | ~1h |

**Checkpoint**: Why can't you use R² to evaluate a CATE model? What's the fundamental problem?

### Week 2: Meta-Learners (~10 hours)

| Day | Chapter | Focus | Time |
|-----|---------|-------|------|
| 1-2 | 20 | F-learner, target transformation | ~1.5h |
| 3-4 | 21 (1-2) | S-learner, T-learner, X-learner | ~2.5h |
| 5-6 | 21 (3-4) | Meta-learner comparison, R-learner | ~2h |
| 7-8 | A2 | Orthogonalization refresher | ~2h |

**Checkpoint**: When does T-learner beat S-learner? What is the regularization bias problem?

### Week 3: DML & Challenges (~8 hours)

| Day | Chapter | Focus | Time |
|-----|---------|-------|------|
| 1-2 | 05b (3-5) | Cross-fitting, DML implementation | ~3h |
| 3-4 | **22** [CORE] | Full DML, EconML | ~2h |
| 5-6 | 23 | Binary outcomes, nonlinearity | ~1h |
| 7 | Review | Practice all interview Qs | ~2h |

**Key Deliverable**: Implement DML from scratch. Compare to EconML's LinearDML.

---

## Path 4: Panel Methods Specialist

**For**: Economists, policy researchers working with panel data
**Duration**: 2 weeks (~18-22 hours)
**Goal**: Master DiD, synthetic control, and panel methods

### Prerequisites
Complete Ch 5 (Linear Regression) before starting.

### Week 1: DiD & Fixed Effects (~10 hours)

| Day | Chapter | Focus | Time |
|-----|---------|-------|------|
| 1-2 | **13** [CORE] | DiD intuition, parallel trends | ~2h |
| 3-4 | 14 | Panel structure, within transform | ~2h |
| 5-6 | 14 (3-4) | Two-way FE, limitations | ~2h |
| 7-8 | 24 | TWFE bias, Goodman-Bacon | ~2h |

**Checkpoint**: What's the difference between entity FE and time FE? When does TWFE give negative weights?

### Week 2: Synthetic Control & Advanced DiD (~10 hours)

| Day | Chapter | Focus | Time |
|-----|---------|-------|------|
| 1-2 | 15 (1-2) | SCM concept, optimization | ~2h |
| 3-4 | 15 (3-4) | Treatment effect, inference | ~2.5h |
| 5-6 | 25 | SDID foundations, estimation | ~2h |
| 7 | A1 | Conformal SCM, per-period CIs | ~1.5h |
| 8 | Review | All interview Qs | ~2h |

**Key Interview Topics**:
- When to use SCM vs. DiD?
- How do you do inference for synthetic control?
- What is SDID and when is it useful?

---

## Comparison: Which Path?

| Path | Duration | Notebooks | Best For |
|------|----------|-----------|----------|
| Foundations First | 4-6 weeks | ~65 | New to causal inference |
| Interview Fast Track | 2 weeks | ~25 | Job interviews |
| HTE Deep Dive | 3 weeks | ~30 | ML practitioners, CATE |
| Panel Specialist | 2 weeks | ~20 | Economists, policy |

---

## Tips for All Paths

1. **Do the interview questions** — They're designed to test deep understanding
2. **Run the code** — Don't just read; execute every cell
3. **Check your intuition** — Before reading proofs, guess what the result should be
4. **Connect concepts** — FWL → Robinson → DML is one thread; backdoor → PS → IPTW is another
5. **Take breaks** — Causal inference requires careful thinking; don't rush

---

## Progress Tracking

Use this checklist format:

```markdown
## My Progress

### Path: [Your Path]
### Started: [Date]

- [ ] Ch 01: Introduction to Causality
- [ ] Ch 02: Randomized Experiments
- [ ] Ch 03: Stats Review
...

### Interview Qs Completed: __ / 300
### Estimated Hours Completed: __ / 50
```
