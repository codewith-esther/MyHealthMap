from flask import Blueprint, render_template, request
import joblib
import os

heart_bp = Blueprint("heart", __name__, url_prefix="/heart")


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "models", "heart_model.pkl")

heart_model = joblib.load(MODEL_PATH)

# Load model
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
model_path = os.path.join(BASE_DIR, "..", "models", "heart_model.pkl")
model = joblib.load(model_path)

@heart_bp.route("/", methods=["GET", "POST"])
def heart():
    prediction = None
    error = None

    if request.method == "POST":
        try:
            age = float(request.form["age"])
            gender = float(request.form["gender"])
            impulse = float(request.form["impulse"])
            glucose = float(request.form["glucose"])
            kcm = float(request.form["kcm"])
            troponin = float(request.form["troponin"])
            pulse_pressure = float(request.form["pulse_pressure"])

            # Predict using your model
            features = [[age, gender, impulse, glucose, kcm, troponin, pulse_pressure]]
            result = model.predict(features)[0]

            prediction = "High Risk" if result == 1 else "Low Risk"

        except ValueError:
            error = "Please enter valid numeric values."
        except Exception as e:
            error = f"Error: {e}"

    return render_template("heart.html", prediction=prediction, error=error)
