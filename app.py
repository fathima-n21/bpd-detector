#####################################################
from flask import Flask, render_template, request
import numpy as np
import pandas as pd
import joblib
from sklearn.linear_model import LogisticRegression
from tensorflow.keras.models import load_model
#####################################################

app = Flask(__name__)

from sklearn.preprocessing import LabelEncoder, StandardScaler

# Load the trained model 
model = load_model('model.keras')
print('trained model : ', model)

@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "GET":
        return render_template("index.html")

    else:
        new_data = {
          "abandonment": request.form["abandonment"],
          "feels empty": request.form["feels_empty"],
          "traumatic events": request.form["traumatic_events"],
          "thoughts of self-harming": request.form["thoughts_of_self_harming"],
          "attempted suicide": request.form["attempted_suicide"],
          "brain damage": request.form["brain_damage"],
          "reckless driving": request.form["reckless_driving"],
          "substance abuse": request.form["substance_abuse"],
          "gambling": request.form["gambling"],
          "unsafe sex": request.form["unsafe_sex"],
          "unhealthy eating": request.form["over_eating"],
          "enjoy eating": request.form["enjoy_food"],
          "unstable relationships": request.form["unstable_relationship"],
          "relationships been troubled": request.form["breakups"],
          "people donot understand me": request.form["dont_understant_me"],
          "spacing out": request.form["spacing_out"],
          "My views of others": request.form["views_of_others"],
          "changing goals": request.form["value_my_self"],
          "anger issues": request.form["anger"],
          "mood swings": request.form["mood_shift"],
          "life difficulties": request.form["difficulties_in_life"],
          "irregular menstruation": request.form["menstruation"],
        }

        # Label encoding (replace with your encoding scheme if used during training)
        le = LabelEncoder()
        for col in new_data:
          new_data[col] = le.fit_transform([new_data[col]])[0]

        # Standardize numerical features (replace with your scaling logic if used during training)
        # Assuming there are no numerical features in this example, we skip scaling

        # Convert data to a NumPy array
        new_data_array = np.array([list(new_data.values())])

        # Make prediction
        predictions = model.predict(new_data_array)
        
        # Print results (assuming the first element is BPD risk and second is Suicidal risk)
        print("BPD Risk:", predictions[0][0])
        print("Suicidal Risk:", predictions[0][1])
        
        # Interpretation (replace with your risk thresholds based on model training)
        if predictions[0][0] > 0.8:
          print("BPD Risk: Extreme")
          bpd_risk_factor = "Extreme"
        elif predictions[0][0] > 0.6:
          print("BPD Risk: High")
          bpd_risk_factor = "High"
        elif predictions[0][0] > 0.4:
          print("BPD Risk: Moderate")
          bpd_risk_factor = "Moderate"
        else:
          print("BPD Risk: Low")
          bpd_risk_factor = "Low"

        if predictions[0][1] > 0.8:
          print("Suicidal Risk: Extreme")
          suicidal_risk_factor = "Extreme"
        elif predictions[0][1] > 0.6:
          print("Suicidal Risk: High")
          suicidal_risk_factor = "High"
        elif predictions[0][1] > 0.4:
          print("Suicidal Risk: Moderate")
          suicidal_risk_factor = "Moderate"
        else:
          print("Suicidal Risk: Low")
          suicidal_risk_factor = "Low"

        return render_template(
            "result.html", scd=suicidal_risk_factor, bpd=bpd_risk_factor
        )


@app.route("/learn")
def learn():
    return render_template("learn.html")


@app.route("/working")
def working():
    return render_template("working.html")


# Handling error 404
@app.errorhandler(404)
def not_found_error(error):
    return render_template("error.html", code=404, text="Page Not Found"), 404


# Handling error 500
@app.errorhandler(500)
def internal_error(error):
    return render_template("error.html", code=500, text="Internal Server Error"), 500


if __name__ == "__main__":

    # use 0.0.0.0 for replit hosting
    # app.run(host="0.0.0.0", port=8080)

    # for localhost testing
    app.run(debug=True)
    app.run()
