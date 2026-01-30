"""
Shared pytest fixtures for augmented notebook testing.

This module provides fixtures for:
- Loading notebooks
- Schema validation
- Notebook execution
- Output validation
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, Generator, List

import nbformat
import pytest
from nbclient import NotebookClient
from nbclient.exceptions import CellExecutionError

# =============================================================================
# Paths
# =============================================================================

FACURE_AUGMENT_ROOT = Path(__file__).parent.parent
NOTEBOOKS_DIR = FACURE_AUGMENT_ROOT / "notebooks"
SCHEMA_DIR = FACURE_AUGMENT_ROOT / "schema"
DATA_DIR = FACURE_AUGMENT_ROOT / "data"

# Core chapters that require highest rigor
CORE_CHAPTERS = [5, 8, 13, 16, 22]


# =============================================================================
# Notebook Discovery
# =============================================================================


def get_all_notebooks() -> List[Path]:
    """Discover all section notebooks."""
    return sorted(NOTEBOOKS_DIR.glob("**/*.ipynb"))


def get_chapter_notebooks(chapter_num: int) -> List[Path]:
    """Get all notebooks for a specific chapter."""
    chapter_dir = NOTEBOOKS_DIR / f"{chapter_num:02d}_*"
    return sorted(NOTEBOOKS_DIR.glob(f"{chapter_num:02d}_*/**/*.ipynb"))


def get_core_chapter_notebooks() -> List[Path]:
    """Get notebooks from core chapters only."""
    notebooks = []
    for ch in CORE_CHAPTERS:
        notebooks.extend(get_chapter_notebooks(ch))
    return notebooks


# =============================================================================
# Fixtures
# =============================================================================


@pytest.fixture(scope="session")
def section_schema() -> Dict[str, Any]:
    """Load the section notebook JSON schema."""
    schema_path = SCHEMA_DIR / "section.schema.json"
    with open(schema_path) as f:
        return json.load(f)


@pytest.fixture(scope="module")
def all_notebooks() -> Dict[str, nbformat.NotebookNode]:
    """Load all augmented notebooks."""
    notebooks = {}
    for nb_path in get_all_notebooks():
        with open(nb_path) as f:
            # Use relative path from notebooks dir as key
            rel_path = nb_path.relative_to(NOTEBOOKS_DIR)
            notebooks[str(rel_path)] = nbformat.read(f, as_version=4)
    return notebooks


@pytest.fixture
def notebook_paths() -> List[Path]:
    """Return list of all notebook paths."""
    return get_all_notebooks()


@pytest.fixture
def core_notebook_paths() -> List[Path]:
    """Return list of core chapter notebook paths."""
    return get_core_chapter_notebooks()


# =============================================================================
# Notebook Execution Fixtures
# =============================================================================


@pytest.fixture(scope="session")
def notebook_executor():
    """Factory for creating notebook executors."""

    def _execute(
        notebook_path: Path,
        timeout: int = 300,
        allow_errors: bool = False,
    ) -> nbformat.NotebookNode:
        """
        Execute a notebook and return the executed version.

        Parameters
        ----------
        notebook_path : Path
            Path to the notebook.
        timeout : int
            Timeout per cell in seconds.
        allow_errors : bool
            Whether to allow cell errors.

        Returns
        -------
        nbformat.NotebookNode
            The executed notebook.

        Raises
        ------
        CellExecutionError
            If a cell fails and allow_errors is False.
        """
        with open(notebook_path) as f:
            nb = nbformat.read(f, as_version=4)

        client = NotebookClient(
            nb,
            timeout=timeout,
            kernel_name="python3",
            allow_errors=allow_errors,
        )

        return client.execute()

    return _execute


# =============================================================================
# Validation Helpers
# =============================================================================


def extract_notebook_metadata(nb: nbformat.NotebookNode) -> Dict[str, Any]:
    """
    Extract structured metadata from notebook.

    Looks for metadata in:
    1. nb.metadata.augmented
    2. First markdown cell with YAML-like structure
    """
    # Check notebook metadata
    if "augmented" in nb.metadata:
        return nb.metadata["augmented"]

    # Fallback: parse first markdown cell
    for cell in nb.cells:
        if cell.cell_type == "markdown":
            # Look for metadata markers
            if "**Chapter**:" in cell.source or "chapter_number" in cell.source:
                # TODO: Parse YAML-like metadata from markdown
                pass
            break

    return {}


def extract_section_types(nb: nbformat.NotebookNode) -> List[str]:
    """
    Extract section types from notebook markdown headers.

    Returns list of section type identifiers found.

    Only examines ## level headers (first line starting with ##).
    """
    sections = []

    for cell in nb.cells:
        if cell.cell_type != "markdown":
            continue

        # Only check the first line that starts with ##
        header_line = None
        for line in cell.source.split("\n"):
            stripped = line.strip().lower()
            if stripped.startswith("##") and not stripped.startswith("###"):
                header_line = stripped
                break

        if header_line is None:
            continue

        # Check for standard section headers (match on header line only)
        if "table of contents" in header_line or "toc" in header_line:
            sections.append("table_of_contents")
        elif "intuition" in header_line:
            sections.append("facure_intuition")
        elif "formal" in header_line:
            sections.append("formal_treatment")
        elif "numeric" in header_line:
            sections.append("numeric_demonstration")
        elif "implementation" in header_line:
            sections.append("implementation")
        elif "interview" in header_line:
            sections.append("interview_appendix")
        elif "references" in header_line:
            sections.append("references")
        elif "methodological" in header_line:
            sections.append("methodological_concerns")

    return sections


def count_code_cells(nb: nbformat.NotebookNode) -> int:
    """Count code cells in notebook."""
    return sum(1 for cell in nb.cells if cell.cell_type == "code")


def count_figure_outputs(nb: nbformat.NotebookNode) -> int:
    """Count figure outputs in executed notebook."""
    count = 0
    for cell in nb.cells:
        if cell.cell_type != "code":
            continue
        for output in cell.get("outputs", []):
            if "data" in output:
                if "image/png" in output["data"] or "image/svg+xml" in output["data"]:
                    count += 1
    return count


def has_latex_content(nb: nbformat.NotebookNode) -> bool:
    """Check if notebook has LaTeX mathematical content."""
    for cell in nb.cells:
        if cell.cell_type == "markdown":
            if "$$" in cell.source or "\\begin{" in cell.source:
                return True
    return False


def has_collapsible_solutions(nb: nbformat.NotebookNode) -> bool:
    """Check if notebook has collapsible solution blocks."""
    for cell in nb.cells:
        if cell.cell_type == "markdown":
            if "<details>" in cell.source and "<summary>" in cell.source:
                return True
    return False


def count_interview_questions(nb: nbformat.NotebookNode) -> int:
    """Count interview questions in notebook."""
    count = 0
    for cell in nb.cells:
        if cell.cell_type == "markdown":
            # Look for Q1, Q2, etc. patterns
            import re

            matches = re.findall(r"\*\*Q\d+", cell.source)
            count += len(matches)
    return count


# =============================================================================
# Numerical Validation
# =============================================================================


def check_for_nan_inf(nb: nbformat.NotebookNode) -> List[str]:
    """
    Check executed notebook outputs for NaN or Inf values.

    Returns list of cell indices with problematic outputs.
    """
    problematic = []

    for i, cell in enumerate(nb.cells):
        if cell.cell_type != "code":
            continue

        for output in cell.get("outputs", []):
            output_text = ""

            if "text" in output:
                output_text = output["text"]
            elif "data" in output and "text/plain" in output["data"]:
                output_text = output["data"]["text/plain"]

            if "nan" in output_text.lower() or "inf" in output_text.lower():
                problematic.append(f"Cell {i}")

    return problematic


# =============================================================================
# Pytest Hooks
# =============================================================================


def pytest_collection_modifyitems(config, items):
    """Add markers to slow tests."""
    for item in items:
        if "execution" in item.nodeid or "execute" in item.name:
            item.add_marker(pytest.mark.slow)
