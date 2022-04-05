from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!!'

@app.route('/dojo')
def dojo():
    return 'Dojo!'

@app.route('/say/<string:name>')
def sayHi(name):
    return f"Hi {name}!"

@app.route('/repeat/<int:num>/<string:text>')
def repeat(num, text):
    return f"{text} <br/>" * num

@app.errorhandler(404)
def page_not_found(e):
    return "Sorry! No response. Try again."

if __name__=="__main__":
    app.run(debug=True)