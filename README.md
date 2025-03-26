# Phishing Email Classifier

An ML based detection model that analyses email text using NLP, Sentiment Analysis and TF-IDF to classify emails as phishing or legitimate.
Tech Stack:
- Python (NLTK, Scikit-learn, Pandas)
- Flask (API deployment)
- Github LFS (dataset handling)
- cURL/Postman (API testing)

---

# Model training and evaluation
![image](https://github.com/VedSorathiya/phishing-email-classifier/blob/main/model%20ssr.png)

---

## Installation & Setup
1. clone the repository: 
`git clone https://github.com/VedSorathiya/phishing-email-classifier.git`
`cd phishing-email-classifier`
2. install dependencies: 
`pip install -r requirements.txt`
3. download [dataset](https://www.kaggle.com/datasets/naserabdullahalam/phishing-email-dataset?select=phishing_email.csv)
4. preprocess dataset: 
`python scripts/preprocess.py`
5. train the model: 
`python scripts/train_model.py`
6. test locally (CLI): 
`python main.py`

---

## API Usage (flask deployment)
1. run flask API: 
`python app.py`
2. test API using cURL: 
`curl -X POST "http://127.0.0.1:5000/predict" -H "Content-Type: application/json" -d '{"email_text": "Urgent! Your bank account has been compromised."}'`
3. (alt) using postman:
   - select POST method
   - enter url: https://127.0.0.1:5000/predict
   - go to body -> raw -> JSON
   - Enter: `{
                 "email_text": "Congratulations! You have won $5000. Click here to claim now."
             }`
   - send
4. expected response:
   `{
   "prediction": "Phishing Email"
   }`

---


