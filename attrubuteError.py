from urllib.request import urlopen
from urllib.request import HTTPError
from urllib.request import URLError
from bs4 import BeautifulSoup as bs
import ssl
# AttributeError : 존재하지 않는 태그에 접근하려 할 때 발생하는 예외

context = ssl._create_unverified_context()
try:
    html = urlopen("https://pythonscraping.com")
except HTTPError as e:
    print(e)
except URLError as e:
    print(e)
else:
    print("it worked")

# 불러오기 성공했을 경우 가정

try:
    badContent = bs.nonExistingTag.anotherTag
except AttributeError as e :
    print("Tag was not found")
else:
    if badContent == None:
        print("Tag was not Found")
    else:
        print(badContent)
