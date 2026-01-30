#!/usr/bin/env python
"""
Validate all augmented notebooks execute without errors.

Standalone script for manual validation, CI/CD, or pre-commit hooks.

Usage:
    python augmented/scripts/validate_notebooks.py
    python augmented/scripts/validate_notebooks.py --parallel
    python augmented/scripts/validate_notebooks.py --verbose

Exit Codes:
    0: All notebooks validated successfully
    1: One or more notebooks failed
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from concurrent.futures import ProcessPoolExecutor, as_completed
from pathlib import Path
from typing import NamedTuple

# Find notebooks directory relative to this script
SCRIPT_DIR = Path(__file__).parent
NOTEBOOKS_DIR = SCRIPT_DIR.parent / "notebooks"


class ValidationResult(NamedTuple):
    """Result of validating a single notebook."""

    notebook: Path
    success: bool
    error_message: str | None = None


def validate_notebook(notebook_path: Path, timeout: int = 300) -> ValidationResult:
    """
    Validate a single notebook executes without errors.

    Parameters
    ----------
    notebook_path : Path
        Path to the notebook file.
    timeout : int
        Maximum seconds per notebook.

    Returns
    -------
    ValidationResult
        Named tuple with (notebook, success, error_message).
    """
    try:
        result = subprocess.run(
            ["jupyter", "execute", str(notebook_path)],
            capture_output=True,
            timeout=timeout,
            text=True,
        )
        if result.returncode == 0:
            return ValidationResult(notebook_path, True)
        else:
            # Extract error from stderr
            error = result.stderr.strip()
            # Truncate long errors
            if len(error) > 500:
                error = error[:500] + "..."
            return ValidationResult(notebook_path, False, error)
    except subprocess.TimeoutExpired:
        return ValidationResult(
            notebook_path, False, f"Timeout after {timeout}s"
        )
    except Exception as e:
        return ValidationResult(notebook_path, False, str(e))


def get_all_notebooks() -> list[Path]:
    """Discover all notebooks in the notebooks directory."""
    if not NOTEBOOKS_DIR.exists():
        print(f"ERROR: Notebooks directory not found: {NOTEBOOKS_DIR}")
        sys.exit(1)
    return sorted(NOTEBOOKS_DIR.glob("**/*.ipynb"))


def main() -> int:
    """
    Main entry point.

    Returns
    -------
    int
        Exit code (0=success, 1=failure).
    """
    parser = argparse.ArgumentParser(
        description="Validate augmented notebooks execute without errors."
    )
    parser.add_argument(
        "--parallel",
        action="store_true",
        help="Run validations in parallel (faster but uses more resources)",
    )
    parser.add_argument(
        "--verbose",
        "-v",
        action="store_true",
        help="Show detailed output",
    )
    parser.add_argument(
        "--timeout",
        type=int,
        default=300,
        help="Timeout per notebook in seconds (default: 300)",
    )
    args = parser.parse_args()

    notebooks = get_all_notebooks()
    if not notebooks:
        print("No notebooks found!")
        return 1

    print(f"Validating {len(notebooks)} notebooks...")
    if args.parallel:
        print("(Running in parallel mode)")

    failed: list[ValidationResult] = []
    passed = 0

    if args.parallel:
        # Parallel execution
        with ProcessPoolExecutor(max_workers=4) as executor:
            futures = {
                executor.submit(validate_notebook, nb, args.timeout): nb
                for nb in notebooks
            }
            for future in as_completed(futures):
                result = future.result()
                if result.success:
                    passed += 1
                    print(f"  ✅ {result.notebook.name}")
                else:
                    failed.append(result)
                    print(f"  ❌ {result.notebook.name}")
                    if args.verbose and result.error_message:
                        print(f"     Error: {result.error_message[:200]}")
    else:
        # Sequential execution
        for nb in notebooks:
            print(f"  {nb.name}...", end=" ", flush=True)
            result = validate_notebook(nb, args.timeout)
            if result.success:
                passed += 1
                print("✅")
            else:
                failed.append(result)
                print("❌")
                if args.verbose and result.error_message:
                    print(f"     Error: {result.error_message[:200]}")

    # Summary
    print()
    print("=" * 60)
    if failed:
        print(f"❌ {len(failed)} notebook(s) FAILED:")
        for result in failed:
            print(f"   - {result.notebook}")
            if result.error_message:
                # Show first line of error
                first_line = result.error_message.split("\n")[0][:80]
                print(f"     {first_line}")
        print()
        print(f"Passed: {passed}/{len(notebooks)}")
        return 1
    else:
        print(f"✅ All {len(notebooks)} notebooks validated successfully")
        return 0


if __name__ == "__main__":
    sys.exit(main())
