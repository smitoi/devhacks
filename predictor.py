import pandas as pd
import gc

data_dir_path = "./data"

gc.enable()

orders = pd.read_csv(f"{data_dir_path}/orders.csv")

products = pd.read_csv(f"{data_dir_path}/products.csv")
companies = pd.read_csv(f"{data_dir_path}/companies.csv")

company_categories = pd.read_csv(f"{data_dir_path}/company_categories.csv")
product_categories = pd.read_csv(f"{data_dir_path}/product_categories.csv")

orders['company_id'] = orders['company_id'].astype('category')

orders['product_id'] = orders['product_id'].astype('category')

orders_count_per_customer = orders.groupby('company_id')['order_id'].count()

reorder_probability = orders.groupby('company_id')['is_reorder'].mean().to_frame("reorder_probability")

companies = companies.merge(reorder_probability, on='company_id', how='left')

product_purchases_count = orders.groupby('product_id')['order_id'].count().to_frame('product_purchases_count')

product_probability_reorder = orders.groupby('product_id')['is_reorder'].sum() / orders.groupby('product_id')['is_reorder'].count()

print(product_probability_reorder)

print(companies)