import re
import string
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS
from sklearn.preprocessing import OneHotEncoder
import numpy as np

# Sample messy sentences
sentences = [
    "OMG!!! This movie is sooo good 😂",
    "Hey bro, are you coming to class???",
    "I cant beleive this happend!!!",
    "This place is lit 🔥🔥"
]

# Function to clean text
def clean_text(text):
    # Lowercase
    text = text.lower()
    
    # Remove emojis (simple way)
    text = re.sub(r'[^\x00-\x7F]+', '', text)
    
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    
    # Remove extra spaces
    text = re.sub(r'\s+', ' ', text).strip()
    
    # Remove stopwords
    words = text.split()
    words = [word for word in words if word not in ENGLISH_STOP_WORDS]
    
    return " ".join(words)

# Clean all sentences
cleaned_sentences = [clean_text(s) for s in sentences]

print("Cleaned Sentences:")
for s in cleaned_sentences:
    print(s)

# One-Hot Encoding (word-level)
all_words = list(set(" ".join(cleaned_sentences).split()))
all_words = sorted(all_words)

word_to_index = {word: i for i, word in enumerate(all_words)}

one_hot_vectors = []

for sentence in cleaned_sentences:
    vector = [0] * len(all_words)
    for word in sentence.split():
        vector[word_to_index[word]] = 1
    one_hot_vectors.append(vector)

print("\nVocabulary:", all_words)
print("\nOne-Hot Encoded Vectors:")
for vec in one_hot_vectors:
    print(vec)