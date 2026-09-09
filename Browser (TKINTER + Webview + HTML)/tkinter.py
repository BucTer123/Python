import tkinter as tk 
import Browser

root = tk.Tk()

root.title("App")

root.geometry("800x600")

def browse():
    Browser.starter_comm()

def leave_callbck():
    exit(0)

tk.Label(root, text="Welcome!")

tk.Button(root, text="Start", command=browse)

tk.Button(root, text="Leave", command=leave_callbck)

root.mainloop()
