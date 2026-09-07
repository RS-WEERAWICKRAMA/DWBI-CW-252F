import sqlite3
import pandas as pd

def main():
    # Connect to an in-memory SQLite database
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()

    print("--- BUILDING THE DATA WAREHOUSE (STAR SCHEMA) ---")
    
    # 1. Create Dimensions
    cursor.execute('''
        CREATE TABLE dim_product (
            product_id INTEGER PRIMARY KEY,
            product_name TEXT,
            category TEXT
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE dim_store (
            store_id INTEGER PRIMARY KEY,
            store_name TEXT,
            region TEXT
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE dim_time (
            time_id INTEGER PRIMARY KEY,
            date TEXT,
            month TEXT,
            year INTEGER
        )
    ''')

    # 2. Create Fact Table
    cursor.execute('''
        CREATE TABLE fact_sales (
            sale_id INTEGER PRIMARY KEY,
            product_id INTEGER,
            store_id INTEGER,
            time_id INTEGER,
            quantity INTEGER,
            revenue REAL,
            FOREIGN KEY(product_id) REFERENCES dim_product(product_id),
            FOREIGN KEY(store_id) REFERENCES dim_store(store_id),
            FOREIGN KEY(time_id) REFERENCES dim_time(time_id)
        )
    ''')

    # 3. Populate Dimensions
    products = [(1, 'Laptop', 'Electronics'), (2, 'Desk', 'Furniture'), (3, 'Chair', 'Furniture')]
    cursor.executemany("INSERT INTO dim_product VALUES (?, ?, ?)", products)

    stores = [(1, 'Downtown Store', 'East'), (2, 'Uptown Store', 'West')]
    cursor.executemany("INSERT INTO dim_store VALUES (?, ?, ?)", stores)

    times = [(1, '2023-01-15', 'January', 2023), (2, '2023-01-20', 'January', 2023), (3, '2023-02-10', 'February', 2023)]
    cursor.executemany("INSERT INTO dim_time VALUES (?, ?, ?, ?)", times)

    # 4. Populate Fact Table
    sales = [
        (1, 1, 1, 1, 2, 2000.0),
        (2, 2, 1, 1, 1, 500.0),
        (3, 3, 2, 2, 4, 600.0),
        (4, 1, 2, 3, 1, 1000.0)
    ]
    cursor.executemany("INSERT INTO fact_sales VALUES (?, ?, ?, ?, ?, ?)", sales)
    conn.commit()
    print("Warehouse schema created and populated successfully.\n")

    print("--- LISTING THE DIMENSIONS ---")
    # List all tables
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    dimensions = [table[0] for table in tables if table[0].startswith('dim_')]
    
    print("Identified Dimension Tables in the Warehouse:")
    for dim in dimensions:
        print(f" - {dim}")
        
    print("\n--- SIMULATING OLAP CUBE QUERIES ---")
    print("OLAP cubes allow slicing, dicing, and rolling up data across dimensions.")
    
    # Simulating a Roll-up (aggregating revenue by Region and Category)
    query = '''
        SELECT s.region, p.category, SUM(f.revenue) as total_revenue
        FROM fact_sales f
        JOIN dim_store s ON f.store_id = s.store_id
        JOIN dim_product p ON f.product_id = p.product_id
        GROUP BY s.region, p.category
        ORDER BY s.region, p.category;
    '''
    df_cube = pd.read_sql_query(query, conn)
    print("\nOLAP Query Result (Total Revenue by Region and Category):")
    print(df_cube.to_string(index=False))

    conn.close()

if __name__ == "__main__":
    main()
