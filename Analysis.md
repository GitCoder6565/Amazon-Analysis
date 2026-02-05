1️⃣ DESCRIPTIVE ANALYSIS (What happened?)

Purpose: Understand business performance
Industry usage: Monthly business review, executive dashboards

Examples

Total revenue, orders, customers

Category-wise sales

Country / state performance

Payment method usage

Order status breakdown

📌 Key questions answered:

Which category sells the most?

Where is most revenue coming from?

How many orders are delivered vs returned?

2️⃣ DIAGNOSTIC ANALYSIS (Why did it happen?)

Purpose: Identify drivers and issues
Industry usage: Operations & strategy teams

Examples

Why are returns higher in some categories?

Why does revenue vary by region?

Does discount increase sales volume?

📌 Analyses

Discount vs quantity correlation

Return rate by category / brand

Shipping cost impact by region

```python
return_rate = (
    df[df['OrderStatus']=='Returned']
    .groupby('Category')['OrderID']
    .count()
    /
    df.groupby('Category')['OrderID'].count()
).fillna(0)
```

3️⃣ TIME-SERIES ANALYSIS (When does it happen?)

Purpose: Trend & seasonality detection
Industry usage: Forecasting, inventory planning

Examples

Monthly / weekly sales trends

Seasonal demand by category

Weekend vs weekday sales

📌 Questions answered:

When should inventory be stocked?

Which months are high-revenue months?

4️⃣ CUSTOMER ANALYSIS (Who is buying?)

Purpose: Customer segmentation & retention
Industry usage: CRM, marketing campaigns

Analyses

Repeat vs one-time customers

High-value customers

Geographic customer concentration

RFM Analysis (VERY IMPORTANT)
Metric	Meaning
Recency	How recently customer bought
Frequency	How often they buy
Monetary	How much they spend

This is industry-standard.

5️⃣ PRODUCT & CATEGORY ANALYSIS (What sells?)

Purpose: Product optimization
Industry usage: Catalog & pricing teams

Examples

Top / bottom products

Brand performance

Category profit contribution

Discount sensitivity per product

📌 Questions:

Which products should be promoted?

Which products should be discontinued?

6️⃣ PRICE & DISCOUNT ANALYSIS (How price affects sales)

Purpose: Pricing strategy
Industry usage: Revenue management

Analyses

Discount vs revenue regression

Price elasticity by category

Profit loss due to over-discounting

📌 This is high-value analysis in interviews.

7️⃣ PROFITABILITY ANALYSIS (What is actually profitable?)

Purpose: Cost control & margin optimization
Industry usage: Finance & operations

Analyses

Profit by category / country

Shipping cost vs profit

Tax impact on net revenue

Low-margin high-volume products

📌 Executives care about profit, not sales.

8️⃣ REGRESSION ANALYSIS (What drives revenue?)

Purpose: Quantify impact of variables
Industry usage: Data science & strategy teams

Regression Targets

Revenue

Profit

Quantity sold

Predictors

UnitPrice

Discount

Quantity

ShippingCost

Tax

📌 This proves analytical maturity.

9️⃣ GEOGRAPHICAL ANALYSIS (Where to invest?)

Purpose: Market expansion
Industry usage: Regional growth teams

Examples

Country vs revenue share

State-wise performance

City-level demand hotspots

🔟 OPERATIONAL ANALYSIS (Process efficiency)

Purpose: Improve delivery & fulfillment
Industry usage: Supply chain teams

Analyses

Order status delays

Cancellation & return reasons

Payment method failures

1️⃣1️⃣ PREDICTIVE ANALYSIS (Next-level)

Purpose: Forecast future outcomes
Industry usage: Planning & AI teams

Examples

Sales forecasting (next month)

Customer churn prediction

High-value customer prediction

1️⃣2️⃣ EXECUTIVE DASHBOARDING (Final Output)

Purpose: Decision-making
Industry usage: Leadership dashboards

Dashboard Sections

KPIs

Trends

Category & region insights

Profit drivers

Regression insights