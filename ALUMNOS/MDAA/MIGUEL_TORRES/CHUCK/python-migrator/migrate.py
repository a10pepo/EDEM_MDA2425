import pymongo
import psycopg2
from psycopg2 import sql
import os


mongo_uri = os.environ.get('MONGO_URI', 'mongodb://root:example@mongo:27017')
mongo_client = pymongo.MongoClient(mongo_uri)
mongo_db = mongo_client['chuckdb']
mongo_collection = mongo_db['jokes']


postgres_uri = os.environ.get('POSTGRES_URI', 'postgresql://admin:admin@postgres:5432/cuckpostgress')
postgres_conn = psycopg2.connect(postgres_uri)
postgres_cursor = postgres_conn.cursor()


create_table_query = """
CREATE TABLE IF NOT EXISTS jokes (
    id SERIAL PRIMARY KEY,
    text TEXT NOT NULL,
    category TEXT
);

CREATE TABLE IF NOT EXISTS words (
    id SERIAL PRIMARY KEY,
    word TEXT NOT NULL,
    joke_id INT NOT NULL,
    frequency INT DEFAULT 1,
    FOREIGN KEY (joke_id) REFERENCES jokes(id) ON DELETE CASCADE,
    UNIQUE (word, joke_id)
);
"""
postgres_cursor.execute(create_table_query)
postgres_conn.commit()


for joke in mongo_collection.find():
    joke_text = joke.get('value', '')
    joke_category = joke.get('category', '')

    
    insert_joke_query = sql.SQL("INSERT INTO jokes (text, category) VALUES (%s, %s) RETURNING id")
    postgres_cursor.execute(insert_joke_query, (joke_text, joke_category))
    joke_id = postgres_cursor.fetchone()[0]  

   
    words = joke_text.split()  

    
    insert_word_query = sql.SQL("""
        INSERT INTO words (word, joke_id) VALUES (%s, %s)
    """)

    for word in words:
        word = word.lower()  

        
        postgres_cursor.execute(insert_word_query, (word, joke_id))

    postgres_conn.commit()


postgres_cursor.close()
postgres_conn.close()
mongo_client.close()

print("Datos migrados y palabras actualizadas en PostgreSQL.")