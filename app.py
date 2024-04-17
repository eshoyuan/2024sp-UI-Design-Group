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
teas_type1 = [
    {
        "name": "Green Tea",
        "image": "static/Green.png",
        "features": "Light flavor, green color, high antioxidants.",
        "processing": "Quick heating to prevent oxidation.",
        "notables": "Longjing, Sencha."
    },
    {
        "name": "Oolong Tea",
        "image": "static/Oolong.png",
        "features": "Partially oxidized, range of flavors.",
        "processing": "Partial oxidation, shaping.",
        "notables": "Tieguanyin, Da Hong Pao."
    }
]


teas_type2 = [
    {
        "name": "Black Tea",
        "image": "static/black.png",
        "features": "Robust flavor, fully oxidized.",
        "processing": "Full oxidation, drying.",
        "notables": "Assam, Earl Grey."
    },
    {
        "name": "White Tea",
        "image": "static/white.png",
        "features": "Delicate flavor, minimally processed.",
        "processing": "Plucked, naturally dried.",
        "notables": "Silver Needle, White Peony."
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


@app.route('/spread/<int:page>')
def spread(page):
    page_template = f'spread_{page}.html'
    return render_template(page_template) 

@app.route('/type')
def type():
    global teas
    return render_template('type.html', teas=teas_type1)
  
@app.route('/type2')
def type2():
    return render_template('type2.html', teas=teas_type2) 

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
