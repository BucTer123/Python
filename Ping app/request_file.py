import requests
import os

def request_func():
    req = input("Write domain to ping :")
    times = int(input("How many times :"))
    
    for i in range(times):
        resp = requests.get(req)
        print(resp.status_code)