from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import ssl
import re
import datetime
import random

pages = set()
random.seed(datetime.datetime.now())


# 페이지에서 발견된 내부 링크를 모두 목록으로 만듦
def getInternalLinks(bs, includeURL):
    includeURL = '{}://{}'.format(urlparse(includeURL).scheme,
                                  urlparse(includeURL).netloc)

    internalLinks = []  # 내부링크를 저장할 리스트

    # /로시작하는 링크를 모두 찾음
    # 내부링크 : 현재 url을 포함하고 괄호로 싸여서 //로 시작하는 경우가 많음
    for link in bs.findAll('a', href=re.compile('^(/|.*' + includeURL + ')')):
        if link.attrs["href"] is not None:
            if link.attrs['href'] not in internalLinks:
                if (link.attrs['href'].startswith('/')):
                    internalLinks.append(includeURL + link.attr['href'])
                else:
                    internalLinks.append(link.attrs['href'])
    return internalLinks


# 페이지에서 발견된 외부 링크를 목록으로 만듬
def getExternalLinks(bs, excludeURL):
    externalLinks = []
    # 현재 URL을 포함하지 않으면서 http나 www로 시작하는 링크를 모두 찾음
    for link in bs.findAll('a', href=re.compile('^(http|www)((?!' + excludeURL + ').)*$')):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in externalLinks:
                externalLinks.append(link.attrs['href'])
    return externalLinks


def getRandomExternalLink(startingPage):
    context = ssl._create_unverified_context()
    html = urlopen(startingPage, context=context)
    bs = BeautifulSoup(html, 'html.parser')
    externalLinks = getExternalLinks(bs, urlparse(startingPage).netloc)
    if len(externalLinks) == 0:
        print("No external Links. Looking around the site for one.\n")
        domain = "%s://%s" % (urlparse(startingPage).scheme,
                              urlparse(startingPage).netloc)
        internalLinks = getInternalLinks(bs, domain)
        return getRandomExternalLink(internalLinks[random.randint(0, len(externalLinks) - 1)])
    else:
        return externalLinks[random.randint(0, len(externalLinks) - 1)]


def followExternalOnly(startingSite):
    externalLink = getRandomExternalLink(startingSite)
    print('Random external link is : %s' % externalLink)
    followExternalOnly(externalLink)


followExternalOnly('https://www.naver.com')
