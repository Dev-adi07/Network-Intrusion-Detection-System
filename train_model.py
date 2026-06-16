from sklearn.ensemble import RandomForestClassifier
import numpy as np
import joblib

# Dummy training data
X = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [2,3,4]
])

y = np.array([0,1,1,0])

# Train model
model = RandomForestClassifier()
model.fit(X, y)

# Save model
joblib.dump(model, 'model.pkl')

print("Model Saved Successfully")