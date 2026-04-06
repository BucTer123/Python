import tkinter as tk 
import Browser

root = tk.Tk()

root.title("App")

root.geometry("800x600")

def browse():
    Browser.starter_comm()

def leave_callbck():
    tk.Label(root, text="SHUTDOWN")
    root.destroy()
    exit(0)

tk.Label(root, text="Welcome!")

tk.Button(root, text="Leave", command=leave_callbck)

tk.Button(root, text="Browser", command=browse)

root.mainloop()