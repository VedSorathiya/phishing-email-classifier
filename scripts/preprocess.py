import pandas as pd
import re
import nltk
from nltk.corpus import stopwords

# stopwords
nltk.download('stopwords')

# convert stopwords to a set for faster lookup
stop_words = set(stopwords.words('english'))

# load ds
df = pd.read_csv("data/phishing_email.csv")
print("....................")

# optimized text cleaning function includes: convert ot lowercase, remove urls and email addresses, and keep only words
def clean_text(text):
    text = str(text).lower()
    text = re.sub(r"http\S+|www\S+", "", text)
    text = re.sub(r"\S*@\S*\s?", "", text)
    text = re.sub(r"[^a-zA-Z\s]", "", text)
    
    words = text.split()  # Tokenize using split() instead of word_tokenize()
    words = [word for word in words if word not in stop_words]  # Remove stopwords
    
    return " ".join(words)

# cleaning function
df["clean_text"] = df["text_combined"].map(clean_text)

# save cleaned dataset
df.to_csv("data/cleaned_data.csv", index=False)

print("Preprocessing completed!")
