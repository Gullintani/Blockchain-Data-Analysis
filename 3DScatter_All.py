import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
 
# Read Data
df = pd.read_csv('./TRON_ALL.csv')
df = df[['Vol', 'Txs', 'Rank']]

cm = plt.get_cmap("plasma")
col = [cm(float(i)/(9917)) for i in range(9917)]
# ETH 26246 winter
# EOS 12412 plasma
# TRON 9917 copper


# Plot Scatter
fig = plt.figure()
ax = Axes3D(fig)
ax.scatter(df['Vol'], df['Txs'], df['Rank'], c=col)
 
# Set Legend
# ax.legend(loc='best')
 
# Set Axis
ax.set_xlabel('Vol')
ax.set_ylabel('Transaction')
ax.set_zlabel('Rank')

# 展示
plt.show()