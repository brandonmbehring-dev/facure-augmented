# CLAUDE.md - Facure Educational Materials

This file provides guidance to Claude Code when working in this repository.

---

## Shared Foundation (Hub Reference)

**This project uses shared patterns from lever_of_archimedes**:

See: `~/Claude/lever_of_archimedes/patterns/` for:
- `git.md` - Commit format and workflow
- `sessions.md` - Session workflow (CURRENT_WORK.md, ROADMAP.md)
- `burst.md` - Brandon Burst™ ADHD methodology
- `style/python_style.yaml` - Black 100-char, strict mypy
- `style/coding_philosophy.yaml` - Fail-fast, simplicity, immutability

**Core principles** (from hub):
1. NEVER fail silently - explicit errors always
2. Simplicity over complexity - 20-50 line functions
3. Immutability by default
4. Fail fast with diagnostics

---

## Project Overview

Combined causal inference educational repository:

| Component | Content | Purpose |
|-----------|---------|---------|
| `facure_original/` | 30 original notebooks | Matheus Facure's textbook |
| `augmented/` | 102 enhanced notebooks | 6-section pedagogical structure |

### Augmented Notebook Structure

Each topic follows 6 sections:
1. **Intuition** — Conceptual explanation with visualizations
2. **Formal** — Mathematical formulation (LaTeX)
3. **Numeric** — Computational examples
4. **Implementation** — Code walkthrough
5. **Interview** — Practice questions (Q1, Q2, ...)
6. **References** — Citations and further reading

---

## Quick Reference Commands

```bash
# Install augmented package
cd augmented && pip install -e ".[dev]"

# Run all tests
pytest augmented/tests/ -v

# Run specific chapter
pytest augmented/tests/test_execution.py -k "05_linear" -v

# Run core chapters only (5, 8, 13, 16, 22)
pytest augmented/tests/test_execution.py -k "core" -v

# Verify imports
python -c "from augmented.common import *; print('✓ OK')"

# Verify data loading
python -c "from augmented.common import load_facure_data; print(load_facure_data('invest_email.csv').shape)"
```

---

## Project Structure

```
facure_augment/
├── .claude/                        # Claude Code configuration
│   ├── settings.json               # Permissions, hooks
│   └── skills/                     # Custom skills
├── .mcp.json                       # research-kb MCP server
├── CLAUDE.md                       # This file
├── CURRENT_WORK.md                 # 30-second context
├── ROADMAP.md                      # Master plan
│
├── facure_original/                # Original Facure book (30 notebooks)
│   └── causal-inference-for-the-brave-and-true/
│       ├── NN-Topic.ipynb          # Original notebooks
│       └── data/                   # Original datasets
│
└── augmented/                      # Enhanced notebooks (102)
    ├── pyproject.toml              # Package config
    ├── common.py                   # Shared utilities
    ├── notebooks/                  # 31 chapter directories
    │   ├── 01_introduction_to_causality/
    │   ├── 02_randomised_experiments/
    │   └── ...
    ├── data/facure/                # Datasets (21 CSV, ~13MB)
    ├── docs/                       # Documentation
    │   ├── CHAPTER_INDEX.md        # Detailed chapter guide
    │   ├── DATA_DICTIONARY.md      # Dataset schemas
    │   └── LEARNING_PATHS.md       # Study sequences
    ├── tests/                      # pytest suite
    └── viz/tufte.py                # Tufte-style visualizations
```

---

## Testing Standards

### Notebook Validation
- **All 102 notebooks must execute** without errors
- **Core chapters** (5, 8, 13, 16, 22): Extra scrutiny
- **Interview questions**: Regex validation for Q1, Q2, ... format

### Test Commands
```bash
pytest augmented/tests/test_execution.py -v          # Full execution
pytest augmented/tests/test_schema.py -v             # Schema validation
pytest augmented/tests/test_coverage.py -v           # Coverage checks
```

### Test Markers
- `@pytest.mark.slow` — Long-running notebook execution
- `@pytest.mark.core` — Core chapter tests

---

## Code Style

### Python
- **Formatter**: Black with 100-character lines
- **Type hints**: Required everywhere
- **Docstrings**: NumPy style
- **Error handling**: Fail fast with diagnostics

### Notebooks
- **Clear markdown** cells explaining each step
- **Tufte visualizations** via `from augmented.common import *`
- **Interview questions** marked with **Q1:**, **Q2:**, etc.

---

## Data Management

### Locations
- **Primary**: `augmented/data/facure/` (21 CSV files)
- **Fallback**: `facure_original/causal-inference-for-the-brave-and-true/data/`

### Loading Data
```python
from augmented.common import load_facure_data
df = load_facure_data("invest_email.csv")
```

**Note**: Package renamed from `facure_augment` to `augmented` for cleaner naming.

### Datasets Available
See `augmented/docs/DATA_DICTIONARY.md` for full schemas:
- `invest_email.csv` — Email investment RCT
- `online_classroom.csv` — Online learning
- `wage.csv` — Wage data (Mincer equation)
- `drinking.csv` — Minimum legal drinking age RDD
- ... (21 total)

---

## MCP Tools Available

This project connects to `research-kb` for causal inference literature:

| Tool | Purpose | Example |
|------|---------|---------|
| `research_kb_search` | Search papers/textbooks | `"difference-in-differences"` |
| `research_kb_get_concept` | Get method definition | `"instrumental variables"` |
| `research_kb_list_sources` | Browse bibliography | Find Angrist papers |

---

## Session Workflow

1. **Start**: Check `CURRENT_WORK.md` for context
2. **Plan**: For tasks >1hr, create `docs/plans/active/TASK_DATE.md`
3. **Implement**: Test-first, document as you go
4. **Validate**: Run `pytest augmented/tests/`
5. **Complete**: Update `CURRENT_WORK.md`, move plan to `implemented/`

---

## Git Commit Format

```
type(scope): Short description

- Detail 1
- Detail 2

🤖 Generated with [Claude Code](https://claude.com/claude-code)
Co-Authored-By: Claude <noreply@anthropic.com>
```

Types: `feat`, `fix`, `test`, `docs`, `refactor`

---

## Companion Repository

**Production implementations**: [causal_inference_mastery](https://github.com/brandonmbehring-dev/causal_inference_mastery)
- 25 method families (54,727 Python lines, 43,699 Julia lines)
- Cross-language Python ↔ Julia validation to 10 decimal places
- 8,975 tests with 99%+ pass rate
- 6-layer validation architecture

---

## Context Budget

| Document | Size | When to Load |
|----------|------|--------------|
| `CLAUDE.md` | ~8KB | Always (auto-loaded) |
| `CURRENT_WORK.md` | ~2KB | Session start |
| `augmented/docs/CHAPTER_INDEX.md` | ~10KB | Planning work |
| `augmented/docs/DATA_DICTIONARY.md` | ~8KB | Working with data |

---

## Attribution

Based on Matheus Facure's [Causal Inference for the Brave and True](https://matheusfacure.github.io/python-causality-handbook/).

Original work: © Matheus Facure (MIT License)
Augmented materials: © Brandon Behring (MIT License)
