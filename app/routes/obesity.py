from flask import Blueprint, render_template, request
import joblib
import os
import pickle
obesity_bp = Blueprint("obesity", __name__, url_prefix="/obesity")
import os
import joblib

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "models", "obesity_model.pkl")

obesity_model = joblib.load(MODEL_PATH)


# Load model
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
model_path = os.path.join(BASE_DIR, "..", "models", "obesity_model.pkl")
model = joblib.load(model_path)

@obesity_bp.route("/", methods=["GET", "POST"])
def obesity():
    prediction = None
    error = None
    bmi = None

    if request.method == "POST":
        try:
            height = float(request.form["height"])
            weight = float(request.form["weight"])
            age = float(request.form["age"])
            gender = float(request.form["gender"])

            bmi = round(weight / ((height / 100) ** 2), 2)

            result = model.predict([[height, weight, age, gender, bmi]])[0]

            if result == 0:
                prediction = "Normal Weight"
            elif result == 1:
                prediction = "Overweight"
            else:
                prediction = "Obese"

        except ValueError:
            error = "Please enter valid numeric values."
        except Exception as e:
            error = f"Error: {e}"

    return render_template("obesity.html", prediction=prediction, error=error, bmi=bmi)
