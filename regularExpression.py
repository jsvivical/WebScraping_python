from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup
import ssl
import re  # 정규표현식

# 정규표현식을 사용해서 해당 웹사이트에서 제품 이미지만 저장하기

context = ssl._create_unverified_context()
try:
    html = urlopen(
        "https://pythonscraping.com/pages/page3.html", context=context)

except HTTPError as e:
    print("http error\n")
except URLError as e:
    print("url error\n")

else:
    print("URL Open\n")
    bs = BeautifulSoup(html, 'html.parser')
    images = bs.findAll(
        'img', {'src': re.compile('\.\./img\/gifts/img.*\.jpg')})

    for image in images:
        print(image['src'])
