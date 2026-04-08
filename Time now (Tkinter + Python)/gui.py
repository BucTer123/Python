import tkinter as tk 
import time 

w1 = tk.Tk()

w1.title("Time now")

w1.geometry("300x200")

def leave_callback():
    w1.destroy()
    exit(0)

def gui():

    now2 = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    time_now_text = tk.Label(w1, text=now2)
    time_now_text.pack()

    btn1 = tk.Button(w1, text="Leave", command=leave_callback)
    btn1.pack()

w1.mainloop()