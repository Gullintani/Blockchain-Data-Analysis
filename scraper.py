import requests
import pandas as pd
import numpy as np
import time
import json

id_dict = {"8102": "超级贪食蛇","8978": "八宝树","6140": "区块链萌宠","6298": "Play-GOC","8632": "Eggies-World","6636": "Traps","8076": "澳波钱包","5752": "Tronman","8908": "Snail-Trails","6455": "TronGoo","7535": "Tronjedies-space","8727": "CryptoFlowers","6582": "BLOCKLORDS","9451": "Planet-BOOM-","9588": "NewGoo","9504": "ENME","8804": "BeeHive","8693": "Aftermath-Islands","8590": "TronBoard","8574": "0xRacers","7181": "TronOY","6569": "疯狂拼音","6489": "Cipher","9453": "Golden-craft","9222": "Tronvr-space","9192": "PlanetCrypto","9051": "MegaCryptoPolis","8972": "Golden-Craft","8934": "BomberTRON","8911": "出琦制胜","8883": "Knightlands","8802": "HXXD--Play---Win-TRX--","8797": "SoloPoker","8744": "NoleLegends-2019--Gaming-for-charity","8578": "Candy-Crunch-DApp","8061": "Tron-Treasure-Hunt","7843": "亚当的冒险","7643": "Tron-Battles","7633": "Dragon-Castle","7524": "TronEgypt","7477": "Stake-Them-ALL--Tron-Edition-","7291": "Tron-Tanks","7259": "TRON-Birds","7244": "CryptoRacing--TRON-","7197": "TRONRAIDER","7168": "TronCountry","7159": "TRONLOTO","7130": "KuaiXiYou","7118": "Smart-Town","7087": "Tronzinc","6804": "ClashRoyale","6763": "TronLegend","6731": "PlanetCrypto","6715": "Red-Wall---红包墙","6641": "0xWarriors","6640": "Tron-MineWars","6537": "TRONLegend-波场传奇","6534": "FaceWorths","6531": "Crypto-Beauty","6510": "TronKingdom","6504": "鱼雷发射","6503": "HDX20","6502": "EtherKnight--Tron-Edition-","6486": "Epic-Dragons","6477": "Tron-Flappy-Bird","6462": "TronGuess","6458": "Rage-of-Ramonov","6457": "CryptoElement-","6456": "Crazy-Dogs-Live","6450": "Tron-Idol","6449": "TycoonWay","6425": "进化星球","6396": "Pixel-Wars","6387": "Cryptofaucet","6383": "CATDICE","6303": "永恒之龙","6273": "Coloron","6117": "SpiritWarrior","6110": "TronPixel","6056": "Chibi-战士","5751": "TRONCryptoMahjong3D","5746": "最后的旅途","5745": "Snatch3D"}
def StoreCSV(str, key):
    df = pd.read_json(str, encoding="utf-8", orient='records')
    file_name = "./JSON_TRON/" + id_dict[key] + ".csv"
    df.to_csv(file_name)

def StoreJson(str, key):
    j = json.loads(str)
    j = j["content"]
    file_name = "./JSON_TRON/" + id_dict[key] + ".json"
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