# Chapter Index

Detailed summaries for all 102 notebooks across 31 chapter directories.

**[CORE]** = Chapters with highest mathematical rigor (full proofs, interview appendices)

---

## Part I: Foundations

### Chapter 1: Introduction to Causality

**Notebooks**: 3 | **Est. Time**: ~1.5 hours | **Prerequisites**: None

| Notebook | Title | Interview Qs |
|----------|-------|--------------|
| 01 | Potential Outcomes | 2 Basic, 1 Advanced |
| 02 | Association vs. Causation | 2 Basic, 1 Advanced |
| 03 | Confounding Example | 1 Basic, 1 Advanced |

**Key Concepts**: Potential outcomes Y(0)/Y(1), ITE, ATE, ATT, counterfactuals, fundamental problem of causal inference

**Data**: `enem_scores.csv` (simulated tablet study)

---

### Chapter 2: Randomized Experiments

**Notebooks**: 3 | **Est. Time**: ~1.5 hours | **Prerequisites**: Ch 1

| Notebook | Title | Interview Qs |
|----------|-------|--------------|
| 01 | RCT Gold Standard | 2 Basic, 1 Advanced |
| 02 | Ideal Experiment | 1 Basic, 2 Advanced |
| 03 | RCT Analysis | 2 Basic, 1 Advanced |

**Key Concepts**: Independence (Y₀,Y₁) ⊥ T, randomization, assignment mechanisms, compliance

**Data**: `online_classroom.csv` (323 students, education RCT)

---

### Chapter 3: Stats Review

**Notebooks**: 4 | **Est. Time**: ~2 hours | **Prerequisites**: None (reference)

| Notebook | Title | Interview Qs |
|----------|-------|--------------|
| 01 | Standard Error | 2 Basic |
| 02 | Confidence Intervals | 1 Basic, 1 Advanced |
| 03 | Hypothesis Testing | 2 Basic, 1 Advanced |
| 04 | Practical Significance | 1 Basic, 1 Advanced |

**Key Concepts**: SE = σ/√n, CI interpretation, p-values, multiple testing, A/B framework

**Data**: `enem_scores.csv` (school size paradox demonstration)

---

### Chapter 4: Graphical Causal Models

**Notebooks**: 4 | **Est. Time**: ~2 hours | **Prerequisites**: Ch 1

| Notebook | Title | Interview Qs |
|----------|-------|--------------|
| 01 | DAG Basics | 2 Basic, 1 Advanced |
| 02 | Confounding | 2 Basic, 2 Advanced |
| 03 | Selection Bias | 1 Basic, 2 Advanced |
| 04 | Good/Bad Controls | 2 Basic, 2 Advanced |

**Key Concepts**: DAGs, d-separation, forks/chains/colliders, backdoor criterion, front-door criterion

**Data**: Conceptual (DAG exercises)

---

## Part I: Regression Methods

### Chapter 5: Linear Regression [CORE]

**Notebooks**: 4 | **Est. Time**: ~2.5 hours | **Prerequisites**: Ch 3, 4

| Notebook | Title | Interview Qs |
|----------|-------|--------------|
| 01 | All You Need is Regression | 2 Basic, 2 Advanced |
| 02 | Regression Theory | 2 Basic, 3 Advanced |
| 03 | Regression on Non-Random Data | 2 Basic, 2 Advanced |
| 04 | Omitted Variable Bias | 2 Basic, 3 Advanced |

**Key Concepts**: OLS, FWL theorem (full proof), residual maker M_X, conditional expectation, OVB formula

**Why Core**: FWL is foundational for DML; OVB formula appears in every interview

**Data**: `online_classroom.csv`, `wage.csv`

