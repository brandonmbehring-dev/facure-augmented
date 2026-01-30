"""
Schema validation tests for augmented notebooks.

Verifies that notebooks conform to the section schema structure.
"""

from __future__ import annotations

from pathlib import Path

import pytest
from jsonschema import validate, ValidationError

from facure_augment.tests.conftest import (
    get_all_notebooks,
    get_core_chapter_notebooks,
    extract_notebook_metadata,
    extract_section_types,
    has_latex_content,
    CORE_CHAPTERS,
)


# =============================================================================
# Required Sections
# =============================================================================

# Minimum required section types for any notebook
REQUIRED_SECTIONS = [
    "facure_intuition",
    "formal_treatment",
    "numeric_demonstration",
    "implementation",
]

# Additional requirements for core chapters
CORE_REQUIRED_SECTIONS = REQUIRED_SECTIONS + [
    "interview_appendix",
    "references",
]


# =============================================================================
# Schema Tests
# =============================================================================


class TestNotebookSchema:
    """Test notebooks against JSON schema."""

    @pytest.mark.parametrize("notebook_path", get_all_notebooks(), ids=lambda p: p.stem)
    def test_has_required_sections(self, notebook_path: Path, all_notebooks):
        """Each notebook must have required section types."""
        if not notebook_path.exists():
            pytest.skip(f"Notebook not yet created: {notebook_path}")

        rel_path = notebook_path.relative_to(
            notebook_path.parent.parent.parent / "notebooks"
        )
        nb = all_notebooks.get(str(rel_path))

        if nb is None:
            pytest.skip("Notebook not loaded")

        sections_found = extract_section_types(nb)

        for required in REQUIRED_SECTIONS:
            assert required in sections_found, (
                f"Missing required section: {required}\n"
                f"Found sections: {sections_found}"
            )

    @pytest.mark.parametrize(
        "notebook_path", get_core_chapter_notebooks(), ids=lambda p: p.stem
    )
    def test_core_has_full_structure(self, notebook_path: Path, all_notebooks):
        """Core chapter notebooks must have full structure including interview appendix."""
        if not notebook_path.exists():
            pytest.skip(f"Notebook not yet created: {notebook_path}")

        rel_path = notebook_path.relative_to(
            notebook_path.parent.parent.parent / "notebooks"
        )
        nb = all_notebooks.get(str(rel_path))

        if nb is None:
            pytest.skip("Notebook not loaded")

        sections_found = extract_section_types(nb)

        for required in CORE_REQUIRED_SECTIONS:
            assert required in sections_found, (
                f"Core chapter missing section: {required}\n"
                f"Found sections: {sections_found}"
            )

    @pytest.mark.parametrize(
        "notebook_path", get_core_chapter_notebooks(), ids=lambda p: p.stem
    )
    def test_core_has_latex(self, notebook_path: Path, all_notebooks):
        """Core chapter notebooks must have LaTeX mathematical content."""
        if not notebook_path.exists():
            pytest.skip(f"Notebook not yet created: {notebook_path}")

        rel_path = notebook_path.relative_to(
            notebook_path.parent.parent.parent / "notebooks"
        )
        nb = all_notebooks.get(str(rel_path))

        if nb is None:
            pytest.skip("Notebook not loaded")

        assert has_latex_content(nb), (
            "Core chapter notebooks must contain LaTeX mathematical content "
            "(proofs, theorems, derivations)"
        )


class TestMetadataSchema:
    """Test notebook metadata against schema."""

    @pytest.mark.parametrize("notebook_path", get_all_notebooks(), ids=lambda p: p.stem)
    def test_has_valid_metadata(self, notebook_path: Path, all_notebooks, section_schema):
        """Notebook metadata should conform to schema."""
        if not notebook_path.exists():
            pytest.skip(f"Notebook not yet created: {notebook_path}")

        rel_path = notebook_path.relative_to(
            notebook_path.parent.parent.parent / "notebooks"
        )
        nb = all_notebooks.get(str(rel_path))

        if nb is None:
            pytest.skip("Notebook not loaded")

        metadata = extract_notebook_metadata(nb)

        if not metadata:
            pytest.skip("No structured metadata found")

        # Validate metadata against the SectionMetadata sub-schema only
        # (not the full schema which requires sections array)
        metadata_schema = section_schema.get("$defs", {}).get("SectionMetadata", {})
        if not metadata_schema:
            pytest.skip("SectionMetadata schema not found")

        try:
            validate(instance=metadata, schema=metadata_schema)
        except ValidationError as e:
            pytest.fail(f"Metadata validation failed: {e.message}")
