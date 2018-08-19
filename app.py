import os
from flask import Flask, render_template, request, redirect, url_for 
score = 0
 
app = Flask(__name__)
        
class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer
        
questions = [
    Question([0], "Python"),
    Question([1], "Paris"),
    Question([2], "Moonlight"),
    Question([3], "Lemonade")
            
]

@app.route('/')
def quiz():    
    return render_template('index.html')
    
@app.route('/quiz', methods=['POST'])    
def quiz_answers():
    for Question in questions:
        answer = request.form['language']
        global score
        if answer == Question.answer:
            score = score+1
            return render_template('capitals.html',data=score)
    return render_template('capitals.html',data=score)
    
@app.route('/question', methods=['POST'])
def question_two():
    for Question in questions:
        answer = request.form['capital']
        global score
        if answer == Question.answer:
            score = score+1
            return render_template('movies.html',data=score)
    return render_template('movies.html',data=score)
            
@app.route('/movie', methods=['POST'])
def question_three():
    for Question in questions:
        answer = request.form['movie']
        if answer == Question.answer:
            global score
            score += 1
            return render_template('music.html',data=score)
    return render_template('music.html',data=score)       
    
@app.route('/music', methods=['POST'])
def question_four():
    for Question in questions:
        answer = request.form['album']
        if answer == Question.answer:
            global score
            score += 1
            return render_template('results.html',data=score)
    return render_template('results.html',data=score)           
            
            
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True)
    