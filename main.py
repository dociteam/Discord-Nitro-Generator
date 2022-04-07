# DociTeam
# YouTube Video Link : https://youtu.be/ZRDL3LrH1qo

import requests
import numpy
import string
import time
from dhooks import Webhook

ATTEMPT = int(input('Enter attempt value : '))
WEBHOOK = str(input('Enter your Discord Webhook : '))
hook = Webhook(WEBHOOK)
chars = []
chars[:0] = string.ascii_letters + string.digits

c = numpy.random.choice(chars, size=[ATTEMPT, 16])

def stop(reason):
    hook.send("||@everyone||\n**Script Has Stopped! Reason : **"+reason)

for i in c:
    try:
        code = "".join(i)
        code_req = requests.get(f"https://discordapp.com/api/v9/entitlements/gift-codes/{code}?with_application=false&with_subscription_plan=true")
        if code_req.status_code == 200:
            valid_nitro = f"https://discord.gift/{code}"
            print("[+] Valid Nitro!")
            print(valid_nitro)
            hook.send("||@everyone||\n"+valid_nitro)
        if code_req.status_code == 404:
            print("[-] Unvalid Nitro!")
        if code_req.status_code == 429:
            print("[-] Rate Limited")
            server_info = code_req.json()
            rate_time = server_info["retry_after"]
            print(f"[!] Wait for -----> {rate_time}")
            time.sleep(rate_time)
    except:
        stop("Connection Error With Discord's Server!")
        exit()
stop("Finished!")
