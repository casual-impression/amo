# Original: https://colab.research.google.com/drive/1O3aSnJSjyxb6PHY5oB4RXgEghG8Fsgde
import numpy as np
import pandas as pd
import sys

from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier

def get_proper_name(x):
    if x == 0:
        val = 'setosa'
    elif x == 1:
        val = 'versicolor'
    else:
        val = 'virginica'
    return val


iris_data = load_iris()
iris_df = pd.DataFrame(data = iris_data['data'], columns = iris_data['feature_names'])
iris_df['iris type'] = iris_data['target']
iris_df['iris name'] = iris_df['iris type'].apply(get_proper_name)

X = iris_df[['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)','petal width (cm)']]
y = iris_df['iris name']
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 0)

vals = []
for i, arg in enumerate(sys.argv):
        # print(f"Аргумент {i}: {arg}")
        vals.append(arg)
sizes = vals[1].split(' ')

print("Исходные данные:")
print(f"sepal length (cm) = {sizes[0]}")
print(f"sepal width (cm) = {sizes[1]}")
print(f"petal length (cm) = {sizes[2]}")
print(f"petal width (cm) = {sizes[3]}")

new_row = pd.DataFrame({'sepal length (cm)': sizes[0], 'sepal width (cm)': sizes[1], 'petal length (cm)': sizes[2], 'petal width (cm)': sizes[3]}, index=[0])
X_new = X_train.iloc[0:0]
X_new = pd.concat([new_row, X_new.loc[:]], axis=0).reset_index(drop=True)

knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)

# y_pred = knn.predict(X_test)
y_pred = knn.predict(X_new)



print(f"Предсказанный класс: {y_pred[0]}")
