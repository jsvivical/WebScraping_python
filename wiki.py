from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup
import ssl
import datetime
import random
import re

# getLinks() : 정해진 형태의 url을 받고, 링크된 항목 url 목록 전체를 반환
# 시작 항목에서 getLinks()를 호출하고 반환된 리스트에서 무작위로 항목링크를 선택하고 getLinks를 다시 호출하는 작업을
# 프로그램을 끝내거나 새 페이지에 팡목 링크가 없을 때까지 반복하는 함수

random.seed(datetime.datetime.now())


def getLinks(articleUrl):
    context = ssl._create_unverified_context()
    html = urlopen("http://en.wikipedia.org%s" % articleUrl, context=context)
    bs = BeautifulSoup(html, 'html.parser')

    return bs.find('div', {'id': 'bodyContent'}).findAll('a', href=re.compile('^(/wiki/)((?!:).)*$'))


links = getLinks("/wiki/Kevin_Bacon")
for i in range(len(links)):
    newArticle = links[i].attrs['href']
    print(newArticle)
    links = getLinks(newArticle)
