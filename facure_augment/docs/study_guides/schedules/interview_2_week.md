# Interview Prep: 2-Week Intensive Schedule

**Goal**: Master causal inference fundamentals for DS/Econ interviews
**Time commitment**: 2-3 hours/day
**Prerequisites**: Basic statistics, regression

---

## Week 1: Foundations & Core Methods

### Day 1 (Monday) — Potential Outcomes & RCTs
**Morning (1 hour)**
- [ ] Read Ch 01: Potential Outcomes (01_potential_outcomes.ipynb)
- [ ] Read Ch 02: RCT Gold Standard (01_rct_gold_standard.ipynb)
- [ ] Complete Interview Q1-Q3 from Chapter 2

**Evening (1 hour)**
- [ ] Review method card: RCT
- [ ] Practice explaining: "Why are RCTs the gold standard?"

**Checkpoint**: Can you derive $E[\hat{ATE}] = ATE$ under randomization?

---

### Day 2 (Tuesday) — Linear Regression & FWL
**Morning (1.5 hours)**
- [ ] Read Ch 05.2: FWL Theorem (02_regression_theory.ipynb)
- [ ] Read Ch 05.3: Regression for Non-Random Data (03_regression_nonrandom_data.ipynb)
- [ ] Complete Interview Q1-Q5 from Chapter 5

**Evening (1 hour)**
- [ ] Review method card: OLS
- [ ] Practice deriving OVB formula

**Checkpoint**: Explain FWL to a colleague in 2 minutes

---

### Day 3 (Wednesday) — Propensity Scores & IPW
**Morning (1.5 hours)**
- [ ] Read Ch 11.1: Balancing Score (01_balancing_score.ipynb)
- [ ] Read Ch 11.2: IPTW (02_iptw.ipynb)
- [ ] Complete Interview Q1-Q3 from Chapter 11

**Evening (1 hour)**
- [ ] Review method card: IPW
- [ ] Practice: When does IPTW fail? (Extreme weights, no overlap)

**Checkpoint**: Why is the propensity score a "balancing score"?

---

### Day 4 (Thursday) — Matching & Doubly Robust
**Morning (1.5 hours)**
- [ ] Read Ch 10.1: Matching Intuition (01_matching_intuition.ipynb)
- [ ] Read Ch 12.1: Doubly Robust (01_dr_estimator.ipynb)
- [ ] Complete Interview Q1-Q3 from Chapters 10 & 12

**Evening (1 hour)**
- [ ] Review method cards: PSM, DR
- [ ] Practice: "Why is DR 'doubly robust'?"

**Checkpoint**: Write the DR formula from memory

---

### Day 5 (Friday) — Instrumental Variables
**Morning (1.5 hours)**
- [ ] Read Ch 08.1: IV Intuition (01_iv_intuition.ipynb)
- [ ] Read Ch 08.2: 2SLS (02_two_stage_least_squares.ipynb)
- [ ] Read Ch 08.4: Weak Instruments (04_weak_instruments.ipynb)
- [ ] Complete Interview Q1-Q5 from Chapter 8

**Evening (1 hour)**
- [ ] Review method card: IV
- [ ] Practice deriving $\kappa_{IV} = \frac{Cov(Y,Z)}{Cov(T,Z)}$

**Checkpoint**: What are the 3 conditions for a valid instrument? Which is testable?

---

### Day 6 (Saturday) — Week 1 Review
**Full review (2-3 hours)**
- [ ] Complete Week 1 Quiz (quizzes/week_1_quiz.md)
- [ ] Review any topics where quiz performance was weak
- [ ] Practice explaining each method in < 2 minutes

**Checkpoint Quiz**:
1. When does regression identify causal effects?
2. Write the IPTW and DR estimators
3. Derive the IV estimator from first principles

---

### Day 7 (Sunday) — Rest or Catch-Up
- Light review of method cards
- Re-read any confusing sections

---

## Week 2: Advanced Methods & Interview Practice

### Day 8 (Monday) — Difference-in-Differences
**Morning (1.5 hours)**
- [ ] Read Ch 13.1: DiD Intuition (01_did_intuition.ipynb)
- [ ] Read Ch 13.3: Parallel Trends (03_parallel_trends.ipynb)
- [ ] Complete Interview Q1-Q3 from Chapter 13

