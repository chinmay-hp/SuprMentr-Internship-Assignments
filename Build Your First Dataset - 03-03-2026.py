#  Create a dataset (e.g., study hours vs marks), identify features & labels, predict relationship.

import numpy as np
from sklearn.linear_model import LinearRegression

# Dataset
X = np.array([1,2,3,4,5,6,7,8,9,10]).reshape(-1,1)
y = np.array([40,45,50,55,65,70,75,85,90,95])

# Model
model = LinearRegression()
model.fit(X, y)

# Prediction
predicted_marks = model.predict([[7]])
print("Predicted Marks:", predicted_marks[0])