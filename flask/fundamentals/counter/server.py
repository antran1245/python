from flask import Flask, render_template, request, redirect, session, url_for
app = Flask(__name__)
app.secret_key = 'secret'

@app.route('/')
@app.route('/', methods=['POST'])
def visit():
    counter = 0
    visited = 0
    if not session.get("count") is None:
        counter = session["count"]
    if not session.get("visited") is None:
        visited = session["visited"]
    if request.method == "POST":
        print(request.method)
        if request.form.get("add") == "Add":
            num = request.form.get("num")
            if(num != ""):
                counter += (int(num)-1)
        elif request.form.get("add") == "Add + 2":
            counter += 1
        elif request.form.get("reset") == "Reset":
            counter = 0
        session["count"] = counter
        visited -= 1
        session["visited"] = visited
        return redirect(url_for('visit'))
    else:
        counter += 1
        visited += 1
    session["count"] = counter
    session["visited"] = visited
    return render_template('index.html', counter=counter, visited=visited)


@app.route('/destroy_session')
def destroy_session():
    if 'count' in session:
        session.pop("count")
    return redirect('/')
if __name__=="__main__":
    app.run(debug=True)