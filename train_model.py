import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

# Load dataset
data = pd.read_csv("dataset/student_data.csv")

X = data.drop("Performance", axis=1)
y = data["Performance"]

# Train model
model = RandomForestClassifier(random_state=42)
model.fit(X, y)

# Create models folder if it doesn't exist
os.makedirs("models", exist_ok=True)

# Save model
joblib.dump(model, "models/student_model.pkl")

print("✅ Model trained and saved successfully!")