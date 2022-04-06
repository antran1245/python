from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html', show=False)

@app.route('/play')
@app.route('/play/<int:num>')
@app.route('/play/<int:num>/<string:color>')
def play(num = 3, color = "lightblue"):
    return render_template('index.html', show=True, times=num, color=color)

@app.errorhandler(404)
def page_not_found(e):
    return "Page not found. <br/> Try '/play', '/play/(x)', '/play/(x)/(color)'"

if __name__=="__main__":
    app.run(debug=True)