# Dev by scarlxrd_1337
# Github: https://github.com/scarlxrd211
# Discord: https://discord.gg/puritybots

import requests
import random
from colorama import *
from datetime import datetime
import os
import time 

R = Fore.RED
G = Fore.GREEN
W = Fore.WHITE

def rntime():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return current_time

def banner():
     return f"""{Fore.MAGENTA}
████████╗ ██████╗ ██╗  ██╗███████╗███╗   ██╗    ███████╗██████╗  █████╗ ███╗   ███╗███╗   ███╗███████╗██████╗ 
╚══██╔══╝██╔═══██╗██║ ██╔╝██╔════╝████╗  ██║    ██╔════╝██╔══██╗██╔══██╗████╗ ████║████╗ ████║██╔════╝██╔══██╗
   ██║   ██║   ██║█████╔╝ █████╗  ██╔██╗ ██║    ███████╗██████╔╝███████║██╔████╔██║██╔████╔██║█████╗  ██████╔╝
   ██║   ██║   ██║██╔═██╗ ██╔══╝  ██║╚██╗██║    ╚════██║██╔═══╝ ██╔══██║██║╚██╔╝██║██║╚██╔╝██║██╔══╝  ██╔══██╗
   ██║   ╚██████╔╝██║  ██╗███████╗██║ ╚████║    ███████║██║     ██║  ██║██║ ╚═╝ ██║██║ ╚═╝ ██║███████╗██║  ██║
   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝    ╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝                                                                                         
                                                                                              by scarlxrd_1337
"""

def clear():
    return os.system('cls')

def nonce_generator(length=19):
    return ''.join(str(random.randint(1, 9)) for _ in range(length))

def payload(message):
    json = {
    "mobile_network_type": "unknown",
    "content": message,
    "nonce": "",
    "tts": False,
    "flags": 0
    }
    return json

def main(channel_id, amount, message):
    start = time.time()
    clear()
    print(banner())
    token_index = 0
    count = 0
    with open("tokens.txt") as f:
        tokens = f.read().splitlines()
    num_tokens = len(tokens)
    for _ in range(amount):
        header = {
            "Authorization": tokens[token_index]
        }
        token_index = (token_index + 1) % num_tokens
        req = requests.post(f"https://discord.com/api/v9/channels/{channel_id}/messages", headers=header, json=payload(message))
        if req.status_code == 200:
            count += 1
            print(f"{W}[{G}{rntime()}{W}] {G}[+] Message sent: {tokens[token_index][:49]}****.****.******")
        else:
            print(f"{W}[{R}{rntime()}{W}] {R}[!] Error with token: {tokens[token_index][:49]}****.****.****** : {req.status_code}")

    after = time.time()
    print(f"Time Taken: {Fore.WHITE}{after - start:.2f}")

if __name__ == "__main__":
    clear()
    channel_id = input(f"{Fore.MAGENTA}[?] Enter channel ID: {Fore.RESET}")
    amount = int(input(f"{Fore.MAGENTA}[?] Number of message you want send : {Fore.RESET}"))
    message = input(f"{Fore.MAGENTA}[?] Message you want to send : {Fore.RESET}")
    main(channel_id, amount, message)