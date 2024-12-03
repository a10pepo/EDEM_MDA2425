import pymongo
import psycopg2
from psycopg2 import sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from collections import Counter
import string
import os

MONGO_URI = "mongodb://root:example@localhost:27017/"
MONGO_DB = "jokesDB"
MONGO_COLLECTION = "jokesCollection"

POSTGRES_HOST = os.getenv("POSTGRES_HOST", "localhost")
POSTGRES_DB = os.getenv("POSTGRES_DB", "jokes")
POSTGRES_USER = os.getenv("POSTGRES_USER", "postgres")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "Welcome01")

def create_database_if_not_exists(host, user, password, db_name):
    try:
        conn = psycopg2.connect(
            host=host,
            user=user,
            password=password,
        )
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cursor = conn.cursor()

        cursor.execute(f"SELECT 1 FROM pg_database WHERE datname = %s", (db_name,))
        if not cursor.fetchone():
            cursor.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier(db_name)))
        else:
            print(f"Database '{db_name}' already exists.")

        cursor.close()
        conn.close()
    except Exception as e:
        print(f"Error creating database: {e}")
        raise

create_database_if_not_exists(POSTGRES_HOST, POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_DB)

client = pymongo.MongoClient(MONGO_URI)
mongo_db = client[MONGO_DB]
collection = mongo_db[MONGO_COLLECTION]

conn = psycopg2.connect(
    host=POSTGRES_HOST,
    database=POSTGRES_DB,
    user=POSTGRES_USER,
    password=POSTGRES_PASSWORD,
)
cursor = conn.cursor()
while True:
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS joke_words (
        word VARCHAR(255) PRIMARY KEY,
        count INT DEFAULT 0
    );

    CREATE TABLE IF NOT EXISTS processed_jokes (
        joke_id VARCHAR(255) PRIMARY KEY,
        joke_date TIMESTAMP
    )
    """)
    conn.commit()

    documents = collection.find()
    all_words = []

    for doc in documents:
        joke_id = str(doc["_id"])
        joke_date = doc.get("date", "")
        joke_text = doc.get("joke", "")

        cursor.execute("SELECT 1 FROM processed_jokes WHERE joke_id = %s", (joke_id,))
        if cursor.fetchone():
            continue

        words = joke_text.translate(str.maketrans("", "", string.punctuation)).lower().split()
        all_words.extend(words)

        cursor.execute("""
        INSERT INTO processed_jokes (joke_id, joke_date)
        VALUES (%s, %s)
        """, (joke_id, joke_date))

    print(all_words)
    word_counts = Counter(all_words)
    print(word_counts)

    for word, count in word_counts.items():
        cursor.execute("""
        INSERT INTO joke_words (word, count)
        VALUES (%s, %s)
        ON CONFLICT (word)
        DO UPDATE SET count = joke_words.count + EXCLUDED.count
        """, (word, count))

    conn.commit()

    cursor.close()
    conn.close()
    client.close()
