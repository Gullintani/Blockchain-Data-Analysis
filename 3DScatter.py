import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd

df = pd.read_csv("./ETH_ALL.csv")
df = df['']

fig = plt.figure()
ax = Axes3D(fig)
ax.scatter(df['ETH_Vol'], df['DAU'], df['Txs'])
ax.set_xlabel('ETH_Vol')
ax.set_ylabel('DAU')
ax.set_zlabel('Txs')

plt.show()