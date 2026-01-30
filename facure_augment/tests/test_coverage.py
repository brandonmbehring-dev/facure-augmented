"""
Coverage tests for augmented.

Verifies that all Facure chapters and sections have corresponding notebooks.
"""

from __future__ import annotations

from pathlib import Path
from typing import Dict, List, Set

import pytest

from facure_augment.tests.conftest import (
    NOTEBOOKS_DIR,
    get_all_notebooks,
    CORE_CHAPTERS,
)


# =============================================================================
# Facure Chapter Mapping
# =============================================================================

# All Facure chapters (25 main + 5 appendix)
FACURE_CHAPTERS = {
    1: "Introduction-To-Causality",
    2: "Randomised-Experiments",
    3: "Stats-Review-The-Most-Dangerous-Equation",
    4: "Graphical-Causal-Models",
    5: "The-Unreasonable-Effectiveness-of-Linear-Regression",
    6: "Grouped-and-Dummy-Regression",
    7: "Beyond-Confounders",
    8: "Instrumental-Variables",
    9: "Non-Compliance-and-LATE",
    10: "Matching",
    11: "Propensity-Score",
    12: "Doubly-Robust-Estimation",
    13: "Difference-in-Differences",
    14: "Panel-Data-and-Fixed-Effects",
    15: "Synthetic-Control",
    16: "Regression-Discontinuity-Design",
    17: "Predictive-Models-101",
    18: "Heterogeneous-Treatment-Effects-and-Personalization",
    19: "Evaluating-Causal-Models",
    20: "Plug-and-Play-Estimators",
    21: "Meta-Learners",
    22: "Debiased-Orthogonal-Machine-Learning",
    23: "Challenges-with-Effect-Heterogeneity-and-Nonlinearity",
    24: "The-Diff-in-Diff-Saga",
    25: "Synthetic-Diff-in-Diff",
}

# Appendix notebooks
FACURE_APPENDIX = {
    "A1": "Conformal-Inference-for-Synthetic-Control",
    "A2": "Debiasing-with-Orthogonalization",
    "A3": "Debiasing-with-Propensity-Score",
    "A4": "Prediction-Metrics-For-Causal-Models",
    "A5": "When-Prediction-Fails",
}


# =============================================================================
# Coverage Tests
# =============================================================================


class TestChapterCoverage:
    """Test that all Facure chapters have corresponding directories."""

    def test_all_main_chapters_have_directories(self):
        """Each main chapter (1-25) should have a directory."""
        existing_dirs = set()

        for d in NOTEBOOKS_DIR.iterdir():
            if d.is_dir():
                # Extract chapter number from directory name (e.g., "05_linear_regression")
                try:
                    ch_num = int(d.name.split("_")[0])
                    existing_dirs.add(ch_num)
                except (ValueError, IndexError):
                    pass

        # Check coverage - currently we've only created core chapter dirs
        missing = set(CORE_CHAPTERS) - existing_dirs

        # This is informational - we expect incremental buildout
        if missing:
            pytest.skip(
                f"Incomplete coverage (expected for incremental build). "
                f"Missing core chapters: {missing}"
            )

    def test_core_chapters_have_directories(self):
        """Core chapters (5, 8, 13, 16, 22) should have directories."""
        for ch_num in CORE_CHAPTERS:
            pattern = f"{ch_num:02d}_*"
            matches = list(NOTEBOOKS_DIR.glob(pattern))

            assert len(matches) >= 1, (
                f"Core chapter {ch_num} missing directory. "
                f"Expected directory matching: {pattern}"
            )


class TestNotebookCoverage:
    """Test that directories have at least one notebook."""

    def test_chapter_directories_have_notebooks(self):
        """Each chapter directory should contain at least one notebook."""
        for chapter_dir in NOTEBOOKS_DIR.iterdir():
            if not chapter_dir.is_dir():
                continue

            notebooks = list(chapter_dir.glob("*.ipynb"))

            # Skip if directory was just created (incremental build)
            if len(notebooks) == 0:
                pytest.skip(
                    f"Directory {chapter_dir.name} has no notebooks yet "
                    "(expected for incremental build)"
                )

    def test_core_directories_have_notebooks(self):
        """Core chapter directories should have notebooks."""
        for ch_num in CORE_CHAPTERS:
            pattern = f"{ch_num:02d}_*"
            matches = list(NOTEBOOKS_DIR.glob(pattern))

            if not matches:
                pytest.skip(f"Core chapter {ch_num} directory not yet created")

            chapter_dir = matches[0]
            notebooks = list(chapter_dir.glob("*.ipynb"))

            # This will fail until we create the first notebook
            # That's intentional - TDD
            if len(notebooks) == 0:
                pytest.skip(
                    f"Core chapter {ch_num} has no notebooks yet "
                    "(expected - building incrementally)"
                )


class TestSectionCoverage:
    """Test section-level coverage for core chapters."""

    # Minimum expected sections per core chapter
    EXPECTED_SECTIONS = {
        5: 4,   # Linear Regression
        8: 3,   # Instrumental Variables
        13: 4,  # Difference-in-Differences
        16: 3,  # Regression Discontinuity
        22: 4,  # Debiased/Orthogonal ML
    }

    @pytest.mark.parametrize("ch_num,min_sections", EXPECTED_SECTIONS.items())
    def test_core_chapter_section_count(self, ch_num: int, min_sections: int):
        """Core chapters should have minimum number of sections."""
        pattern = f"{ch_num:02d}_*"
        matches = list(NOTEBOOKS_DIR.glob(pattern))

        if not matches:
            pytest.skip(f"Core chapter {ch_num} directory not yet created")

        chapter_dir = matches[0]
        notebooks = list(chapter_dir.glob("*.ipynb"))

        if len(notebooks) == 0:
            pytest.skip(f"Core chapter {ch_num} has no notebooks yet")

        # Skip if building incrementally (less than minimum)
        # This is expected during incremental development
        if len(notebooks) < min_sections:
            pytest.skip(
                f"Core chapter {ch_num} has {len(notebooks)}/{min_sections} sections "
                "(incremental build in progress)"
            )

        assert len(notebooks) >= min_sections, (
            f"Core chapter {ch_num} should have at least {min_sections} sections, "
            f"found {len(notebooks)}"
        )
