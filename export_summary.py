import sqlite3
import pandas as pd

conn = sqlite3.connect("inventory.db")

df = pd.read_sql_query(
    "SELECT * FROM vendor_sales_summary",
    conn
)

df.to_csv("vendor_sales_summary.csv", index=False)

conn.close()

print("CSV Export Completed!")
print("Rows:", len(df))
print("Columns:", len(df.columns))

# ---------------- BRAND PERFORMANCE ----------------

brand_performance = df.groupby("Brand", as_index=False).agg({
    "TotalPurchaseDollars": "sum",
    "TotalSalesDollars": "sum",
    "GrossProfit": "sum",
    "TotalPurchaseQuantity": "sum",
    "TotalSalesQuantity": "sum"
})

brand_performance["ProfitMargin"] = (
    brand_performance["GrossProfit"]
    / brand_performance["TotalSalesDollars"]
) * 100

brand_performance["StockTurnover"] = (
    brand_performance["TotalSalesQuantity"]
    / brand_performance["TotalPurchaseQuantity"]
)

brand_performance.to_csv(
    "BrandPerformance.csv",
    index=False
)

print("BrandPerformance CSV Created!")
print("Rows:", len(brand_performance))
print("Columns:", len(brand_performance.columns))

# ---------------- LOW TURNOVER VENDOR ----------------

low_turnover_vendor = (
    df[df["StockTurnover"] < 1]
    .groupby("VendorName", as_index=False)
    .agg(
        AvgStockTurnOver=("StockTurnover", "mean")
    )
)

low_turnover_vendor.to_csv(
    "LowTurnoverVendor.csv",
    index=False
)

print("LowTurnoverVendor CSV Created!")
print("Rows:", len(low_turnover_vendor))
print("Columns:", len(low_turnover_vendor.columns))


# ---------------- PURCHASE CONTRIBUTION ----------------

purchase_contribution = (
    df.groupby("VendorName", as_index=False)["TotalPurchaseDollars"]
      .sum()
)

total_purchase = purchase_contribution["TotalPurchaseDollars"].sum()

purchase_contribution["PurchaseContribution%"] = (
    purchase_contribution["TotalPurchaseDollars"]
    / total_purchase
) * 100

purchase_contribution = purchase_contribution.sort_values(
    "PurchaseContribution%",
    ascending=False
)

purchase_contribution["Cumulative_Contribution%"] = (
    purchase_contribution["PurchaseContribution%"].cumsum()
)

purchase_contribution.to_csv(
    "PurchaseContribution.csv",
    index=False
)

print("PurchaseContribution CSV Created!")
print("Rows:", len(purchase_contribution))
print("Columns:", len(purchase_contribution.columns))

