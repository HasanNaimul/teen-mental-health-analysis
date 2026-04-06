import pandas as pd
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW_PATH = ROOT / "data" / "raw" / "Teen_Mental_Health_Dataset.csv"
OUTPUT_PATH = ROOT / "data" / "processed" / "teen_mental_health_processed.csv"

def build_dataset() -> pd.DataFrame:
    df = pd.read_csv(RAW_PATH)

    df["sleep_bucket"] = pd.cut(
        df["sleep_hours"],
        bins=[0, 5.99, 6.99, 7.99, 24],
        labels=["<6h", "6-6.9h", "7-7.9h", "8h+"],
        include_lowest=True,
    )
    df["social_media_bucket"] = pd.cut(
        df["daily_social_media_hours"],
        bins=[0, 1.99, 3.99, 5.99, 8.01],
        labels=["0-2h", "2-4h", "4-6h", "6h+"],
        include_lowest=True,
    )
    df["stress_bucket"] = pd.cut(
        df["stress_level"],
        bins=[0, 3, 6, 8, 10],
        labels=["Low (1-3)", "Moderate (4-6)", "High (7-8)", "Very high (9-10)"],
        include_lowest=True,
    )

    df["risk_profile"] = "Lower observed risk"
    df.loc[
        (df["sleep_hours"] < 6)
        & (df["daily_social_media_hours"] >= 5)
        & (df["stress_level"] >= 7)
        & (df["anxiety_level"] >= 7),
        "risk_profile",
    ] = "Highest risk pattern"
    df.loc[
        (df["risk_profile"] == "Lower observed risk")
        & (df["sleep_hours"] < 6)
        & ((df["stress_level"] >= 7) | (df["anxiety_level"] >= 7)),
        "risk_profile",
    ] = "Sleep + emotional strain"
    df.loc[
        (df["risk_profile"] == "Lower observed risk")
        & (df["daily_social_media_hours"] >= 5)
        & ((df["stress_level"] >= 7) | (df["anxiety_level"] >= 7)),
        "risk_profile",
    ] = "Heavy usage + emotional strain"

    return df

if __name__ == "__main__":
    df = build_dataset()
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUTPUT_PATH, index=False)
    print(f"Saved processed dataset to {OUTPUT_PATH}")
