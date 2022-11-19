import xgboost as xgb
import pandas as pd
import numpy as np

x_train = pd.DataFrame(np.arange(128).reshape((16,8)), columns=[letter for letter in 'abcdefgh'])
y_train = pd.DataFrame(np.random.randint(2, size=16))
d_train = xgb.DMatrix(x_train, label=y_train)

x_test = pd.DataFrame(np.arange(128).reshape((16,8)), columns=[letter for letter in 'abcdefgh'])
y_test = pd.DataFrame(np.random.randint(2, size=16))
d_test = xgb.DMatrix(x_test, label=y_test)

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