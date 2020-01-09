import matplotlib
import matplotlib.pyplot as plt

import pandas as pd
import numpy as np

from sklearn import svm
import joblib

df = pd.read_csv("../eth-correlation-std.csv")
target = df["GameDAU"]
FMatrix = df.drop("GameDAU",1)

def transform_data(input):
    outcome = []
    for item in input:
        outcome.append(int(item*14211))
    return outcome
        
train_input = np.array(FMatrix)
train_output = np.array(target)
list_train_input = train_input.tolist()
list_train_output = train_output.tolist()

list_train_output = transform_data(list_train_output)
clf = svm.SVC()
clf.fit(list_train_input, list_train_output)
joblib.dump(clf, "./models/ETH_SVM.m")