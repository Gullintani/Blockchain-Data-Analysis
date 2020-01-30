import pandas as pd
import os
from sklearn import preprocessing

path_test = './CSV_TRON/'

def getData(path):
    files = os.listdir(path)
    DF = pd.DataFrame(columns = ['Balance', 'DAU', 'Vol', 'Txs', 'Rank'])
    i = 1
    e = 0

    for file_name in files:
        file_path = path + file_name
        df = pd.read_csv(file_path)
        df = df[['Balance', 'DAU', 'Vol', 'Txs', 'Cate Rank']]
        df = df.dropna()
        df = df[(df.T != 0).any()]

        #Check Ranking
        # df['Exchange Rank'] = df['Exchange Rank'].map(lambda x: 1 if x <= 10 else 0)

        x = df.values
        min_max_scaler = preprocessing.MinMaxScaler()
        try:
            x_scaled = min_max_scaler.fit_transform(x)
        except:
            e += 1
            print("Normalization Failed...")
            continue
        df = pd.DataFrame(x_scaled, index = None, columns = ['Balance', 'DAU', 'Vol', 'Txs', 'Rank'])
        DF = pd.concat([DF, df])
        print(str(i) + " Files Collected...")
        i += 1
    print("==============================================")
    print("All Avaliable Files Loaded ✔")
    print("Except " + str(e) + " File(s) Failed.")
    return DF

DF = getData(path_test)
DF = DF.sort_values("Rank")
DF.to_csv("./TRON_ALL.csv")