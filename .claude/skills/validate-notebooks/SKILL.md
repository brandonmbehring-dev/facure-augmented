# Validate Notebooks Skill

Run notebook validation tests for the augmented materials.

## Usage

/validate-notebooks [chapter]

## Examples

/validate-notebooks                    # All notebooks
/validate-notebooks 05_linear          # Single chapter
/validate-notebooks --quick            # Core chapters only

## Implementation

```bash
# All notebooks
pytest augmented/tests/test_execution.py -v

# Single chapter
pytest augmented/tests/test_execution.py -k "$chapter" -v

# Core chapters only (5, 8, 13, 16, 22)
pytest augmented/tests/test_execution.py -k "core" -v --quick
```
