import argparse
import json
import logging
import math
import random
import re

import requests

logging.basicConfig(level=logging.INFO)

parser = argparse.ArgumentParser()
parser.add_argument('-a', '--account', required=True, help="account number of network")
parser.add_argument('-p', '--password', required=True, help="password of network")

args = parser.parse_args()

params = {
    'callback': 'dr1003',
    'DDDDD': args.account,
    'upass': args.password,
    '0MKKey': '123456',
    'R1': '0',
    'R2': '',
    'R3': '0',
    'R6': '0',
    'para': '00',
    'v6ip': '',
    'terminal_type': '1',
    'jsVersion': '4.1',
    'v': math.floor(random.random() * 10000 + 500),
    'lang': 'zh'
}

r = requests.get("http://192.168.100.200/drcom/login", params=params)

if r.status_code != 200:
    logging.error("Cannot connect to network.")
    exit()

j = re.search("{.*}", r.text)
if not j:
    logging.error("Error from network authentication system.")
    exit()
j = json.loads(j.group())
if not j['result']:
    logging.error(j['msga'])
    exit()
logging.info("Login success.")
