import pandas as pd
import gc

from sklearn.ensemble import RandomForestClassifier

data_dir_path = "./data"

orders = pd.read_csv(f"{data_dir_path}/orders.csv")
companies = pd.read_csv(f"{data_dir_path}/companies.csv")

number_of_orders_per_customer = orders.groupby('company_id')['order_number'].max().to_frame("number_of_orders_per_customer")

how_frequent_customer_reorders_products = orders.groupby('company_id')['consecutive_order_count'].mean().to_frame('how_frequent_customer_reorders_products')

average_day_of_week = orders.groupby('company_id')['day_of_week'].mean().to_frame('average_day_of_week')

companies = companies.merge(how_frequent_customer_reorders_products, on='company_id', how='left')

# TO REMOVE
companies = companies.drop(['name'], axis=1)

number_of_purchases_for_products = orders.groupby('product_id')['order_id'].count().to_frame('number_of_purchases_for_products')

product_probability_to_be_reordered = (orders[orders.consecutive_order_count > 1].groupby('product_id').size() / orders.groupby('product_id').size()).to_frame("product_probability_to_be_reordered")

product_probability_to_be_reordered = product_probability_to_be_reordered.fillna(value=0)

orders = orders.merge(product_probability_to_be_reordered, on=['product_id'], how='left')

how_many_times_user_bought_product = orders.groupby(['company_id', 'product_id'])['order_id'].count().to_frame('how_many_times_user_bought_product')

orders = orders.merge(how_many_times_user_bought_product, on=['company_id', 'product_id'], how='left')

# Models

train_dataset_percentage = 0.01

orders_count = len(orders)

train_dataset_size = int(train_dataset_percentage * orders_count)
test_dataset_size = int((1 - train_dataset_percentage) * orders_count)

X_train = orders.head(train_dataset_size)
Y_train = X_train['reordered']
X_train = X_train.drop(['reordered'], axis=1)

X_test = orders.tail(test_dataset_size)
Y_test = X_test['reordered']
X_test = X_test.drop(['reordered'], axis=1)


rfc = RandomForestClassifier(n_estimators=20,max_depth=4, n_jobs=-1 ,random_state=69)

model = rfc.fit(X_train, Y_train)

feature_importances_df = pd.DataFrame(model.feature_importances_, index = X_train.columns, columns=['importance']).sort_values('importance',ascending=False)

print(feature_importances_df)

test_pred = model.predict(X_test).astype(int)

acc = (test_pred == Y_test).mean()

print(f"Accuracy: {acc}")
