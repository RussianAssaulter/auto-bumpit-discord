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
    def bump():
     r = requests.post(f"https://discord.com/api/v9/channels/{channelid}/messages", data=message, headers=header)
     if r.status_code == 204:
        print(Fore.GREEN+"Succesfully Bumped!")
        time.sleep(3600)
        bump()
                  
     else:
        print("Failed To Bump!")
        bump()
    
    
    

 
 #simple auto-bumpit python script using plain post requests.


