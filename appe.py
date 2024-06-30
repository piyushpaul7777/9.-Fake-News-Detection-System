from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

# Load the trained model
with open('fake_news_model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        text = request.form['text']
        prediction = model.predict([text])[0]
        return render_template('index.html', prediction=prediction)
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
