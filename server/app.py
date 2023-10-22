from scipy.stats import mode
from sklearn.metrics import accuracy_score, confusion_matrix
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from flask import Flask, request, jsonify
import numpy as np
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

dataset = pd.read_csv('Data/Training.csv').dropna(axis=1)
encoder = LabelEncoder()
dataset["prognosis"] = encoder.fit_transform(dataset["prognosis"])
x = dataset.iloc[:, :-1]
y = dataset.iloc[:, -1]
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=24)


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

final_svm_model = SVC()
final_nb_model = GaussianNB()
final_rf_model = RandomForestClassifier(random_state=18)
final_svm_model.fit(x, y)
final_nb_model.fit(x, y)
final_rf_model.fit(x, y)

test_data = pd.read_csv("Data/Testing.csv").dropna(axis=1)

test_X = test_data.iloc[:, :-1]
test_Y = encoder.transform(test_data.iloc[:, -1])

svm_preds = final_svm_model.predict(test_X)
nb_preds = final_nb_model.predict(test_X)
rf_preds = final_rf_model.predict(test_X)

symptoms = x.columns.values

symptom_index = {}
for index, value in enumerate(symptoms):
    symptom = " ".join([i.capitalize() for i in value.split("_")])
    symptom_index[symptom] = index

data_dict = {
    "symptom_index": symptom_index,
    "predictions_classes": encoder.classes_
}


def predictDisease(symptoms):
    symptoms = symptoms.split(",")
    input_data = [0] * len(data_dict["symptom_index"])
    for symptom in symptoms:
        index = data_dict["symptom_index"][symptom]
        input_data[index] = 1
    input_data = np.array(input_data).reshape(1, -1)

    rf_prediction = data_dict["predictions_classes"][final_rf_model.predict(input_data)[
        0]]
    nb_prediction = data_dict["predictions_classes"][final_nb_model.predict(input_data)[
        0]]
    svm_prediction = data_dict["predictions_classes"][final_svm_model.predict(input_data)[
        0]]
    final_prediction = mode(
        [rf_prediction, nb_prediction, svm_prediction])[0][0]
    predictions = {
        "rf_model_prediction": rf_prediction,
        "naive_bayes_prediction": nb_prediction,
        "svm_model_prediction": svm_prediction,
        "final_prediction": final_prediction
    }
    return predictions


@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        data = request.get_json()
        symptoms = data.get('symptoms')
        prediction = predictDisease(symptoms)
        return jsonify(prediction)


if __name__ == '__main__':
    app.run(debug=True)
