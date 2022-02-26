import requests
import os

req = requests.get('http://localhost/close_kakaotalk')

if req.status_code == 200:
    print("\x1b[1;32m", end="")
    res_text = req.text
else:
    print("\x1b[1;31m", end="")
    res_text = "None"
print("Status: " + str(req.status_code) + "\x1b[1;m")

if res_text != "None":
    print("\x1b[1;36mText\x1b[1;m: " + res_text.replace("</h1>", "").replace("<h1>", ""))

os.system("pause")
