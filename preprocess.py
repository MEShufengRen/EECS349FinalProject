import pandas as pd


def map_gender(gender):
    if gender == 'M':
        return 1
    else:
        return 0


def map_age(age):
    if age == '0-17':
        return 0
    elif age == '18-25':
        return 1
    elif age == '26-35':
        return 2
    elif age == '36-45':
        return 3
    elif age == '46-50':
        return 4
    elif age == '51-55':
        return 5
    else:
        return 6


def map_city_categories(city_category):
    if city_category == 'A':
        return 2
    elif city_category == 'B':
        return 1
    else:
        return 0


def map_stay(stay):
    if stay == '4+':
        return 4
    else:
        return int(stay)


def map_product_category(product_category):
    return int(product_category)


# read raw data
data = pd.read_csv('./test.csv')
data = data.sort_values(data.columns[0])  # sort according to User_ID
data.columns = [each.lower() for each in data.columns]  # Uppercase are converted to lowercase for convenience
# deal with missing value
data.iloc[:, 9] = data.iloc[:, 9].fillna(0)
data.iloc[:, 10] = data.iloc[:, 10].fillna(0)
# data["product_category_1"] = data["product_category_1"].astype(str)
# data["product_category_2"] = data["product_category_2"].astype(str)
# data["product_category_3"] = data["product_category_3"].astype(str)
# data["marital_status"] = data["marital_status"].astype(str)
# data["occupation"] = data["occupation"].astype(str)
# data["user_id"] = data["user_id"].astype(str)

data['gender'] = data['gender'].apply(map_gender)
data['age'] = data['age'].apply(map_age)
data['city_category'] = data['city_category'].apply(map_city_categories)
data['stay_in_current_city_years'] = data['stay_in_current_city_years'].apply(map_stay)

data['product_category_2'] = data['product_category_2'].apply(map_product_category)
data['product_category_3'] = data['product_category_3'].apply(map_product_category)
# data = data.copy()
# data_B = pd.DataFrame(columns=data.columns)
# u_id = np.unique(data['user_id'])
# num = 0
# for i in u_id:
#     data_A = data[data['user_id']==i]
#     data_A.index = range(len(data_A))
#     data_B.loc[num] = data_A.loc[0]
#     data_B.loc[num].purchase = data_A.purchase.sum()
#     num = num+1

# threshold1 = 0.5*sum(data.purchase)/len(data.purchase)
# threshold2 = sum(data.purchase)/len(data.purchase)
# threshold3 = 1.5*sum(data.purchase)/len(data.purchase)
# data['purchase_level'] = None
# for i in range(len(data)):
#     if data.loc[i].purchase > threshold3:
#         data.at[i, 'purchase_level'] = '1'
#     #     data.loc[i].purchase_level = '1'
#     elif data.loc[i].purchase > threshold2:
#         data.at[i, 'purchase_level'] = '2'
#         # data.loc[i].purchase_level = '2'
#     elif data.loc[i].purchase > threshold1:
#         data.at[i, 'purchase_level'] = '3'
#         # data.loc[i].purchase_level = '3'
#     else:
#         data.at[i, 'purchase_level'] = '4'
#         # data.loc[i].purchase_level = '4'

data.to_csv("test_process.csv", index=False, sep=',')
