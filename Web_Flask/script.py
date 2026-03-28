from flask import Flask, render_template

serv = Flask(__name__)

@serv.route("/main")
def main():
    return render_template("main.html")

def zz():
    serv.run(debug=True)
