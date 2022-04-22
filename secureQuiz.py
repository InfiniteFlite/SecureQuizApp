import os
from flask import Flask, url_for, render_template, request, session, redirect

app = Flask(__name__)

app.secret_key=os.environ["SECRET_KEY"];

questions = {
 1 : "Who was the first president of the United States",
 2 : "How many stripes are on the United States Flag",
 3 : "What was the last state to be added to the United States",
 4 : ""
}

answers = ["George Washington", "13", "Alaska"]

def processQuiz(answer):
    print("a")
    if 1 <= session["questionOn"] and session["questionOn"] < 4:
        print("b")
        session["Answer"+str(session["questionOn"])] = answer
        session["questionOn"]+= 1
    else:
        checkAnswers()
        print(url_for("render_results"))
        return redirect(url_for("render_results"))
    return

def checkAnswers():
    session["points"] = 0

    for x in range(1,4):
        if session["Answer"+str(x)]==answers[x-1]:
            session["points"]+=1
    print(session["points"])
    return

@app.route("/")
def render_main():
    session.clear()
    session["questionOn"] = 0
    session["points"] = 0
    return render_template("home.html")

@app.route("/quiz", methods = ['GET', 'POST'])
def render_quiz():
    print(session["questionOn"])
    if session["questionOn"] > 0:
        answer = request.args["Question"]
        processQuiz(answer)
        q = session["questionOn"]
    else:
        q = 1
        session["questionOn"] = 1
    return render_template("quiz.html", Question = questions[q])

@app.route("/results", methods = ['POST'])
def render_results():
    print("REnder REsults")
    return render_template("results.html", Points = session["points"])

if __name__=="__main__":
    app.run(debug=True)
