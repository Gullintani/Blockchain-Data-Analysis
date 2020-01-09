import json
import os
import numpy as np
import pandas as pd
from pandas import DataFrame

path = './JSON_ETH_TOP30/'

def load(file_path):
    with open(file_path,'r') as f:
        data = json.load(f)
        return data
# balance_list, datadau_list, ethvolume_list, exchangerangking_list, totalrangking_list, txs_list

def saveAsCSV(path):
    i = 1
    files = os.listdir(path)
    for file_name in files:
        file_path = path + file_name
        r_dict = load(file_path)
        # print(len(eval(r_dict["balance_list"])))
        # print(len(eval(r_dict["datadau_list"])))
        # print(len(eval(r_dict["ethvolume_list"])))
        # print(len(eval(r_dict["exchangerangking_list"])))
        # print(len(eval(r_dict["totalrangking_list"])))
        # print(len(eval(r_dict["txs_list"])))

        # Load the lists
        stday_list = np.asarray(eval(r_dict["stday_list"]))
        balance_list = np.asarray(eval(r_dict["balance_list"]))
        datadau_list = np.asarray(eval(r_dict["datadau_list"]))
        ethvolume_list = np.asarray(eval(r_dict["ethvolume_list"]))
        exchangerangking_list = np.asarray(eval(r_dict["exchangerangking_list"]))
        totalrangking_list = np.asarray(eval(r_dict["totalrangking_list"]))
        txs_list = np.asarray(eval(r_dict["txs_list"]))

        # Format the arrays
        Date = stday_list.reshape(len(stday_list), 1)
        Balance = balance_list.reshape(len(balance_list), 1)
        DAU = datadau_list.reshape(len(datadau_list), 1)
        ETH_Vol = ethvolume_list.reshape(len(ethvolume_list), 1)
        Exchange_Rank = exchangerangking_list.reshape(len(exchangerangking_list), 1)
        Total_Rank = totalrangking_list.reshape(len(totalrangking_list), 1)
        Txs = txs_list.reshape(len(txs_list), 1)

        # hstack the arrays together
        data_array = np.hstack([Date, Balance, DAU, ETH_Vol, Exchange_Rank, Total_Rank, Txs])

        # Turn Array into Dataframe
        df = DataFrame(data_array, index = None, columns = ['Date', 'Balance', 'DAU', 'ETH_Vol', 'Exchange Rank', 'Total Rank', 'Txs'])

        # Save as CSV file
        save_file_name = file_name[0:-4] + 'csv'
        save_file_path = './CSV_ETH_TOP30/' + save_file_name
        df.to_csv(save_file_path)

        print(str(i) + ' file saved')
        i += 1

saveAsCSV(path)