import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd
from sklearn import preprocessing
from sklearn.preprocessing import PolynomialFeatures
df = pd.read_csv("./CSV_ETH_TOP30/0xUniverse.csv")

# Dropping
df = df.drop('Date', 1)
df = df.drop('Unnamed: 0', 1)
df = df.dropna()

# Normalization
x = df.values
min_max_scaler = preprocessing.MinMaxScaler()
x_scaled = min_max_scaler.fit_transform(x)
df = pd.DataFrame(x_scaled, index = None, columns = ['Balance', 'DAU', 'ETH_Vol', 'Exchange Rank', 'Total Rank', 'Txs'])
df = df[(df.T != 0).any()]

poly = PolynomialFeatures(degree = 3)
x_ = poly.fit_transform(df)

print("feature names")
print(poly.get_feature_names())
print(x_)

# predict = [[0.256, 0.578, 0.0276, 0.582]]
# predict_ = poly.fit_transform(predict)
# print(predict_)