import pickle
import re
from nltk.corpus import stopwords

# load model & vectorizer
with open("models/phishing_model.pkl", "rb") as f:
    model = pickle.load(f)
with open("models/vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

# load stopwords once
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

# testing
if __name__ == "__main__":
    print("\n**Phishing Email Detector**")
    while True:
        email_text = input("\nEnter email text (or type 'exit' to quit): ")
        if email_text.lower() == "exit":
            print("cheers")
            break
        
        cleaned_text = clean_text(email_text)
        email_vectorized = vectorizer.transform([cleaned_text])
        prediction = model.predict(email_vectorized)[0]
        
        result = "🔴 Phishing email" if prediction == 1 else "🟢 Legitimate email"
        print(f"\nPrediction: {result}")
