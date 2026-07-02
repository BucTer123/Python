import tkinter as tk
from gui_file import *
from second_gui_file import *

def settings_window():
    launch_settings()

def start_app():
    launch_app()

def main():
    root = tk.Tk()
    root.title("Menu")
    root.geometry("600x300")

    tk.Label(root, text="Welcome!")
    tk.Button(root, text="Start", command=start_app)
    tk.Button(root, text="Settings", command=settings_window)
    tk.Button(root, text="Exit", command=root.destroy)

    root.mainloop()

if __name__ == "__main__":
    main()