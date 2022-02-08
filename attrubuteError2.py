from urllib.request import urlopen
from urllib.request import HTTPError
from bs4 import BeautifulSoup
import ssl


def getTitle(url):
    context = ssl._create_unverified_context()

    try:
        html = urlopen(url, context=context)
    except HTTPError as e:
        return None
    try:
        bs = BeautifulSoup.(html.read(), 'html.parser')
        title = bs.body.h1
    except AttributeError as e:
        return None
    return title


title = getTitle("http://www.pythonscraping.con/pages/page1.html")
if title == None:
    print("Title could not be found")
else:
    print(title)
