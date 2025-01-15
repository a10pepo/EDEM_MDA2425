import pymongo
from pymongo import MongoClient
import re
import pg8000.native


con = pg8000.native.Connection(user="postgres", password="Welcome01",host='postgres')
myclient=pymongo.MongoClient("mongodb://root:example@localhost:27017/")
mybd=myclient["Chuck"]
mycol=mybd["Database_Chuck"]

# x=mycol.find_one()
#Crear tabla para postgres
create_table=("""CREATE TABLE IF NOT EXISTS chuck (
    palabras varchar(50)  NOT NULL,
    tiempo timestamp  NOT NULL)"""
    )

con.run(create_table)

# print(x)

jokes=[]

for document in mycol.find():
    value=document.get('value')
 
    if value:
        value_limpio=re.sub(r'[^\w\s]','',value)
        jokes.append(value_limpio)

    
    
    print(jokes)


#Lista palabras


for joke in jokes:
    for word in joke.split(" "):
        con.run(f"INSERT INTO chuck(palabras,tiempo) VALUES('{word}',now())")
                
        print(word)
    

