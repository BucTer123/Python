from flask import Flask, render_template

serv = Flask(__name__)

@serv.route("/main")
def open_html1():
    return render_template("main.html")

@serv.route("/")
def open_html2():
    return render_template("main.html")

@serv.route("//")
def open_html4();
    return render_template("main.html")

@serv.route("/qwerty")
def open_html5();
    return render_template("main.html")

@serv,route("/asd")
def open_html6():
    return render_template("main.html")

def zz():
    serv.run(debug=True)
