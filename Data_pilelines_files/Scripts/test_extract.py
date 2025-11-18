"""
Integration test for extract_data() using real inputs.
Checks:
- extract_data() runs without errors
- Returns two DataFrames
"""

import sys
import os
import pandas as pd

# Ensure project root is in sys.path for direct execution
if __name__ == "__main__":
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.extract import extract_data

def test_extract_runs():
    df_reviews, products_df = extract_data()
    assert isinstance(df_reviews, pd.DataFrame)
    assert isinstance(products_df, pd.DataFrame)
    assert not df_reviews.empty, "Reviews DataFrame is empty"
    assert not products_df.empty, "Products DataFrame is empty"
    print(f"✅ Extract test passed. Reviews: {len(df_reviews)}, Products: {len(products_df)}")

if __name__ == "__main__":
    test_extract_runs()
