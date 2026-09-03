# AI Prompt Report: Building an ETL Pipeline

**Name:** RS WEERAWICKRAMA  
**Index:** 21  
**Module:** Data Warehousing & Business Intelligence (DWBI)  

---

## 1. Objective
The objective of this session was to use AI to generate a complete ETL (Extract, Transform, Load) pipeline in Python, utilizing an e-commerce retail dataset (simulating a Kaggle dataset extraction) to demonstrate practical data warehousing techniques.

---

## 2. Research & Development Prompts

### Prompt 1: Dataset Generation & Extraction
**User Prompt:** 
> "I need a Python script to extract a raw e-commerce retail dataset similar to what I would find on Kaggle. It should have columns like OrderID, CustomerName, ProductCategory, Price, Quantity, Discount, and OrderDate."

**AI Response Summary:** 
The AI provided the Python logic for the `Extract` phase, utilizing the `csv` module to generate a realistic `raw_retail_sales.csv` containing 500 records with intentionally messy data (e.g., inconsistent capitalization and missing discount values) to simulate a real-world raw data extraction.

### Prompt 2: Data Transformation & Feature Engineering
**User Prompt:** 
> "Now write the 'Transform' phase of the ETL pipeline. I need the script to clean the text columns, handle the missing discount values, and engineer new Business Intelligence metrics like 'TotalAmount' and 'FinalAmount'."

**AI Response Summary:** 
The AI generated the transformation logic which reads the raw CSV and applies the following rules:
* Standardized text by converting `CustomerName` to Title Case and `ProductCategory` to Capitalized.
* Handled missing values by defaulting empty discounts to `0.0`.
* Engineered derived metrics: `TotalAmount` (Price * Quantity) and `FinalAmount` (TotalAmount applying the discount).
* Categorized orders into a new `OrderSize` column ('Large' vs 'Standard') for easier BI reporting.

### Prompt 3: Loading to the Data Warehouse
**User Prompt:** 
> "Finally, write the 'Load' phase to save this cleaned and transformed data into a final Data Warehouse CSV file format."

**AI Response Summary:** 
The AI concluded the script with the `Load` phase, which takes the transformed data dictionary and writes it to a clean, structured output file named `retail_sales_warehouse.csv`, effectively simulating the insertion of data into a Data Warehouse table.

---

## 3. Conclusion
By strategically prompting the AI, a fully functional Python-based ETL pipeline was successfully constructed. The script effectively demonstrates how raw, unstructured data can be extracted, programmatically cleaned/transformed into valuable business metrics, and loaded into a destination file suitable for Data Warehousing and BI reporting.
