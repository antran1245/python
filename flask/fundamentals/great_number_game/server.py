from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = "randomSercet"

@app.route('/')
def main():
    randNum = random.randint(1,100)
    noShow = "none"
    show = "block"
    if not "randomNum" in session:
        session["randomNum"] = randNum
    if 'guess' in session:
        if session['tries'] > 5:
            return render_template('index.html', low=noShow, high=noShow, result="flex", correct=noShow, color="red", lose=show)
        if session['guess'] == "correct":
            return render_template('index.html', low=noShow, high=noShow, result="flex", correct=show, color="green", lose=noShow)
        if session['guess'] == 'high':
            return render_template('index.html', low=noShow, high=show, result="flex", correct=noShow, color="red", lose=noShow)
        if session['guess'] == 'low':
            return render_template('index.html', low=show, high=noShow, result="flex", correct=noShow, color="red", lose=noShow)
    return render_template('index.html', low=noShow, high=noShow, result=noShow, correct=noShow, color="red", lose=noShow)

@app.route('/guess', methods=["POST"])
def guess():
    if request.method == 'POST':
        req = request.form
        if req['num'] != "":
            if int(req['num']) == session["randomNum"]:
                session['guess'] = "correct"
            if int(req['num']) > session["randomNum"]:
                session['guess'] = "high"
            if int(req['num']) < session["randomNum"]:
                session['guess'] = "low"
            if not "tries" in session:
                session['tries'] = 0
            session['tries'] += 1
    return redirect('/')

@app.route('/reset', methods=["POST"])
@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

@app.route('/scoreboard', methods=["POST"])
def scoreboard():
    score = [
        {"name": "Tony", "tries": 1},
        {"name": "Apple", "tries": 2},
        {"name": "Zac", "tries": 4},
        ]
    if request.form["name"] != "":
        for i in range(len(score)):
            if score[i]["tries"] > int(session['tries']):
                score.insert(i-1, {"name": request.form["name"], "tries": int(session['tries'])})
                break
        return render_template('scoreboard.html', scoreboard=score)
    return redirect('/')
if __name__=="__main__":
    app.run(debug=True)