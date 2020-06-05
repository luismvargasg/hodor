#!/usr/bin/python3
"""Module to fill a simple web form with an id and vote
clicking on a button.
"""
import requests

payload = {'id': '1610', 'holdthedoor': 'submit'}
for i in range(1, 1025):
    requests.post('http://158.69.76.135/level0.php', data=payload)
    i += 1
print("Hodor holds the door {:d} times!".format(i - 1))
