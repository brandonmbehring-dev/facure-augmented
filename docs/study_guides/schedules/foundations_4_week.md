# Foundations Path: 4-Week Schedule

**Goal**: Build solid causal inference fundamentals from first principles.
**Time**: ~1.5 hours/day, 5 days/week
**Prerequisites**: Basic statistics, linear algebra, probability

---

## Week 1: Potential Outcomes & RCTs

### Day 1 (Monday) — 1.5 hours
**Morning (45 min)**
- [ ] Read Ch 1: Introduction to Causality
- [ ] Key concept: Correlation ≠ Causation examples

**Evening (45 min)**
- [ ] Read Ch 2: RCTs (sections 1-2)
- [ ] Review method card: `rct.md`

**Checkpoint**: Can you explain why randomization solves selection bias?

### Day 2 (Tuesday) — 1.5 hours
**Morning (45 min)**
- [ ] Read Ch 2: RCTs (sections 3-4)
- [ ] Run notebook: `02_randomised_experiments/01_rct_gold_standard.ipynb`

**Evening (45 min)**
- [ ] Read Ch 3: Stats Review (Conditional Expectation)
- [ ] Complete 2 quiz questions from `week_1_quiz.md`

**Checkpoint**: Write the potential outcomes framework: $Y_i = T_i Y_i(1) + (1-T_i) Y_i(0)$

### Day 3 (Wednesday) — 1.5 hours
**Morning (45 min)**
- [ ] Read Ch 4: Graphical Causal Models
- [ ] Practice: Draw 3 DAGs (confounder, mediator, collider)

**Evening (45 min)**
- [ ] Run notebook: `04_graphical_causal_models/01_dag_basics.ipynb`
- [ ] Identify adjustment sets for each DAG

**Checkpoint**: Why is conditioning on a collider bad?

### Day 4 (Thursday) — 1.5 hours
**Morning (45 min)**
- [ ] Read Ch 5: Linear Regression as Causal Estimator
- [ ] Key concept: FWL theorem intuition

**Evening (45 min)**
- [ ] Run notebook: `05_linear_regression/01_*.ipynb`
- [ ] Review method card: `ols.md`

**Checkpoint**: Explain OVB formula: $\hat{\tau}_{short} = \tau + \gamma \cdot \delta$

### Day 5 (Friday) — 1.5 hours
**Morning (45 min)**
- [ ] Complete remaining `week_1_quiz.md` questions
- [ ] Review any weak areas

**Evening (45 min)**
- [ ] Synthesis exercise: Compare RCT vs. OLS assumptions
- [ ] Write 1-paragraph summary of the week

**Week 1 Deliverable**: List the 3 key assumptions for causal inference from observational data.

---

## Week 2: Selection on Observables

### Day 6 (Monday) — 1.5 hours
**Morning (45 min)**
- [ ] Read Ch 10: Matching (sections 1-2)
- [ ] Key concept: Exact matching vs. approximate matching

**Evening (45 min)**
- [ ] Run notebook: `10_matching/01_matching_intuition.ipynb`
- [ ] Review method card: `psm.md`

**Checkpoint**: Why does matching reduce to 1 dimension with propensity scores?

### Day 7 (Tuesday) — 1.5 hours
**Morning (45 min)**
- [ ] Read Ch 11: Propensity Score Methods
- [ ] Key formula: $e(X) = P(T=1|X)$

**Evening (45 min)**
- [ ] Run notebook: `11_propensity_score/01_balancing_score.ipynb`
- [ ] Review method card: `ipw.md`

**Checkpoint**: Derive the IPW estimator from reweighting logic.

### Day 8 (Wednesday) — 1.5 hours
**Morning (45 min)**
- [ ] Read Ch 12: Doubly Robust Estimation
- [ ] Key insight: Why "doubly" robust?

**Evening (45 min)**
- [ ] Run notebook: `12_doubly_robust/01_dr_estimator.ipynb`
- [ ] Review method card: `dr.md`

**Checkpoint**: Write the AIPW formula and explain each term.

### Day 9 (Thursday) — 1.5 hours
**Morning (45 min)**
- [ ] Re-read: Overlap/positivity assumption
- [ ] Practice: Diagnose overlap with PS histograms

**Evening (45 min)**
- [ ] Compare estimators: OLS vs. IPW vs. DR on same dataset
- [ ] Complete 3 questions from `week_2_quiz.md`

**Checkpoint**: When would you prefer IPW over OLS?

### Day 10 (Friday) — 1.5 hours
**Morning (45 min)**
- [ ] Complete remaining `week_2_quiz.md` (Section A)
- [ ] Review weak areas

**Evening (45 min)**
- [ ] Synthesis: Decision tree for selection-on-observables methods
- [ ] Write comparison table: OLS vs. PSM vs. IPW vs. DR

**Week 2 Deliverable**: Create a 1-page cheat sheet for propensity score methods.

---

## Week 3: Instrumental Variables & DiD

