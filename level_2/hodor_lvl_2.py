#!/usr/bin/python3
"""Module to fill a simple web form with an id and vote
clicking on a button.
It requests the cookie info from the web and send it back.
It sets the user information as a Windows User.
"""
import requests


url = 'http://158.69.76.135/level2.php'
user_ag = {"Referer": url, "User-Agent": "Mozilla/5.0\
            (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0"}
res = requests.get(url)
for i in range(1024):
    res_key = res.cookies['HoldTheDoor']
    payload = {'id': '1610', 'holdthedoor': 'submit', 'key': res_key}
    requests.post(url, data=payload, cookies={'HoldTheDoor': res_key},
                  headers=user_ag)

print("Hodor holds the door {:d} times!".format(i + 1))
