import csv
import random
from datetime import datetime, timedelta

# Define the column names
columns = [
  "Timestamp",
  "abandonment",
  "feels empty",
  "traumatic events",
  "thoughts of self-harming",
  "attempted suicide",
  "brain damage",
  "reckless driving",
  "substance abuse",
  "gambling",
  "unsafe sex",
  "unhealthy eating",
  "enjoy eating",
  "unstable relationships",
  "relationships been troubled",
  "people donot understand me",
  "spacing out",
  "My views of others",
  "changing goals",
  "anger issues",
  "mood swings",
  "life difficulties",
  "irregular menstruation"
]

# Generate random data for the CSV
def generate_data():
    data = []
    for _ in range(10000):  # Generating 50 rows of data
        row = [
            (datetime.now() - timedelta(days=random.randint(0, 10), hours=random.randint(0, 23))).strftime('%d/%m/%Y %H:%M:%S'),
            random.choice(["Never", "Sometimes", "Always"]),
            random.choice(["Never", "Sometimes", "Always"]),
            random.choice(["No", "Yes"]),
            random.choice(["Never", "Sometimes", "Always"]),
            random.choice(["No", "Yes"]),
            random.choice(["No", "Yes"]),
            random.choice(["Never", "Sometimes", "Always"]),
            random.choice(["Never", "Sometimes", "Always"]),
            random.choice(["Never", "Sometimes", "Always"]),
            random.choice(["Never", "Sometimes", "Always"]),
            random.choice(["Never", "Sometimes", "Always"]),
            random.choice(["Never", "Sometimes", "Always"]),
            random.choice(["No", "Yes"]),
            random.choice(["No", "Yes"]),
            random.choice(["Never", "Sometimes", "Always"]),
            random.choice(["Never", "Sometimes", "Always"]),
            random.choice(["Never", "Sometimes", "Always"]),
            random.choice(["Never", "Sometimes", "Always"]),
            random.choice(["Never", "Sometimes", "Always"]),
            random.choice(["Never", "Sometimes", "Always"]),
            random.choice(["Never", "Sometimes", "Always"]),
            random.choice(["No", "Yes"]),
        ]
        data.append(row)
    return data

# Write data to CSV
with open('large-data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(columns)  # Write column headers
    writer.writerows(generate_data())  # Write generated data
