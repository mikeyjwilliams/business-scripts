from bs4 import BeautifulSoup  # type: ignore
import requests  # type: ignore
from utils import Data  # type: ignore


def scrape_website(website: object):
    '''
    function scrape_site(website: str) -> string
    Description:
        pulls all html content from the website and returns
        html content as a string
    '''

    HEADERS = ({'User-Agent':
               'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0',
                'Accept-Language': 'en-US, en;q=0.5'})

    webpage = requests.get(website, headers=HEADERS)
    dirty_soup = BeautifulSoup(webpage.content, 'lxml')
    return dirty_soup
