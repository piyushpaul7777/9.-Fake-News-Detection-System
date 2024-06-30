# 9.-Fake-News-Detection-System
# Fake News Detection System

A simple Python application to detect fake news using a machine learning model, with a Flask web interface.

## Features

- Detects whether a given news article is fake or real.
- Simple web-based interface for user input.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/fake-news-detection-app.git
Navigate to the project directory:
bash
cd fake-news-detection-app
Create a virtual environment:
bash
python -m venv venv
Activate the virtual environment:
On Windows:
bash
.\venv\Scripts\activate
On macOS and Linux:
bash
source venv/bin/activate
Install the required dependencies:
bash
pip install -r requirements.txt
Download the dataset from Kaggle and place it in the project directory.

Train the model:

bash
python fake_news_detector.py
Usage
Run the Flask application:
bash
python app.py
Open your web browser and go to http://127.0.0.1:5000/.

Enter the news text you want to check and submit.

The prediction result will be displayed on the page.

Requirements
Python 3.6+
pandas
scikit-learn
flask
