from art import text2art
from colorama import Fore 
import gui

def main():
    print(Fore.CYAN + text2art("W E L C O M E !\n"))

    cmd = input(Fore.GREEN + "> ")

    if cmd == "time_now":
        gui.gui()
    else:
        print(Fore.RED + "ERROR!")
        break


if __name__ == "__main__":
    main()