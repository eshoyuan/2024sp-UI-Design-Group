from flask import Flask, render_template

app = Flask(__name__)

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
@app.route('/type2')
def type2():
    return render_template('type2.html') 

@app.route('/quiz')
def quiz():
    return render_template('quiz.html')  

if __name__ == '__main__':
    app.run(debug=True)

