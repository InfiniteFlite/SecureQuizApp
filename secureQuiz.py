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

def processQuiz(answer):
    questionOn+= 1
    if questionOn == 1:
        return questions[questionOn]
    elif 1 < questionOn < 4:
        session["Answer"+str(questionOn)] = answer
    else:
        checkAnswers()
    return questions[questionOn]

def checkAnswers():
    points = 0

    for x in range(1,4):
        if session["Answer"+str(x)]==answers[x-1]:
            points+=1
    return

@app.route("/")
def render_main():
    session.clear()
    session["questionOn"] = 0
    session["points"] = 0
    return render_template("home.html")

@app.route("/quiz")
def render_quiz():
    if session["questionOn"] > 0:
        answer = request.args["Question"]
        processQuiz(answer)
        q = session["questionOn"]
    else:
        q = 1
        session["questionOn"] = 1
    return render_template("quiz.html", Question = questions[q])

if __name__=="__main__":
    app.run(debug=True)
