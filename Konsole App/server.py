import time
from art import text2art
from colorama import Fore
from flask import Flask, render_template

app = Flask(__name__)

now3 = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
print(Fore.CYAN + "Time now :" + now3)

print(Fore.LIGHTGREEN_EX + text2art("W E B S E R V E R !"))

@app.route("/login")
def login():
    return render_template("login.html")

def ll():
    app.run(debug=True)