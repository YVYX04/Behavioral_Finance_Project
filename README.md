
# Interpreting Statistical Data from Behavioral Research

University of St. Gallen, 2026

## The Effects of Attention in Stock Selection among Retail Investors

### Foreword

This repository contains a course project for *Interpreting Statistical Data from Behavioral Research* at the University of St. Gallen. The objective is to illustrate a clean and reproducible empirical workflow commonly used in behavioral research, with a specific focus on how investor attention may affect stock selection among retail investors.

The project is methodological in nature. It does not aim to establish real-world causal claims. Instead, it uses synthetic data to demonstrate how one can formulate a research question, structure a dataset, conduct statistical analyses, interpret results, and present findings in a rigorous and transparent way.

The final output of the project is a presentation summarizing the research question, empirical design, statistical procedures, and main results.

### Repository Structure

The repository follows a simple research-oriented structure:

```text
Behavioral_Finance_Project/
├── README.md
├── data/
│   ├── raw/                # Synthetic input data as initially created or collected
│   ├── interim/            # Cleaned or transformed intermediate datasets
│   └── processed/          # Final analysis-ready datasets
├── notebooks/              # Exploratory notebooks and preliminary analyses
├── src/
│   ├── __init__.py
│   ├── data_prep.py        # Data cleaning and variable construction
│   ├── descriptive.py      # Descriptive statistics and summary tables
│   ├── stat_tests.py.      # Hypothesis tests and inferential procedures
│   ├── regression.py       # Regression specifications
│   └── utils.py            # Helper functions used across the project
├── results/
│   ├── tables/             # Output tables
│   ├── figures/            # Output plots and visualizations
│   └── presentation/       # Final slides or presentation material
├── reports/
│   └── project_notes.md    # Research notes, interpretation, and draft conclusions
├── requirements.txt
└── .gitignore
```
