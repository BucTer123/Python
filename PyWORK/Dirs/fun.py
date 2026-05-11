from art import text2art
from colorama import Fore
import os

def artz():
   cmd_artz = input("Write text :")
   cmd_artz_color = input("Write color :")
   
   if cmd_artz_color == "what?":
        print("1 => RED \n")
        print("2 => BLUE \n")
        print("3 => CYAN \n")
        print("4 => WHITE\n")
        print("5 => GREEN\n")
        print("6 => YELLOW\n")
    elif cmd_artz_color == "RED":
        print(Fore.RED + text_input)
    elif cmd_artz_color == "BLUE":
        print(Fore.BLUE + text_input)
    elif cmd_artz_color == "CYAN":
        print(Fore.CYAN + text_input)
    elif cmd_artz_color == "WHITE":
        print(Fore.WHITE + text_input)
    elif cmd_artz_color == "GREEN":
        print(Fore.GREEN + text_input) 
    elif cmd_artz_color == "YELLOW":
        print(Fore.YELLOW + text_input)
   
def color_text():
    text_input = input("Write text :")
    text_color = input("Write color :")
    
    if text_color == "what?":
        print("1 => RED \n")
        print("2 => BLUE \n")
        print("3 => CYAN \n")
        print("4 => WHITE\n")
        print("5 => GREEN\n")
        print("6 => YELLOW\n")
    elif text_color == "RED":
        print(Fore.RED + text_input)
    elif text_color == "BLUE":
        print(Fore.BLUE + text_input)
    elif text_color == "CYAN":
        print(Fore.CYAN + text_input)
    elif text_color == "WHITE":
        print(Fore.WHITE + text_input)
    elif text_color == "GREEN":
        print(Fore.GREEN + text_input) 
    elif text_color == "YELLOW":
        print(Fore.YELLOW + text_input)
