import requests
import pandas as pd
import numpy as np
import time
import json

id_dict = {"8102":"超级贪食蛇","6140":"区块链萌宠","8978":"八宝树","6636":"Traps","6298":"Play-GOC","8632":"Eggies-World","8908":"Snail-Trails","6455":"TronGoo","5752":"Tronman","8076":"澳波钱包","6582":"BLOCKLORDS","7535":"Tronjedies-space","9451":"Planet-BOOM-","8727":"CryptoFlowers","9588":"NewGoo","9504":"ENME","9192":"PlanetCrypto","8804":"BeeHive","8693":"Aftermath-Islands","6763":"TronLegend","6425":"进化星球","6387":"Cryptofaucet","9453":"Golden-craft","9222":"Tronvr-space","9051":"MegaCryptoPolis","8972":"Golden-Craft","8934":"BomberTRON","8911":"出琦制胜","8883":"Knightlands","8802":"HXXDPlayWinTRX"}
def StoreCSV(str, key):
    df = pd.read_json(str, encoding="utf-8", orient='records')
    file_name = "./TRON_TOP30/" + id_dict[key] + ".csv"
    df.to_csv(file_name)

def StoreJson(str, key):
    j = json.loads(str)
    j = j["content"]
    file_name = "./JSON_TRON_TOP30/" + id_dict[key] + ".json"
    with open(file_name, 'w') as fw:
        json.dump(j, fw)

def ScrapeData(dict):
    i = 1
    for key in dict:
        randsleep = np.random.randint(low = 1, high = 10, size = 1)
        time.sleep(randsleep)
        payload = {
            'daynumber':'all',
            'id': key,
            'sign':'false',
            'langue':'en'
        }

        headers = {"accept":"application/json, text/plain, */*","accept-language":"zh-CN,zh;q=0.9,en;q=0.8,ja;q=0.7","cache-control":"no-cache","content-type":"application/x-www-form-urlencoded","pragma":"no-cache","sec-fetch-mode":"cors","sec-fetch-site":"same-origin"}
        r = requests.post('https://dapptotal.com/api/view',headers = headers, data = payload)
        StoreJson(r.text, key)
        print(str(i) + " file saved")
        i = i + 1

ScrapeData(id_dict)