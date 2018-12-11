import pandas as pd
from sklearn import svm
from sklearn.model_selection import cross_val_score
from sklearn import tree
from sklearn.neighbors import KNeighborsClassifier
from sklearn import preprocessing

labelencoder = preprocessing.LabelEncoder()
onehotencoder = preprocessing.OneHotEncoder()

data = pd.read_csv('./train_process2.csv')
# col_n = data.columns[[1,2,4,5,6,7]]
# X = pd.DataFrame(data, columns=col_n)
# X = preprocessing.scale(X)
# Y = data.purchase_level
X = data.drop(['purchase'], axis=1)
Y = data['purchase']
scoring = ['precision_macro', 'recall_macro']
clf_dt = tree.DecisionTreeClassifier()
clf_svc = svm.SVC(gamma='auto')
clf_neigh = KNeighborsClassifier(n_neighbors=1)
scores_dt = cross_val_score(clf_dt, X, Y, cv=10)
scores_svc = cross_val_score(clf_svc, X, Y, cv=10)
scores_neigh = cross_val_score(clf_neigh, X, Y, cv=10)
print(scores_dt)
print(scores_svc)
print(scores_neigh)
