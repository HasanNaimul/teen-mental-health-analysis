import pandas as pd
from pathlib import Path
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import average_precision_score, roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "raw" / "Teen_Mental_Health_Dataset.csv"

def train_model():
    df = pd.read_csv(DATA_PATH)
    X = df.drop(columns=["depression_label"])
    y = df["depression_label"]

    num_cols = X.select_dtypes(include="number").columns.tolist()
    cat_cols = X.select_dtypes(exclude="number").columns.tolist()

    preprocessor = ColumnTransformer(
        transformers=[
            ("num", Pipeline([
                ("imputer", SimpleImputer(strategy="median")),
                ("scaler", StandardScaler())
            ]), num_cols),
            ("cat", Pipeline([
                ("imputer", SimpleImputer(strategy="most_frequent")),
                ("onehot", OneHotEncoder(handle_unknown="ignore"))
            ]), cat_cols),
        ]
    )

    model = Pipeline([
        ("prep", preprocessor),
        ("clf", LogisticRegression(max_iter=2000, class_weight="balanced"))
    ])

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42, stratify=y
    )

    model.fit(X_train, y_train)
    proba = model.predict_proba(X_test)[:, 1]

    print("ROC AUC:", round(roc_auc_score(y_test, proba), 3))
    print("Average precision:", round(average_precision_score(y_test, proba), 3))

if __name__ == "__main__":
    train_model()
