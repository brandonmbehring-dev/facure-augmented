# facure_augment

**Augmented Causal Inference Notebooks** — 102 Jupyter notebooks with formal proofs, interview questions, and Tufte-styled visualizations.

Based on Matheus Facure's *[Causal Inference for the Brave and True](https://matheusfacure.github.io/python-causality-handbook/)*, enhanced with:
- **Full mathematical rigor** — Complete proofs, formal assumptions, LaTeX derivations
- **Interview preparation** — 300+ questions grouped by difficulty (Basic/Advanced)
- **Production code** — Links to `causal_inference_mastery` implementations
- **Tufte-styled plots** — Research-grade visualizations

---

## Quick Start

```bash
# Install
cd facure_augment
pip install -e .

# Run a notebook
jupyter lab notebooks/05_linear_regression/01_all_you_need_is_regression.ipynb
```

---

## What This Is

Each notebook follows a 6-section structure:

1. **Intuition** — Facure's original narrative preserved
2. **Formal Treatment** — Theorems, proofs, and assumptions
3. **Numeric Demonstration** — Worked examples with real data
4. **Implementation** — Production code references
5. **Interview Appendix** — Practice questions with solutions
6. **References** — Footnote-style citations

**Core chapters** (5, 8, 13, 16, 22) have the highest rigor with full proofs. Other chapters emphasize intuition with key formulas.

---

## Chapter Overview

| Ch | Topic | Notebooks | Est. Time | Key Methods |
|----|-------|-----------|-----------|-------------|
| **Foundations** |
| 01 | Introduction to Causality | 3 | ~1.5h | Potential outcomes, ATE, ATT |
| 02 | Randomized Experiments | 3 | ~1.5h | RCT analysis, randomization |
| 03 | Stats Review | 4 | ~2h | SE, CI, hypothesis testing |
| 04 | Graphical Causal Models | 4 | ~2h | DAGs, d-separation, backdoor |
| **Regression Methods** |
| 05 | Linear Regression [CORE] | 4 | ~2.5h | FWL theorem, OLS, OVB formula |
| 05b | Intro to Double ML | 5 | ~3h | Neyman orthogonality, cross-fitting |
| 06 | Grouped/Dummy Regression | 3 | ~1.5h | WLS, interactions, HC variance |
| 07 | Beyond Confounders | 4 | ~2h | Good/bad controls, colliders |
| **Instrumental Variables** |
| 08 | Instrumental Variables [CORE] | 4 | ~2.5h | 2SLS, LIML, weak instruments |
| 09 | Non-Compliance & LATE | 4 | ~2h | Principal strata, Wald estimator |
| **Matching & Weighting** |
| 10 | Matching | 4 | ~2h | KNN, Mahalanobis, bias correction |
| 11 | Propensity Score | 4 | ~2.5h | IPTW, balancing, diagnostics |
| 12 | Doubly Robust | 3 | ~1.5h | AIPW, double robustness |
| **Panel Methods** |
| 13 | Difference-in-Differences [CORE] | 3 | ~2h | TWFE, parallel trends |
| 14 | Panel Data & Fixed Effects | 4 | ~2h | Entity/time FE, within transform |
| 15 | Synthetic Control | 4 | ~2.5h | SCM optimization, inference |
| 16 | Regression Discontinuity [CORE] | 3 | ~2h | Sharp/fuzzy RDD, McCrary |
| **ML for Causal Inference** |
| 17 | Predictive Models 101 | 3 | ~1.5h | ML fundamentals, policies |
| 18 | Heterogeneous Effects | 3 | ~2h | ATE to CATE, heterogeneity |
| 19 | Evaluating Causal Models | 3 | ~2h | Cumulative gain, sensitivity |
| 20 | F-Learner | 3 | ~1.5h | Target transformation |
| 21 | Meta-Learners | 4 | ~2.5h | S/T/X/R-learners |
| 22 | Debiased ML [CORE] | 3 | ~2h | DML algorithm, R-learner |
| 23 | Challenges with Heterogeneity | 2 | ~1h | Binary outcomes, nonlinearity |
| **Advanced DiD** |
| 24 | The DiD Saga | 3 | ~2h | TWFE bias, Goodman-Bacon |
| 25 | Synthetic DiD | 3 | ~2h | SDID, staggered adoption |
| **Appendices** |
| A1 | Conformal SCM | 2 | ~1.5h | Block permutation, CIs |
| A2 | Orthogonalization | 3 | ~2h | FWL refresher, ML residuals |
| A3 | PS Debiasing | 2 | ~1h | IPTW mechanics, positivity |
| A4 | When Prediction Fails | 3 | ~1.5h | ML pitfalls, elasticity |
| A5 | Causal Metrics | 2 | ~1h | R² failures, evaluation |

