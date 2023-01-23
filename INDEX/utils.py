from bs4 import BeautifulSoup
import requests
import socket
import re
import json
import numpy as np 

def load_page(url):
    socket.setdefaulttimeout(2)

    try : # If the page load
        page = requests.get(url)
        if page.ok:
            return BeautifulSoup(page.content, 'html.parser')
        else:
            return False
    except: # If the page d'ont load
        return False

def tokenize(elem):
    return elem.split()

def clean_test(string):
    return re.sub(r'[^\w\s]', '', string.lower())


def flatten_list(lists):
    return [item for sublist in lists for item in sublist]

class NpEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        if isinstance(obj, np.floating):
            return float(obj)
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return super(NpEncoder, self).default(obj)