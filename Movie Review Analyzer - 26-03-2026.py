from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

# Training Data
reviews = [
    "This movie was amazing and very interesting",
    "I loved the acting and story",
    "The movie was boring and too long",
    "Worst film I have ever seen",
    "It was okay not that great"
]

labels = ["positive", "positive", "negative", "negative", "negative"]

# TF-IDF Vectorization
vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(reviews)

# Model Training
model = MultinomialNB()
model.fit(X, labels)

# Test Reviews
test_reviews = [
    "I really loved this movie",
    "This film was terrible",
    "Amazing story and acting",
    "Not good very boring",
    "It was fine"
]

# Prediction
X_test = vectorizer.transform(test_reviews)
predictions = model.predict(X_test)

# Output
print("Sentiment Predictions:\n")
for review, pred in zip(test_reviews, predictions):
    print(f"{review} --> {pred}")