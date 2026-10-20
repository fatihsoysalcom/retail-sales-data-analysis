import pandas as pd

# Sample retail sales data
data = {
    'ProductID': ['A101', 'B202', 'A101', 'C303', 'B202', 'A101', 'C303', 'B202', 'A101', 'C303'],
    'Category': ['Electronics', 'Clothing', 'Electronics', 'Home Goods', 'Clothing', 'Electronics', 'Home Goods', 'Clothing', 'Electronics', 'Home Goods'],
    'Sales': [1200, 50, 1150, 200, 60, 1250, 220, 55, 1180, 210],
    'Date': pd.to_datetime(['2023-01-15', '2023-01-16', '2023-01-17', '2023-01-18', '2023-01-19', '2023-01-20', '2023-01-21', '2023-01-22', '2023-01-23', '2023-01-24'])
}

df = pd.DataFrame(data)

# --- Core Data Analysis Tasks for a Retail Analyst ---

# 1. Total Sales by Category
print("--- Total Sales by Category ---")
sales_by_category = df.groupby('Category')['Sales'].sum().reset_index()
print(sales_by_category)
print("\n")

# 2. Top Selling Products (by total sales)
print("--- Top Selling Products ---")
top_products = df.groupby('ProductID')['Sales'].sum().nlargest(3).reset_index()
print(top_products)
print("\n")

# 3. Sales Trend Over Time (daily)
print("--- Daily Sales Trend ---")
daily_sales = df.groupby(df['Date'].dt.date)['Sales'].sum().reset_index()
daily_sales['Date'] = pd.to_datetime(daily_sales['Date'])
print(daily_sales.sort_values('Date'))
print("\n")

# 4. Average Sale Value per Product
print("--- Average Sale Value per Product ---")
avg_sale_per_product = df.groupby('ProductID')['Sales'].mean().reset_index()
print(avg_sale_per_product)
print("\n")

# 5. Identify potential insights (e.g., high sales in Electronics)
print("--- Potential Insights ---")
# Example: Electronics category has significantly higher sales values than others.
# This could prompt further investigation into pricing, marketing, or product features.
print("The 'Electronics' category shows the highest total sales, indicating its importance to revenue.")
print("Further analysis could explore average transaction value and customer demographics for this category.")
