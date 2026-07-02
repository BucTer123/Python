from request_file import *

def main():
    question = input("Do you want to start (y/n) :")
    
    if question == "y" or question == "Y":
        request_func()
    else:
        print("Bye!")

if __name__ == "__main__":
    main()