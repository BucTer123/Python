from art import text2art
from colorama import Fore
import mainscript

print(Fore.CYAN + text2art("W E L C O M E !"))

linez = input(Fore.BLUE + "> ")

if linez.lower() == "exit":
    print(text2art("S H U T D O W N "))
    exit(0)
if linez.lower() == "start":
    print(text2art("S T A R T !"))
    mainscript.ai()