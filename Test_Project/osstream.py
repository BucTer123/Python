import os
import time

def time_now(boolean):
    if boolean:
        now = time.strftime("%Y-%m-%d %H:%M:%S")
        print(now)
    else:
        exit(0)

def mkdir(path):
    os.mkdir(path)
    print("Created directory: ", path)

def rmdir(path):
    os.rmdir(path)
    print("Removed directory: ", path)

def list(path):
    os.system("dir")
