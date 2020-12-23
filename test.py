import pymongo
import pandas as pd

# mongodb+srv://USER1:*****@cluster0.loonh.mongodb.net/test?authSource=admin&replicaSet=atlas-n1o4yx-shard-0&readPreference=primary&appname=MongoDB%20Compass&ssl=true

class Mongodbconnect:

    def insert_database(database, collection, datasets):
        client = pymongo.MongoClient("mongodb+srv://USER1:mamu13@cluster0.loonh.mongodb.net/test?authSource=admin&replicaSet=atlas-n1o4yx-shard-0&readPreference=primary&appname=MongoDB%20Compass&ssl=true")
        mydb = client[database]
        mycol = mydb[collection]
        mycol.insert_many(datasets) #insert_one for 1 entry
    



#--> CSV Dateien konvertieren in JSON und automatisch in DB hochladen
# Connection DB der Unternehmen --> bestimmte ERP-Systeme

#pipenv install flask flask-pymongo python-dotenv
# init.py ln 110 = uri = ersetzen durch mongouri

client = pymongo.MongoClient("mongodb+srv://USER1:mamu13@cluster0.loonh.mongodb.net/test?authSource=admin&replicaSet=atlas-n1o4yx-shard-0&readPreference=primary&appname=MongoDB%20Compass&ssl=true")
mydb = client["Prüfdaten"]
mycol = mydb["Unternehmen_1"]
datasets = {"Name": "Yildirim"}


mycol.insert_one({datasets})