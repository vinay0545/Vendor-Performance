import sqlite3
import pandas as pd

conn = sqlite3.connect("inventory.db")

queries = {
    "Summary Rows": "SELECT COUNT(*) AS rows FROM vendor_sales_summary",

    "Summary Sales": """
        SELECT SUM(TotalSalesDollars) AS total_sales
        FROM vendor_sales_summary
    """,

    "Summary Purchase": """
        SELECT SUM(TotalPurchaseDollars) AS total_purchase
        FROM vendor_sales_summary
    """,

    "Summary Vendors": """
        SELECT COUNT(DISTINCT VendorNumber) AS vendors
        FROM vendor_sales_summary
    """
}

for name, query in queries.items():
    result = pd.read_sql_query(query, conn)
    print("\n", name)
    print(result)

conn.close()

import sqlite3
import pandas as pd

conn = sqlite3.connect("inventory.db")

query = """
SELECT
    COUNT(*) AS total_rows,
    COUNT(DISTINCT
        VendorNumber || '|' ||
        VendorName || '|' ||
        Brand || '|' ||
        Description || '|' ||
        PurchasePrice
    ) AS unique_rows
FROM vendor_sales_summary
"""

result = pd.read_sql_query(query, conn)

print(result)

conn.close()