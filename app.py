import os
import json
from flask import Flask, render_template, request, redirect, url_for 
score = 0
score2 = 0
username = ""
 
app = Flask(__name__)

class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer
        
questions = [
    Question([0], "Python"),
    Question([1], "Paris"),
    Question([2], "Moonlight"),
    Question([3], "Lemonade"),
    Question([4], "Yes"),
    Question([5], "Call Me By Your Name"),
    Question([6], "Engels & Marx"),
    Question([7], "Freud"),
    Question([8], "Gordon Ramsay")
            
]



@app.route('/')
def quiz():
    return render_template('user.html')
    
@app.route('/start',methods=["POST"])
def getUser():
    name = request.form["username"]
    global username
    if username == name:
        return render_template('index.html')
    
@app.route('/quiz', methods=['POST'])    
def quiz_answers():
    for Question in questions:
        answer = request.form['language']
        global score
        if answer == Question.answer:
            score = score+1
            return render_template('capitals.html',data=score) 
    return render_template("index.html") + answer + "<h4>is not correct, guess again.</h4>"
    
@app.route('/question', methods=['POST'])
def question_two():
    for Question in questions:
        answer = request.form['capital']
        global score
        if answer == Question.answer:
            score = score+1
            return render_template('movies.html',data=score)
    return render_template('capitals.html', data=score) + answer + "<h4>is not correct, guess again.</h4>"
     
@app.route('/movie', methods=['POST'])
def question_three():
    for Question in questions:
        answer = request.form['movie']
        if answer == Question.answer:
            global score
            score += 1
            return render_template('music.html',data=score)
    return render_template("movies.html", data=score) + answer + "<h4>is not correct. Wanna guess again</h4>"
          
    
@app.route('/music', methods=['POST'])
def question_four():
    for Question in questions:
        answer = request.form['album']
        if answer == Question.answer:
            global score
            score += 1
            return render_template('results.html',data=score)
    return render_template("music.html", data=score) + answer + "<h4>is not correct, guess again.</h4>"
    
@app.route('/ready', methods=['POST'])
def results1():
    for Question in questions:
        answer = request.form['ready']
        if answer == Question.answer:
            return render_template('novel.html')
    return render_template('novel.html') 
    
@app.route('/novel', methods=['POST'])
def question5():
    for Question in questions:
        answer = request.form['novel']
        if answer == Question.answer:
            global score2
            score2 += 1
            return render_template('history.html',data2=score2)
    return render_template('novel.html',data2=score2) + answer + "<h4>is not correct, guess again.</h4>"
            
@app.route('/history', methods=['POST'])
def question6():
    for Question in questions:
        answer = request.form['history']
        if answer == Question.answer:
            global score2
            score2 += 1
            return render_template('psychology.html',data2=score2)
    return render_template('history.html',data2=score2) + answer + "<h4>is not correct, guess again.</h4>"
    
@app.route('/psychology', methods=['POST'])
def question7():
    for Question in questions:
        answer = request.form['psychology']
        if answer == Question.answer:
            global score2
            score2 += 1
            return render_template('cuisine.html',data2=score2)
    return render_template('psychology.html',data2=score2) + answer + "<h4>is not correct, guess again.</h4>"
                        
@app.route('/cuisine', methods=['POST'])
def question8():
    for Question in questions:
        global score
        answer = request.form['cuisine']
        if answer == Question.answer:
            global score2
            score2 += 1
            return render_template('results2.html',data2=score2, data=score)
    return render_template('cuisine.html',data2=score2) + answer + "<h4>is not correct, guess again.</h4>"
        
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True)
    