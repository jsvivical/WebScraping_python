import requests
from bs4 import BeautifulSoup


class Content:
    # 글/페이지 전체에 사용할 기반 클래스
    def __init__(self, url, title, body):
        self.url = url
        self.title = title
        self.body = body

    def print(self):
        print("URL : %s" % self.url)
        print("title : %s" % self.title)
        print("\nbody\n%s" % self.body)


class Website:
    # 웹사이트 구조에 관한 정보를 저장하는 클래스

    def __init__(self, name, url, titleTag, bodyTag):
        self.name = name
        self.url = url
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
        # BeautifulSoup객체와 선택자를 받아 콘텐츠 문자열을 추출하는 함수
        # 주어진 선택자로 검색된 결과가 없다면 빈 문자열을 반환
        selectedElems = pageObj.select(selector)
        if selectedElems is not None and len(selectedElems) > 0:
            # 선택자에서 텍스트만 리스트에 저장
            return '\n'.join([elem.get_text() for elem in selectedElems])
        return ''

    def parse(self, site, url):  # site는 website클래스의 객체를 받음.
        # url에서 콘텐츠를 추출
        bs = self.getPage(url)
        if bs is not None:
            title = self.safeGet(bs, site.titleTag)
            body = self.safeGet(bs, site.bodyTag)
            if title != '' and body != '':
                content = Content(url, title, body)
                content.print()
            else:
                print("없음")


# 메인함수
crawler = Crawler()  # 크롤러 인스턴스 생성

siteData = [
    ['MBN뉴스', 'https://www.mbn.co.kr', 'h1', 'div#newsViewArea.detail'],
    ['서울신문', 'https://seoul.co.kr', 'h1', 'div#atic_txt1.S20_v_article'],
    ['해럴드경제', 'https://www.biz.heraldcorp.com',
        'li.article_title.ellipsis2', 'div#articleText.article_view']
]

websites = []

urls = [
    'https://www.mbn.co.kr/news/economy/4683171',
    'https://www.seoul.co.kr/news/newsView.php?id=20220120001009&wlog_sub=svt_006',
    'http://biz.heraldcorp.com/view.php?ud=20220119000754'
]
for row in siteData:
    websites.append(Website(row[0], row[1], row[2], row[3]))
# 0 : 사이트이름, 1 : url, 2 : 제목 태그, 3 : 본문태그


crawler.parse(websites[0], urls[0])
crawler.parse(websites[1], urls[1])
crawler.parse(websites[2], urls[2])
