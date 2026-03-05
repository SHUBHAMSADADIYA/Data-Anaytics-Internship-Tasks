# Data Analytics Internship Tasks

This repository contains the complete portfolio of advanced data analytics projects completed during the Data Analytics Internship. The projects encompass end-to-end data processing pipelines—from raw data extraction and intensive data cleaning using Python, to advanced feature engineering and interactive data visualization using tools like Microsoft Excel and Power BI.

---

## 📂 Project Overview

The repository is divided into three comprehensive analytical tasks, detailed below:

### 1. [Task 1: Superstore Sales Analysis & Dashboard](FUTURE_DS_01/)
A complete business intelligence project focused on retail transactional data.
- **Objective:** Identify key sales trends, regional profitability, and product category dynamics.
- **Process:** Data standardization (snake_case columns, datetime parsing), noise reduction, and Profit Margin feature engineering using Python (Pandas).
- **Visualization:** A stakeholder-ready Interactive Excel Dashboard (`dashboard.xlsx`) tracking KPIs over time.

### 2. [Task 2: RavenStack Synthetic SaaS Dataset](FUTURE_DS_02/)
An exploratory data analysis of a multi-table, event-driven dataset for a stealth-mode SaaS startup.
- **Objective:** Discover primary drivers behind user conversions, support workloads, and subscription churn patterns.
- **Process:** Managing relational data across multiple entities (Accounts, Subscriptions, Feature Usage, Support Tickets, and Churn Events), handling complex statistical distributions, and tracking temporal subscription logic.
- **Visualization:** Analyzed through comprehensive tracking dashboards mapping product latency, feature adoption, and SaaS metric KPIs.

### 3. [Task 3: E-Commerce Funnel Analysis](FUTURE_DS_03/)
A user journey analysis project to optimize an e-commerce sales funnel.
- **Objective:** Identify high-drop-off points, conversion bottlenecks, and regional performance trends to enhance platform revenue.
- **Process:** Processing granular user event logs (`funnel_analysis_data.csv`) encompassing sessions from initial browsing to final transaction checkout.
- **Visualization:** An interactive **Power BI Dashboard** (`Funnel_Aanalysis.pbix`) presenting step-by-step drop-off visualizations, acquisition efficiency by channel, and overall demographic behavior.

---

## 🛠️ Technology Stack
* **Python (3.8+)**: Core language used for data engineering logic.
* **Pandas & NumPy**: Essential libraries applied for stringent data manipulation, aggregation, and null-value handling.
* **Microsoft Excel**: Used for building preliminary executive dashboards and visualizing normalized datasets.
* **Power BI**: Handled complex relationship modeling and deep-dive interactive visualizations for the funnel analysis.
* **fpdf2**: Programmatic PDF report generation directly from analytical summaries.

---

## 🚀 Getting Started

Each individual project directory contains its own specific instructions and requirements. However, as a general guideline:

1. **Environment Setup:** Ensure Python 3.8+ and the `pandas` library are installed on your local environment (`pip install pandas`).
2. **Execute Pipelines:** Navigate into the specific task folders (e.g., `FUTURE_DS_01/Notebooks`) and run the Python processing scripts (`Cleaning.py`, `Profite_Margin.py`, etc.).
3. **View Dashboards:** Open the resulting `.xlsx` or `.pbix` files located in the respective `Dashboard/` directories to interact with the visualizations.

---
*Developed by Shubham Girishbhai Sadadiya (23CS407028)*
*In Fulfillment of B.Sc. IT Sem V (A.Y. 2025–2026)*
