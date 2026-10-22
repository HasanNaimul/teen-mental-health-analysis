# Teen mental health analysis

An exploratory dataset case study using Python to examine sleep, social-media use, stress, anxiety and a binary depression label. Its purpose is to practise preparing data, interpreting associations and evaluating a model with an imbalanced target.

## Included evidence

- [Exploratory notebook](notebooks/01_teen_mental_health_analysis.ipynb)
- [Data preparation](src/data_prep.py), [modelling](src/modeling.py) and [visualisation](src/visualize.py)
- Raw and processed CSV files under `data/`
- Existing charts under [reports/figures](reports/figures)

No Power BI source dashboard, build guide, DAX measures or theme file is included. The processed data is suitable for a separate dashboard-building exercise.

## Findings

The supplied raw CSV has 1,200 records and 13 columns. Its positive-label share is approximately 2.6%. The original analysis reports higher positive-label shares among records with less sleep or heavier social-media use. These are associations in the supplied dataset, not estimates for the wider teenage population.

![Sleep and target label](reports/figures/sleep_vs_depression.png)
![Social media and target label](reports/figures/social_media_vs_depression.png)
![Stress and anxiety](reports/figures/stress_anxiety_heatmap.png)

## Modelling

The existing pipeline uses median imputation and scaling for numeric columns, most-frequent imputation and one-hot encoding for categorical columns, and class-weighted logistic regression. A stratified 75/25 train/test split uses random seed 42.

The October 2026 reproduction check returned **ROC AUC 0.985** and **average precision 0.702**. Strongly structured labels and the small positive class limit interpretation. These are results from one held-out split, not cross-validated or externally validated clinical performance.

![Model coefficients](reports/figures/model_coefficients.png)

## Run locally

From the repository root:

```bash
cd teen_mental_health_project
python -m venv .venv
```

Activate `.venv\Scripts\Activate.ps1` in PowerShell or `source .venv/bin/activate` on macOS/Linux, then:

```bash
python -m pip install -r requirements.txt
python src/modeling.py
```

The modelling script prints metrics and does not save a trained model. To regenerate the processed CSV and target-distribution chart:

```bash
python src/data_prep.py
python src/visualize.py
```

These two commands overwrite their existing output files. Preserve copies before comparing with historical outputs. `visualize.py` regenerates only `target_distribution.png`; it does not recreate every figure. The notebook contains additional exploratory work and was not executed end to end in the review.

No credentials or external API calls are needed. The scripts locate their input files relative to their own project directory. Python 3.12 was used for the reproduction check; the requirements are not version-pinned.

## Limitations and responsible interpretation

The original source, collection method and redistribution terms of the dataset need confirmation. The existing analysis describes the target as synthetic or strongly rule-driven; provenance has not been independently established. This is not a diagnostic tool, and it does not establish that sleep or social-media changes cause clinical outcomes.

The data-preparation script's `risk_profile` values are descriptive rules within this exercise, not validated risk scores. No new personal data or source records were added. The existing licence is unchanged and does not establish rights to third-party data.

Future work: confirm provenance, document label construction and compare model stability across several splits. No new model claims are made until those checks are completed.
