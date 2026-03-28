import time
from colorama import Fore
from art import text2art

def ss():
    print(text2art("T I M E :"))

    now2 = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print(Fore.CYAN + "Time now :" + now2)

if __name__ == "__main__":
    ss()