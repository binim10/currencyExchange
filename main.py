import time
from datetime import *

import requests
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://binim1010:Aa2015binim92@cluster0.8dzfq.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

db=cluster["currency"]
collectionUSDILS = db["usd"]
collectionUSDEUR=db["EUR"]
# Where USD is the base currency you want to use

url_usd_ils = 'https://v6.exchangerate-api.com/v6/cbf2fd927138d10551eccbf1/pair/USD/ILS'
url_usd_eur='https://v6.exchangerate-api.com/v6/cbf2fd927138d10551eccbf1/pair/USD/EUR'


# Making our request

response_usd_ils = requests.get(url_usd_ils)
response_usd_eur = requests.get(url_usd_eur)

data_usd_ils = response_usd_ils.json()
data_usd_eur = response_usd_eur.json()

now = datetime.now()

usd_ils={'_id':now.strftime("%d/%m/%Y %H:%M:%S"),'USD-ILS':data_usd_ils['conversion_rate']}
usd_eur={'_id':now.strftime("%d/%m/%Y %H:%M:%S"),'USD-EUR':data_usd_eur['conversion_rate']}

collectionUSDILS.insert_one(usd_ils)
collectionUSDEUR.insert_one(usd_eur)
