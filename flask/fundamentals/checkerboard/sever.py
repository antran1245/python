from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
@app.route('/<int:x>')
@app.route('/<int:x>/<int:y>')
@app.route('/<int:x>/<int:y>/<string:color>/<string:color1>')
def create_checkerboard(x = 8, y = 8, color="black", color1="red"):
    x = int(x/2)
    y = int(y/2)
    return render_template('index.html', row=y, col=x, color=color, color1=color1)

if __name__=="__main__":
    app.run(debug=True)