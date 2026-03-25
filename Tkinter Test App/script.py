import tkinter as tk
import os

root = tk.Tk()

root.title("App")

root.geometry("800x600")

def create_call():
    input_create_text = tk.Label(root, text="Write name to create dir :")
    input_create = tk.Entry(root)

    input_create.pack()
    input_create_text.pack()

    mk = input_create.get()
    os.mkdir(mk)

def remove_call():
    input_remove_text = tk.Label(root, text="Write name to remove dir :")
    input_remove = tk.Entry(root)

    input_remove.pack()
    input_remove_text.pack()

    rm = input_remove.get()
    os.rmdir(rm)

def lnx_call():
    os.system("Konsole")
    os.system("terminal")
    os.system("cmd")

def win_call():
    os.system("cmd")

tk.Label(root, text="Welcome!")

tk.Label(root, text="Choice button! :")

tk.Button(root, text="Create Dir", command=create_call)

tk.Button(root, text="Remove Dir", command=remove_call)

tk.Button(root, text="Open Terminal Linux", command=lnx_call)

tk.Button(root, text="Open Terminal Windows", command=win_call)