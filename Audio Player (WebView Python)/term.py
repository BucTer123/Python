from art import text2art 
from colorama import Fore 
import script 

def main():
    print(Fore.BLUE + text2art("W E L C O M E !\n"))

    cmd = input(Fore.RED + "Start? (y/n) :")

    if cmd == "y" or cmd == "Y":
        second_script()
    else:
        print(Fore.RED + "Bye!\n")
        exit(0)


if __name__ == "__main__":
    main()