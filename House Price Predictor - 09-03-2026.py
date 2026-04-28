import numpy as np
from sklearn.linear_model import LinearRegression

# Dataset
X = np.array([
    [800, 2],
    [1000, 2],
    [1200, 3],
    [1500, 3],
    [1800, 4]
])

y = np.array([40, 50, 60, 75, 90])

# Model
model = LinearRegression()
model.fit(X, y)

# Prediction (new house)
new_house = np.array([[1400, 3]])
predicted_price = model.predict(new_house)

print("Predicted Price:", predicted_price[0], "Lakhs")