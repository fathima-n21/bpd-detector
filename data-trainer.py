#####################################################
# Loading Dataset Globally
# Data Preprocessing (assuming your data is in a CSV file)
import numpy as np
from sklearn.linear_model import LogisticRegression
import pandas as pd
import joblib
from sklearn.preprocessing import LabelEncoder, StandardScaler

# Read the data from the CSV file
data = pd.read_csv("dataset.csv")

# Drop the Timestamp column (not relevant for risk assessment)
data.drop("Timestamp", axis=1, inplace=True)

# Handle Missing Values (replace with your preferred method)
# Option 1: Fill missing values with mode (most frequent value) for categorical data and mean for numerical data
from scipy import stats

for col in data.columns:
  if data[col].dtype == 'object':
    data[col].fillna(data[col].mode()[0], inplace=True)  # Fill categorical with mode
  else:
    data[col].fillna(data[col].mean(), inplace=True)  # Fill numerical with mean

# Encode Categorical Variables
label_encoder = LabelEncoder()
for col in data.columns:
  if data[col].dtype == 'object':
    data[col] = label_encoder.fit_transform(data[col])

# Separate features and target variables
X = data.drop(columns=["BPD Risk", "Suicidal Risk"])
y = data[["BPD Risk", "Suicidal Risk"]]

# Standardize Numerical Features
scaler = StandardScaler()
numerical_cols = [col for col in X.columns if X[col].dtype != 'object']  # Get numerical columns
X[numerical_cols] = scaler.fit_transform(X[numerical_cols])

# Split data into training, validation, and testing sets (replace 0.2 with your desired validation split ratio)
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.15, random_state=42)  # Set random_state for reproducibility
X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=0.15, random_state=42)  # Further split training for validation


# Model Building
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

model = Sequential([
  Dense(128, activation="relu", input_shape=(X_train.shape[1],)),  # Replace 128 with chosen number of neurons
  Dense(64, activation="relu"),  # Replace 64 with chosen number of neurons
  Dense(2, activation="sigmoid")  # Output layer with 2 units (sigmoid for probability)
])

model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])

# Model Training
model.fit(X_train, y_train, epochs=10, validation_data=(X_val, y_val))  # Adjust epochs as needed

# Evaluation
model.evaluate(X_test, y_test)
#####################################################

# Save the model
model.save('model.keras')