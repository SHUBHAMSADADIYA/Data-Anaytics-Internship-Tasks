# Funnel Analysis: E-Commerce User Journey

## 1. Executive Summary
This project focuses on analyzing the user journey of an e-commerce platform to identify conversion bottlenecks and optimize the sales funnel. By tracking user events from the initial browse to the final purchase, we can understand high-drop-off points, regional performance, and device-specific behavior.

The analysis utilizes a synthetic event-driven dataset to simulate real-world e-commerce scenarios, culminating in a Power BI dashboard designed for stakeholder decision-making.

## 2. Project Architecture

The repository is organized as follows:

```
├── Assets/          # Design assets and static resources
├── Dashboard/       # Interactive reporting layer
│   └── Funnel_Aanalysis.pbix  # Power BI Dashboard (Analysis & Viz)
└── Data/            # Data storage layer
    └── funnel_analysis_data.csv  # Granular user event logs
```

## 3. Data Pipeline & Schema

### Data Description (`funnel_analysis_data.csv`)
The dataset contains transaction-level event data with the following primary attributes:

| Column | Type | Description |
| :--- | :--- | :--- |
| `User_ID` | ID | Unique identifier for the user. |
| `Session_ID` | ID | Unique identifier for the browsing session. |
| `Event` | Categorical | The user action: `Browse`, `Add to Cart`, `Checkout`, `Purchase`. |
| `Timestamp` | Datetime | Exact time of the event. |
| `Device` | Categorical | Device used: `Desktop`, `Mobile`, `Tablet`. |
| `Region` | Categorical | User's geographic location (`West`, `East`, `North`, `South`). |
| `Channel` | Categorical | Acquisition channel (`Organic`, `Email`, `Social Media`, `Google Ads`). |
| `Product_Category`| Categorical | Category of interest (e.g., `Home`, `Beauty`, `Electronics`). |
| `Revenue` | Currency | Transaction value (only populated for `Purchase` events). |
| `Bounce_Flag` | Boolean | Indicates if the session was a single-event session (`Yes`/`No`). |

### Key Performance Indicators (KPIs)
- **Conversion Rate**: Percentage of users moving from one funnel stage to the next.
- **Overall Conversion Rate**: Percentage of browsing users who completed a purchase.
- **Bounce Rate**: Ratio of sessions where users exited after a single event.
- **Average Revenue Per User (ARPU)**: Total revenue divided by unique customers.

## 4. Analysis & Dashboard
The **Funnel Analysis Dashboard** (`Funnel_Aanalysis.pbix`) provides:
- **Funnel Visualization**: Step-by-step drop-off analysis.
- **Revenue Insights**: Top-performing categories and channels.
- **Demographic Breakdown**: Performance across regions and devices.
- **Acquisition Efficiency**: Comparison of conversion rates across different marketing channels.

## 5. Future Scope
- **Time-to-Conversion Analysis**: Measuring the average time spent between funnel stages.
- **Churn Prediction**: Identifying users at risk of abandoning the funnel based on behavior patterns.
- **A/B Testing Integration**: Analyzing the impact of UI/UX changes on conversion metrics.

---
*Confidential - Internal Use Only*
