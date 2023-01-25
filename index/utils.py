from bs4 import BeautifulSoup
import requests
import socket
import re
import json
import numpy as np 
socket.setdefaulttimeout(1)

def load_page(url):
    try : # If the page load
        page = requests.get(url, timeout=5)
        if page.ok:
            return BeautifulSoup(page.content, 'html.parser')
        else:
            return False
    except: # If the page don't load
        return False

def tokenize(elem):
    return elem.split()

def clean_text(string):
    clean=''
    try:
        clean = re.sub(r'[^\w\s]', '', string.lower())
    except:
        pass
    return clean


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