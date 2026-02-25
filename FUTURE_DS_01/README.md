# Superstore Sales Analysis & Dashboard


## 1. Executive Summary
This project aims to provide actionable business intelligence based on the Superstore retail dataset. By establishing a robust data processing pipeline and an interactive reporting interface, we identify key trends in sales performance, regional profitability, and product category dynamics.

The solution transforms raw transactional data into a clean, analytical dataset, enriched with key metrics such as Profit Margin, culminating in a stakeholder-ready Excel Dashboard.

## 2. Project Architecture

The repository is organized to separate data storage, processing logic, and presentation layers:

```
├── Assets/          # Static assets and resources
├── Dashboard/       # Presentation layer
│   └── dashboard.xlsx  # Interactive Excel Dashboard for stakeholders
├── Data/            # Data storage layer
│   ├── superstore.csv          # Raw input data
│   ├── superstore_cleaned.csv  # Normalized intermediate data
│   └── Superstore_Data.xlsx    # Final enriched dataset
└── Notebooks/       # ETL and analysis scripts
    ├── Cleaning.py         # Data cleaning and standardization pipeline
    └── Profite_Margin.py   # Feature engineering (Profit aggregation & margin calc)
```

## 3. Data Pipeline & Methodology

Our analytical workflow follows a strict ETL (Extract, Transform, Load) process to ensure data integrity:

### Phase 1: Data Cleaning (`Cleaning.py`)
- **Standardization**: All column names are converted to snake_case for consistency.
- **Data Type Casting**: `order_date` and `ship_date` are converted to datetime objects to facilitate time-series analysis.
- **Noise Reduction**: Removal of summary rows (e.g., "Grand Total") to prevent skewing of aggregations.
- **Normalization**: Text data is sanitized to remove artifacts.

### Phase 2: Feature Engineering (`Profite_Margin.py`)
- **Profit Margin Calculation**: A critical KPI, calculated as:
  $$ \text{Profit Margin (\%)} = \left( \frac{\text{Profit}}{\text{Sales}} \right) \times 100 $$
  This metric helps identify high-efficiency products and regions regardless of the raw sales volume.

### Phase 3: Reporting
- The processed data is exported to `Superstore_Data.csv/xlsx`.
- The **Executive Dashboard** (`dashboard.xlsx`) consumes this data to visualize:
  - Total Sales & Profit trends over time.
  - Regional performance hotspots.
  - Category-wise profit distribution.

## 4. Getting Started

### Prerequisites
- Python 3.8+
- Pandas library (`pip install pandas`)
- Microsoft Excel (2016 or later)

### Execution Steps
1. **Run the Cleaning Pipeline**:
   ```bash
   cd Notebooks
   python Cleaning.py
   ```
2. **Generate Metrics**:
   ```bash
   python Profite_Margin.py
   ```
3. **Launch Dashboard**:
   Open `Dashboard/dashboard.xlsx` to view the latest insights. Ensure the data connection is refreshed if applicable.

## 5. Future Scope
- Integration of a SQL database for scalable data storage.
- Migration of the dashboard to Tableau/PowerBI for advanced interactivity.
- Automated weekly reporting scripts.

---
*Confidential - Internal Use Only*
