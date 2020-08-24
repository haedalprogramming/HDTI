import loadquestion
from flask import render_template,  Flask

app = Flask(__name__)

@app.route('/')
def index():

    return render_template('index.html', questions=loadquestion.questions, tracks=loadquestion.tracks)

@app.route('/result', methods=["POST"])
def result():
    loadquestion.types
    return render_template('result.html', img=img, type=type, explanation=explanation, track1=track1, track2=track2)

if __name__ == '__main__':
    app.run(debug=1)