from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import learning_curve
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('./train.csv')
df.fillna(0,inplace=True)
# processing
le_U_ID = LabelEncoder()
df['User_ID'] = le_U_ID.fit_transform(df['User_ID'])
le_P_ID = LabelEncoder()
df['Product_ID'] = le_P_ID.fit_transform(df['Product_ID'])
df['Gender'] = np.where(df['Gender']=='M',1,0) # Female: 0, Male: 1
df_Age = pd.get_dummies(df.Age)
df_CC = pd.get_dummies(df.City_Category)
df_SIC = pd.get_dummies(df.Stay_In_Current_City_Years)
df_encoded = pd.concat([df,df_Age,df_CC,df_SIC],axis=1)
df_encoded.drop(['Age','City_Category','Stay_In_Current_City_Years'],axis=1,inplace=True)
# part data
# df_frac = df_encoded.sample(frac=0.05,random_state=100)
# X = df_frac.drop(['Purchase'], axis=1)
# y = df_frac['Purchase']
# X_train,X_test,y_train,y_test = train_test_split(X,y,random_state=100)
# scaler = StandardScaler().fit(X_train)
# X_train_scaled = scaler.transform(X_train)
# X_test_scaled = scaler.transform(X_test)
# find the best param
# param_grid = {'n_estimators':[1,3,5,10,30,50,100,150,200]}
# grid_rf = GridSearchCV(RandomForestRegressor(),param_grid,cv=10,scoring='neg_mean_squared_error').fit(X_train_scaled,y_train)
# plt.figure()
# plt.plot(list(param_grid.values())[0],(-1*grid_rf.cv_results_['mean_test_score'])**0.5)
# plt.xlabel('Number of trees')
# plt.ylabel('10-fold CV RMSE')
# plt.show()
# print('Best parameter: {}'.format(grid_rf.best_params_))
# print('Best score: {:.2f}'.format((-1*grid_rf.best_score_)**0.5))
# learning curve
# train_sizes, train_scores, valid_scores = learning_curve(RandomForestRegressor(n_estimators=200), X_train_scaled, y_train, cv=10, scoring='neg_mean_squared_error')
# train_scores = (-1*train_scores)**0.5
# valid_scores = (-1*valid_scores)**0.5
# train_scores_mean = np.mean(train_scores, axis=1)
# train_scores_std = np.std(train_scores, axis=1)
# valid_scores_mean = np.mean(valid_scores, axis=1)
# valid_scores_std = np.std(valid_scores, axis=1)
#
# plt.figure()
# plt.plot(train_sizes,valid_scores_mean,label='valid')
# plt.plot(train_sizes,train_scores_mean,label='train')
# # plt.fill_between(train_sizes, train_scores_mean - train_scores_std, train_scores_mean + train_scores_std, alpha=0.3,color="g")
# # plt.fill_between(train_sizes, valid_scores_mean - valid_scores_std,valid_scores_mean + valid_scores_std, alpha=0.3, color="b")
# plt.xlabel('Number of samples')
# plt.ylabel('RMSE')
# plt.legend()
# plt.show()
# important relative
# rf = RandomForestRegressor(max_depth=7, n_estimators=150).fit(X_train_scaled,y_train)
# f_im = rf.feature_importances_.round(3)
# ser_rank = pd.Series(f_im,index=X.columns).sort_values(ascending=False)
#
# plt.figure()
# sns.barplot(y=ser_rank.index,x=ser_rank.values,palette='deep')
# plt.xlabel('Features Rank Related to Purchase')
# plt.show()
# Entire Dataset RMSE
X = df_encoded.drop(['Purchase'], axis=1)
y = df_encoded['Purchase']
X_train,X_test,y_train,y_test = train_test_split(X,y,random_state=100)

scaler = StandardScaler().fit(X_train)
X_train_scaled = scaler.transform(X_train)
X_test_scaled = scaler.transform(X_test)

rf = RandomForestRegressor(max_depth=7, n_estimators=150).fit(X_train_scaled,y_train)
y_predicted = rf.predict(X_test_scaled)
print('Test set RMSE: {:.3f}'.format(mean_squared_error(y_test,y_predicted)**0.5))
