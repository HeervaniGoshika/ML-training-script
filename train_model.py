# train_model.py
import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Load data
data = pd.read_csv("data.csv")

# Split
X = data[['feature1', 'feature2']]
y = data['target']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

print("Model trained successfully!")
print("Accuracy:", model.score(X_test, y_test))

# Save model
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)