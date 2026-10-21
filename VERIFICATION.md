# Verification notes — 21 October 2026

Documentation-only changes. Before and after the edits, the existing preparation function returned 1,200 rows and the existing model script returned ROC AUC 0.985 and average precision 0.702. Model execution used `python teen_mental_health_project/src/modeling.py` from the repository root.

The raw CSV contains 13 columns and 31 positive target labels (approximately 2.6%). The preparation function was called without writing its returned dataframe to disk. The notebook and all figures were not regenerated. There is no automated test suite in this repository.

All original data, code, notebook, figures, requirements and licence are preserved. Links to retained assets were checked. README claims of included Power BI files were corrected because those files are absent.

The source dataset's provenance and redistribution terms remain unresolved. The original analysis describes strongly structured labels; clinical validity is not established. These model metrics describe a single stratified holdout, not cross-validation or external validation.

Environment: Python 3.12.14, pandas 2.2.3 and scikit-learn 1.8.0. No dependency files were changed.
