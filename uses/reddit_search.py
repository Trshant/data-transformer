from pprint import pprint
import requests
import json
import sys , os
sys.path.append(os.path.abspath("../"))
from dataTransformer import * 

def get_data(url):
    r = requests.get(url, headers={'User-Agent': 'TBhatBot'})
    data = r.json()
    return data

def get_data_make_url(part_of_url):
    return get_data(part_of_url+'.json')

def dofunc(data):
    try:
        urlurl = "https://reddit.com" + data["data"]["permalink"]
        body = data["data"]["body"]
        if 'news' in body.lower():
            print(urlurl)
    except KeyError:
        pass

process_line_definition = [
    "data/children" ,
    "loop" ,
    None ,
    [
        "data/url" ,
        "process",
        get_data_make_url ,
        [
            "1/data/children" ,
            "loop",
            dofunc,
            []
        ]
    ]
]

data = get_data(
    r'http://www.reddit.com/r/india/search/.json?q=Weekly%20Coders%2C%20Hackers%20%26%20All%20Tech%20related%20thread%20news&restrict_sr=1')
process(data, process_line_definition)
