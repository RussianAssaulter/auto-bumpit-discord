import requests
import time
import colorama
from colorama import *



token = input("token: ")
channelid = input("channelid: ")

message = {
    'content': '/bump'
}

header = {
    'authorization': token
}

r = requests.post(f"https://discord.com/api/v9/channels/{channelid}/messages", data=message, headers=header)

while True:
    r
    time.sleep(3600)
    if r.status_code == 204:
        print(Fore.GREEN+"Succesfully Bumped!")
    else:
        print("Failed To Bump!")

 
 #simple auto-bumpit python script using plain post requests.


