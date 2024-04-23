import csv

def assess_bpd_risk(row):
  bpd_indicators = ['abandonment', 'feels empty', 'traumatic events', 'thoughts of self-harming', 'attempted suicide',
                    'brain damage', 'reckless driving', 'substance abuse', 'gambling', 'unsafe sex', 'unhealthy eating',
                    'unstable relationships', 'relationships been troubled', 'people donot understand me', 'spacing out',
                    'My views of others', 'changing goals', 'anger issues', 'mood swings', 'life difficulties', 'irregular menstruation']
  risk_score = 0
  for indicator in bpd_indicators:
    if indicator in row:
      answer = row[indicator]
      # Assign weights based on answer severity (adjust weights as needed)
      if answer == "Always":
        risk_score += 3
      elif answer == "Sometimes":
        risk_score += 2
      elif answer == "Never":
        risk_score += 0
      elif answer == "Yes":
        risk_score += 2  # Adjust weight for "Yes" as needed
      elif answer == "No":
        risk_score += 0  # Adjust weight for "No" as needed

  # Risk categories remain the same
  if risk_score <= 3:
    return 'No Risk'
  elif risk_score <= 6:
    return 'Low Risk'
  elif risk_score <= 10:
    return 'Medium Risk'
  elif risk_score <= 15:
    return 'High Risk'
  else:
    return 'Extreme Risk'

def assess_suicidal_risk(row):
  # Similar logic as assess_bpd_risk with adjusted weights for suicidal indicators
  if ('thoughts of self-harming' in row and (row['thoughts of self-harming'] == "Always" or row['thoughts of self-harming'] == "Sometimes")) or \
     ('attempted suicide' in row and row['attempted suicide'] == "Yes"):
    return 'Extreme Risk'
  elif ('anger issues' in row and (row['anger issues'] == "Always" or row['anger issues'] == "Sometimes")) or \
       ('mood swings' in row and (row['mood swings'] == "Always" or row['mood swings'] == "Sometimes")):
    return 'High Risk'
  elif ('feels empty' in row and (row['feels empty'] == "Always" or row['feels empty'] == "Sometimes")) or \
       ('unhealthy eating' in row and (row['unhealthy eating'] == "Always" or row['unhealthy eating'] == "Sometimes")):
    return 'Medium Risk'
  elif ('traumatic events' in row and row['traumatic events'] == "Yes") or \
       ('people donot understand me' in row and (row['people donot understand me'] == "Always" or row['people donot understand me'] == "Sometimes")):
    return 'Low Risk'
  else:
    return 'No Risk'

def analyze_csv(file_path, output_file_path):
  with open(file_path, 'r') as file, open(output_file_path, 'w', newline='') as output_file:
    reader = csv.DictReader(file)
    writer = csv.DictWriter(output_file, fieldnames=reader.fieldnames + ['BPD Risk', 'Suicidal Risk'])
    writer.writeheader()
    for row in reader:
      bpd_risk = assess_bpd_risk(row)
      suicidal_risk = assess_suicidal_risk(row)
      row['BPD Risk'] = bpd_risk
      row['Suicidal Risk'] = suicidal_risk
      writer.writerow(row)

# Example usage (assuming data.csv has headers matching bpd_indicators)
analyze_csv('google-form-data.csv', 'dataset.csv')
# analyze_csv('large-data.csv', 'dataset.csv')

