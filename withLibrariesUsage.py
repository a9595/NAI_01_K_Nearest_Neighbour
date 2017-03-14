import numpy as np
from sklearn import preprocessing, neighbors, cross_validation
import pandas as pd

df = pd.read_csv('train.txt')
df.drop(['name'], 1, inplace=True)
print(df)

sizeColumnName = 'size1'
X = np.array(df.drop([sizeColumnName], 1))
y = np.array(df.drop([sizeColumnName]))

X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.2)

clf = neighbors.KNeighborsClassifier()
clf.fit(X_train, y_train)

accuracy = clf.score(X_test, y_test)
print(accuracy)
