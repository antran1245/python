from flask import Flask, session, render_template, redirect, request
import random
from datetime import datetime

app = Flask(__name__)
app.secret_key = "ninaja_gold"

@app.route('/')
def main():
    if not 'gold' in session:
        session['gold'] = 0
    if not 'activities' in session:
        session['activities'] = ""
    return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def process():
    randGold = 0
    date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    if request.method == 'POST':
        if request.form["building"] == "farm":
            randGold = random.randint(10,20)
            session['activities'] += "<li class='green'>Earned "+ str(randGold) +" golds from the farm! (" +date+ ")</li>"
        elif request.form["building"] == "cave":
            randGold = random.randint(5,10)
            session['activities'] += "<li class='green'>Earned "+ str(randGold) +" golds from the cave! (" +date+ ")</li>"
        elif request.form["building"] == "house":
            randGold = random.randint(2,5)
            session['activities'] += "<li class='green'>Earned "+ str(randGold) +" golds from the house! (" +date+ ")</li>"
        else:
            randGold = random.randint(0,50)
            take = random.randint(0,1)
            if take == 0:
                randGold = -randGold
                session['activities'] += "<li class='red'>Entered a casino and lost "+ str(randGold) +" golds! (" +date+ ")</li>"
            else:
                session['activities'] += "<li class='green'>Entered a casino and won "+ str(randGold) +" golds! (" +date+ ")</li>"
    session['gold'] += randGold
    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

if __name__=='__main__':
    app.run(debug=True)