import tkinter as tk

def about_callback():
    ws2 = tk.Tk()
    ws2.title("OPEN !")
    ws2.geometry("300x200")

    tk.Label(ws2, text="OPEN HTML FILE!").pack()

    ws2.mainloop()
    ws2.destroy()

def launch_settings():
    ws = tk.Tk()
    ws.title("Settings")
    ws.geometry("900x450")

    tk.Label(ws, text="Welcome to Settings !")
    tk.Button(ws, text="Exit", command=ws.destroy).pack()

    tk.Button(ws, text="About App", command=about_callback).pack()


    ws.mainloop()
    exit(0)