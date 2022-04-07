from flask import Flask, render_template, request, redirect, session, url_for
app = Flask(__name__)
app.secret_key = 'secret'

@app.route('/')
@app.route('/', methods=['POST'])
def visit():
    counter = 0
    if not session.get("count") is None:
        counter = session["count"]
    if request.method == "POST":
        print(request.method)
        if request.form.get("add") == "Add + 2":
            counter += 1
        elif request.form.get("reset") == "Reset":
            counter = 0
        session["count"] = counter
        return redirect(url_for('visit'))
    else:
        counter += 1
    session["count"] = counter
    return render_template('index.html', counter=counter)


@app.route('/destroy_session')
def destroy_session():
    if 'count' in session:
        session.pop("count")
    return redirect('/')
if __name__=="__main__":
    app.run(debug=True)