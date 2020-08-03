import requests
from bs4 import BeautifulSoup
import json

def process():
    jkdz = "http://www.cwl.gov.cn/cwl_admin/"
    url = jkdz + "kjxx/findDrawNotice"
    param = {'name': 'ssq', 'issueCount': '30'} 
    header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}
    resp = requests.get(url, params=param, headers=header) 
    result = resp.text
    if result == None or result == '':
        result = r'{}'
        print( 'result: null')
    else:
        print( 'result: ' + result)
    return json.loads(result)