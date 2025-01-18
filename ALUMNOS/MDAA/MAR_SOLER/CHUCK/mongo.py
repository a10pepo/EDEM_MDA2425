import pymongo
import re
import pg8000.native

from pymongo import MongoClient

# Conexión a Postgres
con = pg8000.native.Connection(user="postgres", password="Welcome01",host='postgres')

# Creaomos tabla en Postgres
con.run("""CREATE TABLE IF NOT EXISTS chuck (
    word VARCHAR(50) NOT NULL,
    time TIMESTAMP NOT NULL)"""
)

# Conexión a MongoDB
client = MongoClient("mongodb://root:example@mongo:27017/")


db = client["chuck"]
collection = db["all"]

# Para comprobar que funciona Mongo
#   print(collection.find_one())

# Lista para almacenar los chistes
jokes = []

# Revisamos cada document y cogemos el value
for document in collection.find():
    value = document.get("value")
    
    if value:
        value_limpio = re.sub(r'[^a-zA-Z ]', '', value)
        jokes.append(value_limpio)

# Revisamos cada chiste y separamos las palabras
for joke in jokes:
    for word in joke.split(" "):
        con.run(f"insert into chuck (word,time) values ('{word}',now())") #La f nos permite meter word como parámtero