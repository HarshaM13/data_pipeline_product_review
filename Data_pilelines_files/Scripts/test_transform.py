"""
Integration test for transform_data() using extract_data() output.
Checks:
- Combined DataFrame is created
- CSV file is saved in data/processed/
"""

import sys
import os
from pathlib import Path
import pandas as pd

# Ensure project root is in sys.path for direct execution
if __name__ == "__main__":
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.extract import extract_data
from src.transform import transform_data

def test_transform_runs():
    df_reviews, products_df = extract_data()
    combined = transform_data(df_reviews, products_df)

    assert isinstance(combined, pd.DataFrame)
    assert len(combined) == len(df_reviews)  # Left join keeps all reviews

    base_dir = Path(__file__).resolve().parent.parent
    csv_path = base_dir / "data" / "processed" / "reviews_products.processed.csv"
    assert csv_path.exists(), f"Expected file not found: {csv_path}"

    print(f"✅ Transform test passed. Combined shape: {combined.shape}")

if __name__ == "__main__":
    test_transform_runs()