from flask import Flask, render_template, request, session, redirect
app = Flask(__name__)
app.secret_key = "survey_dojo"

@app.route('/')
def form():
    session.clear()
    return render_template('form.html')

@app.route('/process', methods=["POST"])
def process():
    name = "2px red solid"
    location = "2px red solid"
    language = "2px red solid"
    if request.form["name"] != "":
        session["name"] = request.form["name"]
        name = "none"
    if request.form["location"] != "default":
        session["location"] = request.form["location"]
        location = "none"
    if request.form["language"] != "default":
        session["language"] = request.form["language"]
        language = "none"
    if request.form["comment"] != "":
        session["comment"] = request.form["comment"]
    if "radioColor" in request.form:
        session["color"] = request.form['radioColor']
    if "checkFood" in request.form:
        session["food"] = request.form['checkFood']
    if name=="none" and location=="none" and language=="none":
        return redirect('/result')
    else:
        return render_template('form.html', name=name, location=location, language=language )

@app.route('/result')
def result():
    return render_template('result.html')


if __name__=="__main__":
    app.run(debug=True)