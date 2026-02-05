# 📊 E-Commerce Business Analytics Framework

This repository contains a comprehensive end-to-end analytical framework designed to transform raw transactional data into actionable business intelligence. The project covers 12 critical dimensions of analysis used by industry-leading data teams.

---

## 🔍 1. Descriptive Analysis

*What happened?*
Focuses on historical data to summarize business performance for executive reviews.

* **Key Metrics:** Total revenue, order volume, and unique customer count.
* **Dimensions:** Sales by category, geographic performance (Country/State), and payment method distribution.
* **Operational Health:** Breakdown of "Delivered" vs. "Returned" statuses.

---

## 🧪 2. Diagnostic Analysis

*Why did it happen?*
Deep-dives into specific drivers to identify operational bottlenecks or successes.

* **Correlation Studies:** Analyzing the relationship between **Discount %** and **Sales Volume**.
* **Root Cause Analysis:** Investigating high return rates in specific categories or shipping cost impacts by region.
* **Implementation Example:**

```python
# Calculating Return Rate by Category
return_rate = (
    df[df['OrderStatus']=='Returned'].groupby('Category')['OrderID'].count() /
    df.groupby('Category')['OrderID'].count()
).fillna(0)

```

---

## 📈 3. Time-Series Analysis

*When does it happen?*
Detecting seasonality and trends to inform inventory and staffing.

* **Trends:** Monthly/Weekly sales growth.
* **Seasonality:** Identifying high-revenue months (e.g., Q4 holiday peaks).
* **Cycle Analysis:** Comparing weekend vs. weekday consumer behavior.

---

## 👥 4. Customer Analysis (RFM)

*Who is buying?*
Segmentation strategies for targeted CRM and marketing.

* **RFM Analysis (Industry Standard):**
| Metric | Meaning | Business Value |
| :--- | :--- | :--- |
| **Recency** | Days since last purchase | Identifying churn risk |
| **Frequency** | Total number of orders | Measuring loyalty |
| **Monetary** | Total spend amount | Identifying VIP customers |

---

## 📦 5. Product & Category Analysis

*What sells?*
Optimizing the product catalog and pricing tiers.

* **Performance Ranking:** Identifying "Hero" products vs. "Laggards" (to be discontinued).
* **Contribution:** Which categories drive the highest profit margins?
* **Sensitivity:** Analyzing how specific brands react to price changes.

---

## 💸 6. Price & Discount Analysis

*How price affects sales?*
High-value analysis for revenue management and margin protection.

* **Price Elasticity:** Quantifying how demand shifts when prices change.
* **Discount Efficiency:** Identifying "Profit Leaks" due to over-discounting.
* **Regression:** Modeling the impact of Unit Price on Quantity sold.

---

## 💰 7. Profitability Analysis

*What is actually profitable?*
Shifting focus from "Top-line" (Sales) to "Bottom-line" (Profit).

* **Net Revenue:** Calculating profit after Shipping, Taxes, and Discounts.
* **Efficiency:** Finding high-volume products that suffer from low margins.
* **Geographic Profit:** Identifying regions where shipping costs eat the entire margin.

---

## 📉 8. Regression Analysis

*What drives revenue?*
Using statistical modeling to prove analytical maturity.

* **Target Variables:** Revenue, Profit, Quantity.
* **Predictors:** Unit Price, Discount level, Tax, and Shipping Cost.
* **Goal:** Quantify the exact impact of a 1% increase in discount on total volume.

---

## 🌍 9. Geographical Analysis

*Where to invest?*
Market expansion and regional resource allocation.

* **Market Share:** Revenue distribution across countries and states.
* **Hotspots:** Identifying high-demand cities for potential warehouse expansion.

---

## ⚙️ 10. Operational Analysis

*Process efficiency*
Identifying friction in the supply chain and fulfillment process.

* **Lead Times:** Analyzing delays in order fulfillment.
* **Failure Rates:** Investigating payment method failures and cancellation reasons.

---

## 🔮 11. Predictive Analysis

*What will happen next?*
Leveraging Machine Learning for proactive decision-making.

* **Forecasting:** Predicting next month's sales using ARIMA or Prophet.
* **Churn Prediction:** Identifying customers likely to stop buying.
* **CLV:** Predicting the future Lifetime Value of a new customer.

---

## 🖥️ 12. Executive Dashboarding

*Final Delivery*
Consolidating all insights into a single source of truth for leadership.

* **KPI Overview:** Real-time revenue and margin tracking.
* **Visual Storytelling:** Moving from high-level trends to granular profit drivers.
* **Actionable Insights:** Directing stakeholders toward specific "Next Steps."

---

### How to use this repository

1. **Data Cleaning:** See `notebooks/01_cleaning.ipynb`
2. **Exploratory Analysis:** See `notebooks/02_eda.ipynb`
3. **Modeling:** See `notebooks/03_regression_modeling.ipynb`