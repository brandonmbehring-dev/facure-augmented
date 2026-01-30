#!/usr/bin/env python3
"""
Execute all notebooks and save with outputs.

Usage:
    python scripts/execute_all_notebooks.py [--workers N] [--timeout SECONDS]
"""

from __future__ import annotations

import argparse
import sys
import traceback
from concurrent.futures import ProcessPoolExecutor, as_completed
from pathlib import Path
from typing import Tuple

import nbformat
from nbclient import NotebookClient
from nbclient.exceptions import CellExecutionError


NOTEBOOKS_DIR = Path(__file__).parent.parent / "facure_augment" / "notebooks"


def execute_notebook(notebook_path: Path, timeout: int = 300) -> Tuple[Path, bool, str]:
    """
    Execute a single notebook and save with outputs.

    Returns:
        Tuple of (path, success, message)
    """
    try:
        # Read notebook
        nb = nbformat.read(notebook_path, as_version=4)

        # Execute
        client = NotebookClient(
            nb,
            timeout=timeout,
            kernel_name="python3",
            resources={"metadata": {"path": str(notebook_path.parent)}},
        )
        client.execute()

        # Save with outputs
        nbformat.write(nb, notebook_path)

        return (notebook_path, True, "OK")

    except CellExecutionError as e:
        return (notebook_path, False, f"CellExecutionError: {e.ename}: {e.evalue}")
    except Exception as e:
        return (notebook_path, False, f"{type(e).__name__}: {str(e)[:200]}")


def main():
    parser = argparse.ArgumentParser(description="Execute all notebooks")
    parser.add_argument("--workers", type=int, default=8, help="Number of parallel workers")
    parser.add_argument("--timeout", type=int, default=300, help="Timeout per cell in seconds")
    parser.add_argument("--single", type=str, help="Execute single notebook (relative path)")
    args = parser.parse_args()

    if args.single:
        # Execute single notebook
        nb_path = NOTEBOOKS_DIR / args.single
        if not nb_path.exists():
            print(f"ERROR: Notebook not found: {nb_path}")
            sys.exit(1)

        print(f"Executing: {nb_path}")
        path, success, msg = execute_notebook(nb_path, args.timeout)
        print(f"  {'✓' if success else '✗'} {msg}")
        sys.exit(0 if success else 1)

    # Discover all notebooks
    notebooks = sorted(NOTEBOOKS_DIR.glob("**/*.ipynb"))
    total = len(notebooks)

    print(f"Found {total} notebooks in {NOTEBOOKS_DIR}")
    print(f"Using {args.workers} workers, {args.timeout}s timeout per cell")
    print("=" * 60)

    successes = []
    failures = []

    with ProcessPoolExecutor(max_workers=args.workers) as executor:
        futures = {
            executor.submit(execute_notebook, nb, args.timeout): nb
            for nb in notebooks
        }

        for i, future in enumerate(as_completed(futures), 1):
            path, success, msg = future.result()
            rel_path = path.relative_to(NOTEBOOKS_DIR)

            status = "✓" if success else "✗"
            print(f"[{i:3d}/{total}] {status} {rel_path}")

            if success:
                successes.append(rel_path)
            else:
                failures.append((rel_path, msg))
                print(f"         └─ {msg}")

    # Summary
    print("=" * 60)
    print(f"SUMMARY: {len(successes)} passed, {len(failures)} failed")

    if failures:
        print("\nFAILED NOTEBOOKS:")
        for path, msg in failures:
            print(f"  ✗ {path}")
            print(f"    └─ {msg}")
        sys.exit(1)
    else:
        print("\n✓ All notebooks executed successfully!")
        sys.exit(0)


if __name__ == "__main__":
    main()
