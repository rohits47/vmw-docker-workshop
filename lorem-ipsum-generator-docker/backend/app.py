from flask import Flask
from flask import render_template
import parse_json
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/gen")
def generate():
    paragraphs = 1
    sentences = 1
    words = 5
    tags = True
    return parse_json.text_generator(paragraphs, sentences, words, tags)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
