"""
Shared imports, data loaders, and helper functions for augmented notebooks.

This module provides common functionality so each section notebook can run
independently while sharing standard setup code.

Usage
-----
In each notebook, start with:

    from facure_augment.common import *

This imports:
- Standard data science libraries (numpy, pandas, matplotlib, etc.)
- Tufte styling functions
- Data loading utilities
- Common causal inference imports
"""

from __future__ import annotations

# =============================================================================
# Standard Library
# =============================================================================
import warnings
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple, Union

# =============================================================================
# Core Data Science
# =============================================================================
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Suppress common warnings in notebooks
warnings.filterwarnings("ignore", category=FutureWarning)
warnings.filterwarnings("ignore", category=UserWarning, module="matplotlib")

# =============================================================================
# Statistical Libraries
# =============================================================================
import statsmodels.api as sm
import statsmodels.formula.api as smf
from scipy import stats
from scipy.optimize import minimize

# =============================================================================
# Tufte Styling
# =============================================================================
from facure_augment.viz.tufte import (
    TUFTE_PALETTE,
    COLORS,
    apply_tufte_style,
    create_tufte_figure,
    direct_label,
    direct_label_line,
    set_tufte_title,
    set_tufte_labels,
    add_subtle_grid,
    range_frame,
    minimal_spines,
)

# =============================================================================
# Paths
# =============================================================================
FACURE_AUGMENT_ROOT = Path(__file__).parent
DATA_DIR = FACURE_AUGMENT_ROOT / "data"
FACURE_DATA_DIR = DATA_DIR / "facure"
EXTENDED_DATA_DIR = DATA_DIR / "extended"
NOTEBOOKS_DIR = FACURE_AUGMENT_ROOT / "notebooks"

# Original Facure repo data (sibling directory in combined repo)
REPO_ROOT = FACURE_AUGMENT_ROOT.parent
FACURE_ORIGINAL_DATA = REPO_ROOT / "facure_original" / "causal-inference-for-the-brave-and-true" / "data"


# =============================================================================
# Data Loading
# =============================================================================


def load_facure_data(filename: str) -> pd.DataFrame:
    """
    Load a dataset from Facure's original data.

    Parameters
    ----------
    filename : str
        Name of the CSV file (e.g., "online_classroom.csv").

    Returns
    -------
    pd.DataFrame
        The loaded dataset.

    Examples
    --------
    >>> df = load_facure_data("online_classroom.csv")
    >>> df.head()
    """
    # Try local copy first, then original
    local_path = FACURE_DATA_DIR / filename
    if local_path.exists():
        return pd.read_csv(local_path)

    original_path = FACURE_ORIGINAL_DATA / filename
    if original_path.exists():
        return pd.read_csv(original_path)

    raise FileNotFoundError(
        f"Dataset '{filename}' not found in:\n"
        f"  - {local_path}\n"
        f"  - {original_path}"
    )


def load_extended_data(filename: str) -> pd.DataFrame:
    """
    Load a dataset from extended examples.

    Parameters
    ----------
    filename : str
        Name of the CSV file.

    Returns
    -------
    pd.DataFrame
        The loaded dataset.
    """
    path = EXTENDED_DATA_DIR / filename
    if not path.exists():
        raise FileNotFoundError(f"Extended dataset '{filename}' not found at {path}")
    return pd.read_csv(path)


# =============================================================================
# Notebook Utilities
# =============================================================================


def set_notebook_style() -> None:
    """
    Configure matplotlib and pandas display settings for notebooks.

    Call this at the start of each notebook after imports.
    """
    # Matplotlib settings
    plt.style.use("seaborn-v0_8-whitegrid")
    plt.rcParams.update({
        "figure.facecolor": TUFTE_PALETTE["background"],
        "axes.facecolor": TUFTE_PALETTE["background"],
        "font.family": "sans-serif",
        "font.size": 10,
        "axes.labelsize": 10,
        "axes.titlesize": 11,
        "xtick.labelsize": 9,
        "ytick.labelsize": 9,
        "legend.fontsize": 9,
        "figure.dpi": 100,
        "savefig.dpi": 150,
        "savefig.bbox": "tight",
    })

    # Pandas display settings
    pd.set_option("display.max_columns", 20)
    pd.set_option("display.max_rows", 50)
    pd.set_option("display.precision", 4)
    pd.set_option("display.float_format", "{:.4f}".format)


def print_section(title: str, level: int = 1) -> None:
    """
    Print a formatted section header.

    Parameters
    ----------
    title : str
        Section title.
    level : int
        Header level (1 = main, 2 = sub, 3 = subsub).
    """
    if level == 1:
        print(f"\n{'=' * 60}")
        print(f"  {title}")
        print(f"{'=' * 60}\n")
    elif level == 2:
        print(f"\n{'-' * 40}")
        print(f"  {title}")
        print(f"{'-' * 40}\n")
    else:
        print(f"\n  {title}")
        print(f"  {'-' * len(title)}\n")


