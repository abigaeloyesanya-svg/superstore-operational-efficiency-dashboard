"""
data_cleaning.py

Reproduces the cleaning steps applied to the raw Superstore Sales Dataset
before it was used in the Power BI dashboard and the executive summary.

Two issues were identified and removed:
  1. Invalid/missing Ship Mode values (6 rows)
  2. Zero-price rows: both cost price and List Price recorded as 0 (507 rows)

Run:
    python data_cleaning.py

Input:  superstore_raw.csv
Output: superstore_cleaned.csv (9,481 rows, from an original 9,994)
"""

import pandas as pd

RAW_PATH = "superstore_raw.csv"
CLEAN_PATH = "superstore_cleaned.csv"


def main():
    # keep_default_na=False is deliberate: pandas' default NA handling silently
    # converts literal strings like "N/A" into true nulls, which hides what's
    # actually in the raw data. Reading raw strings first, then handling
    # invalid values explicitly, avoids that trap.
    df = pd.read_csv(RAW_PATH, keep_default_na=False)
    print(f"Raw rows: {len(df)}")

    # --- Issue 1: invalid/missing Ship Mode -------------------------------
    invalid_ship_mode = ["Not Available", "unknown", "N/A", ""]
    ship_mode_mask = df["Ship Mode"].isin(invalid_ship_mode)
    print(f"Invalid Ship Mode rows removed: {ship_mode_mask.sum()}")
    df = df.loc[~ship_mode_mask].copy()

    # --- Issue 2: zero-price rows ------------------------------------------
    # Concentrated in cheap Office Supplies sub-categories (up to 20.7% of all
    # Fasteners rows), not evenly distributed, which rules out a legitimate
    # "free item" explanation and points to a data entry gap instead.
    zero_price_mask = (df["cost price"].astype(float) == 0) & (
        df["List Price"].astype(float) == 0
    )
    print(f"Zero-price rows removed: {zero_price_mask.sum()}")
    df = df.loc[~zero_price_mask].copy()

    print(f"Final cleaned rows: {len(df)}")

    # --- Derived financial fields -------------------------------------------
    # Sales, Cost, and Profit are not provided in the raw file and are
    # derived here for reference; the same formulas are implemented as DAX
    # measures in the Power BI file itself.
    df["Sales"] = (
        df["List Price"].astype(float)
        * df["Quantity"].astype(float)
        * (1 - df["Discount Percent"].astype(float) / 100)
    )
    df["Cost"] = df["cost price"].astype(float) * df["Quantity"].astype(float)
    df["Profit"] = df["Sales"] - df["Cost"]

    df.to_csv(CLEAN_PATH, index=False)
    print(f"Saved cleaned dataset to {CLEAN_PATH}")


if __name__ == "__main__":
    main()
