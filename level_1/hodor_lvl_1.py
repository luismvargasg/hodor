#!/usr/bin/python3
"""Module to fill a simple web form with an id and vote
clicking on a button.
It requests the cookie info from the web and send it back.
"""
import requests

url = 'http://158.69.76.135/level1.php'
res = requests.get(url)
for i in range(1, 4097):
    res_key = res.cookies['HoldTheDoor']
    payload = {'id': '1610', 'holdthedoor': 'submit', 'key': res_key}
    requests.post(url, data=payload, cookies={'HoldTheDoor': res_key})
    i += 1
print("Hodor holds the door {:d} times!".format(i - 1))
