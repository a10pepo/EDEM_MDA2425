import pymongo
from collections import Counter
import re

client = pymongo.MongoClient(f"mongodb://root:example@localhost:27017/?authSource=admin")

db = client["chuckdb"]
col = db["jokes"]

all_documents = col.find()

word_counter = Counter()

for doc in all_documents:
    joke_text = doc.get('value', '')
    
    joke_text = joke_text.lower()
    
    words = re.findall(r'\b\w+\b', joke_text)
    
    word_counter.update(words)

for word, count in word_counter.items():
    print(f"{word}: {count}")
    