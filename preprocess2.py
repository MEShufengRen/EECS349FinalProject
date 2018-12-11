import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder

data = pd.read_csv('./train.csv')
data = data.sort_values(data.columns[0])
data.columns = [each.lower() for each in data.columns]
# deal with missing value
data.iloc[:, 9] = data.iloc[:, 9].fillna(0)
data.iloc[:, 10] = data.iloc[:, 10].fillna(0)
data["product_category_2"] = data["product_category_2"].astype(int)
data["product_category_3"] = data["product_category_3"].astype(int)
# labelEncoder
le_U_ID = LabelEncoder()
data['user_id'] = le_U_ID.fit_transform(data['user_id'])
le_P_ID = LabelEncoder()
data['product_id'] = le_P_ID.fit_transform(data['product_id'])
le_G_ID = LabelEncoder()
data['gender'] = le_G_ID.fit_transform(data['gender'])
le_A_ID = LabelEncoder()
data['age'] = le_A_ID.fit_transform(data['age'])
le_S_ID = LabelEncoder()
data['stay_in_current_city_years'] = le_S_ID.fit_transform(data['stay_in_current_city_years'])
le_M_ID = LabelEncoder()
data['marital_status'] = le_M_ID.fit_transform(data['marital_status'])
le_C_ID = LabelEncoder()
data['city_category'] = le_C_ID.fit_transform(data['city_category'])
# OneHotEncoder
data_occ = pd.get_dummies(data.occupation)
data_cc = pd.get_dummies(data.city_category)
data_pc1 = pd.get_dummies(data.product_category_1)
data_pc2 = pd.get_dummies(data.product_category_2)
data_pc3 = pd.get_dummies(data.product_category_3)
data_encoded = pd.concat([data,data_occ,data_cc,data_pc1,data_pc2,data_pc3],axis=1)
data_encoded.drop(['occupation', 'city_category', 'product_category_1','product_category_2','product_category_3'],axis=1,inplace=True)
# onehotencoder = OneHotEncoder(categorical_features = [4,5,8,9,10]) #occupation city_category product_category_123
# data = onehotencoder.fit_transform(data).toarray()


data_encoded.to_csv("train_process2.csv", index=False, sep=',')
