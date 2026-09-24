# 📊 Vendor Performance Analysis

## 📌 Project Overview

**Vendor Performance Analysis** is a data analytics project focused on analyzing vendor sales, purchases, inventory, pricing, and profitability data.

The project uses Python, Pandas, SQL/SQLite, statistical analysis, and data visualization techniques to transform raw business data into meaningful insights.

The main objective is to understand vendor performance and identify patterns related to sales, purchasing, profitability, and inventory turnover.

## 🎯 Business Objectives

This project answers important business questions such as:

* Which vendors generate the highest sales?
* Which vendors contribute the most to total purchases?
* Which vendors have higher profit margins?
* Which brands perform better?
* Which vendors have low inventory turnover?
* How does sales performance differ between high-sales and low-sales vendors?
* Is there a statistical difference in profit margins between high-sales and low-sales vendors?

---

## 🛠️ Tools & Technologies

| Tool             | Purpose                      |
| ---------------- | ---------------------------- |
| Python           | Data analysis and processing |
| Pandas           | Data manipulation            |
| NumPy            | Numerical calculations       |
| Matplotlib       | Data visualization           |
| Seaborn          | Statistical visualization    |
| SciPy            | Statistical testing          |
| SQLite           | Database storage             |
| SQL              | Data querying                |
| Jupyter Notebook | Analysis and experimentation |
| Git              | Version control              |
| GitHub           | Project hosting              |

---

## 📂 Project Structure

```text
Vendor-Performance/
│
├── data/
│
├── Exploratory_Data_Analysis.ipynb
├── Vendor_Performance_Analysis.ipynb
├── Vendore.ipynb
│
├── ingestion_db.py
├── Convert_csv.py
├── export_summary.py
├── get_vendor_summary.py
│
├── BrandPerformance.csv
├── LowTurnoverVendor.csv
├── PurchaseContribution.csv
├── vendor_sales_summary.csv
│
├── .gitignore
└── README.md
```

---

## 🔍 Project Workflow

```text
Raw Data
   ↓
Data Cleaning
   ↓
Exploratory Data Analysis
   ↓
Data Processing
   ↓
Vendor-Level Analysis
   ↓
Brand Analysis
   ↓
Profitability Analysis
   ↓
Statistical Analysis
   ↓
Business Insights
```

---

## 📊 Analysis Performed

### 1. Exploratory Data Analysis

The project begins with exploratory analysis to understand the structure and quality of the data.

The analysis includes:

* Dataset dimensions
* Data types
* Missing values
* Duplicate records
* Numerical summaries
* Distribution analysis
* Vendor-level exploration

---

### 2. Vendor Performance Analysis

Vendors are analyzed using important business metrics such as:

* Total Sales
* Total Purchases
* Gross Profit
* Profit Margin
* Sales Contribution
* Purchase Contribution

This helps understand differences in vendor performance.

---

### 3. Top Vendor Analysis

The project identifies vendors with high sales performance and examines their contribution to overall business sales.

---

### 4. Purchase Contribution Analysis

Vendor purchase data is analyzed to understand how much each vendor contributes to the overall purchasing activity.

The output is stored in:

```text
PurchaseContribution.csv
```

---

### 5. Brand Performance Analysis

Brand-level performance is analyzed using sales and profitability-related metrics.

The output is stored in:

```text
BrandPerformance.csv
```

---

### 6. Low-Turnover Vendor Analysis

Vendors with lower inventory turnover are identified for further analysis.

The output is stored in:

```text
LowTurnoverVendor.csv
```

---

### 7. Profit Margin Analysis

Profit margins are compared across vendors to understand the relationship between sales performance and profitability.

---

### 8. Statistical Testing

A **Two-Sample T-Test** is used to compare the profit margins of high-sales vendors and low-sales vendors.

The test helps determine whether the observed difference between the two groups is statistically significant.

---

## 📈 Generated Outputs

The project generates the following analysis files:

### Brand Performance

```text
BrandPerformance.csv
```

Contains brand-level performance information.

### Low Turnover Vendors

```text
LowTurnoverVendor.csv
```

Contains information related to vendors with lower inventory turnover.

### Purchase Contribution

```text
PurchaseContribution.csv
```

Shows vendor contribution to purchasing activity.

### Vendor Sales Summary

```text
vendor_sales_summary.csv
```

Contains summarized vendor-level sales information.

---

## 🗄️ Dataset Note

The original raw datasets contain very large files.

For this reason, large files such as:

```text
sales.csv
purchases.csv
inventory.db
```

are excluded from the GitHub repository using `.gitignore`.

This keeps the GitHub repository lightweight while the analysis code and notebooks remain available.

---

## 🚀 How to Run the Project

### Step 1 — Clone the Repository

```bash
git clone https://github.com/vinay0545/Vendor-Performance.git
```

### Step 2 — Open the Project

```bash
cd Vendor-Performance
```

### Step 3 — Install Required Libraries

```bash
pip install pandas numpy matplotlib seaborn scipy sqlalchemy
```

### Step 4 — Open the Jupyter Notebooks

Open:

```text
Exploratory_Data_Analysis.ipynb
```

or

```text
Vendor_Performance_Analysis.ipynb
```

and run the analysis cells.

---

## 📷 Project Dashboard

A dashboard can be added here to visually present the major findings from the analysis.

<!-- Add your dashboard screenshot here -->

---

## 💡 Key Business Insights

The analysis focuses on identifying:

* High-performing vendors
* Low-performing vendors
* Major purchasing contributors
* High and low profit-margin vendors
* Brand-level performance differences
* Low inventory turnover
* Relationships between sales and profitability

These insights can help businesses understand vendor performance and support data-driven operational decisions.

---

## 📚 Skills Demonstrated

This project demonstrates practical experience with:

* Python Programming
* Data Cleaning
* Exploratory Data Analysis
* Data Manipulation
* SQL
* SQLite
* Statistical Analysis
* Hypothesis Testing
* Data Visualization
* Business Analysis
* Git & GitHub
* Jupyter Notebook

---

 Author

Vinay Yadav
**Aspiring Data Analyst**

Skills:

`Python` • `SQL` • `Pandas` • `NumPy` • `Power BI` • `Data Analysis` • `Statistics`

