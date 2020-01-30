# Import required libraries
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import sklearn
from sklearn import preprocessing
from sklearn.neural_network import MLPRegressor
import joblib

# Import necessary modules
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report,confusion_matrix

df = pd.read_csv("./ETH_ALL.csv")

predictor = ['Vol', 'Txs', 'DAU']
target = ['Rank']


X = df[predictor].values
y = df[target].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, shuffle=True)
print("===================================================================================")
print("Train Shape is: " + str(X_train.shape)); print("Test Shape is: " + str(X_test.shape))
print("===================================================================================")

mlp = MLPRegressor(hidden_layer_sizes=(9,3), activation='logistic', solver='adam', max_iter=1000, alpha=0.0001, batch_size=100, learning_rate='adaptive', learning_rate_init=0.001)
mlp.fit(X_train,y_train)

predict_train = mlp.predict(X_train)
predict_test = mlp.predict(X_test)

x_axis = np.arange(len(y_train))
plt.scatter(x_axis, y_train, c='b', alpha= 0.6)
plt.scatter(x_axis, predict_train, c='r', alpha= 0.6)
plt.show()

model_name = "./Models/test.m"
joblib.dump(mlp, model_name)