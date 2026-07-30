import requests as rq
import tkinter as tk 
import math
import time 
from colorama import Fore
import os

class pywork_cmd:    
    def time_now():
        now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        print("Time now :" + now)
    
    def math(a, b, c) -> float:
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
    def output(text_output):
        print(text_output)
    def echoln(text_echoln):
        print(text_echoln):
    def printf(text_printf):
        print(text_printf)
    def echo(text_echo):
        print(text_echo)
    def out(text_out):
        print(text_out)
    def sprints(text_sprints):
        print(sprints)

class pywork_os:
    def ext(status) -> int:
        exit(status)
    def ret(boolean) -> bool:
        return boolean
    def mkd(name_dir_create):
        os.mkdir(name_dir_create)
    def rmd(name_dir_remove):
        os.rmdir(name_dir_remove):
    def opn(name_dir_open, variable):
        variable = open(name_dir_open)
        
class pywork_gui:
    def new_button(text_button, function_buttoncallback):
        tk.Button(root, text_button, command=function_buttoncallback)
    def new_label(text_label):
        tk.Label(root, text_label)
    def new_window(screen_widthheight, name_window):
        root = tk.Tk()
        root.title(name_window)
        root.geometry(screen_widthheight)
        root.mainloop()
    def destroy_window():
        root.destroy()
    def placeholder(text_placeholder):
        tk.Input(root, text_placeholder)
