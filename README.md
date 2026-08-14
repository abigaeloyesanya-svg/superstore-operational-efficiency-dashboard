# Superstore Operational Efficiency Dashboard

Executive-level BI dashboard and business recommendation built for a simulated board presentation, analyzing profitability, discounting, and shipping efficiency, not just sales volume, using a modified Superstore retail dataset.

**Live write-up:** [Notion executive summary](https://app.notion.com/p/3bb5420aae2d81c09c56ef27388a4eba)

---

## Business Question

The brief: build a single-view executive dashboard and a 3-point action plan that tells a CEO a clear, defensible story about the company's operational health, ahead of a board meeting.

## Key Finding

Profit margin was essentially flat year over year (+0.68%), not because the business is shrinking, but because it is quietly giving away margin through discounting faster than it is growing it back. A 5% discount runs nearly 3 percentage points lower margin than a 2% one, and two product lines, Phones and Chairs, account for over $117,000 of that loss on their own.

## Recommendations (ranked by priority)

| # | Recommendation | Estimated Impact |
|---|---|---|
| 1 | Cap discounts at 3–4% on Phones and Chairs | ~$9,200 (targeted) up to ~$30,000 (company-wide) |
| 2 | Reprice or bundle Fasteners before it turns unprofitable | Protects a category running at $458.60 total profit over 2 years |
| 3 | Review Same Day shipping economics (8.8% margin vs. 9.5% on Standard Class) | ~$4,000 on current volume |

Full reasoning, risks, and a section on a state-level margin pattern that was investigated and ruled out (small sample size) are in the [Notion executive summary](https://app.notion.com/p/3bb5420aae2d81c09c56ef27388a4eba) and the presentation deck below.

## Files in This Repository

| File | What it is |
|---|---|
| `superstore_raw.csv` | Original dataset, 9,994 rows |
| `superstore_cleaned.csv` | Cleaned dataset used in analysis, 9,481 rows |
| `data_cleaning.py` | Reproducible cleaning + derived-field script |
| `Superstore_Operational_Efficiency_Dashboard.pbix` | The actual interactive Power BI file |
| `Superstore_Operational_Efficiency_Dashboard.pdf` | Static export of the full dashboard |
| `Executive_Summary.pptx` | 5-slide executive presentation | 

## Dataset

Superstore-style retail dataset, 9,994 orders, FY2022–2023. Unlike the commonly-used Kaggle version, this file does **not** include pre-built `Sales` or `Profit` columns, a returns table, customer IDs, or ship dates, only `cost price`, `List Price`, `Quantity`, `Discount Percent`, and shipping method. All financial fields were derived (see `data_cleaning.py` and the DAX measures in the `.pbix` file).

**Data cleaning:** two issues identified and removed before analysis.
1. 6 rows (0.06%) with missing/invalid `Ship Mode` values
2. 507 rows (5.1%) with both `cost price` and `List Price` recorded as $0, concentrated in specific low-cost sub-categories (up to 20.7% of Fasteners), identified as a data entry gap rather than a legitimate business pattern

**Final analysis dataset:** 9,481 clean records.

## Methodology

- **Sales** = List Price × Quantity × (1 − Discount % / 100)
- **Cost** = cost price × Quantity
- **Profit** = Sales − Cost
- All KPIs and chart values were independently verified against manual calculations before being trusted, including catching and fixing a filter-context bug in the original YoY growth DAX measure.

## Dashboard

Built in Power BI Desktop. 4 KPI cards, 6 visuals (line, bar, column, treemap, matrix, filled map), Year and Region slicers. Open `Superstore_Operational_Efficiency_Dashboard.pbix` in Power BI Desktop for the full interactive version, or view `Superstore_Operational_Efficiency_Dashboard.pdf` for a static export.

## Tools Used

Power BI Desktop (DAX, Power Query) · Python (pandas, for data auditing and cross-verification) · Notion · PowerPoint

## Limitations

This dataset does not include customer-level data, returns data, or actual shipping-time data. These are stated explicitly in the executive summary rather than worked around or implied.

## Author

Oluwapelumi Abigael Oyesanya, Data Analyst
[LinkedIn](https://www.linkedin.com/in/oluwapelumi-oyesanya) · [Email](mailto:abigaeloyesanya@gmail.com)
