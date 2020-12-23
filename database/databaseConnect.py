import pymongo

class ConnectToMongoDB:

    def insert_Database(db, col, data):
        client = pymongo.MongoClient("mongodb+srv://USER1:mamu13@cluster0.loonh.mongodb.net/test?authSource=admin&replicaSet=atlas-n1o4yx-shard-0&readPreference=primary&appname=MongoDB%20Compass&ssl=true")
        db = client[db]
        col = db[col]
        col.insert_many(data)

    def read_Database(db, col, *arg):
        client = pymongo.MongoClient("mongodb+srv://USER1:mamu13@cluster0.loonh.mongodb.net/test?authSource=admin&replicaSet=atlas-n1o4yx-shard-0&readPreference=primary&appname=MongoDB%20Compass&ssl=true")
        db = client[db]
        col = db[col].find()

        output = []
        for x in list:
            output.append(x)
        return output