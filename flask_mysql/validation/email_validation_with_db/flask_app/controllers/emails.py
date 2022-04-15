from flask_app import app
from flask import render_template, redirect, request, url_for, session

from flask_app.models.email import Email

# Display Route
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/success')
def success():
    emails = Email.get_all()
    return render_template('success.html', emails=emails)

# Action Route
@app.route('/process', methods=["POST"])
def process():
    if not Email.validation_email(request.form):
            return redirect('/')
    data = {
        "address": request.form['email']
    }
    Email.insert(data)
    return redirect('/success')

@app.route('/delete/<int:id>')
def delete(id):
    data={"id":id}
    Email.delete(data)
    return redirect('/success')