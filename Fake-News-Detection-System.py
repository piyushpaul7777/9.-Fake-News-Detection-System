import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
import pickle

# Load dataset
data = pd.read_csv('fake_or_real_news.csv')
X = data['text']
y = data['label']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a pipeline with a TfidfVectorizer and a LogisticRegression classifier
model = make_pipeline(TfidfVectorizer(), LogisticRegression())
model.fit(X_train, y_train)

# Save the model to a file
with open('fake_news_model.pkl', 'wb') as f:
    pickle.dump(model, f)

print(f"Model accuracy: {model.score(X_test, y_test)}")
