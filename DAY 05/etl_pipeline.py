import csv
import random
from datetime import datetime, timedelta

def run_etl():
    print("--- Starting ETL Pipeline ---")
    
    # 1. EXTRACT
    print("1. Extracting data (Generating Kaggle Retail Dataset)...")
    extract_path = "DAY 05/raw_retail_sales.csv"
    
    categories = ['electronics', 'Clothing', 'home', 'Sports', 'TOYS']
    names = ['alice', 'BOB', 'charlie', 'David', 'eve', 'FRANK']
    
    with open(extract_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['OrderID', 'CustomerName', 'ProductCategory', 'Price', 'Quantity', 'Discount', 'OrderDate'])
        start_date = datetime(2026, 1, 1)
        for i in range(1001, 1501):
            name = random.choice(names)
            cat = random.choice(categories)
            price = round(random.uniform(10.0, 500.0), 2)
            qty = random.randint(1, 10)
            disc = random.choice(['0.0', '0.1', '0.15', '0.2', ''])
            date = start_date + timedelta(hours=i-1001)
            writer.writerow([i, name, cat, price, qty, disc, date.strftime('%Y-%m-%d %H:%M:%S')])
            
    print("   -> Extracted 500 records.")
    
    # 2. TRANSFORM
    print("2. Transforming data...")
    transformed_data = []
    
    with open(extract_path, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Clean text columns
            row['CustomerName'] = row['CustomerName'].title()
            row['ProductCategory'] = row['ProductCategory'].capitalize()
            
            # Handle missing values
            discount = float(row['Discount']) if row['Discount'] != '' else 0.0
            row['Discount'] = discount
            
            # Derived Metrics
            price = float(row['Price'])
            qty = int(row['Quantity'])
            total_amt = price * qty
            final_amt = total_amt * (1 - discount)
            
            row['TotalAmount'] = round(total_amt, 2)
            row['FinalAmount'] = round(final_amt, 2)
            
            # Categorization
            row['OrderSize'] = 'Large' if final_amt > 500 else 'Standard'
            transformed_data.append(row)
            
    print("   -> Transformation complete.")
    
    # 3. LOAD
    print("3. Loading data into final Data Warehouse CSV...")
    load_csv_path = "DAY 05/retail_sales_warehouse.csv"
    
    if len(transformed_data) > 0:
        with open(load_csv_path, 'w', newline='') as f:
            fieldnames = transformed_data[0].keys()
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(transformed_data)
            
    print(f"   -> Loaded successfully into {load_csv_path}!")
    print("--- ETL Pipeline Finished ---")

if __name__ == "__main__":
    run_etl()
