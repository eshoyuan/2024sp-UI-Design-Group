from flask import Flask, render_template

app = Flask(__name__)

quiz_questions = [
    {
        "questions": "Question-Zero",
        "choices": ["AnswerA", "AnswerB", "AnswerC", "AnswerD"]
    },
    {
        "questions": "Question-One",
        "choices": ["AnswerA", "AnswerB", "AnswerC", "AnswerD"]
    }
]

quiz_answers = ["AnswerA", "AnswerC"]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/origin')
def original():
    return render_template('origin.html')


@app.route('/spread')
def spread():
    return render_template('spread.html')


@app.route('/type')
def type():
    return render_template('type.html')


@app.route('/quiz/<id>')
def quiz(id):
    global quiz_questions
    return render_template('quiz.html', id=id, quiz_questions=quiz_questions)

@app.route('/result')
def result():
    global quiz_answers
    return render_template('result.html',quiz_answers=quiz_answers)

if __name__ == '__main__':
    app.run(debug=True)
