
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup
import ssl
import re

context = ssl._create_unverified_context()
html = urlopen("https://en.wikipedia.org/wiki/Eric_Idle", context=context)
bs = BeautifulSoup(html, 'html.parser')
for link in bs.findAll('a'):
    # a 태그인 부분을 찾기
    # <a accesskey = "v" href = "https://en.wikipedia.org/wiki/Eric_Idle?action = edit" class = "oo-ui-element-hidden>"
    if 'href' in link.attrs:
        print(link.attrs['href'])  # 페이지에 있는 링크 목록을 불러옴
