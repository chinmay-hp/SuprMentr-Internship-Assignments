import re
import string
from sklearn.feature_extraction.text import TfidfVectorizer

# Sample Text
text = """
Machine learning is a powerful technology that allows computers to learn from data.
It is widely used in artificial intelligence, data science, and automation.
Machine learning helps in prediction, classification, and decision making.
"""

# Text Cleaning Function
def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^\x00-\x7F]+', '', text)
    text = text.translate(str.maketrans('', '', string.punctuation))
    return text

cleaned_text = clean_text(text)

# TF-IDF Vectorization
vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform([cleaned_text])

# Extract Keywords
feature_names = vectorizer.get_feature_names_out()
scores = X.toarray()[0]

# Get top 5 keywords
keyword_scores = dict(zip(feature_names, scores))
top_keywords = sorted(keyword_scores.items(), key=lambda x: x[1], reverse=True)[:5]

print("Top Keywords:\n")
for word, score in top_keywords:
    print(f"{word} : {score:.3f}")