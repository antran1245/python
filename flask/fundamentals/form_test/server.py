from flask import Flask, render_template, request, redirect # added request
app = Flask(__name__)
            
@app.route('/users', methods=['POST'])
def create_user():
    print("Got Post Info")
    print(request.form)
    # Never render a template on a POST request.
    # Instead we will redirect to our index route.
    return redirect('/')

# our index route will handle rendering our form
@app.route('/')
def index():
    return render_template("index.html")
if __name__ == "__main__":
    app.run(debug=True)
