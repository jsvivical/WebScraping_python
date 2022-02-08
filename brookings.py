# 다양한 웹사이트 레이아웃 다루기
# 웹사이트 콘텐츠에 대응하는 Content 클래스와
# BeautifulSoup 객체를 받아 Content 인스턴스를 반환하는 스크레이퍼 함수 두 개로 구성된 프로그램

import requests
from bs4 import BeautifulSoup

# 클래스 선언

# 스스로 필요한 정보를 생각해 class를 만들어야 함


class Content:
    def __init__(self, url, title, body):  # 생성자
        self.url = url
        self.title = title
        self.body = body


def getPage(url):  # 주어진  url에서 BeautifulSoup 인스턴스를 반환
    req = requests.get(url)
    return BeautifulSoup(req.text, 'html.parser')


def scrapeNYTimes(url):  # 뉴욕타임즈 스크래핑 함수
    bs = getPage(url)  # BeautifulSoup 객체를 만듦
    title = bs.find('h1').text  # h1태그의 텍스트를 저장
    lines = bs.select('div.StoryBodyCompanionColumn div p')
    body = '\n'.join([line.text for line in lines])
    return Content(url, title, body)


def scrapeBrookings(url):  # brooking 사이트 스크래핑 함수
    bs = getPage(url)
    title = bs.find('h1').text
    body = bs.find('div', {'class', 'post-body'}).text
    return Content(url, title, body)


url = "https://www.brookings.edu/blog/future-development/2018/01/26/delivering-inclusive-urban-access-3-uncomfortable-truths/"
content = scrapeBrookings(url)
print("Title : %s" % content.title)
print("URL : %s" % content.url)
print(content.body)

url = "https://www.nytimes.com/2018/01/25/opinion/sunday/silicon-valley-immortality.html"
content = scrapeNYTimes(url)
print("Title : %s" % content.title)
print("URL : %s" % content.url)
print(content.body)
