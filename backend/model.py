from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

texts = [
    "heart attack chest pain",
    "not breathing unconscious",
    "car accident bleeding",
    "burn fire injury",
    "fracture broken bone",
    "snake bite poison"
]

labels = [
    "heart_attack",
    "cpr",
    "bleeding",
    "burn",
    "fracture",
    "poison"
]

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)

model = MultinomialNB()
model.fit(X, labels)

# ✅ THIS FUNCTION MUST EXIST
def predict_emergency(text):
    X_test = vectorizer.transform([text])
    return model.predict(X_test)[0]