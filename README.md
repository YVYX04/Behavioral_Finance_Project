# The Effects of Attention in Stock Selection among Retail Investors

**Interpreting Statistical Data from Behavioral Research** — University of St. Gallen, 2026

**Authors:** Yvan Richard, Antoine Pittet, Alexandre Zaza, Arthur Glauser, Samuel Payne

---

## Overview

This repository contains a course project investigating how media attention affects stock-buying intentions among retail investors. The empirical design is a three-way factorial experiment in which three independent variables — media channel, exposure level, and industry sector — are crossed to explain variation in a self-reported buying-intention score.

The project uses **synthetic data** to demonstrate a clean, reproducible empirical workflow: data cleaning, exploratory analysis, hypothesis testing (three-way ANOVA with post-hoc comparisons), and diagnostic checking. The final deliverable is a presentation summarizing the research design, statistical procedures, and main findings.

---

## Repository Structure

```
Behavioral_Finance_Project/
├── data/
│   ├── baseline_sample.xlsx        # Original synthetic data (professor-provided)
│   ├── data.csv                    # Cleaned data — 720 observations, 4 variables
│   └── data.pkl                    # Same, in pickle format (faster I/O)
├── notebooks/
│   ├── 01_analysis.qmd             # Main analysis notebook (Quarto / Jupyter)
│   └── 01_analysis.html            # Rendered HTML output
├── src/
│   ├── __init__.py
│   └── clean_xlsx.py               # Reads baseline_sample.xlsx → data.csv + data.pkl
├── results/
│   └── plots/                      # PDF figures produced by the notebook
│       ├── bivariate_analysis.pdf
│       ├── buying_intention_distribution.pdf
│       ├── interaction_plot.pdf
│       ├── residuals_diagnostics.pdf
│       ├── residuals_distribution.pdf
│       └── residuals_qqplot.pdf
├── reports/
│   └── research_proposal/
│       ├── research_proposal.pdf
│       └── latex_code/
│           ├── main.tex
│           └── references.bib
├── pyproject.toml
├── uv.lock
└── .python-version                 # Pins Python 3.13
```

---

## Setup

The project uses [**uv**](https://docs.astral.sh/uv/) for environment and dependency management.

### 1 — Install uv

```bash
# macOS / Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows (PowerShell)
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Restart your shell (or run `source $HOME/.local/bin/env`) so that `uv` is on your `PATH`.

### 2 — Clone and enter the repository

```bash
git clone <repo-url>
cd Behavioral_Finance_Project
```

### 3 — Create the virtual environment and install dependencies

```bash
uv sync
```

`uv sync` reads `pyproject.toml` and `uv.lock`, installs the pinned Python version (3.13) automatically if it is not already present, and creates `.venv/` in the project root. No manual `pip install` is needed.

### 4 — Verify the installation

```bash
uv run python -c "import pandas, statsmodels, seaborn; print('OK')"
```

---

## Running the Data Cleaning Script

The raw file `data/baseline_sample.xlsx` must be cleaned before the notebook can run. Execute the cleaning script from the **project root**:

```bash
uv run python src/clean_xlsx.py
```

This produces `data/data.csv` and `data/data.pkl`. Both files are already committed, so this step is only needed if you modify the raw data or start from scratch.

---

## Rendering the Quarto Notebook

The main analysis lives in `notebooks/01_analysis.qmd`. Rendering it requires [**Quarto**](https://quarto.org/docs/get-started/) (installed separately from Python) and a Jupyter kernel that points to the project's uv-managed environment.

### 1 — Install Quarto

Download and install from <https://quarto.org/docs/get-started/>, or with Homebrew on macOS:

```bash
brew install --cask quarto
```

### 2 — Register a Jupyter kernel from the uv environment

Run this **once** after `uv sync`:

```bash
uv run python -m ipykernel install \
    --user \
    --name behavioral-finance \
    --display-name "Python (behavioral-finance)"
```

This registers the `.venv` interpreter as a named Jupyter kernel. Quarto will use it when rendering the notebook.

### 3 — Render the notebook

```bash
quarto render notebooks/01_analysis.qmd
```

The output is written to `notebooks/01_analysis.html`. Pass `--to pdf` instead for a PDF output (requires a LaTeX distribution).

### 4 — Interactive editing in VS Code or JupyterLab

Open the `.qmd` file in VS Code with the [Quarto extension](https://marketplace.visualstudio.com/items?itemName=quarto.quarto) and select **Python (behavioral-finance)** as the kernel, or launch JupyterLab via:

```bash
uv run jupyter lab
```

---

## Dependencies

All dependencies are declared in `pyproject.toml` and locked in `uv.lock`.

| Package | Purpose |
|---|---|
| `pandas` | Data manipulation |
| `numpy` | Numerical operations |
| `scipy` | Statistical tests (Shapiro-Wilk, etc.) |
| `statsmodels` | ANOVA, OLS, post-hoc comparisons |
| `matplotlib` / `seaborn` | Visualisation |
| `openpyxl` | Reading `.xlsx` files |
| `ipykernel` / `jupyter` | Jupyter kernel for Quarto rendering |

---

## Research Design at a Glance

| Variable | Role | Levels |
|---|---|---|
| `media_attention` | Independent (IV1) | Google Search, News, Social Media |
| `exposure_level` | Independent (IV2) | Low, High |
| `industry` | Independent (IV3) | Industry A, Industry B |
| `buying_intention` | Dependent (DV) | 1 – 5 ordinal scale |

The main statistical procedure is a **three-way ANOVA** with partial eta-squared effect sizes, Tukey's HSD post-hoc tests, and residual diagnostics (Q-Q plot, Shapiro-Wilk).
