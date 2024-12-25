from flask import Flask, redirect, render_template
from flask_session import Session

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/game')
def game():
    return render_template('match.html')