### Day 11 (Monday) — 1.5 hours
**Morning (45 min)**
- [ ] Read Ch 8: IV Intuition
- [ ] Key concept: Exclusion restriction

**Evening (45 min)**
- [ ] Run notebook: `08_instrumental_variables/01_iv_intuition.ipynb`
- [ ] Review method card: `iv.md`

**Checkpoint**: Why does IV solve endogeneity?

### Day 12 (Tuesday) — 1.5 hours
**Morning (45 min)**
- [ ] Read Ch 8: 2SLS mechanics
- [ ] Derive: $\kappa_{IV} = \frac{Cov(Y,Z)}{Cov(T,Z)}$

**Evening (45 min)**
- [ ] Run notebook: `08_instrumental_variables/02_two_stage_least_squares.ipynb`
- [ ] Practice: Identify valid instruments (examples)

**Checkpoint**: What are the 3 conditions for a valid instrument?

### Day 13 (Wednesday) — 1.5 hours
**Morning (45 min)**
- [ ] Read Ch 13: DiD Intuition
- [ ] Key concept: Parallel trends assumption

**Evening (45 min)**
- [ ] Run notebook: `13_difference_in_differences/01_did_intuition.ipynb`
- [ ] Review method card: `did.md`

**Checkpoint**: Write the DiD estimator as difference of differences.

### Day 14 (Thursday) — 1.5 hours
**Morning (45 min)**
- [ ] Read Ch 13: DiD as regression
- [ ] Key concern: TWFE bias with staggered adoption

**Evening (45 min)**
- [ ] Run notebook: `13_difference_in_differences/02_did_regression.ipynb`
- [ ] Review method card: `fe.md`

**Checkpoint**: Why is TWFE biased with staggered treatment?

### Day 15 (Friday) — 1.5 hours
**Morning (45 min)**
- [ ] Complete `week_2_quiz.md` (Sections B & D)
- [ ] Review IV and DiD weak areas

**Evening (45 min)**
- [ ] Compare: When IV vs. DiD vs. selection-on-observables?
- [ ] Practice interview questions from notebooks

**Week 3 Deliverable**: Explain when you would use IV vs. DiD vs. matching.

---

## Week 4: RDD & Synthesis

### Day 16 (Monday) — 1.5 hours
**Morning (45 min)**
- [ ] Read Ch 16: RDD Intuition
- [ ] Key concept: Local randomization at cutoff

**Evening (45 min)**
- [ ] Run notebook: `16_regression_discontinuity/01_rdd_intuition.ipynb`
- [ ] Review method card: `rdd.md`

**Checkpoint**: What is the continuity assumption?

### Day 17 (Tuesday) — 1.5 hours
**Morning (45 min)**
- [ ] Read Ch 16: Sharp vs. Fuzzy RDD
- [ ] Key formula: Fuzzy RDD = ITT / First Stage

**Evening (45 min)**
- [ ] Run notebook: `16_regression_discontinuity/02_rdd_estimation.ipynb`
- [ ] Practice: McCrary density test interpretation

**Checkpoint**: Explain why RDD is "local" in two senses.

### Day 18 (Wednesday) — 1.5 hours
**Morning (45 min)**
- [ ] Read Ch 15: Synthetic Control
- [ ] Key concept: Weighted combination of controls

**Evening (45 min)**
- [ ] Run notebook: `15_synthetic_control/01_synthetic_concept.ipynb`
- [ ] Review method card: `scm.md`

**Checkpoint**: How do you do inference with N=1?

### Day 19 (Thursday) — 1.5 hours
**Morning (45 min)**
- [ ] Master synthesis: Build decision tree for ALL methods
- [ ] Complete `week_2_quiz.md` (Section C)

**Evening (45 min)**
- [ ] Practice: Given a scenario, choose the best method
- [ ] Review all method cards

**Checkpoint**: Create a complete method selection flowchart.

### Day 20 (Friday) — 1.5 hours
**Morning (45 min)**
- [ ] Final review: All quiz questions
- [ ] Identify remaining weak areas

**Evening (45 min)**
- [ ] Synthesis exercise: Write 2-page "Causal Inference Essentials" summary
- [ ] Self-assessment: Ready for applied work?

**Week 4 Deliverable**: Complete method selection decision tree + 2-page summary.

---

## Assessment Checkpoints

| Week | Quiz | Target Score |
|------|------|--------------|
| 1 | `week_1_quiz.md` | 20/30 (67%) |
| 2 | `week_2_quiz.md` (A, D) | 15/20 (75%) |
| 3 | `week_2_quiz.md` (B, C) | 15/20 (75%) |
| 4 | All quizzes review | 55/70 (80%) |

## Next Steps After Completion

- **Interview prep**: Move to `interview_2_week.md` for intensive practice
- **HTE focus**: Move to `hte_3_week.md` for heterogeneous effects
- **Advanced methods**: Explore Ch 21-25 (DML, DiD saga, Synthetic DiD)