**Reference**: [causal_inference_mastery](https://github.com/brandonmbehring-dev/causal_inference_mastery) — `src/causal_inference/rct/estimators_regression.py`

---

### Chapter 5b: Introduction to Double ML

**Notebooks**: 5 | **Est. Time**: ~3 hours | **Prerequisites**: Ch 5

| Notebook | Title | Interview Qs |
|----------|-------|--------------|
| 01 | From FWL to Robinson | 1 Basic, 2 Advanced |
| 02 | Neyman Orthogonality | 1 Basic, 3 Advanced |
| 03 | Regularization Problem | 2 Basic, 2 Advanced |
| 04 | Cross-Fitting | 2 Basic, 2 Advanced |
| 05 | DML Implementation | 2 Basic, 4 Advanced |

**Key Concepts**: Robinson transformation, Neyman orthogonality (Definition 2.1), n^{-1/4} rates, K-fold cross-fitting, influence functions

**Data**: `ice_cream_sales.csv`, simulated DGPs

**Reference**: [causal_inference_mastery](https://github.com/brandonmbehring-dev/causal_inference_mastery) — `src/causal_inference/cate/dml.py`

---

### Chapter 6: Grouped/Dummy Regression

**Notebooks**: 3 | **Est. Time**: ~1.5 hours | **Prerequisites**: Ch 5

| Notebook | Title | Interview Qs |
|----------|-------|--------------|
| 01 | Grouped Regression | 2 Basic, 1 Advanced |
| 02 | Dummy Variables | 2 Basic, 1 Advanced |
| 03 | Interactions & Nonparametric | 1 Basic, 2 Advanced |

**Key Concepts**: WLS, heteroskedasticity, HC0-HC3 variance, categorical encoding, interaction effects

**Data**: `enem_scores.csv`, `wage.csv`

---

### Chapter 7: Beyond Confounders

**Notebooks**: 4 | **Est. Time**: ~2 hours | **Prerequisites**: Ch 4, 5

| Notebook | Title | Interview Qs |
|----------|-------|--------------|
| 01 | Good Controls | 2 Basic, 1 Advanced |
| 02 | Bad Controls & Colliders | 2 Basic, 2 Advanced |
| 03 | Selection Bias & Mediators | 1 Basic, 2 Advanced |
| 04 | COP Decomposition | 1 Basic, 2 Advanced |

**Key Concepts**: Variance reduction, SE ∝ 1/√Var(T̃), collider bias, mediation, COP decomposition

**Data**: `collections_email.csv`, `hospital_treatment.csv`

---

## Part I: Instrumental Variables

### Chapter 8: Instrumental Variables [CORE]

**Notebooks**: 4 | **Est. Time**: ~2.5 hours | **Prerequisites**: Ch 5

| Notebook | Title | Interview Qs |
|----------|-------|--------------|
| 01 | IV Intuition | 2 Basic, 2 Advanced |
| 02 | Two-Stage Least Squares | 2 Basic, 3 Advanced |
| 03 | Multiple Instruments | 1 Basic, 2 Advanced |
| 04 | Weak Instruments | 2 Basic, 3 Advanced |

**Key Concepts**: Exclusion restriction, relevance, 2SLS mechanics, Sargan test, Stock-Yogo, F > 10 rule, LIML

**Why Core**: IV is fundamental; weak instrument detection critical for interviews

**Data**: `ak91.csv` (Angrist-Krueger quarter-of-birth)

**Reference**: [causal_inference_mastery](https://github.com/brandonmbehring-dev/causal_inference_mastery) — `src/causal_inference/iv/two_stage_least_squares.py`

---

### Chapter 9: Non-Compliance & LATE

**Notebooks**: 4 | **Est. Time**: ~2 hours | **Prerequisites**: Ch 8

| Notebook | Title | Interview Qs |
|----------|-------|--------------|
| 01 | Compliance Types | 2 Basic, 1 Advanced |
| 02 | LATE vs. ATE | 2 Basic, 2 Advanced |
| 03 | Wald & 2SLS | 2 Basic, 2 Advanced |
| 04 | Compliance Diagnostics | 1 Basic, 2 Advanced |

**Key Concepts**: Principal strata (compliers, always/never-takers, defiers), LATE, monotonicity, Wald estimator

**Data**: `app_engagement_push.csv` (push notification RCT)

---

## Part I: Matching & Weighting

### Chapter 10: Matching

**Notebooks**: 4 | **Est. Time**: ~2 hours | **Prerequisites**: Ch 5, 7

| Notebook | Title | Interview Qs |
|----------|-------|--------------|
| 01 | Matching Intuition | 2 Basic, 1 Advanced |
| 02 | Distance Metrics | 2 Basic, 2 Advanced |
| 03 | KNN & Bias | 1 Basic, 2 Advanced |
| 04 | Matching vs. Regression | 2 Basic, 1 Advanced |

**Key Concepts**: Exact matching, Mahalanobis distance, curse of dimensionality, bias correction, common support

**Data**: `trainees.csv`, `medicine_impact_recovery.csv`

**Reference**: [causal_inference_mastery](https://github.com/brandonmbehring-dev/causal_inference_mastery) — `src/causal_inference/psm/matching.py`

---

### Chapter 11: Propensity Score

**Notebooks**: 4 | **Est. Time**: ~2.5 hours | **Prerequisites**: Ch 10

| Notebook | Title | Interview Qs |
|----------|-------|--------------|
| 01 | Balancing Score | 2 Basic, 2 Advanced |
| 02 | IPTW | 2 Basic, 2 Advanced |
| 03 | PS Matching | 1 Basic, 2 Advanced |
| 04 | PS Diagnostics | 2 Basic, 2 Advanced |

**Key Concepts**: e(X) = P(T=1|X), balancing property, IPTW, stabilized weights, positivity, overlap

**Data**: `learning_mindset.csv` (10,391 students)

**Reference**: [causal_inference_mastery](https://github.com/brandonmbehring-dev/causal_inference_mastery) — `src/causal_inference/psm/propensity.py`

---

### Chapter 12: Doubly Robust

**Notebooks**: 3 | **Est. Time**: ~1.5 hours | **Prerequisites**: Ch 10, 11

| Notebook | Title | Interview Qs |
|----------|-------|--------------|
| 01 | DR Estimator | 2 Basic, 2 Advanced |
| 02 | Double Robustness | 2 Basic, 2 Advanced |
| 03 | DR vs. Alternatives | 1 Basic, 2 Advanced |

**Key Concepts**: AIPW formula, double robustness property (only ONE model needs to be correct), efficiency

**Data**: `learning_mindset.csv`

**Reference**: [causal_inference_mastery](https://github.com/brandonmbehring-dev/causal_inference_mastery) — `src/causal_inference/observational/doubly_robust.py`

---

## Part I: Panel Methods

### Chapter 13: Difference-in-Differences [CORE]

**Notebooks**: 3 | **Est. Time**: ~2 hours | **Prerequisites**: Ch 5

| Notebook | Title | Interview Qs |
|----------|-------|--------------|
| 01 | DiD Intuition | 2 Basic, 2 Advanced |
| 02 | DiD Estimation | 2 Basic, 3 Advanced |
| 03 | Parallel Trends | 2 Basic, 3 Advanced |

**Key Concepts**: TWFE, parallel trends, before-after bias, treatment-control bias, event studies, pre-trends

**Why Core**: DiD is ubiquitous; TWFE bias is critical for interviews

**Data**: `billboard_impact.csv` (marketing campaign)

**Reference**: [causal_inference_mastery](https://github.com/brandonmbehring-dev/causal_inference_mastery) — `src/causal_inference/did/classic_did.py`

---

### Chapter 14: Panel Data & Fixed Effects

**Notebooks**: 4 | **Est. Time**: ~2 hours | **Prerequisites**: Ch 13

| Notebook | Title | Interview Qs |
|----------|-------|--------------|
| 01 | Panel Structure | 2 Basic, 1 Advanced |
| 02 | Fixed Effects | 2 Basic, 2 Advanced |
| 03 | Entity & Time Effects | 2 Basic, 2 Advanced |
| 04 | FE Limitations | 1 Basic, 2 Advanced |

**Key Concepts**: Within transformation, two-way FE, clustered SEs, time-invariant confounders

**Data**: `wage_panel` (linearmodels, 4,360 rows)

---

### Chapter 15: Synthetic Control

**Notebooks**: 4 | **Est. Time**: ~2.5 hours | **Prerequisites**: Ch 13

| Notebook | Title | Interview Qs |
|----------|-------|--------------|
| 01 | Synthetic Concept | 2 Basic, 1 Advanced |
| 02 | Optimization | 1 Basic, 3 Advanced |
| 03 | Treatment Effect | 2 Basic, 1 Advanced |
| 04 | Inference | 2 Basic, 2 Advanced |

**Key Concepts**: Synthetic counterfactual, convex optimization, pre-treatment fit, Fisher's exact test, placebo

**Data**: `smoking.csv` (Proposition 99, 39 states × 31 years)

**Reference**: [causal_inference_mastery](https://github.com/brandonmbehring-dev/causal_inference_mastery) — `src/causal_inference/scm/synthetic_control.py`

---

### Chapter 16: Regression Discontinuity [CORE]

**Notebooks**: 3 | **Est. Time**: ~2 hours | **Prerequisites**: Ch 5

| Notebook | Title | Interview Qs |
|----------|-------|--------------|
| 01 | RDD Intuition | 2 Basic, 2 Advanced |
| 02 | RDD Estimation | 2 Basic, 3 Advanced |
| 03 | Fuzzy RDD | 2 Basic, 3 Advanced |

**Key Concepts**: Local randomization, LATE at cutoff, triangular kernel, bandwidth selection, fuzzy RDD as IV, McCrary test

**Why Core**: RDD is interview favorite; bandwidth selection is tricky

**Data**: `drinking.csv` (MLDA mortality), `sheepskin.csv` (diploma effect)

**Reference**: [causal_inference_mastery](https://github.com/brandonmbehring-dev/causal_inference_mastery) — `src/causal_inference/rdd/sharp_rdd.py`, `src/causal_inference/rdd/mccrary.py`

---

## Part II: ML for Causal Inference

### Chapter 17: Predictive Models 101

**Notebooks**: 3 | **Est. Time**: ~1.5 hours | **Prerequisites**: Ch 5

| Notebook | Title | Interview Qs |
|----------|-------|--------------|
| 01 | Prediction Problem | 2 Basic, 1 Advanced |
| 02 | Model Evaluation | 2 Basic, 1 Advanced |
| 03 | Predictions to Policies | 1 Basic, 2 Advanced |

**Key Concepts**: ML fundamentals, prediction ≠ causation, cross-validation, policy thresholds

**Data**: `customer_transactions.csv`, `customer_features.csv`

---

### Chapter 18: Heterogeneous Treatment Effects

**Notebooks**: 3 | **Est. Time**: ~2 hours | **Prerequisites**: Ch 17

| Notebook | Title | Interview Qs |
|----------|-------|--------------|
| 01 | ATE to CATE | 2 Basic, 2 Advanced |
| 02 | Estimating Heterogeneity | 2 Basic, 2 Advanced |
| 03 | Causal vs. Predictive | 2 Basic, 2 Advanced |

**Key Concepts**: CATE τ(x), individual treatment effects, interaction terms, effect heterogeneity

**Data**: `ice_cream_sales_rnd.csv`

**Reference**: [causal_inference_mastery](https://github.com/brandonmbehring-dev/causal_inference_mastery) — `src/causal_inference/cate/`

---

### Chapter 19: Evaluating Causal Models

**Notebooks**: 3 | **Est. Time**: ~2 hours | **Prerequisites**: Ch 18

| Notebook | Title | Interview Qs |
|----------|-------|--------------|
| 01 | Evaluation Challenge | 2 Basic, 1 Advanced |
| 02 | Sensitivity by Band | 2 Basic, 2 Advanced |
| 03 | Cumulative Gain | 2 Basic, 2 Advanced |

**Key Concepts**: Unobservable individual effects, sensitivity curves, cumulative gain, CIs for CATE

**Data**: `ice_cream_sales.csv` (confounded), `ice_cream_sales_rnd.csv` (evaluation)

---

### Chapter 20: F-Learner

**Notebooks**: 3 | **Est. Time**: ~1.5 hours | **Prerequisites**: Ch 18

| Notebook | Title | Interview Qs |
|----------|-------|--------------|
| 01 | Target Transformation | 2 Basic, 2 Advanced |
| 02 | Continuous Treatment | 1 Basic, 2 Advanced |
| 03 | F-Learner Limitations | 2 Basic, 2 Advanced |

**Key Concepts**: Y* = Y(T-e)/(e(1-e)), binary and continuous treatments, variance issues

**Data**: `invest_email_rnd.csv`, `ice_cream_sales_rnd.csv`

---

### Chapter 21: Meta-Learners

**Notebooks**: 4 | **Est. Time**: ~2.5 hours | **Prerequisites**: Ch 18, 20

| Notebook | Title | Interview Qs |
|----------|-------|--------------|
| 01 | S & T Learner | 2 Basic, 2 Advanced |
| 02 | X-Learner | 2 Basic, 2 Advanced |
| 03 | Meta-Learner Comparison | 2 Basic, 2 Advanced |
| 04 | R-Learner Intro | 2 Basic, 3 Advanced |

**Key Concepts**: S-learner (single model), T-learner (two models), X-learner (two-stage), R-learner (orthogonal)

**Data**: `invest_email_biased.csv` (train), `invest_email_rnd.csv` (eval)

**Reference**: [causal_inference_mastery](https://github.com/brandonmbehring-dev/causal_inference_mastery) — `src/causal_inference/cate/meta_learners.py`

---

### Chapter 22: Debiased ML [CORE]

**Notebooks**: 3 | **Est. Time**: ~2 hours | **Prerequisites**: Ch 5b, 21

| Notebook | Title | Interview Qs |
|----------|-------|--------------|
| 01 | DML Intuition | 2 Basic, 2 Advanced |
| 02 | DML Estimation | 2 Basic, 3 Advanced |
| 03 | DML Advanced | 2 Basic, 3 Advanced |

**Key Concepts**: Full DML algorithm, cross-fitting, EconML implementation, CATE with CausalForestDML

**Why Core**: DML is state-of-the-art; expected in senior interviews

**Data**: `ice_cream_sales.csv`

**Reference**: [causal_inference_mastery](https://github.com/brandonmbehring-dev/causal_inference_mastery) — `src/causal_inference/cate/dml.py`

---

### Chapter 23: Challenges with Heterogeneity

**Notebooks**: 2 | **Est. Time**: ~1 hour | **Prerequisites**: Ch 18, 21

| Notebook | Title | Interview Qs |
|----------|-------|--------------|
| 01 | Binary Outcomes | 2 Basic, 1 Advanced |
| 02 | Nonlinear Treatment | 1 Basic, 2 Advanced |

**Key Concepts**: Logistic S-curve effects, baseline targeting, pricing elasticity, linearization

**Data**: Simulated conversion nudge, Netflix pricing

---

## Part II: Advanced DiD

### Chapter 24: The DiD Saga

**Notebooks**: 3 | **Est. Time**: ~2 hours | **Prerequisites**: Ch 13, 14

| Notebook | Title | Interview Qs |
|----------|-------|--------------|
| 01 | TWFE Fundamentals | 2 Basic, 2 Advanced |
| 02 | TWFE Bias | 2 Basic, 3 Advanced |
| 03 | Flexible TWFE | 2 Basic, 2 Advanced |

**Key Concepts**: TWFE mechanics, time heterogeneity bias, Goodman-Bacon decomposition, cohort×date interactions

**Data**: Simulated app rollout (100 cities × 92 days, 3 cohorts)

**Reference**: [causal_inference_mastery](https://github.com/brandonmbehring-dev/causal_inference_mastery) — `src/causal_inference/did/callaway_santanna.py`

---

### Chapter 25: Synthetic DiD

**Notebooks**: 3 | **Est. Time**: ~2 hours | **Prerequisites**: Ch 15, 24

| Notebook | Title | Interview Qs |
|----------|-------|--------------|
| 01 | SDID Foundations | 2 Basic, 2 Advanced |
| 02 | SDID Estimation | 2 Basic, 2 Advanced |
| 03 | Staggered Inference | 2 Basic, 2 Advanced |

**Key Concepts**: DiD + SC combination, unit/time weights (cvxpy), placebo variance, staggered cohorts

**Data**: `smoking.csv`, staggered simulation

---

## Appendices

### Appendix A1: Conformal SCM

**Notebooks**: 2 | **Est. Time**: ~1.5 hours | **Prerequisites**: Ch 15

| Notebook | Title | Interview Qs |
|----------|-------|--------------|
| 01 | Conformal Foundations | 2 Basic, 2 Advanced |
| 02 | SCM Confidence Intervals | 2 Basic, 2 Advanced |

**Key Concepts**: Conformal prediction, exchangeability, block permutation, per-period CIs, test inversion

**Data**: `smoking.csv` (Proposition 99)

---

### Appendix A2: Orthogonalization

**Notebooks**: 3 | **Est. Time**: ~2 hours | **Prerequisites**: Ch 5

| Notebook | Title | Interview Qs |
|----------|-------|--------------|
| 01 | FWL Refresher | 2 Basic, 1 Advanced |
| 02 | ML Residualization | 2 Basic, 2 Advanced |
| 03 | Cross-Fitting | 2 Basic, 2 Advanced |

**Key Concepts**: FWL review, ML-based orthogonalization, t*/y* construction, overfitting prevention

**Data**: `ice_cream_sales.csv`

---

### Appendix A3: PS Debiasing

**Notebooks**: 2 | **Est. Time**: ~1 hour | **Prerequisites**: Ch 11

| Notebook | Title | Interview Qs |
|----------|-------|--------------|
| 01 | IPTW Mechanics | 2 Basic, 2 Advanced |
| 02 | Practical Issues | 2 Basic, 2 Advanced |

**Key Concepts**: Horvitz-Thompson vs. Hajek, stored vs. estimated PS, positivity violations, effective sample size

**Data**: `invest_email.csv`

---

### Appendix A4: When Prediction Fails

**Notebooks**: 3 | **Est. Time**: ~1.5 hours | **Prerequisites**: Ch 17

| Notebook | Title | Interview Qs |
|----------|-------|--------------|
| 01 | Hammer Pitfall | 2 Basic, 2 Advanced |
| 02 | Elasticity Flattening | 2 Basic, 2 Advanced |
| 03 | When Prediction Helps | 1 Basic, 2 Advanced |

**Key Concepts**: Y vs. dY/dT confusion, ML partitioning flattens curves, monotonic elasticity cases

**Data**: Simulated coupon, pricing data

---

### Appendix A5: Causal Metrics

**Notebooks**: 2 | **Est. Time**: ~1 hour | **Prerequisites**: Ch 19

| Notebook | Title | Interview Qs |
|----------|-------|--------------|
| 01 | R² Failures | 2 Basic, 2 Advanced |
| 02 | Residualized Evaluation | 2 Basic, 2 Advanced |

**Key Concepts**: Why R² fails for CATE (g(X) vs. f(T,W)), cumulative elasticity curves, nuisance removal

**Data**: Simulated causal models

---

## Summary Statistics

| Category | Count |
|----------|-------|
| Total Notebooks | 102 |
| Total Chapters | 31 (25 core + 5 appendix + ch5b) |
| CORE Chapters | 5 (Ch 5, 8, 13, 16, 22) |
| Estimated Total Time | ~50 hours |
| Interview Questions | ~300+ |

---

## Navigation Tips

1. **New to causal inference?** Start with Ch 1-4 (Foundations)
2. **Interview prep?** Focus on [CORE] chapters: 5, 8, 13, 16, 22
3. **ML background?** Jump to Part II (Ch 17-25)
4. **Panel data focus?** Ch 13-15, 24-25, A1
