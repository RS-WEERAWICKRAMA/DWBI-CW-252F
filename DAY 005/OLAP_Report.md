# Data Warehouse & OLAP Cube Report

## 1. Introduction
This report outlines the structure of the in-memory Data Warehouse constructed as part of our **DAY 005** exercise. The project simulates an Online Analytical Processing (OLAP) environment using a **Star Schema** to organize the data into Facts and Dimensions.

## 2. The Star Schema Architecture
A Star Schema is designed to optimize read performance for analytical queries. It consists of a central **Fact Table** surrounded by multiple **Dimension Tables**. 

### 2.1 The Fact Table (`fact_sales`)
The Fact table holds the quantitative, measurable metrics of our business process (in this case, sales).
* **Metrics stored:**
  * `quantity`: The number of items sold.
  * `revenue`: The total monetary value of the sale.
* **Foreign Keys:** It contains IDs that link out to the Dimension tables (`product_id`, `store_id`, `time_id`).

### 2.2 The Dimensions
Dimensions provide the context—the "who, what, where, and when"—to the numbers in the fact table. They allow us to slice and dice the data.

#### Dimension 1: Product (`dim_product`)
This dimension tracks **what** is being sold.
* `product_id` (Primary Key)
* `product_name` (e.g., Laptop, Desk, Chair)
* `category` (e.g., Electronics, Furniture)

#### Dimension 2: Store (`dim_store`)
This dimension tracks **where** the sales are taking place geographically.
* `store_id` (Primary Key)
* `store_name` (e.g., Downtown Store, Uptown Store)
* `region` (e.g., East, West)

#### Dimension 3: Time (`dim_time`)
This dimension tracks **when** the sales occurred, allowing for temporal analysis like monthly trends.
* `time_id` (Primary Key)
* `date` (e.g., 2023-01-15)
* `month` (e.g., January, February)
* `year` (e.g., 2023)

## 3. OLAP Cube Operations Simulation
By querying this Star Schema, we simulate OLAP cube operations such as **Roll-ups**, **Drill-downs**, **Slicing**, and **Dicing**.

### Example: Roll-up Aggregation
In the accompanying Python/Jupyter Notebook script, we executed a roll-up query to aggregate total revenue grouped by the Store `region` and Product `category`. 

**SQL Query Used:**
```sql
SELECT s.region, p.category, SUM(f.revenue) as total_revenue
FROM fact_sales f
JOIN dim_store s ON f.store_id = s.store_id
JOIN dim_product p ON f.product_id = p.product_id
GROUP BY s.region, p.category
ORDER BY s.region, p.category;
```

**Results:**
| Region | Category | Total Revenue |
| :--- | :--- | :--- |
| East | Electronics | $2000.00 |
| East | Furniture | $500.00 |
| West | Electronics | $1000.00 |
| West | Furniture | $600.00 |

## 4. Conclusion
The implementation successfully demonstrates how normalized transactional data can be restructured into a Star Schema. This structure empowers stakeholders to rapidly query multidimensional aggregates, a foundational requirement for any Business Intelligence (BI) and Data Warehousing (DW) system.
