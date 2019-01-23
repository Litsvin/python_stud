import base64
import json

import requests


def do_get(url, headers):
    response = requests.get(url, headers)
    # print(response.content.decode('base64'))
    # base64.b64decode(response.content)
    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        return None


def decode():
    url = 'https://api.github.com/repos/qaprosoft/carina/contents/pom.xml'
    headers = {
        'user-agent': 'Listvin',
        'Authorization': 'token {SET_YOUR_TOKEN_HERE}', # <==== WARNING!
        'accept': 'application/vnd.github.v3.raw'
    }
    response = requests.get(url, headers)

    # print(response.content)
    print(base64.b64decode(response.content))


# def sli():
#     str = '123456789'
#     print(str[2:str.__len__() - 1])


# sli()
decode()
