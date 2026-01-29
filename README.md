# Causal Inference Educational Materials

Combined repository containing Matheus Facure's **Causal Inference for the Brave and True** plus **102 augmented notebooks** with enhanced pedagogical structure.

## Quick Start

```bash
# Install augmented package
cd augmented
pip install -e ".[dev]"

# Run tests
pytest tests/ -v

# Start learning
jupyter lab notebooks/01_introduction_to_causality/
```

## Contents

### facure_original/
The original 30-chapter textbook by Matheus Facure:
- Comprehensive causal inference curriculum
- Real-world datasets and examples
- MIT Licensed

### augmented/
102 enhanced notebooks following a 6-section structure:
1. **Intuition** — Conceptual explanation
2. **Formal** — Mathematical formulation
3. **Numeric** — Computational examples
4. **Implementation** — Code walkthrough
5. **Interview** — Practice questions
6. **References** — Further reading

## Learning Paths

See `augmented/docs/LEARNING_PATHS.md` for guided sequences:
- **Foundations Track** — Core concepts (Chapters 1-5)
- **Interview Fast Track** — Key methods for interviews
- **HTE Deep Dive** — Treatment effect heterogeneity
- **Panel Methods** — DiD, Fixed Effects, SCM

## Datasets

21 datasets covering:
- RCTs (invest_email, online_classroom)
- Observational studies (wage, smoking)
- RDD examples (drinking)
- Panel data (trainees)

See `augmented/docs/DATA_DICTIONARY.md` for full schemas.

## Testing

```bash
pytest augmented/tests/ -v              # All tests
pytest augmented/tests/ -k "core" -v    # Core chapters only
```

## Companion Repository

Production-grade implementations: [causal_inference_mastery](https://github.com/brandonmbehring-dev/causal_inference_mastery)

## Attribution

Based on Matheus Facure's [Causal Inference for the Brave and True](https://matheusfacure.github.io/python-causality-handbook/).

## License

MIT License — See [LICENSE](LICENSE)
