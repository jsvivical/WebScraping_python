from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

context = ssl._create_unverified_context()


html = urlopen(
    "https://www.pythonscraping.com/pages/page1.html", context=context)
bs = BeautifulSoup(html.read(), 'html.parser')
print(bs.h1)
