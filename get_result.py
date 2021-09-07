from flask import Flask, render_template, request, redirect, url_for
from joblib import load
from pyvi import ViTokenizer, ViPosTagger


pipeline = load("model/text_classification.joblib")

vectorizer = load("model/vectorizer.pkl")

def transform_text(text):
    string = ViTokenizer.tokenize(text.lower().replace('\n', ' '))
    string_word_emb = vectorizer.transform([string])
    return string_word_emb

def requestResults(text):
    embedded = transform_text(str(text))
    returning_str = pipeline.predict(embedded)
    return str(returning_str)

app=Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/', methods=['POST', 'GET'])
def get_data():
    if request.method == 'POST':
        user = request.form['search']
        return redirect(url_for('success', name=user))


@app.route('/success/<name>')
def success(name):
    return "<xmp>" + str(requestResults(name)) + " </xmp> "


if __name__ == '__main__' :
    app.run(debug=True)
