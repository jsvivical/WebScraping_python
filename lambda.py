# BeautifulSoul에서는 특정 타입의 함수를 findAll함수에 매개변수로 넘길 수 있음.
# 이들 함수는 태그 객체를 매개변수로 하고, 불리언 값만 반환가능
# BeautifulSoup에서는 모든 태그 객체를 이 함수에서 평가하고, True인 태그는 반환, 아니면 버림.

from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup
import re
import ssl

cntx = ssl._create_unverified_context()
try:
    html = urlopen("https://pythonscraping.com/pages/page3.html", context=cntx)
    bs = BeautifulSoup(html, 'html.parser')
except HTTPError as e:
    print("http error")
except URLError as e:
    print("url error")
else:
    print("open successfully")

bs.findAll(lambda tag: len(tag.attrs) == 2)
# 속성이 두 개인 태그를 찾음.

for attr in bs.findAll(lambda tag: len(tag.attrs) == 2):
    print(attr)
