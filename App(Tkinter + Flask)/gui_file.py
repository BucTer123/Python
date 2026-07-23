import tkinter as tk
import os
from flask import Flask, render_template

def launch_app():
    w1 = tk.Tk()
    w1.title("Main")
    w1.geometry("600x400")

    e1_text = tk.Label(w1, text="Write route to create for site :")
    e1_text.pack()
    e1 = tk.Entry(w1)

    if e1.get() == "":
        print("ERROR!")
        w1.destroy()
    else:
        os.mkdir("templates")
        file = open("templates/index.html", "w")
        file.write("<!DOCTYPE html>")
        file.write("<html>")
        file.write("<head>")
        file.write("    <meta charset='utf-8'>")
        file.write("    <title>Page title</title>")
        file.write("</head>")
        file.write("<body>")
        file.write("<h1>Example page: you can modernize all files </h1>")
        file.write("</body>")

        file2 = open("templates/style.css", "w")
        file2.write("* {")
        file2.write("   background: whitesmoke;")
        file2.write("   color: black;")
        file2.write("   font-family: sans-serif;")
        file2.write("}")

        file3 = open("templates/script.js", "w")
        file3.write("console.log('Welcome!');")

        app = Flask(__name__)
        @app.route(e1.get())
        def open_html():
            return render_template("index.html")

        print("Site is opened on 8000 localhost!")

        app.run(debug=True, port=8000)

        exit(0)