# =============================================================================
# Statistical Utilities
# =============================================================================


def ols_summary_table(model: sm.regression.linear_model.RegressionResultsWrapper) -> pd.DataFrame:
    """
    Create a clean summary table from OLS results.

    Parameters
    ----------
    model : statsmodels RegressionResults
        Fitted OLS model.

    Returns
    -------
    pd.DataFrame
        Summary table with coefficients, SEs, t-stats, p-values.
    """
    return pd.DataFrame({
        "Coefficient": model.params,
        "Std. Error": model.bse,
        "t-stat": model.tvalues,
        "p-value": model.pvalues,
        "CI Lower": model.conf_int()[0],
        "CI Upper": model.conf_int()[1],
    }).round(4)


def compare_coefficients(
    coef1: float,
    coef2: float,
    name1: str = "Model 1",
    name2: str = "Model 2",
    rtol: float = 1e-10,
) -> bool:
    """
    Compare two coefficients and report whether they match.

    Useful for FWL demonstrations.

    Parameters
    ----------
    coef1, coef2 : float
        Coefficients to compare.
    name1, name2 : str
        Names for display.
    rtol : float
        Relative tolerance.

    Returns
    -------
    bool
        True if coefficients match within tolerance.
    """
    match = np.isclose(coef1, coef2, rtol=rtol)
    print(f"{name1}: {coef1:.10f}")
    print(f"{name2}: {coef2:.10f}")
    print(f"Difference: {abs(coef1 - coef2):.2e}")
    print(f"Match (rtol={rtol}): {match}")
    return match


# =============================================================================
# Causal Inference Utilities
# =============================================================================


def generate_rct_data(
    n: int = 1000,
    ate: float = 2.0,
    seed: int = 42,
) -> Tuple[np.ndarray, np.ndarray, float]:
    """
    Generate simple RCT data for demonstrations.

    Parameters
    ----------
    n : int
        Sample size.
    ate : float
        True average treatment effect.
    seed : int
        Random seed.

    Returns
    -------
    Y : np.ndarray
        Outcomes.
    T : np.ndarray
        Treatment assignment (0/1).
    true_ate : float
        The true ATE used in generation.
    """
    np.random.seed(seed)
    T = np.random.binomial(1, 0.5, n)
    Y0 = np.random.normal(10, 2, n)
    Y1 = Y0 + ate + np.random.normal(0, 0.5, n)
    Y = T * Y1 + (1 - T) * Y0
    return Y, T, ate


def generate_confounded_data(
    n: int = 1000,
    ate: float = 2.0,
    confounding_strength: float = 1.0,
    seed: int = 42,
) -> Tuple[np.ndarray, np.ndarray, np.ndarray, float]:
    """
    Generate observational data with confounding.

    Parameters
    ----------
    n : int
        Sample size.
    ate : float
        True average treatment effect.
    confounding_strength : float
        Strength of confounding (0 = no confounding).
    seed : int
        Random seed.

    Returns
    -------
    Y : np.ndarray
        Outcomes.
    T : np.ndarray
        Treatment assignment (0/1).
    X : np.ndarray
        Confounder.
    true_ate : float
        The true ATE.
    """
    np.random.seed(seed)
    X = np.random.normal(0, 1, n)
    prob_T = 1 / (1 + np.exp(-confounding_strength * X))
    T = np.random.binomial(1, prob_T)
    Y = 5 + ate * T + confounding_strength * X + np.random.normal(0, 1, n)
    return Y, T, X, ate


# =============================================================================
# Exports
# =============================================================================

__all__ = [
    # Core libraries
    "np",
    "pd",
    "plt",
    "sns",
    "sm",
    "smf",
    "stats",
    "minimize",
    # Paths
    "FACURE_AUGMENT_ROOT",
    "DATA_DIR",
    "FACURE_DATA_DIR",
    "EXTENDED_DATA_DIR",
    "NOTEBOOKS_DIR",
    # Data loading
    "load_facure_data",
    "load_extended_data",
    # Tufte styling
    "TUFTE_PALETTE",
    "COLORS",
    "apply_tufte_style",
    "create_tufte_figure",
    "direct_label",
    "direct_label_line",
    "set_tufte_title",
    "set_tufte_labels",
    "add_subtle_grid",
    "range_frame",
    "minimal_spines",
    # Utilities
    "set_notebook_style",
    "print_section",
    "ols_summary_table",
    "compare_coefficients",
    # Data generation
    "generate_rct_data",
    "generate_confounded_data",
]
