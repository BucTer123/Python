import tkinter as tk

def main_ui():
    def ui_name(window_name):
        def ui_size(window_size):
            root = tk.Tk()

            root.title(window_name)
            root.geometry(window_size)

            tk.Label(root, text="Welcome!")
            tk.Label(root, text=window_name).pack()
            tk.Button(root, text="Close", command=root.destroy).pack()
            tk.Label(root, text=window_size).pack()

            root.mainloop()

def start_ui(window_started):
    if window_started:
        main_ui()
    else:
        exit(0)