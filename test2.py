import pandas as pd
import os
from sklearn import preprocessing

path = './CSV_ETH_TOP30/'

def getData():
    files = os.listdir(path)
    DF = pd.DataFrame(columns = ['Balance', 'DAU', 'ETH_Vol', 'Txs'])
    i = 1

    for file_name in files:
        file_path = path + file_name
        df = pd.read_csv(file_path)
        df = df[['Balance', 'DAU', 'ETH_Vol', 'Txs']]
        df = df.dropna()
        df = df[(df.T != 0).any()]
        x = df.values
        min_max_scaler = preprocessing.MinMaxScaler()
        x_scaled = min_max_scaler.fit_transform(x)
        df = pd.DataFrame(x_scaled, index = None, columns = ['Balance', 'DAU', 'ETH_Vol', 'Txs'])
        DF.append(df)
        print(str(i) + " Files Collected...")
        i += 1
    print("All Files Loaded ✔")
    return DF

DF = getData()
print(DF)