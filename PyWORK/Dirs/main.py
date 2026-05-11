import requests as rq
import tkinter as tk 
import math
import time 

def time_now():
    now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print("Time now :" + now)
    
def math():
    a = float(input("Write first number :"))
    b = float(input("Write second number :"))
    c = input("> ");
    
    if c == "hlp_math":
        print("1 => hlp_math\n")
        print("2 => +(plus) \n")
        print("3 => -(minus) \n")
        print("4 => *(multiply/multi)\n")
        print("5 => /(divide)\n")
        print("6 => **(power/pow)\n")
    elif c == "+" or c == "plus":
        plus = a + b
        print("A + B =" + plus)
    elif c == "-" or c == "minus":
        minus = a - b 
        print("A - B =" + minus)
    elif c == "*" or c == "multiply" or c == "multi":
        multi = a * b
        print("A * B =" + multi)
    elif c == "/" or c == "divide":
        if (a == 0 or b == 0):
            print("ERROR!: Divide by zero!")
        else:
            divide = a / b 
            print("A / B =" + divide)
    elif c == "**" or c == "power" or c == "pow":
        powa = a * a 
        powb = b * b 
        
        print("Power(a) =" + powa + "\n")
        print("Power(b) =" + powb + "\n")

def function_click_button():
    win2 = tk.Tk()
    
    win2.geometry("300x200")
    win2.title("New Window")
    
    tk.Label(win2, text="Created New Window!")
    
    win2.mainloop()
    
def ui():
    root = tk.Tk()
    
    tk.geometry("800x600")
    tk.title("UI")
    
    tk.Label(root, text="Welcome!")
    tk.Button(root, text="click", command=function_click_button)
    
def ui_label():
    label_win = tk.Tk()
    
    tk.geometry("800x600")
    tk.title("Label")
    
    tk.Label(label_win, text="Text :")
    
    label_win.mainloop()

def ui_button():
    button_win = tk.Tk()
    
    tk.geometry("400x200")
    tk.title("Button")
    
    tk.Button(button_win, text="click")
   
    button_win.mainloop()