from bs4 import BeautifulSoup  # type: ignore
import requests  # type: ignore
from utils import Data as SITE  # type: ignore


def pull_soup():

    HEADERS = ({'User-Agent':
               'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0',
                'Accept-Language': 'en-US, en;q=0.5'})

    webpage = requests.get(SITE.AMAZON, headers=HEADERS)
    soup = BeautifulSoup(webpage.content, 'lxml')

    tag = soup.title
    print(tag)
