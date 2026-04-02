import tkinter as tk
import script_flask_python

root = tk.Tk()

root.geometry("1920x1080")

root.title("App")

def strt():
    script_flask_python.aa()

tk.Label(root, text="Press button :")

tk.Button(root, text="Start Flask", command=strt)