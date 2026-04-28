from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

# Documents
documents = [
    "Machine learning is very useful in data science",
    "Data science uses machine learning algorithms",
    "Artificial intelligence and machine learning are related fields",
    "Data analysis is important in science",
    "Machine learning helps in prediction and analysis"
]

# TF-IDF Vectorizer
vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(documents)

# Convert to DataFrame
df = pd.DataFrame(X.toarray(), columns=vectorizer.get_feature_names_out())

# Display TF-IDF values
print("TF-IDF Matrix:\n")
print(df)

# Extract Top Keywords from each document
print("\nTop Keywords per Document:\n")
for i, row in df.iterrows():
    top_words = row.sort_values(ascending=False).head(3)
    print(f"Document {i+1}: {list(top_words.index)}")


# Explanation:- 

# Common words like “machine”, “data”, “learning” appear in many documents → lower importance
# Unique words like:
# “artificial”, “prediction”, “algorithms” → higher importance
# TF-IDF highlights distinctive words in each document