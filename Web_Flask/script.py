from flask import Flask, render_template

serv = Flask(__name__)

@serv.route("/main")
def main():
    return render_template("main.html")

if __name__ == "__main__":
    serv.run(debug=True)