import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

data = {
    'message': [
        "Win a free iPhone now",
        "Congratulations you won a prize",
        "Call me later",
        "Let's meet tomorrow",
        "Free entry in contest",
        "Important meeting at 10 AM",
        "Claim your reward now",
        "Are you coming to class?"
    ],
    'label': [
        'spam', 'spam', 'ham', 'ham',
        'spam', 'ham', 'spam', 'ham'
    ]
}

df = pd.DataFrame(data)

df['label'] = df['label'].map({'ham': 0, 'spam': 1})

X_train, X_test, y_train, y_test = train_test_split(
    df['message'], df['label'], test_size=0.2, random_state=42
)

vectorizer = TfidfVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

model = MultinomialNB()
model.fit(X_train_vec, y_train)

y_pred = model.predict(X_test_vec)
print("Accuracy:", accuracy_score(y_test, y_pred))

new_message = ["You have won a free ticket"]
new_vec = vectorizer.transform(new_message)

prediction = model.predict(new_vec)

if prediction[0] == 1:
    print("Spam Message 🚫")
else:
    print("Not Spam Message ✅")