# 검색을 통한 크롤링
# 대부분의 사이트에서는 http://example.co.kr?search=Topic처럼 검색결과를 얻을 수 있음
# 검색 결과 페이지는 보통 <span class="result"> 태그로 둘러싸여 있음(Website객체의 속성으로 저장)

import requests
from bs4 import BeautifulSoup


class Content:
    # 글/페이지 전체에 사용할 기반클래스
    def __init__(self, topic, url, title, body):
        self.topic = topic
        self.url = url
        self.title = title
        self.body = body

    def print(self):
        print("New Article found for topic : %s" % self.topic)
        print("URL : %s" % self.url)
        print("title : %s" % self.title)
        print("Body\n%s" % self.body)


class Website:
    # 웹사이트 구조에 관한 정보를 저장할 클래스
    def __init__(self, name, url, searchURL, resultListing, resultURL, absoluteURL, titleTag, bodyTag):
        self.name = name
        self.url = url
        self.searchURL = searchURL  # URL에 검색어를 추가한 경우 검색 결과를 어디에서 얻는지 정의
        self.resultListing = resultListing  # 각 결과에 관한 정보를 담고 있는 박스
        self.resultURL = resultURL  # 결과에서 정확한 URL을 추출할 때 사용할 태그 정보
        self.absoluteURL = absoluteURL  # 절대경로인지 알려주는 불리언 값
        self.titleTag = titleTag
        self.bodyTag = bodyTag


class Crawler:
    def getPage(self, url):
        try:
            req = requests.get(url)
        except requests.exceptions.RequestException:
            return None
        return BeautifulSoup(req.content.decode('utf-8', 'replace'), 'html.parser')

    def safeGet(self, pageObj, selector):
        childObj = pageObj.select(selector)
        if childObj is not None and len(childObj) > 0:  # 내용이 있으면
            return childObj[0].get_text()
        return ''  # 아무것도 없는 경우

    def search(self, topic, site):
        # 주어진 검색어로 주어진 웹사이트를 검색해 결과 페이지를 모두 기록
        bs = self.getPage(site.searchURL + topic)
        searchResults = bs.select(site.resultListing)
        for result in searchResults:
            url = result.select(site.resultURL)[0].attrs['href']
            print('\n\n', url, '\n\n')
            # 상대URL인지 확인
            if(site.absoluteURL):
                bs = self.getPage(url)
            else:
                bs = self.getPage(site.url + url)
            if bs is None:
                print("something was wrong with that page or URL. Skipping")
                return
            title = self.safeGet(bs, site.titleTag)
            body = self.safeGet(bs, site.bodyTag)
            if title != '' and body != '':  # 내용이 있으면
                content = Content(topic, url, title, body)
                content.print()


crawler = Crawler()

siteData = [
    [
        "헤럴드경제",  # name
        "http://biz.heraldcorp.com",  # url
        "http://biz.heraldcorp.com/search/index.php?q=",  # searchURL
        "div.list>ul>li",  # resultListing
        "a",  # resultURL
        False,  # absoluteURL
        "li.article_title.ellipsis2",  # titleTag
        "div#articleText.article_view"   # bodyTag
    ],
    [
        "서울신문",
        "https://seoul.co.kr",
        "https://search.seoul.co.kr/index.php?keyword=",
        "dl.article",
        "dt>a",
        True,
        "h1.atit2",
        "div#atic_txt1.S20_v_article"
    ]
]
sites = []
for row in siteData:
    sites.append(Website(row[0], row[1], row[2],
                 row[3], row[4], row[5], row[6], row[7]))
topics = ['빅데이터', '파이썬']
for topic in topics:
    print('getting info about : ' + topic)
    for targetSite in sites:
        crawler.search(topic, targetSite)
