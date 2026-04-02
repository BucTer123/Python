from flask import Flask, render_template
from art import text2art

print(text2art("S T A R T I N G !"))

app = Flask(__name__)

@app.route("/login")
def login_main():
    render_template("Login.html")

@app.route("/continue")
def continue_main():
    render_template("main.html")

def aa():
    app.run(debug=True)
