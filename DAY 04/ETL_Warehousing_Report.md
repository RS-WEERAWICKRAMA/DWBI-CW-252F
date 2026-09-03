# ETL Data Warehousing: Research & Analysis Report

**Name:** RS WEERAWICKRAMA  
**Index:** 21  
**Module:** Data Warehousing & Business Intelligence (DWBI)  

---

## 1. Objective
The purpose of this report is to document the research conducted on the core concepts, methodologies, and tools associated with ETL (Extract, Transform, Load) and Data Warehousing. The insights below were gathered through AI-assisted research to better understand how modern data architectures operate.

---

## 2. Research Prompts & Findings

### Prompt 1: "Can you explain the concept of ETL Data Warehousing simply, as if I were a beginner?"
**Summary of Findings:**
ETL stands for Extract, Transform, and Load. It is the fundamental process used to build a Data Warehouse. 
* **Extract:** Pulling data from various scattered sources (like databases, apps, or flat files).
* **Transform:** Cleaning, filtering, and formatting the data so that it is consistent and reliable.
* **Load:** Moving this cleaned data into a central storage system called a Data Warehouse, where business analysts can run queries and generate BI reports.

### Prompt 2: "Give me some practical, real-world industry examples of ETL processes."
**Summary of Findings:**
* **Retail (E-commerce):** Extracting daily sales data from Shopify, transforming it to match a standard currency, and loading it into a warehouse to analyze monthly revenue trends.
* **Healthcare:** Extracting patient records from different hospital branches, standardizing patient IDs (Transform), and loading them into a centralized database for research without duplicating records.
* **Finance:** Pulling transaction logs from ATMs, removing incomplete transactions, and loading them into a data warehouse for fraud detection analysis.

### Prompt 3: "What is the main difference between ETL and ELT architectures?"
**Summary of Findings:**
* **ETL (Extract, Transform, Load):** Data is transformed *before* it enters the warehouse. This is better for legacy systems or when strict data privacy scrubbing is needed before storage.
* **ELT (Extract, Load, Transform):** Data is loaded into the warehouse exactly as it is (raw), and the transformation happens *inside* the warehouse. This is much faster and is heavily used in modern cloud data warehouses (like Snowflake or BigQuery) because they possess immense processing power.

### Prompt 4: "List the most popular software tools and platforms used for ETL and Data Warehousing today."
**Summary of Findings:**
* **ETL/Data Integration Tools:** Talend, Informatica PowerCenter, Apache Airflow, dbt (Data Build Tool), and Matillion.
* **Cloud Data Warehouses:** Snowflake, Amazon Redshift, Google BigQuery, and Microsoft Azure Synapse.

---

## 3. Conclusion
Through this AI-assisted research, it is clear that ETL remains the backbone of Business Intelligence. While modern cloud environments are shifting slightly towards ELT to leverage cloud computing power, the fundamental requirement to clean and integrate data centrally remains critical for accurate business decision-making.
