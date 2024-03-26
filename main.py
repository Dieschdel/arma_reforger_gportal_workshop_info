import requests
from bs4 import BeautifulSoup
import json
import os
from pathlib import Path

def get_html(url):
    response = requests.get(url)
    return response.text

def find_info(html_content, info):
    soup = BeautifulSoup(html_content, 'html.parser')
    div_elements = soup.find_all('div')
    
    for div in div_elements:
        isValid = False
        for child in div.children:
            if child.name == "dt" and child.text.strip() == info:
                isValid = True
                
        for child in div.children:        
            if isValid and child.name == "dd":
                return child.text.strip()
                
def find_name(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    h1_elements = soup.find_all('h1')
    
    assert len(h1_elements)==1, "Unexpected top level heading found; Cannot derive title"
    return h1_elements[0].text.strip()

REQUIRED_ATTRIBUTES = [("ID", "modId"), ("Version", "version")]



def get_mod_infos(domain):
    info = {}
    
    html_content = get_html(domain)
    for attribute, attributeName in REQUIRED_ATTRIBUTES:
        value = find_info(html_content, attribute)

        info[attributeName] = value
    
    info["name"] = find_name(html_content)
    
    print(f"{json.dumps(info, indent=4)},")
    
def manual_input():
    print("Input mod Urls")
    while True:
        url = input()
        
        if url.lower() == "exit":
            break
        
        get_mod_infos(url)

def by_list(filename):
    SCRIPT_ROOT = Path(os.path.dirname(os.path.realpath(__file__)))
    
    with open(SCRIPT_ROOT/filename) as mods_file:
        for line in mods_file:
            url = line.strip()
            get_mod_infos(url)

import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
            description='Arma 3 mod server mod downloaded. See https://github.com/Dieschdel/arma3-automate for more info')
    parser.add_argument(
        "--list", help="retrieve all URLs via a mod list.txt instead of manual input")
    args = parser.parse_args()

    if args.list:
        by_list(args.list)
    else:
        manual_input()
