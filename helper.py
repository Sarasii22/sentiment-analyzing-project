# helper.py – use TF-IDF version

import pickle
import pandas as pd
import re
import string
from nltk.stem import SnowballStemmer

# Load TF-IDF vectorizer and model (the ones you just trained)
with open('static/model/tfidf_vectorizer.pickle', 'rb') as f:
    tfidf = pickle.load(f)

with open('static/model/model.pickle', 'rb') as f:
    model = pickle.load(f)

with open('static/model/corpora/stopwords/english', 'r') as file:
    sw = file.read().splitlines() #take line by line as a list

from nltk.stem import PorterStemmer
ps = PorterStemmer()

from nltk.stem import SnowballStemmer
snowball = SnowballStemmer("english")


def remove_punctuations(text):
    for p in string.punctuation:
        text = text.replace(p, '')
    return text

def preprocessing(text):
    data = pd.DataFrame([text], columns=["tweet"])
    data["tweet"] = data["tweet"].str.lower()
    data["tweet"] = data["tweet"].apply(lambda x: re.sub(r'https?://\S+|www\.\S+', '', x))
    data["tweet"] = data["tweet"].apply(remove_punctuations)
    data["tweet"] = data["tweet"].str.replace(r'\d+', '', regex=True)
    
    data["tweet"] = data["tweet"].apply(lambda x: " ".join(x for x in x.split() if x not in ['a','an','the','and','or','but','if','not','then']))
    data["tweet"] = data["tweet"].apply(lambda x: " ". join(x for x in x.split() if x not in sw))
    data["tweet"] = data["tweet"].apply(lambda x: " ".join(snowball.stem(x) for x in x.split()))
    return data["tweet"]

def get_prediction(text):
    # text must be string
    processed_series = preprocessing(text)
    processed_str = processed_series.iloc[0]
    
    vector = tfidf.transform([processed_str])
    proba_negative = model.predict_proba(vector)[0][1]
    
    threshold = 0.60   # your last used value
    
    return "negative" if proba_negative >= threshold else "positive"