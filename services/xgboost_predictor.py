import xgboost as xgb
import pandas as pd
import numpy as np

from data_parser import prepare_data

X_train, Y_train, X_test, Y_test = prepare_data()

d_train = xgb.DMatrix(X_train, label=Y_train)
d_test = xgb.DMatrix(X_test, label=Y_test)

# dtrain = xgb.DMatrix('train.csv?format=csv&label_column=0')
# dtest = xgb.DMatrix('test.csv?format=csv&label_column=0')

param = {'max_depth': 2, 'eta': 1, 'objective': 'binary:logistic'}
param['nthread'] = 4
param['eval_metric'] = 'auc'
param['eval_metric'] = ['auc', 'ams@0']

evallist = [(d_train, 'train'), (d_test, 'eval')]

num_round = 10
bst = xgb.train(param, d_train, num_round, evallist)
# bst.save_model('0001.model')