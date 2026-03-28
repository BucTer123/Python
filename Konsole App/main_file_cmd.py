import time
from colorama import Fore
from art import text2art
import times_now
import rq_cmd
import server

def main():
    print(Fore.LIGHTGREEN_EX + text2art("W E L C O M E !"))

    now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print(Fore.CYAN + "Time now :" + now)

    cmd = input(Fore.BLUE + "Write command or write 'help_cmd' :")

    if cmd == "help_cmd":
        print(Fore.LIGHTGREEN_EX + text2art("L I S T O F C O M M A N D S !"))

        print(Fore.CYAN + "time_now\n")
        print(Fore.CYAN + "req\n")
        print(Fore.CYAN + "web\n")

    elif cmd == "time_now":
        times_now.ss()

    elif cmd == "req":
        rq_cmd.zz()

    elif cmd == "web":
        server.ll()

if __name__ == "__main__":
    main()