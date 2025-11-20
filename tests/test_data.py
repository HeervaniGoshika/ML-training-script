import pandas as pd
import os

def test_data_file_exists():
    assert os.path.exists("data.csv"), "data.csv file is missing!"

def test_data_schema():
    df = pd.read_csv("data.csv")

    # Required columns in your training script
    expected_columns = ["feature1", "feature2", "target"]

    for col in expected_columns:
        assert col in df.columns, f"{col} column missing in data.csv!"

    # Check numeric types (important for LinearRegression)
    assert pd.api.types.is_numeric_dtype(df["feature1"]), "feature1 must be numeric"
    assert pd.api.types.is_numeric_dtype(df["feature2"]), "feature2 must be numeric"
    assert pd.api.types.is_numeric_dtype(df["target"]), "target must be numeric"
