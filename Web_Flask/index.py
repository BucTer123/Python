import time
import script
from colorama import Fore

def main():
    now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    print(now + "\n")

    question = input("Do you want to start ? (y/n) :")

    if question == "y" or question == "Y":
        print("Okay!")
        script.zz()
    else:
        print(Fore.RED + "SHUTDOWN!")
        exit(0)
    
if __name__ == "__index__":
    main()
