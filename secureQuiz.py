import os
from flask import Flask, url_for, render_template, request, session

app = Flask(__name__)

app.secret_key=os.environ["SECRET_KEY"];

questions = {
 1 : "Who was the first president of the United States",
 2 : "How many stripes are on the United States Flag",
 3 : "What was the last state to be added to the United States"
}

answers = ["George Washington", "13", "Alaska"]

questionOn = 0

def processQuiz(answer):
    questionOn+= 1
    if questionOn == 1:
        return questions[questionOn]
    elif 1 < questionOn < 4:
        session["Answer"+questionOn] = answer
    else:
        points = checkAnswers()
    return

def checkAnswers():
    points = 0

    for x in range(1,4):
        if session["Answer"+x]==answers[x-1]:
            points+=1
    return points

@app.route("/")
def render_main():
    session.clear()
    return render_template("home.html")

@app.route("/quiz")
def render_quiz():
    answer = request.form["Question"]
    q = processQuiz(answer)
    return render_template("quiz.html", Question = q)

if __name__=="__main__":
    app.run(debug=True)
