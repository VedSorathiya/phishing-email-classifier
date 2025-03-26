from flask import Flask, request, jsonify
import pickle
import re
from nltk.corpus import stopwords

app = Flask(__name__)

# load model & vectorizer
with open("models/phishing_model.pkl", "rb") as f:
    model = pickle.load(f)
with open("models/vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

# stopwords optimization
stop_words = set(stopwords.words('english'))

# text preprocessing function
def clean_text(text):
    text = str(text).lower()
    text = re.sub(r"http\S+|www\S+", "", text)
    text = re.sub(r"\S*@\S*\s?", "", text)
    text = re.sub(r"[^a-zA-Z\s]", "", text)
    words = text.split()
    words = [word for word in words if word not in stop_words]
    return " ".join(words)

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    email_text = data.get("email_text", "")
    cleaned_text = clean_text(email_text)
    vectorized_text = vectorizer.transform([cleaned_text])
    prediction = model.predict(vectorized_text)[0]
    result = "Phishing Email" if prediction == 1 else "Legitimate Email"
    return jsonify({"prediction": result})

if __name__ == "__main__":
    app.run(debug=True)
