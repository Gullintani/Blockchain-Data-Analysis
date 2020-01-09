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

predictor = ['Balance', 'ETH_Vol', 'Txs']
target = ['DAU']


X = df[predictor].values
y = df[target].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=40)
print("===================================================================================")
print("Train Shape is: " + str(X_train.shape)); print("Test Shape is: " + str(X_test.shape))
print("===================================================================================")

mlp_score_train = 0
mlp_score_test = 0
middle_l = 4
loop = 1

while(mlp_score_test < 0.8 and mlp_score_train < 0.8):
    mlp = MLPRegressor(hidden_layer_sizes=(300,middle_l,100), activation='tanh', solver='adam', max_iter=1000)
    mlp.fit(X_train,y_train)

    predict_train = mlp.predict(X_train)
    predict_test = mlp.predict(X_test)

    mlp_score_train = mlp.score(X_train, y_train)
    mlp_score_test = mlp.score(X_test, y_test)
    print("Starting Loop " + str(loop) + "; Using Middle Layer of " + str(middle_l))
    print('The Train Score Is ', mlp_score_train); print('The Test Score Is ', mlp_score_test)
    print("===================================================================================")
    model_name = "./ETH_models/ETH_300_" + str(middle_l) + "_100_tanh_adam_500.m"
    joblib.dump(mlp, model_name)
    loop += 1
    middle_l *= 2
    if middle_l >= 4096:
        print("middle layer reaches 4096, breaking tests")
        break