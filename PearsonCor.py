import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn import preprocessing
df = pd.read_csv("./CSV_ETH_TOP30/0xUniverse.csv")
df = df.drop('Unnamed: 0', 1)
x = df.values
min_max_scaler = preprocessing.MinMaxScaler()
x_scaled = min_max_scaler.fit_transform(x)
df = pd.DataFrame(x_scaled, index = None, columns = ['Balance', 'DAU', 'ETH_Vol', 'Exchange Rank', 'Total Rank', 'Txs'])

print(df)

plt.figure(figsize=(15,15))
cor = df.corr()
sns.heatmap(cor, annot=True, cmap=plt.cm.Reds)
plt.show()