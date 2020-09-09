import json
import logging
import math
import random
import re

import requests

logging.basicConfig(level=logging.INFO)

params = {
    'callback': 'dr1002',
    'jsVersion': '4.1',
    'v': math.floor(random.random() * 10000 + 500),
    'lang': 'zh'
}

r = requests.get("http://192.168.100.200/drcom/logout", params=params)

if r.status_code != 200:
    logging.error("Logout failed.")
    exit()

j = re.search("{.*}", r.text)
if not j:
    logging.error("Logout failed.")
    exit()
j = json.loads(j.group())
if not j['result']:
    logging.error(j['msga'])
    exit()
logging.info("Logout success.")
