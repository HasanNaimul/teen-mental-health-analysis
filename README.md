# Teen mental health: a dataset case study

Python exploration of associations between sleep, social-media use, stress, anxiety and a depression label in a 1,200-row dataset. The project demonstrates data preparation, visual analysis and a class-weighted logistic-regression pipeline.

**This is an analytical exercise, not a diagnostic tool or clinical evidence.** The dataset's original provenance has not been verified. Its labels appear strongly rule-driven, so model performance should not be generalised to real people.

![Target distribution](teen_mental_health_project/reports/figures/target_distribution.png)

## Explore the project

- [Analysis, findings and setup](teen_mental_health_project/README.md)
- [Notebook](teen_mental_health_project/notebooks/01_teen_mental_health_analysis.ipynb)
- [Python scripts](teen_mental_health_project/src)
- [Existing figures](teen_mental_health_project/reports/figures)

The existing project folder and all data, notebooks and figures are preserved. A processed CSV can be imported into Power BI, but no PBIX, Power BI build guide, DAX file or theme file is present in this repository.

## Verified results and limits

The supplied data contains 1,200 records and 13 columns. About 2.6% of records have a positive target label. Running the existing model script reproduced ROC AUC **0.985** and average precision **0.702** in the October 2026 review. It uses a stratified 75/25 split with `random_state=42`, imputation, scaling, categorical encoding and class-weighted logistic regression.

Those metrics describe one split of this dataset. They do not demonstrate clinical validity or causal effects. No original data values, model logic or saved results were changed. There is no automated test suite; the review used script execution and input/output checks.

The existing [MIT licence](teen_mental_health_project/LICENSE) remains unchanged. Confirm the source dataset's licence and provenance separately before wider reuse.
