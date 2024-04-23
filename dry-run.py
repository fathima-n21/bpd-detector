# Run this file to see a test run of the trained model

import numpy as np
from sklearn.preprocessing import LabelEncoder, StandardScaler
from tensorflow.keras.models import load_model

# Sample data (replace with yours)
new_data = {
  "abandonment": "Always",
  "feels empty": "No",
  "traumatic events": "No",
  "thoughts of self-harming": "Never",
  "attempted suicide": "Yes",
  "brain damage": "No",
  "reckless driving": "Never",
  "substance abuse": "Never",
  "gambling": "Never",
  "unsafe sex": "Never",
  "unhealthy eating": "Never",
  "enjoy eating": "Always",
  "unstable relationships": "No",
  "relationships been troubled": "No",
  "people donot understand me": "Never",
  "spacing out": "Never",
  "My views of others": "Never",
  "changing goals": "Never",
  "anger issues": "Never",
  "mood swings": "Never",
  "life difficulties": "Never",
  "irregular menstruation": "No"
}

# Label encoding (replace with your encoding scheme if used during training)
le = LabelEncoder()
for col in new_data:
  new_data[col] = le.fit_transform([new_data[col]])[0]

# Standardize numerical features (replace with your scaling logic if used during training)
# Assuming there are no numerical features in this example, we skip scaling

# Convert data to a NumPy array
new_data_array = np.array([list(new_data.values())])

# Load a mock model (replace with your actual saved model 'model.keras')
model = load_model('model.keras')

# Make prediction
predictions = model.predict(new_data_array)

# Print results (assuming the first element is BPD risk and second is Suicidal risk)
print("BPD Risk:", predictions[0][0])
print("Suicidal Risk:", predictions[0][1])

# Interpretation (replace with your risk thresholds based on model training)
if predictions[0][0] > 0.8:
  print("BPD Risk: High")
elif predictions[0][0] > 0.5:
  print("BPD Risk: Moderate")
else:
  print("BPD Risk: Low")

if predictions[0][1] > 0.8:
  print("Suicidal Risk: Extreme")
elif predictions[0][1] > 0.5:
  print("Suicidal Risk: High")
else:
  print("Suicidal Risk: Moderate")

# Disclaimer
print("Disclaimer: This is a sample prediction for informational purposes only. Please consult a mental health professional for any risk assessment.")