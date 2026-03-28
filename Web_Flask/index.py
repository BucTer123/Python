import time
import script
from colorama import Fore
from art import text2art

def main():
    print(text2art("W E L C O M E !"))
    print(text2art("S E R V E R !"))
    
    now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    print(now + "\n")

    question = input("Do you want to start ? (y/n) :")

    if question == "y" or question == "Y":
        print(text2art("S T A R T !")
        print("Okay!")
        script.zz()
    else:
        print(Fore.RED + "SHUTDOWN!")
        exit(0)
    
if __name__ == "__index__":
    main()
