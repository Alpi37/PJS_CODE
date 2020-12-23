import pandas as pd
import csv 
import json
import pymongo
from pymongo import MongoClient
from csv2json import convert, load_csv, save_json



client = pymongo.MongoClient("mongodb+srv://USER1:mamu13@cluster0.loonh.mongodb.net/test?authSource=admin&replicaSet=atlas-n1o4yx-shard-0&readPreference=primary&appname=MongoDB%20Compass&ssl=true")
db = client["Prüfdaten"]
col = db["Unternehmen_1"]
#csv_data = pd.read_csv(r'C:\Users\Kanacken-PC\Desktop\PJS_Code\example.csv')   

with open(r"C:\Users\Kanacken-PC\Desktop\PJS_Code\example.csv") as r, open('output.json', 'w') as w:
    json_data = convert(r, w)
#with open(r"C:\Users\Kanacken-PC\Desktop\PJS_Code\output.json") as f:
    file_json = json.load(json_data)

col.insert_one(file_json)



