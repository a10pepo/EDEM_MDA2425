import pymongo
from pymongo import MongoClient
import re
import pg8000.native

MONGO_URI = "mongodb://root:example@localhost:27017"
MONGO_DB = "Chuck"
MONGO_COLLECTION = "Bromas"



mongo_client = pymongo.MongoClient(MONGO_URI)
MONGO_DB = mongo_client["Chuck"]
mongo_collection = MONGO_DB["Bromas"]
jokes=[]




    # Leer documentos de MongoDB
documents = mongo_collection.find()

for doc in documents:
    value=doc.get('value')
    if value:
        value_limpio=re.sub(r'[^\w\s]','',value)
        jokes.append(value_limpio)
    values = value.split()
    for value in values:
        print(value)

conn = pg8000.native.Connection(user="postgres", password="Welcome01",host='localhost')

conn.run("""CREATE TABLE IF NOT EXIST Chuck (word VARCHAR(50) NOT NULL, time TIMESTAMP NOT NULL)""")
