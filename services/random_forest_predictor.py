from sklearn.ensemble import RandomForestClassifier

from data_parser import prepare_data

X_train, Y_train, X_test, Y_test = prepare_data()

rfc = RandomForestClassifier(n_estimators=20,max_depth=4, n_jobs=-1 ,random_state=69)

model = rfc.fit(X_train, Y_train)

feature_importances_df = pd.DataFrame(model.feature_importances_, index = X_train.columns, columns=['importance']).sort_values('importance',ascending=False)

print(feature_importances_df)

test_pred = model.predict(X_test).astype(int)

acc = (test_pred == Y_test).mean()

print(f"Accuracy: {acc}")
