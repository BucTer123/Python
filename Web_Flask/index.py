import time
import script

def main():
    now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    print(now + "\n")

    question = input("Do you want to start ? (y/n) :")

    if question == "y" or question == "Y":
        print("Okay!")
        script.flask()

if __name__ == "__index__":
    main()