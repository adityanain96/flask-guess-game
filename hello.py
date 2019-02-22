from flask import Flask, flash, redirect, render_template, request, session, abort
import random
app = Flask(__name__)
app.secret_key = 'You Will Never Guess'

@app.route("/")
def main():
    x = random.randint(1,1001)      
    session['x'] = x
    return render_template('index.html')    

    

@app.route('/',methods=['POST'])
def guess():
    if 'guess' in session:
        session['guess'] = session.get('guess') + 1
    else:
        session['guess'] = 1
    tries = session.get('guess') 
       
    x = session.get('x')         
    num = int(request.form['number'])       
    return render_template('guess.html',**locals())
    
    
if __name__ == "__main__":
    app.run()