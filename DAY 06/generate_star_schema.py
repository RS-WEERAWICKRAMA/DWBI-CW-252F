import csv
import random
from datetime import datetime, timedelta

def create_star_schema():
    print("--- Generating Star Schema Dataset ---")
    
    # 1. Generate Dim_Customer
    print("Creating dim_customer.csv...")
    customers = []
    cities = ['New York', 'London', 'Tokyo', 'Paris', 'Sydney']
    segments = ['Consumer', 'Corporate', 'Home Office']
    
    with open('DAY 06/dim_customer.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Customer_ID', 'Customer_Name', 'City', 'Segment'])
        for i in range(1, 51):
            name = f"Customer_{i}"
            city = random.choice(cities)
            segment = random.choice(segments)
            customers.append(i)
            writer.writerow([i, name, city, segment])
            
    # 2. Generate Dim_Product
    print("Creating dim_product.csv...")
    products = []
    categories = ['Electronics', 'Furniture', 'Office Supplies']
    
    with open('DAY 06/dim_product.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Product_ID', 'Product_Name', 'Category', 'Unit_Price'])
        for i in range(101, 121):
            name = f"Product_{i}"
            category = random.choice(categories)
            price = round(random.uniform(10.0, 500.0), 2)
            products.append({'id': i, 'price': price})
            writer.writerow([i, name, category, price])
            
    # 3. Generate Dim_Date
    print("Creating dim_date.csv...")
    dates = []
    start_date = datetime(2026, 1, 1)
    
    with open('DAY 06/dim_date.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Date_ID', 'Full_Date', 'Month', 'Quarter', 'Year'])
        for i in range(30):
            current = start_date + timedelta(days=i)
            date_id = int(current.strftime('%Y%m%d'))
            dates.append(date_id)
            month = current.strftime('%B')
            quarter = f"Q{(current.month-1)//3 + 1}"
            year = current.year
            writer.writerow([date_id, current.strftime('%Y-%m-%d'), month, quarter, year])
            
    # 4. Generate Fact_Sales
    print("Creating fact_sales.csv...")
    with open('DAY 06/fact_sales.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Sales_ID', 'Customer_ID', 'Product_ID', 'Date_ID', 'Quantity', 'Total_Amount'])
        for i in range(1001, 1501):
            cust_id = random.choice(customers)
            prod = random.choice(products)
            date_id = random.choice(dates)
            qty = random.randint(1, 5)
            total_amt = round(qty * prod['price'], 2)
            writer.writerow([i, cust_id, prod['id'], date_id, qty, total_amt])
            
    print("--- Star Schema Generation Complete! ---")

if __name__ == "__main__":
    create_star_schema()
