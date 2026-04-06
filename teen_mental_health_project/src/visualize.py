import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "processed" / "teen_mental_health_processed.csv"
FIGURES = ROOT / "reports" / "figures"

def main():
    df = pd.read_csv(DATA_PATH)
    FIGURES.mkdir(parents=True, exist_ok=True)

    counts = df["depression_label"].value_counts().sort_index()
    ax = counts.plot(kind="bar")
    ax.set_xticklabels(["No depression", "Depression"], rotation=0)
    ax.set_title("Target Distribution")
    plt.tight_layout()
    plt.savefig(FIGURES / "target_distribution.png", bbox_inches="tight")

if __name__ == "__main__":
    main()
