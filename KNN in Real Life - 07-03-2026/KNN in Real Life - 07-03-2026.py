# KNN Recommendation – Python Example

import numpy as np
from sklearn.neighbors import NearestNeighbors

# User preference dataset
# [Action, Comedy, Drama]
data = np.array([
    [5, 2, 1],  # User A
    [5, 1, 1],  # User B
    [4, 2, 1],  # User C
    [1, 5, 4]   # User D
])

model = NearestNeighbors(n_neighbors=2, metric='euclidean')
model.fit(data)

target_user = data[0].reshape(1, -1)

distances, indices = model.kneighbors(target_user)

print("Nearest Neighbors (indices):", indices)
print("Distances:", distances)

# Assume:
# User B and C liked a movie → recommend to A

neighbors = indices[0]

print("Recommended based on similar users:")
for n in neighbors:
    print(f"User {chr(65+n)} preferences:", data[n])

