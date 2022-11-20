from collections import defaultdict
import pandas as pd
import numpy as np

order = pd.read_csv("./data/products.csv")

product_ids = [_ for _ in range(1, 36, 1)]

companies_baskets = {
    1: [1, 3, 4, 10, 12],
    2: [4, 10, 12],
    3: [1, 2, 10, 11, 12, 13],
    4: [1, 10, 11, 13],
    5: [1, 2, 5, 6, 7, 8, 9, 14, 15],
    6: [1, 2, 5, 6, 14, 15],
    7: [18, 19, 20, 21, 22, 23, 24, 25, 26, 27],
    8: [28, 29, 30, 31, 32],
    9: [33, 34, 35],
    10: [35],
}

company_categories_by_id = {
    1: 2,
    2: 2,
    3: 3,
    4: 3,
    5: 5,
    6: 6,
    7: 6,
    8: 8,
    9: 8,
    10: 9
}

companies_baskets_outliers = { key: np.setdiff1d(product_ids, companies_baskets[key]) for key in [_ for _ in range(1, 7, 1)] }

min_orders_count = 10
max_orders_count = 15

min_products_in_order = 2
max_products_in_order = 10

outlier_probability = 0.2

orders_array_by_company_id = {
    key: [] for key in range(1, 7, 1)
}

for comany_id in range(1, 7, 1):
    orders_count = np.random.randint(min_orders_count, max_orders_count + 1)

    for order_id in range(orders_count):
        number_of_products = np.random.randint(min_products_in_order, max_products_in_order + 1)

        order = []

        for _ in range(number_of_products):
            is_outlier = np.random.random() < outlier_probability

            if is_outlier:
                array = companies_baskets_outliers[comany_id]
            else:
                array = companies_baskets[comany_id]
        
            random_index = np.random.randint(0, len(array))

            product_id = array[random_index]

            order.append(product_id)

        orders_array_by_company_id[comany_id].append(order)

order_id = 1

csv = "order_id,company_id,company_category_id,product_id,day_of_week,consecutive_order_count,reordered,order_number\n"

for company_id in orders_array_by_company_id:

    company_orders = orders_array_by_company_id[company_id]

    consecutive_order_count_map = defaultdict(lambda: 0)

    for order_number, order in enumerate(company_orders):
        day_of_week = np.random.randint(1, 8)

        for product_id in product_ids:
            if product_id in order:
                consecutive_order_count_map[product_id] += 1
            else:
                consecutive_order_count_map[product_id] = 0

        for product_id in order:
            consecutive_order_count = consecutive_order_count_map[product_id]

            company_category_id = company_categories_by_id[company_id]

            csv += f"{order_id},{company_id},{company_category_id},{product_id},{day_of_week},{consecutive_order_count},{0 if consecutive_order_count > 1 else 1},{order_number + 1}\n"

    order_id += 1

with open("./data/orders.csv", "w") as file:
    file.write(csv)