**Evening (1 hour)**
- [ ] Review method card: DiD
- [ ] Practice: "Explain parallel trends. Why is it untestable?"

**Checkpoint**: Write the DiD estimator as a double difference

---

### Day 9 (Tuesday) — Panel Data & Fixed Effects
**Morning (1.5 hours)**
- [ ] Read Ch 14.2: Fixed Effects (02_fixed_effects.ipynb)
- [ ] Read Ch 24.1: TWFE Fundamentals (01_twfe_fundamentals.ipynb)
- [ ] Understand: Why is TWFE biased with staggered adoption?

**Evening (1 hour)**
- [ ] Review method card: FE
- [ ] Practice: "When do fixed effects help vs. hurt?"

**Checkpoint**: What controls for time-invariant confounders?

---

### Day 10 (Wednesday) — RDD
**Morning (1.5 hours)**
- [ ] Read Ch 16.1: RDD Intuition (01_rdd_intuition.ipynb)
- [ ] Read Ch 16.2: RDD Estimation (02_rdd_estimation.ipynb)
- [ ] Complete Interview Q1-Q5 from Chapter 16

**Evening (1 hour)**
- [ ] Review method card: RDD
- [ ] Practice: "What is continuity and how can it be violated?"

**Checkpoint**: What makes RDD a "local" estimator?

---

### Day 11 (Thursday) — Heterogeneous Treatment Effects
**Morning (1.5 hours)**
- [ ] Read Ch 18.1: ATE to CATE (01_ate_to_cate.ipynb)
- [ ] Read Ch 21.1: Meta-Learners (01_s_and_t_learner.ipynb)
- [ ] Understand S-learner, T-learner, X-learner

**Evening (1 hour)**
- [ ] Review method card: CATE
- [ ] Practice: "When would you estimate heterogeneous effects?"

**Checkpoint**: Explain the difference between S-learner and T-learner

---

### Day 12 (Friday) — Double/Debiased ML
**Morning (1.5 hours)**
- [ ] Read Ch 22.1: DML Intuition (01_dml_intuition.ipynb)
- [ ] Read Ch 22.2: DML Estimation (02_dml_estimation.ipynb)
- [ ] Complete Interview Q1-Q5 from Chapter 22

**Evening (1 hour)**
- [ ] Review method card: DML
- [ ] Practice: "Why can't you just plug ML into regression?"

**Checkpoint**: What is Neyman orthogonality and why does it matter?

---

### Day 13 (Saturday) — Mock Interview Practice
**Full practice (3 hours)**
- [ ] Complete Week 2 Quiz
- [ ] Do 3 mock interview questions (timed, 10 min each):
  1. "Explain DiD to a product manager"
  2. "Your colleague proposes using ML for causal inference. What's wrong?"
  3. "You have observational data on a marketing campaign. Walk me through your approach."

**Checkpoint**: Can you answer each question in < 5 minutes?

---

### Day 14 (Sunday) — Final Review
**Final consolidation (2 hours)**
- [ ] Review all method cards
- [ ] Re-do any weak quiz questions
- [ ] Practice the "method selection" decision tree:
  - RCT available? → Use it
  - No? → Selection on observables plausible? → PSM/DR/DML
  - Unobserved confounders? → IV (if valid instrument)
  - Panel data with treatment timing? → DiD/FE
  - Threshold-based treatment? → RDD

---

## Quick Reference: What Interviewers Look For

| Level | Expectation |
|-------|-------------|
| L5/E5 | Explain methods intuitively, identify assumptions |
| L6/E6 | Derive key results, discuss violations and fixes |
| L7+ | Design studies, critique approaches, suggest alternatives |

## Common Interview Traps

1. **"Adding more controls reduces bias"** → FALSE (bad controls exist)
2. **"Propensity score matching is always better than regression"** → FALSE
3. **"IV gives the average treatment effect"** → FALSE (it's LATE)
4. **"Pre-trends validate parallel trends"** → MISLEADING (necessary but not sufficient)
5. **"RDD is like a local RCT"** → NUANCED (continuity ≠ randomization)

---

## After the 2 Weeks

If you have more time:
- Path 1 (Foundations): Deepen understanding with Monte Carlo simulations
- Path 3 (HTE): Learn causal forests and policy optimization
- Read primary sources: Angrist & Pischke, Imbens & Rubin
