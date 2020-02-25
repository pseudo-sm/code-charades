
import requests

# constants
RUN_URL = u'http://api.hackerearth.com/code/run/'

CLIENT_SECRET = '5db3f1c12c59caa1002d1cb5757e72c96d969a1a'

source = open('test.py', 'r')
"""
test.py
#! -*- coding: utf-8 -*-

def square(no):
    return no * no

print(square(-23))
"""

data = {
    'client_secret': CLIENT_SECRET,
    'async': 0,
    'source': source.read(),
    'lang': "PYTHON",
    'time_limit': 5,
    'memory_limit': 262144,
}

r = requests.post(RUN_URL, data=data)
source.close()
print(r.json())