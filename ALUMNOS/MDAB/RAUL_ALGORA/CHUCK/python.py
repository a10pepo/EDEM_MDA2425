import pymongo
import pandas as pd
from collections import Counter
import re
from nltk.corpus import stopwords
import nltk

nltk.download('stopwords')

client = pymongo.MongoClient('mongodb://root:example@localhost:27017/')
db = client['CHUCK_NORRIS']
collection = db['CHISTE']

data = list(collection.find())

words = set()

for record in data:
    joke = record.get('value', '')
    cleaned_joke = re.sub(r'\W+', ' ', joke.lower())
    words.update(cleaned_joke.split())

stop_words = set(stopwords.words('english'))
filtered_words = [word for word in words if word not in stop_words]

word_count = Counter(filtered_words)

df = pd.DataFrame(word_count.items(), columns=['Word', 'Count'])
df = df.sort_values(by='Count', ascending=False)

print(df)
df.to_csv('word_frequency.csv', index=False)
