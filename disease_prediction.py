from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd

training = pd.read_csv('Data/Training.csv').dropna(axis=1)
testing = pd.read_csv('Data/Testing.csv').dropna(axis=1)

x = training.iloc[:, :-1].values
y = training.iloc[:, -1].values
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.3, random_state=12)

lr = LogisticRegression()
lr.fit(x_train, y_train)
pred1 = lr.predict(x_test)
accuracy1 = accuracy_score(y_test, pred1)*100
accuracy1

svm = SVC(kernel='linear', random_state=0)
svm.fit(x_train, y_train)
pred2 = svm.predict(x_test)
accuracy2 = accuracy_score(y_test, pred2)*100
accuracy2

ksv = SVC(kernel='rbf', random_state=0)
ksv.fit(x_train, y_train)
pred3 = ksv.predict(x_test)
accuracy3 = accuracy_score(y_test, pred3)*100
accuracy3

knn = KNeighborsClassifier(n_neighbors=5, metric='minkowski', p=2)
knn.fit(x_train, y_train)
pred4 = knn.predict(x_test)
accuracy4 = accuracy_score(y_test, pred4)*100
accuracy4

nb = GaussianNB()
nb.fit(x_train, y_train)
pred5 = nb.predict(x_test)
accuracy5 = accuracy_score(y_test, pred5)*100
accuracy5

dt = DecisionTreeClassifier(criterion='entropy', random_state=0)
dt.fit(x_train, y_train)
pred6 = dt.predict(x_test)
accuracy6 = accuracy_score(y_test, pred6)*100
accuracy6

rf = RandomForestClassifier(
    n_estimators=10, criterion='entropy', random_state=0)
rf.fit(x_train, y_train)
pred7 = rf.predict(x_test)
accuracy7 = accuracy_score(y_test, pred7)*100
accuracy7
