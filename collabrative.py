import pandas as pd
from sklearn.model_selection import KFold
import math as math
from scipy.spatial.distance import cosine


class Collabrative(object):
    def __init__(self):
        self.testD = pd.read_csv('./test_process.csv')
        self.testD.loc[:, 'purchase'] = 0
        self.trainD_all = pd.read_csv('./train_process.csv')
        self.trainD = self.trainD_all.sample(frac=0.001,random_state=100)

    def KFoldV(self, k):
        kf = KFold(n_splits=k)
        kf.get_n_splits(self.trainD)
        return kf

    def find_user(self, trainData, product):
        subdata = trainData[trainData.product_id == product]
        return subdata

    def predict(self, subdata, user, KNN):
        subdata.loc[:, 'similarity'] = 0
        for index, row in subdata.iterrows():
            subdata.loc[index, 'similarity'] = cosine(row[2:8].tolist(), user[2:8].tolist())# cosine less
        subdata.sort_values(by="similarity", ascending=True)
        if len(subdata) > KNN:
            predict = subdata.iloc[0:KNN]['purchase'].mean()
        else:
            predict = subdata['purchase'].mean()
        return predict

    def similar_product(self, trainData, product):
        trainData.loc[:, 'similarity'] = 0
        for index, row in trainData.iterrows():
            trainData.loc[index, 'similarity'] = cosine(row[8:11].astype('int64'), product[8:11].astype('int64'))
        trainData.sort_values(by="similarity", ascending=True)
        similar_product = trainData.iloc[0]['product_id']
        return similar_product

    def accuracy(self, train, test, KNN):
        sumdiff = 0
        for index, row in test.iterrows():
            subdata = self.find_user(train, row['product_id'])
            if len(subdata)>0:
                predict = self.predict(subdata, row, KNN)
            else:
                product = self.similar_product(train, row)
                subdata2 = self.find_user(train, product)
                predict = self.predict(subdata2, row, KNN)
            sumdiff = (row['purchase']-predict)**2 + sumdiff
        RMSE = math.sqrt(sumdiff/len(test))
        return RMSE

    def test(self, KNN):
        for index, row in self.testD.iterrows():
            subdata = self.find_user(self.trainD, row['product_id'])
            if len(subdata)>0:
                self.testD.iloc[index]['purchase'] = self.predict(subdata, row, KNN)
            else:
                product = self.similar_product(self.trainD, row)
                subdata2 = self.find_user(self.trainD, product)
                self.testD.iloc[index]['purchase'] = self.predict(subdata2, row, KNN)


def train():
    colla = Collabrative()
    kf = colla.KFoldV(10)
    RMSE = []
    for train_index, test_index in kf.split(colla.trainD):
        train, test = colla.trainD.iloc[train_index, :], colla.trainD.iloc[test_index, :]
        rmse = colla.accuracy(train, test, 3)
        RMSE.append(rmse)
    print(RMSE)
    return RMSE


def test():
    colla = Collabrative()
    colla.test(1)
    colla.testD.to_csv("test_result.csv", index=False, sep=',')

if __name__ == '__main__':
    # train()
    test()
