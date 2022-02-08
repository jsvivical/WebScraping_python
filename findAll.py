from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

context = ssl._create_unverified_context()

html = urlopen(
    "http://pythonscraping.com/pages/warandpeace.html", context=context)
bs = BeautifulSoup(html, 'html.parser')

# bs.findAll(tagName, tagAttributes)
nameList = bs.findAll('span', {'class': 'red'})
for name in nameList:
    print(name.get_text())  # get_text()는 모든 태그를 제거하고 유니코드 텍스트만 들어 있는 문자열 반환
