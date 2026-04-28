import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import OneHotEncoder, StandardScaler
import matplotlib.pyplot as plt

# Sample Mall Dataset
data = {
    'CustomerID': [1,2,3,4,5,6,7,8,9,10],
    'Gender': ['Male','Male','Female','Female','Female','Male','Female','Male','Male','Female'],
    'Age': [19,21,20,23,31,22,35,23,64,30],
    'Annual_Income': [15,15,16,16,17,18,19,20,21,22],
    'Spending_Score': [39,81,6,77,40,76,6,94,3,72]
}

df = pd.DataFrame(data)

# One-Hot Encoding for Gender
encoder = OneHotEncoder(sparse=False)
gender_encoded = encoder.fit_transform(df[['Gender']])

gender_df = pd.DataFrame(gender_encoded, columns=encoder.get_feature_names_out(['Gender']))

# Combine encoded data with original dataset
df = pd.concat([df.drop('Gender', axis=1), gender_df], axis=1)

# Features for clustering
X = df.drop('CustomerID', axis=1)

# Feature Scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# K-Means Model
kmeans = KMeans(n_clusters=3, random_state=42)
df['Cluster'] = kmeans.fit_predict(X_scaled)

# Display clustered data
print(df)

# Plot (Income vs Spending Score)
plt.scatter(df['Annual_Income'], df['Spending_Score'], c=df['Cluster'])
plt.xlabel("Annual Income")
plt.ylabel("Spending Score")
plt.title("Customer Segmentation")
plt.show()