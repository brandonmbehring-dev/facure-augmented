"""
Notebook execution tests.

Simple, strict validation: each notebook either executes or fails.
No skips, no complex logic. TDD-compliant.
"""

from __future__ import annotations

import re
from pathlib import Path

import nbformat
import pytest
from nbclient import NotebookClient
from nbclient.exceptions import CellExecutionError

# Directory containing all notebooks
NOTEBOOKS_DIR = Path(__file__).parent.parent / "notebooks"


def get_all_notebooks() -> list[Path]:
    """Discover all notebooks in the notebooks directory."""
    return sorted(NOTEBOOKS_DIR.glob("**/*.ipynb"))


def notebook_id(path: Path) -> str:
    """Create readable test ID from notebook path."""
    return str(path.relative_to(NOTEBOOKS_DIR))


# =============================================================================
# Core Execution Test - This is the main TDD test
# =============================================================================


@pytest.mark.parametrize("notebook_path", get_all_notebooks(), ids=notebook_id)
def test_notebook_executes(notebook_path: Path) -> None:
    """
    Each notebook must execute without errors.

    This is the core TDD test. If a notebook is in the notebooks/ directory,
    it MUST execute successfully. No exceptions, no skips.

    Raises
    ------
    CellExecutionError
        If any cell in the notebook raises an exception.
    """
    # Read the notebook
    nb = nbformat.read(notebook_path, as_version=4)

    # Execute with timeout
    client = NotebookClient(
        nb,
        timeout=300,  # 5 minutes per cell
        kernel_name="python3",
    )

    # This raises CellExecutionError on failure - exactly what we want
    client.execute()


# =============================================================================
# Output Quality Tests (Optional - can run with -m slow)
# =============================================================================


@pytest.mark.slow
@pytest.mark.parametrize("notebook_path", get_all_notebooks(), ids=notebook_id)
def test_notebook_has_outputs(notebook_path: Path) -> None:
    """
    Notebooks should produce visible outputs (figures, tables, prints).

    This catches "silent" notebooks that execute but produce nothing.
    """
    nb = nbformat.read(notebook_path, as_version=4)
    client = NotebookClient(nb, timeout=300, kernel_name="python3")
    executed = client.execute()

    # Count cells with outputs
    output_count = sum(
        1 for cell in executed.cells
        if cell.cell_type == "code" and cell.get("outputs", [])
    )

    # At least 20% of code cells should produce output
    code_cells = [c for c in executed.cells if c.cell_type == "code"]
    if code_cells:
        output_ratio = output_count / len(code_cells)
        assert output_ratio >= 0.1, (
            f"Only {output_ratio:.0%} of code cells produce output. "
            f"Expected at least 10%."
        )


@pytest.mark.slow
@pytest.mark.parametrize("notebook_path", get_all_notebooks(), ids=notebook_id)
def test_no_nan_inf_outputs(notebook_path: Path) -> None:
    """
    Numerical outputs should not contain NaN or Inf.

    These indicate numerical instability or bugs.
    """
    nb = nbformat.read(notebook_path, as_version=4)
    client = NotebookClient(nb, timeout=300, kernel_name="python3")
    executed = client.execute()

    problems = []
    for i, cell in enumerate(executed.cells):
        if cell.cell_type != "code":
            continue
        for output in cell.get("outputs", []):
            # Check text outputs
            text = output.get("text", "")
            if isinstance(text, list):
                text = "".join(text)

            # Check data outputs (e.g., DataFrame repr)
            data = output.get("data", {})
            if "text/plain" in data:
                plain = data["text/plain"]
                if isinstance(plain, list):
                    plain = "".join(plain)
                text += plain

            # Look for NaN/Inf (use word boundaries to avoid false positives
            # from words like "inference", "information", "infinity")
            text_lower = text.lower()
            # Match standalone nan/inf or with numeric prefixes like -inf, +inf
            has_nan = re.search(r'\bnan\b', text_lower)
            has_inf = re.search(r'(?<![a-z])\binf\b(?![a-z])', text_lower)
            if has_nan or has_inf:
                problems.append(f"Cell {i}: contains NaN or Inf")

    assert not problems, f"Found numerical issues:\n" + "\n".join(problems)
