import ui_pyt
from colorama import Fore
from art import text2art

def main():
    print(Fore.CYAN + text2art("W E L C O M E !\n"))
    
    cmd = input(Fore.GREEN + "Start? (y/n) :")
    
    if (cmd == "y" or cmd == "Y"):
        function_ui_pyt()
    else:
        print(Fore.RED + "Bye!\n")
        exit(0)