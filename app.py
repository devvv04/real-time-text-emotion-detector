from flask import Flask, request, render_template
import joblib

app = Flask(__name__)

# Load model and vectorizer
model = joblib.load("emotion_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    user_input = ""

    if request.method == "POST":
        user_input = request.form["text"]
        input_vec = vectorizer.transform([user_input])
        prediction = model.predict(input_vec)[0]

    return render_template("index.html", prediction=prediction, user_input=user_input)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

