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
reorder_probability = reorder_probability.reset_index()

companies = companies.merge(reorder_probability, on='company_id', how='left')

product_purchases_count = orders.groupby('product_id')['order_id'].count().to_frame('product_purchases_count')
product_purchases_count = product_purchases_count.reset_index()

# Only work with products that are included in at least 2 orders
# orders = orders.groupby('product_id').filter(lambda order: order.shape[0] > 2)

product_probability_reorder = orders.groupby('product_id')['is_reorder'].mean().to_frame("product_probability_reorder")
product_probability_reorder = product_probability_reorder.reset_index()

products = products.merge(product_probability_reorder, on='product_id', how='left')

products['product_probability_reorder'] = products['product_probability_reorder'].fillna(value=0)

companies_and_products_total_bought = orders.groupby(['company_id', 'product_id'])['order_id'].count().to_frame('companies_and_products_total_bought')
companies_and_products_total_bought = companies_and_products_total_bought.reset_index()

# How frequently a user has bought a product AFTER the first purchase
times_company_bought_product = orders.groupby(['company_id', 'product_id'])[['order_id']].count()
times_company_bought_product.columns = ['times_user_bought_product']
times_company_bought_product = times_company_bought_product.reset_index()

total_orders = orders.groupby('company_id')['order_number'].max().to_frame('total_orders')
total_orders = total_orders.reset_index()

first_order_number = orders.groupby(['company_id', 'product_id'])['order_number'].min().to_frame('first_order_number')
first_order_number = first_order_number.reset_index()

span = pd.merge(total_orders, first_order_number, on='company_id', how='right')
span['orders_placed_since_first_order_of_product_count'] = span.total_orders - span.first_order_number + 1

companies_and_products = pd.merge(times_company_bought_product, span, on=['company_id', 'product_id'], how='left')

companies_and_products['reorder_ratio'] = companies_and_products.times_user_bought_product / companies_and_products.orders_placed_since_first_order_of_product_count

companies_and_products['reorder_ratio'] = companies_and_products['reorder_ratio'].fillna(value=0)

companies_and_products = companies_and_products.drop(["times_user_bought_product", "total_orders", "first_order_number", "orders_placed_since_first_order_of_product_count"], axis=1)

times_company_bought_product = times_company_bought_product.merge(companies_and_products, on=['company_id', 'product_id'], how='left')

print(times_company_bought_product)

# 2.3.3 last

