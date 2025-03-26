import pickle
import re
from nltk.corpus import stopwords

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

# prediction function
def predict_email(email_text):
    email_text_cleaned = clean_text(email_text)
    email_vectorized = vectorizer.transform([email_text_cleaned])
    prediction = model.predict(email_vectorized)[0]
    return "🔴 Phishing Email" if prediction == 1 else "🟢 Legitimate Email"

# eg
email_text = "Your account has been suspended! Click here to verify."
print(predict_email(email_text))
