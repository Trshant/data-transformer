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

def process_comments(part_of_url):
    global reddit_comment_process
    data = get_data(part_of_url+'.json')
    return process( data , reddit_comment_process )

def search_print(data):
    try:
        urlurl = "https://reddit.com" + data["data"]["permalink"]
        body = data["data"]["body"]
        if 'news' in body.lower():
            print(urlurl)
    except KeyError:
        pass
    return data

reddit_search_process = [
    "data/children" , # go here first
    "loop" , # loop through the array
    None ,  # Dont do anything here; allow the succeeding process line to work through each item in the loop
    [
        "data/url" , # go here
        "process" , # process this
        process_comments ,  # process the url to process comments in post
        []
    ]
]

reddit_comment_process = [
    "1/data/children",  # go down this data path
    "loop",  # you know what happens here ;-)
    # see the defninition of this function to see what this does - to search if the comment has the word 'news' in it. if it does, print the url out.
    search_print,
    []  # shtap!
]

data = get_data(
    r'http://www.reddit.com/r/india/search/.json?q=Weekly%20Coders%2C%20Hackers%20%26%20All%20Tech%20related%20thread%20news&restrict_sr=1')
process(data, reddit_search_process)
