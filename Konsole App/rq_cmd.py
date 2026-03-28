import requests
from art import text2art
from colorama import Fore

def zz():
    print(text2art("R E Q U E S T S :"))

    resp = input(Fore.CYAN + "Write domain:")

    tm = int(input(Fore.CYAN + "Write how many times :"))

    for i in range(tm):
        rq = requests.get(resp)
        print(rq.status_code)
        print(rq.text + "\n")

if __name__ == "__main__":
    zz()