**Total**: 102 notebooks | ~50 hours of content

---

## Learning Paths

See [docs/LEARNING_PATHS.md](docs/LEARNING_PATHS.md) for detailed guides.

### Foundations First (4-6 weeks)
For systematic learners building from basics.
```
Chapters: 01 → 02 → 03 → 04 → 05 → 06 → 07 → 10 → 11 → 12
```

### Interview Fast Track (2 weeks)
For interview prep, focusing on core chapters.
```
Chapters: 05 → 08 → 13 → 16 → 22
Focus: Interview appendices in each chapter
```

### Advanced HTE Deep Dive (3 weeks)
For CATE and heterogeneous effects specialists.
```
Chapters: 17 → 18 → 19 → 20 → 21 → 22 → 23 → A4 → A5
```

### Panel Methods Specialist (2 weeks)
For DiD, synthetic control, and panel data.
```
Chapters: 13 → 14 → 15 → 24 → 25 → A1
```

---

## Data Included

See [docs/DATA_DICTIONARY.md](docs/DATA_DICTIONARY.md) for full schemas.

| Dataset | Rows | Chapter | Domain |
|---------|------|---------|--------|
| online_classroom.csv | 323 | 05 | Education RCT |
| billboard_impact.csv | 4,600 | 13 | Marketing DiD |
| ak91.csv | 329,509 | 08 | Labor Economics IV |
| learning_mindset.csv | 10,391 | 11-12 | Education PS/DR |
| smoking.csv | 1,209 | 15, 25 | Health SCM |
| ice_cream_sales.csv | 10,000 | 22 | Pricing DML |
| invest_email*.csv | 5-15K | 20-21 | Marketing CATE |
| ... | | | |

**21 datasets** covering RCT, observational, panel, and time-series designs.

---

## Installation

```bash
# Clone the repository
git clone https://github.com/your-repo/causal_inference_mastery.git
cd causal_inference_mastery/facure_augment

# Install in development mode
pip install -e .

# Or with all dependencies
pip install -e ".[dev]"
```

**Requirements**: Python 3.10+, numpy, pandas, statsmodels, scikit-learn, matplotlib, linearmodels

---

## Project Structure

```
facure_augment/
├── README.md                 # This file
├── docs/
│   ├── CHAPTER_INDEX.md      # Detailed chapter summaries
│   ├── LEARNING_PATHS.md     # Guided study sequences
│   └── DATA_DICTIONARY.md    # Dataset specifications
├── notebooks/
│   ├── 01_introduction_to_causality/
│   ├── ...
│   └── A5_causal_metrics/
├── common.py                 # Shared imports and utilities
├── viz/tufte.py              # Tufte-style plotting
├── data/facure/              # 21 CSV datasets
└── tests/                    # Notebook execution tests
```

---

## Testing

```bash
# Run all notebook tests
pytest facure_augment/tests/test_execution.py -v --no-cov

# Test specific chapter
pytest facure_augment/tests/test_execution.py -k "05_linear" -v
```

**306 tests** validate that all 102 notebooks execute without errors.

---

## Links

- **Original Book**: [Causal Inference for the Brave and True](https://matheusfacure.github.io/python-causality-handbook/)
- **Production Code**: `../src/causal_inference/` (25 method families)
- **Interview Prep**: `../interview_prep_series/vol2_causal_inference/`
- **Research KB**: MCP-connected knowledge base with citations

---

## Citation

If you use these materials, please cite:

```bibtex
@misc{facure_augment2026,
  author = {Behring, Brandon},
  title = {facure_augment: Augmented Causal Inference Notebooks},
  year = {2026},
  note = {Based on Facure's Causal Inference for the Brave and True}
}
```

---

## License

Educational use. Original content from Facure's book is subject to its license.
