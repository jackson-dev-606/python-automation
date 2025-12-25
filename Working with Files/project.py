import csv
import datetime
import random

product_data = {
    "P001": ["Wireless Headphones", 100],
    "P002": ["Laptop Backpack", 60],
    "P003": ["Bluetooth Speaker", 50],
    "P004": ["USB Flash Drive", 20],
    "P005": ["Mobile Phone Case", 15],
    "P006": ["Wireless Mouse", 30],
    "P007": ["Laptop Stand", 40],
    "P008": ["HDMI Cable", 15],
    "P009": ["Smartphone", 600],
    "P010": ["External Hard Drive", 100]
}

# List to save to new csv file
sales_tracker = list()

# Open and read text file
with open('product_sales.txt', 'r') as file:
    product_ids = file.readlines()
    sale_id = 1
    today = datetime.date.today()
    for prod_id in product_ids:
        product_id = prod_id.strip()
        product_name = product_data[product_id][0]
        product_price = product_data[product_id][1]
        sales_tracker.append([today, sale_id, product_id, product_name, product_price])
        sale_id = sale_id + 1

with open('sales_tracker.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['current_date', 'sales_id', 'product_id', 'product_name', 'product_price'])
    writer.writerows(sales_tracker)


