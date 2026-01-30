#!/usr/bin/env python3
"""
Execute all notebooks sequentially (no multiprocessing).
"""

import sys
from pathlib import Path

import nbformat
from nbclient import NotebookClient
from nbclient.exceptions import CellExecutionError


NOTEBOOKS_DIR = Path(__file__).parent.parent / "facure_augment" / "notebooks"


def main():
    notebooks = sorted(NOTEBOOKS_DIR.glob("**/*.ipynb"))
    total = len(notebooks)

    print(f"Found {total} notebooks")
    print("=" * 60)

    successes = []
    failures = []

    for i, nb_path in enumerate(notebooks, 1):
        rel_path = nb_path.relative_to(NOTEBOOKS_DIR)
        print(f"[{i:3d}/{total}] {rel_path} ...", end=" ", flush=True)

        try:
            # Read
            nb = nbformat.read(nb_path, as_version=4)

            # Execute
            client = NotebookClient(
                nb,
                timeout=300,
                kernel_name="python3",
                resources={"metadata": {"path": str(nb_path.parent)}},
            )
            client.execute()

            # Save
            nbformat.write(nb, nb_path)
            print("✓")
            successes.append(rel_path)

        except CellExecutionError as e:
            print(f"✗ {e.ename}: {e.evalue[:50]}")
            failures.append((rel_path, f"{e.ename}: {e.evalue}"))
        except Exception as e:
            print(f"✗ {type(e).__name__}: {str(e)[:50]}")
            failures.append((rel_path, str(e)))

    # Summary
    print("=" * 60)
    print(f"SUMMARY: {len(successes)} passed, {len(failures)} failed")

    if failures:
        print("\nFAILED:")
        for path, msg in failures:
            print(f"  ✗ {path}: {msg[:80]}")
        sys.exit(1)


if __name__ == "__main__":
    main()
