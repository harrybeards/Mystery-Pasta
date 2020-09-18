import requests
from bs4 import BeautifulSoup


def getBSObject(url):
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')

    return soup


#def get_wiki_url(soup):
#  first_url = 'https://en.wikipedia.org'
