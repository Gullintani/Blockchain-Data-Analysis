import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd
from sklearn import preprocessing
df = pd.read_csv("./CSV_ETH_TOP30/CryptoDozer.csv")
df = df.drop('Date', 1)
df = df.drop('Unnamed: 0', 1)
x = df.values
min_max_scaler = preprocessing.MinMaxScaler()
x_scaled = min_max_scaler.fit_transform(x)
df = pd.DataFrame(x_scaled, index = None, columns = ['Balance', 'DAU', 'ETH_Vol', 'Exchange Rank', 'Total Rank', 'Txs'])

fig = plt.figure()
ax = Axes3D(fig)
ax.scatter(df['ETH_Vol'], df['DAU'], df['Txs'])
ax.set_xlabel('ETH_Vol')
ax.set_ylabel('DAU')
ax.set_zlabel('Txs')

plt.show()