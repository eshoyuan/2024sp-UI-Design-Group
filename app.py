from flask import Flask, render_template

app = Flask(__name__)

quiz_questions = [
    {
        "questions": 'Who is the author of "The Classic of Tea" (茶经) ?',
        "choices": ["Lu Yu", "Hua Tuo", "Shen Nong", "Li Shizhen"],
        "imageURL": "/static/book.png"
    },
    {
        "questions": "In 1800s, which company began cultivating tea in India?",
        "choices": ["British East India", "British West India", "Ito En", "Lipton"],
        "imageURL": "/static/india.png"
    },
        {
        "questions": "What is the primary difference in the processing of Green Tea and Black Tea?",
        "choices": ["Green Tea is fully oxidized, while Black Tea is not oxidized at all.", "Black Tea is partially oxidized, while Green Tea undergoes a full oxidation process.", "Green Tea is quickly heated to prevent oxidation, while Black Tea undergoes a full oxidation process.", "There is no difference; both are processed in the same way."],
        "imageURL": "/static/process.png"
    },
            {
        "questions": "Which tea is characterized by a range of flavors due to its partial oxidation during processing?",
        "choices": ["Black Tea", "White Tea", "Oolong Tea", "Green Tea"],
        "imageURL": "/static/tea1.png"
    },
                {
        "questions": "Which type of tea is known for its delicate flavor and minimal processing?",
        "choices": ["Black Tea", "White Tea", "Oolong Tea", "Green Tea"],
        "imageURL": "/static/tea2.png"

    },
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

quiz_answers = ["Lu Yu", "British East India",  "Green Tea is quickly heated to prevent oxidation, while Black Tea undergoes a full oxidation process.", "Oolong Tea", "White Tea"]


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
